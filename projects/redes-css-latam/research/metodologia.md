# Protocolo del relevamiento CSS en América Latina

Versión: 2026-10-20. Estado: relevamiento en curso, cobertura no exhaustiva.

## Unidad de observación y alcance
Se registran personas, instituciones, programas y publicaciones con evidencia pública de investigación o aplicación de métodos computacionales a fenómenos sociales. Se distinguen CSS directa, datos sociales aplicados, áreas afines y especialidad individual pendiente. La pertenencia a un centro no basta para confirmar especialidad individual. El país corresponde a la base institucional documentada, no a nacionalidad. Los vínculos con América Latina desde fuera de la región se conservan por separado.

## Cambio de estrategia solicitado el 20 de octubre
El relevamiento inicial partió de centros, equipos y referencias. Se incorpora una búsqueda por país, comenzando por Argentina: inventario institucional, oferta académica y programas, equipos docentes, perfiles individuales y publicaciones. El mismo recorrido debe repetirse en los demás países. Las instituciones sin revisión y los casos sin resultados deben conservarse en el registro; la falta de hallazgos no demuestra ausencia de actividad.

## Fuentes y trazabilidad
Cada incorporación conserva URL, tipo de fuente y fecha de consulta. Prioridad: sitios institucionales, páginas oficiales de programas, repositorios y editoriales. arXiv permite identificar preprints y coautorías; Crossref facilita metadatos bibliográficos. Google Scholar fue intentado pero no estuvo accesible mediante la consulta automatizada; no se declara como fuente efectivamente extraída. LinkedIn se conserva solo cuando el perfil público identifica inequívocamente a la persona. No se infieren direcciones de correo. No se contacta a nadie.

## Validación y deduplicación
La similitud de títulos solo genera candidatos. Se excluyen coincidencias falsas después de comparar títulos y autores. Ejemplo detectado: la búsqueda de Historias del Internet en Colombia devolvió Historias del arte en Colombia; no corresponde incorporarlo. Publicaciones duplicadas por DOI se cuentan una vez. Los preprints y versiones editoriales del mismo trabajo deben consolidarse. La normalización de tildes y orden apellido/nombre no autoriza fusiones ambiguas; las equivalencias adicionales se documentan en una tabla de alias.

## Relaciones
La afiliación es una relación persona-institución y conserva su fuente y temporalidad disponible. La coautoría requiere compartir una publicación incluida. La coincidencia de instituciones en un artículo se deriva exclusivamente de sus afiliaciones documentadas para ese trabajo. No se infiere colaboración institucional de la afiliación actual de los coautores, ni coautoría de compartir programa, centro o evento.

## Análisis estructural
Red no dirigida de coautoría, sin lazos propios; peso igual al número de trabajos compartidos del corpus. Grado: número de coautores distintos. Fuerza: suma de pesos. Intermediación: caminos mínimos no ponderados, normalizada. Centralidad de eigenvector: calculada y comparada dentro del componente principal, debido a la desconexión del grafo. Comunidades: Louvain ponderado con semilla 42. Las estadísticas describen el corpus observado y no permiten estimar prestigio, tamaño total del campo ni crecimiento temporal.

## Registro continuo
Guardar los insumos sin sobreescribirlos; registrar adiciones, exclusiones, correcciones y motivos. Las fechas de revisión deben reflejar una comprobación efectivamente realizada, no la fecha de exportación. Publicar con los datos el código de construcción, el corpus depurado, la cobertura y las limitaciones. Cada actualización requiere recalcular métricas y verificar consistencia de identificadores y relaciones.

## Pendientes explícitos
Completar el inventario de universidades de Argentina y repetirlo país por país. Revisar programas y equipos, incluyendo centros no universitarios y consultoras. Completar correos y LinkedIn solo con evidencia. Ampliar el corpus bibliográfico para reducir dependencia de los centros iniciales y sesgos de indexación e idioma.

## Corte publicado el 20 de octubre de 2026
El directorio contiene 288 personas y 39 organizaciones. Se recuperaron 77 registros bibliográficos candidatos; el corpus depurado retiene 40 trabajos. La red proyectada contiene 137 autores y 315 pares de coautores. Ocho trabajos aportan afiliaciones recuperadas para la red institucional. Las biografías del directorio conservan sus fechas de revisión originales.

La extracción bibliográfica generó una coincidencia falsa entre Historias del Internet en Colombia e Historias del arte en Colombia, que fue excluida. Se consolidaron registros repetidos de Citizens at the forefront of the constitutional debate por DOI. Las exclusiones, metadatos y alias de autor están disponibles en los JSON públicos.

La revisión de programas incorporó el plantel docente publicado por UNSAM y autoridades del programa conjunto UNC-UNVM. La condición de docente en un programa CSS acredita participación formativa, pero no residencia ni producción individual. Los perfiles de docentes sin verificación de base territorial quedan separados de los recuentos regionales confirmados. Los cargos administrativos en un programa se clasifican en datos sociales aplicados, pendientes de revisión bibliográfica individual.

