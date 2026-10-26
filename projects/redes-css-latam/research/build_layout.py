from pathlib import Path
import json,networkx as nx
r=Path(__file__).resolve().parents[3]
n=json.loads((r/'data/css-latam/network.json').read_text());out={'method':'NetworkX spring_layout, seed42, weighted edges, 600 iterations; isolated nodes excluded. Coordinates describe graph layout only, not geography.','graphs':{}}
for key in ['coauthors','institutions']:
 g=nx.Graph();g.add_weighted_edges_from((e['source'],e['target'],e.get('weight',1)) for e in n[key]['edges']);pos=nx.spring_layout(g,seed=42,iterations=600,k=1.0/(len(g)**.5),scale=1)
 xs=[x[0] for x in pos.values()];ys=[x[1] for x in pos.values()];out['graphs'][key]={id:{'x':round(65+(v[0]-min(xs))/(max(xs)-min(xs))*870,2),'y':round(55+(v[1]-min(ys))/(max(ys)-min(ys))*600,2)} for id,v in pos.items()}
(r/'data/css-latam/network-layout.json').write_text(json.dumps(out,indent=2)+'\n')
