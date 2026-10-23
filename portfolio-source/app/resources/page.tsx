import {PageHero,SiteFooter,SiteHeader} from "../site-chrome";

const resources=[
 ["DASHBOARD","ATT arms transfer data","Power BI","https://app.powerbi.com/view?r=eyJrIjoiZjU5YzhmZDQtMzg1Mi00MGMxLTgxN2MtNGVjZGVmNTc3ZTdlIiwidCI6IjVhYWIxMGRlLTMyM2ItNDE5NC04N2M0LWNhNWVjMDQ0YThkOSJ9"],
 ["MAP","Buenos Aires Crime Explorer","ArcGIS","https://storymaps.arcgis.com/stories/471f645af5884c52b1b134b2444c6dc9"],
 ["SURVEY","ESPOP public opinion data","UdeSA","https://udesa.edu.ar/espop"],
 ["REPORTS","ATT Monitor","Transparency data","https://attmonitor.org/en/"],
 ["ANALYSIS","Forum on the Arms Trade","Security policy","https://www.forumarmstrade.org/"],
 ["JOURNAL","REsIDeS","Open access","https://revistasdigitales.udesa.edu.ar/index.php/resides/issue/view/vol1"]
];

const recipes=[
 {label:"R · NETWORKS",title:"Build a co-sponsorship network",code:`library(igraph)\n\ng <- graph_from_data_frame(edges, directed = FALSE)\nV(g)$degree <- degree(g)\nV(g)$betweenness <- betweenness(g, normalized = TRUE)`},
 {label:"PYTHON · TEXT",title:"Prepare a news corpus",code:`docs = (df.dropna(subset=["text"])\n          .assign(text=lambda x: x.text.str.lower())\n          .drop_duplicates("text"))\n\ncounts = docs.groupby("source").size()`},
 {label:"R · SURVEYS",title:"Weighted estimates",code:`library(survey)\n\ndesign <- svydesign(ids = ~1, weights = ~weight, data = survey_data)\nsvymean(~support_policy, design, na.rm = TRUE)`}
];

export default function Resources(){return <main><SiteHeader/><PageHero index="05" kicker="CODE + TOOLS + SOURCES" title="Use the work." intro="Reusable code patterns, datasets, dashboards, and research sources."/><section className="recipe-section"><div className="recipe-head"><p className="kicker">/ QUICK RECIPES</p><h2>Start with<br/>working code.</h2></div><div className="recipe-grid">{recipes.map(r=><article key={r.title}><span>{r.label}</span><h3>{r.title}</h3><pre><code>{r.code}</code></pre></article>)}</div></section><section className="resources resource-page"><p className="kicker">/ OPEN AND EXPLORE</p><div className="resource-list">{resources.map(r=><a href={r[3]} target="_blank" rel="noreferrer" key={r[1]}><span>{r[0]}</span><h3>{r[1]}</h3><p>{r[2]}</p><b>↗</b></a>)}</div></section><SiteFooter/></main>}
