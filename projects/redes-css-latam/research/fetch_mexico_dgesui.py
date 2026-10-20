"""Read the DGESUI directory, limited to its UPE/UPEAS/UI categories.
Not a full Mexican higher-education registry. Raw pages and provenance retained.
"""
import requests,json,pathlib,time
from bs4 import BeautifulSoup
P=pathlib.Path(__file__).parent/'inputs';rows=[];pages=[]
for page in range(7):
 url=f'https://dgesui.ses.sep.gob.mx/instituciones?categoria=All&combine=&estado=All&page={page}'
 path=P/f'mx-dgesui-{page}.html'
 if not path.exists():
  r=requests.get(url,timeout=30);r.raise_for_status();path.write_text(r.text);time.sleep(.5)
 s=BeautifulSoup(path.read_text(),'html.parser');cards=s.select('article.institution');pages.append({'url':url,'records':len(cards)})
 for c in cards:
  rows.append({'name':c.select_one('.field--name-title').get_text(' ',strip=True),'website':c.select_one('a[href]')['href'],'code':c.get('data-history-node-id'),'source':url,'retrieved':'2026-10-20'})
(P/'mx-dgesui.json').write_text(json.dumps({'scope':'UPE, UPEAS y UI; no representa todas las IES mexicanas','pages':pages,'institutions':rows},ensure_ascii=False,indent=2)+'\n')
assert len({r['code'] for r in rows})==len(rows)
print('DGESUI institutions',len(rows))
