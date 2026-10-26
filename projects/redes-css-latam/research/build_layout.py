"""Seeded force layouts within connected components, packed without overlap."""
from pathlib import Path
import json, math
import networkx as nx
root=Path(__file__).resolve().parents[3]
network=json.loads((root/'data/css-latam/network.json').read_text())
output={'method':'NetworkX spring_layout per connected component, seed42,600iterations,weighted edges. Components packed without overlap; isolates excluded. Position is not geography or a measure of social distance.','graphs':{}}
for key in ['coauthors','institutions']:
 graph=nx.Graph()
 graph.add_weighted_edges_from((e['source'],e['target'],e.get('weight',1)) for e in network[key]['edges'])
 components=sorted(nx.connected_components(graph),key=lambda c:(-len(c),sorted(c)[0]))
 x,y,rowheight=35,35,0
 positions={}
 for comp in components:
  size=75+50*math.sqrt(len(comp));width=size+24
  if x+width>965:x=35;y+=rowheight+30;rowheight=0
  local=nx.spring_layout(graph.subgraph(sorted(comp)),seed=42,iterations=600,k=.8,weight='weight')
  xs=[v[0] for v in local.values()];ys=[v[1] for v in local.values()]
  # A pair stays visibly separated along its force-layout orientation.
  scale=size/max(max(xs)-min(xs),max(ys)-min(ys),.001)
  cx=x+width/2;cy=y+width/2
  for id,v in local.items():positions[id]={'x':cx+(v[0]-(min(xs)+max(xs))/2)*scale,'y':cy+(v[1]-(min(ys)+max(ys))/2)*scale}
  x+=width+25;rowheight=max(rowheight,width)
 height=y+rowheight+35
 for pos in positions.values():pos['y']*=700/height;pos['x']=round(pos['x'],2);pos['y']=round(pos['y']+20,2)
 output['graphs'][key]=positions
(root/'data/css-latam/network-layout.json').write_text(json.dumps(output,indent=2)+'\n')
