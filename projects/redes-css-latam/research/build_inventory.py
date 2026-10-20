"""Build a provisional regional review queue from saved source snapshots.
Run from any directory. Requires beautifulsoup4 and openpyxl.
An inventory entry is NOT evidence of CSS activity or a completed review.
"""
import json, pathlib, unicodedata, hashlib, collections
from bs4 import BeautifulSoup
import openpyxl
ROOT=pathlib.Path(__file__).resolve().parents[3]
DATA=ROOT/'data/css-latam'; INPUT=pathlib.Path(__file__).parent/'inputs'
COUNTRIES={'AR':'Argentina','CL':'Chile','UY':'Uruguay','PY':'Paraguay','BR':'Brasil','BO':'Bolivia','PE':'Perú','EC':'Ecuador','CO':'Colombia','VE':'Venezuela','GY':'Guyana','SR':'Surinam','PA':'Panamá','CR':'Costa Rica','NI':'Nicaragua','HN':'Honduras','SV':'El Salvador','GT':'Guatemala','MX':'México','CU':'Cuba','DO':'República Dominicana','HT':'Haití'}
def norm(s):return ' '.join(''.join(c for c in unicodedata.normalize('NFKD',s.lower()) if not unicodedata.combining(c)).split())
previous_path=DATA/'university-inventory.json'
previous={r['id']:r for r in json.loads(previous_path.read_text())} if previous_path.exists() else {}
rows={}
def add(country,name,source,url=None,code=None,edition=None,detail=None):
 key=(country,norm(name))
 if key not in rows:
  rows[key]={'id':hashlib.sha256('|'.join(key).encode()).hexdigest()[:16],'country':country,'name':name,'websites':[], 'sources':[], 'review':{'programs':'pendiente','institutes':'pendiente','people':'pendiente','publications':'pendiente'},'cssStatus':'no evaluado','identityStatus':'pendiente de conciliación con registro nacional'}
 r=rows[key];e={'source':source,'retrieved':'2026-10-20'}
 if code:e['registryCode']=code
 if edition:e['sourceEdition']=edition
 if detail:e['detail']=detail
 if e not in r['sources']:r['sources'].append(e)
 if source!='hipo':r['identityStatus']='presente en fuente institucional; vigencia según edición'
 if url:
  if not url.startswith(('http://','https://')):url='https://'+url
  v={'url':url,'provenance':source,'status':'localizada; contenido pendiente de revisión'}
  if v not in r['websites']:r['websites'].append(v)
for a in json.loads((INPUT/'university-domains.json').read_text()):
 if a['alpha_two_code'] in COUNTRIES:
  for url in a['web_pages'] or [None]:add(COUNTRIES[a['alpha_two_code']],a['name'],'hipo',url)
for a in json.loads((INPUT/'colombia.txt').read_text()):
 if a.get('car_cter_acad_mico')=='Universidad':
  add('Colombia',a['nombre_instituci_n'],'co-men',a.get('p_gina_web'),a['c_digo_instituci_n'],a.get('fecha_actualizacion'),{'branch':a.get('principal_seccional'),'status':a.get('estado')})
for code,name,kind,status,operation in list(openpyxl.load_workbook(INPUT/'chile.xlsx').active.values)[1:]:
 if name and kind and 'UNIVERSIDAD' in kind:add('Chile',name,'cl-mineduc',code=code,edition='mayo 2026',detail={'type':kind,'status':status,'operation':operation})
for filename,source in [('ecuador.txt','ec-ces-publicas'),('ecuador-cofinanciadas.txt','ec-ces-cofinanciadas'),('ecuador-autofinanciadas.txt','ec-ces-autofinanciadas')]:
 s=BeautifulSoup((INPUT/filename).read_text(),'html.parser')
 for tr in s.select('table tbody tr'):
  td=tr.find_all('td')
  if len(td)>=5 and td[0].get_text(strip=True).isdigit():add('Ecuador',td[2].get_text(' ',strip=True),source,code=td[0].get_text(strip=True))
s=BeautifulSoup((INPUT/'peru.txt').read_text(),'html.parser')
for tr in s.select('#tablepress-114 tbody tr'):
 td=tr.find_all('td')
 if len(td)>=5:add('Perú',td[0].get_text(' ',strip=True),'pe-sunedu',detail={'licenseDate':td[1].get_text(' ',strip=True),'management':td[4].get_text(' ',strip=True)})
s=BeautifulSoup((INPUT/'argentina.txt').read_text(),'html.parser')
for box in s.select('.togglebox'):
 h=box.find_previous_sibling(class_='toggle-header')
 if h:
  links=[a['href'] for a in box.select('a[href]') if '.edu.ar' in a['href'] and not a['href'].startswith('mailto:')]
  add('Argentina',h.get_text(' ',strip=True),'ar-cin',links[0] if links else None)
s=BeautifulSoup((INPUT/'paraguay.txt').read_text(),'html.parser')
for tr in s.select('table tbody tr'):
 td=tr.find_all('td')
 if len(td)>=5:
  name=td[4].get_text(' ',strip=True)
  if name and 'universidad' in name.lower():add('Paraguay',name,'py-cones',detail={'scope':'institución mencionada en oferta académica; nómina no necesariamente completa'})
# National registers captured separately from the secondary candidate directory.
extra=INPUT/'register-expansion.json'
if extra.exists():
 for source in json.loads(extra.read_text()):
  if source.get('http')!=200:continue
  if source['id']=='gt-ceps':
   for entry in source.get('links',[]):
    if 'universidad_id=' in entry['url']:
     add('Guatemala',entry['name'],'gt-ceps',code=entry['url'].split('universidad_id=')[-1],detail={'registryPage':source['url'],'recordPath':entry['url']})
  if source['id']=='cr-conesup':
   for entry in source.get('options',[]):
    if ' - ' in entry:
     code,name=entry.split(' - ',1)
     add('Costa Rica',name,'cr-conesup',code=code,detail={'registryPage':source['url'],'scope':'Etiqueta literal del selector CONESUP; conciliar alias, estado y sector público antes de contar universidades únicas'})
result=sorted(rows.values(),key=lambda r:(list(COUNTRIES.values()).index(r['country']),r['name']))
# Preserve completed review evidence and screening logs when rebuilding the frame.
for r in result:
 old=previous.get(r['id'],{})
 for field in ['review','screening','cssStatus']:
  if field in old:r[field]=old[field]
(DATA/'university-inventory.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'records':len(result),'countries':dict(collections.Counter(r['country'] for r in result))},ensure_ascii=False))