Los registros de formación contienen fechas vencidas y ofertas sin fechas verificadas. No constituyen una lista de convocatorias abiertas. Las fichas que conservan anuncios de inscripción asociados a cohortes iniciadas se señalan explícitamente.

### Estado de cobertura institucional
Se localizó el listado oficial argentino de instituciones universitarias de 2024: https://www.argentina.gob.ar/sites/default/files/2024_m12_-_instituciones_universitarias_1.pdf. Su antigüedad exige contrastar altas y cambios posteriores. El inventario completo no fue incorporado ni revisado exhaustivamente en este corte. Se revisaron programas y páginas en Argentina, Brasil, Chile, Colombia, Perú, Uruguay y Costa Rica. El resto de los países conserva la cobertura preliminar del directorio; no se declara finalizado el recorrido país por país.

### Reproducción y decisiones de visualización
El script build_network.py comprueba que cada arista de coautoría se deriva del corpus y reproduce las métricas con NetworkX 3.7. Louvain utiliza resolución 1 y semilla 42. La disposición se calcula por componente y se organiza en recuadros proporcionales a su tamaño; la proximidad entre componentes no tiene interpretación analítica. El archivo de análisis conserva métricas del corpus completo. Los indicadores visibles del dashboard se recalculan con los filtros activos, según la actualización documentada abajo. El gráfico de países utiliza exclusivamente CSS directa y base regional documentada. El gráfico de instituciones cuenta perfiles CSS directa con afiliación documentada y admite múltiples afiliaciones.

### Presentación del informe
Por solicitud de la autora, el informe presenta resultados estructurales agregados y gráficos por país e institución, sin rankings nominales de personas. Los nombres se conservan en el explorador y en las fichas para facilitar la búsqueda.

## Actualización del dashboard y oferta universitaria (20 de octubre de 2026)
La autoría corresponde a Sol Zoe Nottage. La presentación utiliza redacción impersonal.

Se amplió la revisión de oferta argentina mediante consultas por dominio universitario y lectura de programas, contenidos y equipos. Se incorporaron ofertas de UTDT, Austral, ITBA, UBA, UTN La Plata, UNLP, UNCUYO y FLACSO. UdeSA, UNR y UNL cuentan con búsquedas adicionales registradas, sin declarar completa la revisión de sus catálogos. El registro incluye 25 programas y 318 personas; las incorporaciones provenientes de programas de IA general se clasifican como áreas afines, no como CSS confirmada.

La Diplomatura en IA y Políticas Públicas de UTDT se registró bajo su nombre oficial. Se separó del MicroMaster en Data Analytics. Se detectaron versiones incompatibles de horas y duración en la página UTDT y de mes de inicio en ITBA; no se eligió arbitrariamente una versión. Dos páginas de UNCUYO devolvieron HTTP 403; sus anuncios indexados se conservan con verificación ampliada pendiente. Los docentes se incorporan por participación documentada, con base laboral por confirmar cuando no se dispone de perfil individual.

El mapa utiliza geometrías públicas de Natural Earth a escala 1:110m. El país identifica un vínculo institucional documentado o previamente consignado en el directorio; no es un domicilio, nacionalidad ni coordenada personal. No se infieren ciudades. Las personas fuera del recorte latinoamericano permanecen accesibles mediante filtros.

### Texto e indicadores dinámicos
Los filtros de país, región, institución, área, tema y búsqueda se combinan por intersección. Los indicadores de personas y organizaciones cuentan los registros que cumplen esos filtros. Los programas se seleccionan por país, texto, equipo documentado y vínculo institucional, según el filtro activo. Los recuentos no implican convocatorias abiertas.

Para los indicadores bibliográficos se seleccionan los autores que cumplen los filtros y se conserva cada arista solo cuando ambos extremos pertenecen a esa selección (subgrafo inducido). El recuento de publicaciones incluye trabajos con al menos un autor seleccionado. Por ello puede haber publicaciones aun cuando no existan pares de coautores dentro de la selección. Se recalculan autores, aristas, componentes, tamaño del componente principal y grado máximo. El gráfico de países mantiene el subconjunto CSS directa con base regional documentada; el mapa muestra el directorio más amplio, con sus categorías diferenciadas.

Esta especificación reemplaza la decisión inicial de mantener las métricas fijas al filtrar. Las centralidades archivadas en network.json describen el corpus completo; el texto dinámico del informe usa los recuentos y componentes calculados en el navegador. No se muestran rankings nominales en el informe.

## Autoría y asistencia de inteligencia artificial
La autoría del proyecto corresponde a Sol Zoe Nottage. Se utilizó ChatGPT (OpenAI), mediante Codex, para asistir la búsqueda de fuentes, la programación de descargas y extracción de páginas públicas, la estructuración de datos y la implementación del análisis y del dashboard. Las respuestas generadas no se consideran fuentes bibliográficas ni evidencia de afiliación. La evidencia corresponde a las páginas, registros y publicaciones enlazados. No se atribuye coautoría a la herramienta.

