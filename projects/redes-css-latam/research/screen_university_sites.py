"""Pre-screen every listed website in one country's provisional inventory.
Not a completed institutional review. Does not add people or programs.
Usage: python screen_university_sites.py Argentina --output /path/review.json
"""
import argparse,json,pathlib,concurrent.futures,urllib.parse,urllib.robotparser,time,re,unicodedata
import requests
from bs4 import BeautifulSoup
p=argparse.ArgumentParser();p.add_argument('country');p.add_argument('--output',required=True);a=p.parse_args()
ROOT=pathlib.Path(__file__).resolve().parents[3]
rows=[x for x in json.loads((ROOT/'data/css-latam/university-inventory.json').read_text()) if x['country']==a.country]
def norm(s):return ''.join(c for c in unicodedata.normalize('NFKD',s.lower()) if not unicodedata.combining(c))
patterns=['ciencias sociales computacionales','humanidades digitales','inteligencia artificial y politicas','datos para las ciencias sociales','datos aplicados a las politicas','computational social','digital humanities']
menu=re.compile('posgrado|postgrado|diplom|investiga|centro|laboratorio|extension|educacion continua|oferta academica',re.I)
# Deduplicate exact origins before making requests; preserve every institution identifier.
origins={};missing=[]
for row in rows:
 if not row['websites']:missing.append({'institutionIds':[row['id']],'status':'sin web; localización pendiente'});continue
 webs=sorted(row['websites'],key=lambda w:w['provenance']=='hipo');u=webs[0]['url'];v=urllib.parse.urlsplit(u);root=urllib.parse.urlunsplit(('https',v.netloc,'/','',''))
 origins.setdefault(root,[]).append(row['id'])
def scan(item):
 root,ids=item;s=requests.Session();s.headers['User-Agent']='CSS-LATAM public academic-directory research';result={'institutionIds':ids,'startUrl':root,'status':'rastreo preliminar; revisión institucional pendiente','pages':[],'candidateLinks':[]};seen=set()
 try:
  r=s.get(root+'robots.txt',timeout=(4,8));rp=urllib.robotparser.RobotFileParser();rp.parse(r.text.splitlines() if r.status_code==200 else [])
  if r.status_code in (401,403):result['status']='robots inaccesible; revisión manual pendiente';return result
 except requests.RequestException as exc:result['robotsNote']=type(exc).__name__;result['status']='acceso pendiente; robots no recuperado';return result
 queue=[root];allowedHost=urllib.parse.urlsplit(root).netloc.lower().removeprefix('www.')
 for depth in range(5):
  if not queue:break
  url=queue.pop(0)
  if url in seen:continue
  seen.add(url)
  if not rp.can_fetch('*',url):result['pages'].append({'url':url,'status':'robots disallow'});continue
  try:
   r=s.get(url,timeout=(4,9));entry={'url':url,'finalUrl':r.url,'http':r.status_code};result['pages'].append(entry)
   if r.status_code!=200 or 'html' not in r.headers.get('content-type',''):continue
   soup=BeautifulSoup(r.text,'html.parser');entry['title']=soup.title.get_text(' ',strip=True) if soup.title else '';text=norm(soup.get_text(' ',strip=True));entry['candidateTerms']=[t for t in patterns if t in text]
   links=[]
   for tag in soup.select('a[href]'):
    label=tag.get_text(' ',strip=True);dest=urllib.parse.urljoin(r.url,tag['href']).split('#')[0];v=urllib.parse.urlsplit(dest);h=v.netloc.lower().removeprefix('www.')
    if v.scheme not in ('http','https') or not(h==allowedHost or h.endswith('.'+allowedHost)):continue
    if menu.search(norm(label+' '+v.path)) or any(t in norm(label) for t in patterns):
     links.append({'title':label[:180],'url':dest})
   result['candidateLinks'].extend(links)
   queue.extend(x['url'] for x in sorted(links,key=lambda x:0 if 'posgrado' in norm(x['title']+x['url']) else 1) if x['url'] not in seen and not re.search(r'\.(pdf|jpg|png|zip)$',x['url'],re.I))
  except requests.RequestException as exc:result['pages'].append({'url':url,'error':type(exc).__name__})
  time.sleep(.6)
 result['candidateLinks']=list({x['url']:x for x in result['candidateLinks']}.values());return result
results=missing[:];out=pathlib.Path(a.output);out.parent.mkdir(parents=True,exist_ok=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 for i,r in enumerate(ex.map(scan,origins.items()),1):
  results.append(r)
  if i%10==0:print('Origins processed',i,'of',len(origins),flush=True)
  out.write_text(json.dumps({'country':a.country,'date':'2026-10-20','limits':{'maxPagesPerOrigin':5,'workers':6,'scope':'pre-screen only; does not close review'},'results':results},ensure_ascii=False,indent=2))
print('Saved',len(results),'site groups; not completed reviews',flush=True)
