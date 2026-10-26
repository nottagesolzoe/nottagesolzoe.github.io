"""Reapply the published access ledger without changing thematic review decisions.

Run from any directory. Optional --inventory and --ledger support a retained snapshot.
The original 2026-10-25 inventory is also available in Git commit31af1be.
"""
from pathlib import Path
import argparse,json,copy
ROOT=Path(__file__).resolve().parents[3];DATA=ROOT/'data/css-latam'
p=argparse.ArgumentParser();p.add_argument('--inventory',type=Path,default=DATA/'university-inventory.json');p.add_argument('--ledger',type=Path,default=DATA/'recovery-20261026.json');p.add_argument('--output',type=Path);a=p.parse_args()
rows=json.loads(a.inventory.read_text());document=json.loads(a.ledger.read_text());evidence={r['id']:r for r in document['records']}
assert len(evidence)==626 and {r['id']for r in rows}.issuperset(evidence)
assert sum(r['resolved']for r in evidence.values())==document['summary']['recordsResolved']
for row in rows:
 r=evidence.get(row['id'])
 if not r:continue
 original=copy.deepcopy(row.get('originalRapidReview',row.get('rapidReview',{})));row['originalRapidReview']=original
 row['recovery']={k:v for k,v in r.items()if k not in ['evidence','name','country']};row['recovery']['evidenceFile']=a.ledger.name
 if r['urlIdentified']and not r['identityPending']and not r['administrativeResolved']and r.get('officialUrl'):
  u=r['officialUrl'];existing=next((w for w in row['websites']if w['url']==u),None)
  meta={'provenance':'recovery-20261026','status':r['disposition'],'checked':'2026-10-26','coverage':'access_identity_only','historicalRelation':r['administrativeResolved']}
  if existing and existing.get('provenance')=='recovery-20261026':existing.update(meta)
  elif existing:existing['recovery']=meta
  else:row['websites'].append({'url':u,**meta})
  row['recovery']['preferredPublicSource']=r.get('accessibleEvidenceUrl')or u
 row['rapidReview']={**original,'checked':'2026-10-26','status':r['disposition'],'accessible':bool(r['accessRecovered']and not r['identityPending']),'candidate':original.get('candidate',False),'recoveryFile':a.ledger.name,'thematicReviewCompleted':False,'originalStatus':original.get('status'),'partialSourceOnly':r['accessRecovered']and not r['operationalSiteRecovered'],'operationalSiteRecovered':r['operationalSiteRecovered'],'identityPending':r['identityPending']}
(a.output or a.inventory).write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(f'Applied {len(evidence)} access/identity records; thematic review fields preserved.')
