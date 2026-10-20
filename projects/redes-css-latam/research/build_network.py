"""Recalculate network metrics and layout from reviewed public inputs.
Run: python3 projects/redes-css-latam/research/build_network.py
Requires networkx 3.7 and numpy. No network access required.
"""
import pathlib,json,math,collections,networkx as nx
ROOT=pathlib.Path(__file__).resolve().parents[3]
DATA=ROOT/'data/css-latam'
N=json.loads((DATA/'network.json').read_text())
# Reviewed edge lists are the analytical inputs. Metadata and sources are retained.
# Corpus contains all author lists; this assertion checks the projection against it.
P=json.loads((DATA/'corpus.json').read_text())
expected=collections.Counter()
import itertools
for p in P:
 for a,b in itertools.combinations(p['authorIds'],2):expected[tuple(sorted([a,b]))]+=1
observed={tuple(sorted([e['source'],e['target']])):e['weight'] for e in N['coauthors']['edges']}
assert dict(expected)==observed,'Coauthor projection does not match corpus'
def make_graph(part):
 g=nx.Graph()
 for n in part['nodes']:g.add_node(n['id'])
 for e in part['edges']:g.add_edge(e['source'],e['target'],weight=e.get('weight',1))
 return g
G=make_graph(N['coauthors']);cc=sorted(nx.connected_components(G),key=len,reverse=True);L=G.subgraph(cc[0]);eig=nx.eigenvector_centrality(L,weight='weight',max_iter=3000);bt=nx.betweenness_centrality(G,weight=None,normalized=True);communities=nx.community.louvain_communities(G,seed=42,weight='weight',resolution=1)
cl={n:i for i,c in enumerate(communities) for n in c}
for n in N['coauthors']['nodes']:
 k=n['id'];n.update(degree=G.degree(k),strength=G.degree(k,weight='weight'),betweenness=round(bt[k],6),eigenvector=round(eig[k],6) if k in eig else None,community=cl[k])
# Component layouts avoid giving disconnected components a spurious shared geometry.
# Deterministic shelf packing: each component gets an area proportional to its size.
def layout(part):
 g=make_graph(part);comps=sorted(nx.connected_components(g),key=lambda c:(-len(c),sorted(c)[0]));boxes=[]
 for c in comps:
  side=max(45,math.sqrt(len(c))*24);boxes.append((c,side))
 width=max(600,math.sqrt(sum(s*s for _,s in boxes)*1.5));x=y=rowh=0;positions={}
 for c,size in boxes:
  if x+size>width:x=0;y+=rowh+20;rowh=0
  h=g.subgraph(sorted(c));pos=nx.spring_layout(h,seed=42,iterations=180,weight='weight') if len(c)>1 else {next(iter(c)):(0,0)}
  for n,(px,py) in pos.items():positions[n]=(x+size/2+float(px)*size*.38,y+size/2+float(py)*size*.38)
  x+=size+20;rowh=max(rowh,size)
 height=y+rowh
 for n in part['nodes']:
  px,py=positions[n['id']];n['x']=round(40+px/max(width,1)*900,2);n['y']=round(65+py/max(height,1)*610,2)
for key in ['affiliations','coauthors','institutions']:layout(N[key])
(DATA/'network.json').write_text(json.dumps(N,ensure_ascii=False))
print('Validated projection:',len(G),'authors,',G.number_of_edges(),'edges;',len(cc),'components')
