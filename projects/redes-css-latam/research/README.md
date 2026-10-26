# Redes de CSS en LATAM

Autoría: **Sol Zoe Nottage**. Proyecto y fuentes en curso, sin cobertura exhaustiva.

## Replicar el dashboard

Clonar este repositorio y ejecutar desde su raíz:

```sh
git clone https://github.com/nottagesolzoe/nottagesolzoe.github.io.git
cd nottagesolzoe.github.io
python3 -m http.server 8000
```

Abrir `http://localhost:8000/projects/redes-css-latam/`. No requiere claves ni servicios externos para consultar los datos publicados. El formulario de incorporación sí utiliza GitHub.

## Recalcular el análisis de redes

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r projects/redes-css-latam/research/requirements.txt
python3 projects/redes-css-latam/research/build_network.py
```

El script verifica la proyección de coautorías contra las listas de autores del corpus. Actualiza `data/css-latam/network.json`. Conserva afiliaciones revisadas como insumo; no reconstruye evidencia institucional a partir de coautorías. Las definiciones, restricciones y parámetros están en [metodologia.md](metodologia.md).

## Reconstruir el inventario universitario

```sh
python3 projects/redes-css-latam/research/fetch_inventory_sources.py
python3 projects/redes-css-latam/research/build_inventory.py
```

Las fuentes, fechas, alcance y hashes de las descargas originales están en `data/css-latam/university-sources.json`. La tabla extraída del corte está en `university-inventory.json`. Las páginas externas pueden cambiar: descargarlas nuevamente no garantiza reproducir exactamente el corte. El script preserva las descargas ya existentes y no elude bloqueos de acceso. Las copias completas de páginas externas no se distribuyen con este repositorio.

Se comienza por América del Sur. Los registros de un directorio secundario de dominios no sustituyen los registros nacionales. Los nombres equivalentes todavía pendientes de conciliación se conservan separados. Por ello, el número de filas no equivale al total de universidades únicas. La revisión de programas, institutos, personas y publicaciones se registra por separado.

## Incorporaciones

El [formulario público](https://github.com/nottagesolzoe/nottagesolzoe.github.io/issues/new?template=css-directorio.yml) permite solicitar una incorporación o corrección. Las propuestas requieren fuentes y revisión antes de modificar el dashboard. No hay incorporación automática.

## Asistencia y atribución

Se utilizó ChatGPT, mediante Codex, para asistir la búsqueda, programación de extracción, procesamiento y desarrollo. La herramienta no es coautora ni fuente de evidencia sobre personas o instituciones.

OpenAI. (2026). *ChatGPT* [Herramienta de inteligencia artificial, utilizada mediante Codex]. https://chatgpt.com/

El directorio de dominios utilizado como punto de partida corresponde a [Hipo/university-domains-list](https://github.com/Hipo/university-domains-list). Cada registro conserva su procedencia. Las fuentes originales mantienen sus respectivos derechos; la publicación de enlaces y datos no concede una licencia general sobre sus contenidos.

## Versiones de idioma

El dashboard está disponible en `/projects/redes-css-latam/` (español) y `/projects/redes-css-latam/en/` (inglés). Ambos utilizan los mismos JSON y conservan filtros al cambiar idioma. Los nombres y notas de fuentes se mantienen en su idioma original; la interfaz, el informe y la metodología tienen versión inglesa. Tras editar la interfaz española, regenerar y verificar ambas versiones:

```sh
python3 projects/redes-css-latam/research/build_english_page.py
python3 projects/redes-css-latam/research/build_english_js.py
```

## Rastreo preliminar

`screen_university_sites.py` procesa todos los sitios disponibles de un país en el inventario provisional, hasta cinco páginas por origen y seis orígenes en paralelo, con consulta de robots. Guarda respuestas, errores y enlaces candidatos. No incorpora personas ni cierra revisiones institucionales. El rastreo argentino publicado incluye sitios sin acceso y nombres aún pendientes de conciliación. `argentina-register-2024.json` transcribe las entradas numeradas de cuatro secciones del registro oficial de 2024; incluye repeticiones y no es una tabla de instituciones únicas. La revisión de universidades extranjeras y organismos internacionales del mismo documento debe registrarse por separado.

## Coherencia de selecciones (2026-10-23)

El mapa geográfico y el gráfico por país comparten la selección del directorio y cuentan personas únicas de todas las categorías. El subconjunto de CSS directa con base regional documentada se conserva como dato separado en el informe, sin aplicarlo silenciosamente al gráfico. La vista de afiliaciones incluye los perfiles sin vínculos documentados y agrega solo instituciones de contexto, sin incorporar otras personas fuera de los filtros. Los perfiles que aún no están en el archivo de red se muestran sin conexiones adicionales. El gráfico institucional cuenta personas únicas por institución dentro de la selección, con un máximo de diez instituciones visibles; sus barras no son categorías mutuamente excluyentes. Las ubicaciones fuera de la cartografía o pendientes se conservan en el gráfico por país y se indican en el mapa.

Verificación con el corte publicado: sin filtros, 396 personas; Brasil, 92; Brasil con CSS directa, 51; Argentina, 79. Los totales, las barras por país y los nodos de personas de la vista de afiliaciones coincidieron en estos casos; el filtro de Argentina se conservó al cambiar al inglés. Estas cifras son comprobaciones del corte y no constantes del programa.

## Actualización rápida del 25 de octubre de 2026

Se ejecutó un barrido de los 1.281 registros del inventario provisional en 22 países, sobre 1.072 orígenes web. Se reutilizó la evidencia argentina registrada el 20 de octubre. El barrido tuvo hasta cuatro páginas por origen y no leyó planes de estudio en profundidad. Resultado por registros: 655 con alguna página accesible, 459 con acceso fallido y 167 sin sitio registrado. Estos registros pueden incluir alias y no constituyen un universo conciliado de universidades únicas. El barrido está terminado; el relevamiento exhaustivo no lo está.

La definición operativa toma como referencia Lazer et al. (2020), *Computational social science: Obstacles and opportunities*, Science 369(6507), 1060–1062, DOI 10.1126/science.aaz8170. Requiere desarrollo o aplicación de métodos computacionales a datos complejos de conducta humana, incluida simulada. La temática IA, gobernanza algorítmica, humanidades digitales o ciencia de datos general no acredita por sí sola CSC.

El directorio principal aplica base institucional registrada en LATAM, no nacionalidad. Las ubicaciones externas, mixtas o pendientes quedan fuera. Esta restricción utiliza la evidencia registrada y no implica reverificación individual de todas las afiliaciones actuales. Los nombres personales se mantienen solo en equipos de programas. Los identificadores del grafo son opacos y las fuentes identificatorias se conservan en el trabajo privado. Las escuelas y eventos SICSS no se cuentan como afiliaciones institucionales.

La formación se separa entre evidencia explícita en la ficha, formación afín y pendiente de verificación. Esta clasificación rápida de metadatos no sustituye una lectura del plan. El doctorado de Complejidad Social se excluyó por instrucción explícita de Sol. El catálogo de revistas separa tres con alcance CSC explícito y diecisiete contextuales.

Los registros de consultas, fuentes revisadas, candidaturas, marcos oficiales y términos se conservan en los JSON fechados del directorio de datos. Se utilizaron rastreo automatizado y agentes de IA para búsqueda, revisión rápida y consolidación; no hubo validación humana integral.


## Interface revision, 2026-10-25

The English title is Computational Social Science, with Networks in Latin America. Both pages share bilingual map.js. The old translation builders are retained as no-op notices to prevent replacing the revised interface. Views are visible sections, not a view selector. Region and internal scope categories are not UI filters. Training is grouped by recorded program type, without implying equal CSC eligibility. The country map replaces the duplicate country lollipop chart.

The two graph views use seeded NetworkX spring layouts (research/build_layout.py, seed42,600iterations), connected nodes only. Coauthorship has47connected nodes/86edges; institutional collaboration has12connected nodes/18edges. These views omit isolates, while directory counts still include all selected profiles. Node size reflects degree. Node color uses the first recorded affiliation for people and institution ID for institutions; the five permitted colors repeat when institutions outnumber colors. No personal names are displayed in graph labels or tooltips. The reference image does not supply any graph data.

The main journal catalog is data/css-latam/journals-latam.json; international journals remain in the prior audit file but are not rendered. Google Forms incorporation URL and settings are in incorporation-form.json. Raw response data are not published. Audit logs and access failures remain downloadable source material and methodology, not dashboard panels.


## Final requested scope, 2026-10-25

Supersedes prior interface/network descriptions: the displayed graph is now a person–institution network restricted to24people with at least2distinct documented professional/teaching affiliations,15institution nodes and49unique links. It excludes article-only historical affiliations and event participation. It does not assert current simultaneous employment. Labels are full institutional names; people remain anonymous. Original coauthor and institutional publication graphs remain research data but are not displayed. All chart filters share state; program country writes the global country selection and program-type buttons select linked recorded teams. Journal catalog country and search subscribe to the same filter changes.

Program reconciliation recovered8omitted programs from the newer retained local version (7Argentina,1Chile), preserving prior source dates and metadata. There are46programs,20inArgentina; this is not a claim of a fresh curriculum review. The UFLO journal is Desarrollos en Ciencias Sociales Computacionales, not El Faro. The catalog now contains5specialist CSC/technology-and-society journals. Source-verified full institution labels are documented in institution-names.json.
