"""Download current source snapshots for build_inventory.py.
Saved historical inputs are never silently overwritten. Network access required.
"""
import pathlib,json,urllib.request,time
ROOT=pathlib.Path(__file__).resolve().parents[3]
INPUT=pathlib.Path(__file__).parent/'inputs';INPUT.mkdir(exist_ok=True)
for s in json.loads((ROOT/'data/css-latam/university-sources.json').read_text()):
 if not s.get('snapshotFile'):continue
 p=INPUT/s['snapshotFile']
 if p.exists():print('Preserved:',p.name);continue
 try:
  req=urllib.request.Request(s['url'],headers={'User-Agent':'CSS-LATAM academic directory source retrieval'})
  with urllib.request.urlopen(req,timeout=45) as response:raw=response.read()
  p.write_bytes(raw);print('Downloaded:',p.name)
 except Exception as exc:print('FAILED:',s['id'],str(exc))
 time.sleep(1)
