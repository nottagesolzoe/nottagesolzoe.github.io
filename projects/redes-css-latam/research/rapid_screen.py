"""Rapid inventory-wide institutional screening. It does not close an exhaustive review."""
import json,re,time,unicodedata,hashlib,concurrent.futures,threading,urllib.parse,urllib.robotparser
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import requests
from bs4 import BeautifulSoup
BASE=Path(__file__).resolve().parents[3];REPO=BASE;OUT=BASE/'work/css-latam/rapid-screen.json';OUT.parent.mkdir(parents=True,exist_ok=True);DATE=datetime.now(ZoneInfo('America/New_York')).strftime('%Y-%m-%d')
rows=json.loads((REPO/'data/css-latam/university-inventory.json').read_text()); prior=json.loads((REPO/'data/css-latam/university-screening-ar.json').read_text())
def norm(t):return ''.join(c for c in unicodedata.normalize('NFKD',t.lower()) if not unicodedata.combining(c))
DIRECT=['ciencias sociales computacionales','ciências sociais computacionais','ciencias sociais computacionais','computational social science','social data science','humanidades digitales','humanidades digitais','digital humanities','humanites numeriques','inteligencia artificial y politicas publicas','inteligencia artificial e politicas publicas','analisis de redes sociales','social network analysis','computational communication','computational social','ciencia de datos para las ciencias sociales','ciencia de dados sociais','politicas publicas e ciencia de dados']
DIRECT=[norm(t) for t in DIRECT]
CAT=re.compile(r'oferta|academic|posgrado|postgrado|diplom|educacion continua|educacao continuada|pos-graduacao|graduate|programmes|formation',re.I)
RES=re.compile(r'investiga|centro|laboratorio|pesquisa|research|recherche|institut',re.I)
TOPIC=re.compile(r'computacion.*social|social.*computacion|humanidad.*digital|humanidades.*digita|digital.*humanit|inteligencia.artificial.*politic|datos.*social|dados.*socia|data.*soci|redes.sociales',re.I)
origins={};missing=[]
for row in rows:
 webs=sorted(row.get('websites',[]),key=lambda w:w.get('provenance')=='hipo')
 if not webs:missing.append({'institutionIds':[row['id']],'countries':[row['country']],'status':'sin web registrada','checked':DATE,'pages':[]});continue
 u=urllib.parse.urlsplit(webs[0]['url']);host=u.netloc.lower().removeprefix('www.')
 if not host:missing.append({'institutionIds':[row['id']],'countries':[row['country']],'status':'URL inválida en inventario','checked':DATE,'pages':[]});continue
 root='https://'+host+'/'
 origins.setdefault(root,{'ids':[],'countries':set()});origins[root]['ids'].append(row['id']);origins[root]['countries'].add(row['country'])
results=[];done=set()
if OUT.exists():
 results=json.loads(OUT.read_text())['results'];done={x.get('startUrl') for x in results}
else:
 # Reuse the documented October 20 run rather than repeat it; every old date remains visible.
 for x in prior['results']:
  if not x.get('startUrl'):continue
  host=urllib.parse.urlsplit(x['startUrl']).netloc.lower().removeprefix('www.');key='https://'+host+'/'
  if key not in origins:continue
  x=dict(x);x['startUrl']=key;x['institutionIds']=origins[key]['ids'];x['countries']=sorted(origins[key]['countries']);x['checked']=prior['date'];x['reusedEvidence']=True;x['rapidStatus']='evidencia previa reutilizada; revisión rápida registrada';results.append(x);done.add(key)
 results+=missing
lock=threading.Lock();started=time.time()
def snapshot():
 payload={'method':'rapid institutional screening','date':DATE,'scope':'ALL inventory records; not all existing institutions','limits':{'maxPagesPerOrigin':4,'workers':20,'deepCurriculumReading':False,'noFindingMeansAbsence':False},'inventoryRecords':len(rows),'distinctOrigins':len(origins),'processedOrigins':sum(bool(x.get('startUrl')) for x in results),'results':results}
 temp=OUT.with_suffix('.tmp');temp.write_text(json.dumps(payload,ensure_ascii=False,indent=2));temp.replace(OUT)
def fetch(session,url):
 r=session.get(url,timeout=(3,6),stream=True);chunks=[];size=0
 for c in r.iter_content(65536):
  chunks.append(c);size+=len(c)
  if size>=1800000:break
 raw=b''.join(chunks);r.close();return r.status_code,r.url,r.headers,raw

