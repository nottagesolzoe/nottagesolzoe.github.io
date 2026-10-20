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
