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
El script build_network.py comprueba que cada arista de coautoría se deriva del corpus y reproduce las métricas con NetworkX 3.7. Louvain utiliza resolución 1 y semilla 42. La disposición se calcula por componente y se organiza en recuadros proporcionales a su tamaño; la proximidad entre componentes no tiene interpretación analítica. Los filtros afectan la vista, no las métricas globales. El gráfico de países utiliza exclusivamente CSS directa y base regional documentada. El gráfico de instituciones cuenta perfiles CSS directa con afiliación documentada y admite múltiples afiliaciones.

### Presentación del informe
Por solicitud de la autora, el informe presenta resultados estructurales agregados y gráficos por país e institución, sin rankings nominales de personas. Los nombres se conservan en el explorador y en las fichas para facilitar la búsqueda.