def scan(item):
 root,info=item;s=requests.Session();s.headers['User-Agent']='CSS-LATAM academic institutional overview; public sources';out={'startUrl':root,'institutionIds':info['ids'],'countries':sorted(info['countries']),'checked':DATE,'pages':[],'candidateLinks':[],'status':'revisión rápida sin hallazgos en páginas consultadas'};allowed=urllib.parse.urlsplit(root).netloc
 try:
  code,_,_,raw=fetch(s,root+'robots.txt');rp=urllib.robotparser.RobotFileParser();rp.parse(raw.decode('utf8','replace').splitlines() if code==200 else [])
  if code in [401,403] or code>=500:out['status']='robots inaccesible; revisión pendiente';return out
 except requests.RequestException as e:out['status']='acceso bloqueado o fallido';out['error']=type(e).__name__;return out
 queue=[(root,'inicio')];seen=set();selected=set()
 for _ in range(4):
  if not queue:break
  url,kind=queue.pop(0)
  if url in seen:continue
  seen.add(url)
  if not rp.can_fetch('*',url):out['pages'].append({'url':url,'status':'robots disallow'});continue
  try:
   code,final,headers,raw=fetch(s,url);p={'url':url,'finalUrl':final,'http':code,'purpose':kind};out['pages'].append(p)
   if code!=200 or 'html' not in headers.get('content-type','').lower():continue
   doc=BeautifulSoup(raw,'html.parser');p['title']=doc.title.get_text(' ',strip=True)[:240] if doc.title else ''
   for el in doc(['script','style','nav','footer']):el.decompose()
   text=' '.join(doc.stripped_strings);n=norm(text);hits=[t for t in DIRECT if t in n];p['candidateTerms']=hits
   if hits:
    p['evidenceExcerpts']=[text[max(0,n.index(t)-50):n.index(t)+len(t)+110] for t in hits[:3]];out['status']='candidato localizado; validación de inclusión pendiente'
   p['textHash']=hashlib.sha256(text.encode()).hexdigest();links=[]
   # Parse links from a fresh soup because the navigation carries the catalog links.
   navdoc=BeautifulSoup(raw,'html.parser')
   for a in navdoc.select('a[href]'):
    dest=urllib.parse.urljoin(final,a['href']).split('#')[0];v=urllib.parse.urlsplit(dest);host=v.netloc.lower().removeprefix('www.');label=' '.join(a.stripped_strings)[:180];term=norm(label+' '+v.path)
    if v.scheme not in ['https','http'] or not(host==allowed or host.endswith('.'+allowed)):continue
    if re.search(r'\.(pdf|zip|jpg|png|mp4|docx?|xlsx?)$',v.path,re.I):continue
    typ='candidato' if TOPIC.search(term) else 'oferta' if CAT.search(term) else 'investigación' if RES.search(term) else None
    if typ:links.append({'url':dest,'title':label,'purpose':typ})
   out['candidateLinks']+=links
   for typ in ['candidato','oferta','investigación']:
    candidates=[l for l in links if l['purpose']==typ and l['url'] not in seen and l['url'] not in selected]
    if candidates:
     l=candidates[0];queue.append((l['url'],typ));selected.add(l['url'])
   queue=sorted(queue,key=lambda x:['candidato','oferta','investigación','inicio'].index(x[1]))
  except requests.RequestException as e:out['pages'].append({'url':url,'error':type(e).__name__})
  time.sleep(.3)
 out['candidateLinks']=list({x['url']:x for x in out['candidateLinks']}.values())[:80]
 if not any(x.get('http')==200 for x in out['pages']):out['status']='sin páginas accesibles; revisión pendiente'
 return out
snapshot();todo=[x for x in origins.items() if x[0] not in done];print('Inventory',len(rows),'origins',len(origins),'reused',len(done),'remaining',len(todo),flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as pool:
 for i,f in enumerate(concurrent.futures.as_completed([pool.submit(scan,x) for x in todo]),1):
  try:results.append(f.result())
  except Exception as e:print('ERROR',type(e).__name__,str(e)[:100],flush=True);continue
  snapshot()
  if i%25==0:print('Processed',i,'/',len(todo),'elapsed',round(time.time()-started),'sec',flush=True)
print('DONE',len(results),'groups',round(time.time()-started),'sec',flush=True)
