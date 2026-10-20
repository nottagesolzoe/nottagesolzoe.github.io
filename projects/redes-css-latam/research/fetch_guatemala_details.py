import requests,json,pathlib,concurrent.futures
from bs4 import BeautifulSoup
from urllib.parse import urljoin,urlparse
root=pathlib.Path(__file__).resolve().parents[3]; inp=root/'projects/redes-css-latam/research/inputs'
s=BeautifulSoup((inp/'gt-ceps.html').read_text(),'html.parser'); links=[(a.get_text(' ',strip=True),urljoin('https://ceps.edu.gt/ceps/',a['href'])) for a in s.select('a[href]') if 'univ-view-one?' in a['href']]
def fetch(pair):
 name,url=pair
 out={'name':name,'source':url,'retrieved':'2026-10-20'}
 try:
  r=requests.get(url,timeout=25);out['http']=r.status_code;r.raise_for_status();b=BeautifulSoup(r.text,'html.parser');out['websites']=list(dict.fromkeys(urljoin(url,a['href']) for a in b.select('a[href]') if urlparse(urljoin(url,a['href'])).scheme in ['http','https'] and urlparse(urljoin(url,a['href'])).hostname not in ['ceps.edu.gt','www.ceps.edu.gt','www.facebook.com','www.instagram.com','api.whatsapp.com']));out['units']=[{'name':a.parent.get_text(' ',strip=True),'url':urljoin(url,a['href'])} for a in b.select('a[href]') if 'ver programas' in a.get_text().lower()]
 except Exception as e:out['error']=str(e)
 return out
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: rows=list(pool.map(fetch,links))
(inp/'gt-register-details.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'universities':len(rows),'sites':sum(bool(x.get('websites')) for x in rows),'units':sum(len(x.get('units',[])) for x in rows)}))