Referencia de la herramienta: OpenAI. (2026). *ChatGPT* [Herramienta de inteligencia artificial, utilizada mediante Codex]. https://chatgpt.com/ . Consulta y uso documentado: 20 de octubre de 2026. No se afirma una versión específica del modelo.

## Inventario sudamericano y orden de revisión
El recorrido comienza por América del Sur y continúa posteriormente hacia América Central, México y el Caribe latinoamericano. Guyana y Surinam se incluyen en esta etapa por alcance geográfico sudamericano y se distinguen del alcance lingüístico latinoamericano.

La unidad inicial es un registro de institución en una fuente. Se descargaron nóminas oficiales de Chile, Colombia, Ecuador y Perú y listados institucionales de Argentina (CIN, universidades públicas) y Paraguay (CONES, oferta académica). Un directorio secundario de dominios (Hipo) aporta candidatos adicionales para todos los países sudamericanos. Este directorio no certifica reconocimiento oficial ni exhaustividad. La tabla colombiana recuperada indica actualización en 2022; su vigencia requiere comprobación.

La conciliación automática utiliza país y nombre normalizado sin diferencias de mayúsculas o tildes. No fusiona nombres semejantes, traducciones ni siglas. Los registros restantes pueden referirse a una misma institución y no deben interpretarse como un recuento de universidades únicas. Los códigos y sedes del registro colombiano se conservan como evidencia dentro de cada nombre. Los sitios del directorio secundario quedan pendientes de confirmación institucional.

Los estados de revisión de programas, institutos, personas y publicaciones se registran por separado. En este nuevo inventario están pendientes; las revisiones parciales del directorio anterior todavía deben vincularse a estos identificadores. No evaluado no significa ausencia de actividad. La presencia en una nómina no equivale a revisión de la web universitaria.

## Solicitudes de incorporación
La página ofrece un formulario público mediante GitHub Issues. Solicita nombre, país, institución, descripción del trabajo y fuentes públicas; correo institucional y LinkedIn son opcionales. Cada solicitud requiere revisión y deduplicación antes de su incorporación. Las solicitudes no alimentan automáticamente los recuentos del dashboard.

## Procedimiento de investigación por país y ampliación al sector público
La revisión adopta el protocolo operativo publicado en `protocolo-operativo.json`. El marco universitario debe conciliarse con una nómina oficial antes de calcular porcentajes de cobertura. La revisión de cada web comprende catálogos, unidades académicas, programas pertinentes, docentes, eventos, centros y organizaciones asociadas. La inclusión exige aplicación social explícita de IA, métodos computacionales o análisis de datos. La IA general no satisface ese criterio.

La unidad de evidencia es un vínculo documentado: persona-programa, persona-evento, persona-equipo o institución-proyecto. Se conservan rol, URL, fecha de consulta y temporalidad disponible. Participar en una charla no acredita empleo en la universidad organizadora. Compartir una charla o un programa no constituye coautoría. La condición de integrante del ecosistema no acredita por sí misma una especialidad investigadora individual.

El sector público constituye un marco complementario: organismos nacionales, provincias o estados y municipios. Se registran portales de datos abiertos, unidades de análisis, laboratorios públicos y personas con funciones documentadas. Su clasificación inicial corresponde a datos sociales aplicados o infraestructura de datos públicos; CSS directa requiere evidencia adicional. Los portales, organismos responsables y equipos se distinguen para evitar contar un mismo organismo varias veces. Las jurisdicciones todavía no revisadas permanecen pendientes.

El rastreo automatizado solo identifica páginas candidatas. Las coincidencias de palabras clave no producen incorporaciones automáticas ni justifican declarar una institución revisada. El protocolo exige registro de páginas consultadas, obstáculos y resultados, incluidos casos sin hallazgos. El marco de think tanks y consultoras se amplía mediante directorios y referencias institucionales, sin atribuirle exhaustividad.

## Concentración territorial: análisis previsto
La medición por provincia, estado y ciudad queda pendiente de verificar ubicaciones institucionales. Se distinguirán personas, instituciones e iniciativas; un portal no se contará además como un organismo independiente sin justificar la unidad. La localización no se inferirá de una docencia virtual ni se confundirá con residencia personal.

Se calcularán frecuencias, proporciones sobre registros geolocalizados del país seleccionado y el índice de Herfindahl (suma de las proporciones territoriales al cuadrado). Los casos con varias ubicaciones requerirán asignación fraccionaria documentada. Se informarán casos sin localización, regla temporal y cobertura por jurisdicción. Estos indicadores describirán la concentración del relevamiento observado, no la del campo completo. No se publican todavía estimaciones provinciales.
