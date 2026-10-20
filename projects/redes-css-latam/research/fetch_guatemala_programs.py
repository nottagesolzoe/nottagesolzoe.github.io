"""Capture every academic-unit program list linked by the CEPS register.
This records official program names, not an inference of CSS eligibility.
"""
import json,pathlib,time,requests,concurrent.futures,re
from bs4 import BeautifulSoup
ROOT=pathlib.Path(__file__).resolve().parents[3]
INPUT=pathlib.Path(__file__).parent/'inputs'
rows=json.loads((INPUT/'gt-register-details.json').read_text())
units=[(r['name'],x) for r in rows for x in r.get('units',[])]
def fetch(item):
 university,unit=item;out={'university':university,'unit':unit['name'],'url':unit['url'],'retrieved':'2026-10-20'}
 try:
  r=requests.get(unit['url'],timeout=(5,20));out['http']=r.status_code;r.raise_for_status();s=BeautifulSoup(r.text,'html.parser')
  for a in s.select('script,style,header,footer,nav'):a.decompose()
  out['text']=s.get_text(' ',strip=True)
  match=re.search(r'Programas de (.*?) Nombre del programa',out['text'])
  if match:out['unit']=match.group(1)
  out['candidateTerms']=[t for t in ['computacional','digital','datos','artificial','públic','social'] if t in out['text'].lower()]
 except Exception as e:out['error']=str(e)
 time.sleep(.5)
 return out
out=INPUT/'gt-program-lists.json';saved=json.loads(out.read_text()) if out.exists() else [];done={r['url'] for r in saved if r.get('http')==200}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for row in pool.map(fetch,[u for u in units if u[1]['url'] not in done]):
  saved=[r for r in saved if r['url']!=row['url']]+[row];out.write_text(json.dumps(saved,ensure_ascii=False,indent=2)+'\n')
  if len(saved)%20==0:print('Academic units captured',len(saved),flush=True)
print('Saved',len(saved),'unit pages',flush=True)
