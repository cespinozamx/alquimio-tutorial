"""Genera content/level-5.json — Nivel 5: Real-Time Intelligence."""
import json, pathlib

def T(es, en): return {"es": es, "en": en}
def opt(t, why, ok=False):
    o = {"t": t, "why": why}
    if ok: o["ok"] = 1
    return o

COLNOTE = T("<i>El dataset de ejemplo trae columnas como <code>BikepointID</code>, <code>Street</code>, <code>Neighbourhood</code>, <code>No_Bikes</code> y <code>No_Empty_Docks</code>. Si en tu versión alguna se escribe distinto (por ejemplo, <code>Neighborhood</code>), ajusta el nombre en las consultas.</i>",
            "<i>The sample dataset has columns such as <code>BikepointID</code>, <code>Street</code>, <code>Neighbourhood</code>, <code>No_Bikes</code> and <code>No_Empty_Docks</code>. If a name differs in your version (e.g. <code>Neighborhood</code>), adjust it in the queries.</i>")

L = []

# ------------------------------------------------------------------ 5.1
L.append({
 "id": "l5-1", "icon": "⚡", "min": 15,
 "badge": {"e": "📡", "n": T("Explorador del tiempo real", "Real-Time Explorer")},
 "title": T("Del periódico al noticiero: ¿qué es Real-Time Intelligence?", "From newspaper to live news: what is Real-Time Intelligence?"),
 "steps": [
  {"type": "story",
   "say": T("Nivel 5. Hasta ahora procesaste datos “de ayer”. Hoy los verás <b>mientras suceden</b>. ⚡", "Level 5. So far you've processed “yesterday's” data. Today you'll see it <b>as it happens</b>. ⚡"),
   "kicker": T("Periódico vs noticiero", "Newspaper vs live news"),
   "title": T("Cuando “mañana” ya es demasiado tarde", "When “tomorrow” is already too late"),
   "body": T(
    """<p>Todo lo que hiciste hasta ahora es <b>batch</b>: como el periódico, junta las noticias del día y las imprime de noche. Perfecto para ventas o finanzas.</p>
    <p>Pero hay preguntas que no pueden esperar: ¿esta línea de embotellado se está calentando? ¿esta transacción es fraude? ¿se quedó sin bicicletas la estación del centro? Para eso necesitas el <b>noticiero en vivo</b>: procesar cada evento segundos después de que ocurre.</p>
    <p><b>Real-Time Intelligence</b> es la experiencia de Fabric para eso:</p>
    <ul><li>📡 <b>Real-Time hub</b>: el catálogo de todos los flujos de eventos de tu organización.</li>
    <li>🌊 <b>Eventstream</b>: captura, transforma y enruta eventos sin código.</li>
    <li>🏠 <b>Eventhouse</b>: base de datos optimizada para eventos con marca de tiempo, que se consulta con <b>KQL</b>.</li>
    <li>📺 <b>Real-Time Dashboard</b>: tableros que se refrescan solos.</li>
    <li>🚨 <b>Activator</b>: detecta condiciones y actúa: avisa por correo o Teams, o ejecuta un pipeline o un notebook.</li></ul>""",
    """<p>Everything you've done so far is <b>batch</b>: like a newspaper, it gathers the day's news and prints it at night. Perfect for sales or finance.</p>
    <p>But some questions can't wait: is this bottling line overheating? Is this transaction fraud? Did the downtown station run out of bikes? For that you need <b>live news</b>: processing each event seconds after it happens.</p>
    <p><b>Real-Time Intelligence</b> is Fabric's experience for exactly that:</p>
    <ul><li>📡 <b>Real-Time hub</b>: the catalog of every event stream in your organization.</li>
    <li>🌊 <b>Eventstream</b>: captures, transforms and routes events without code.</li>
    <li>🏠 <b>Eventhouse</b>: a database optimized for timestamped events, queried with <b>KQL</b>.</li>
    <li>📺 <b>Real-Time Dashboard</b>: dashboards that refresh themselves.</li>
    <li>🚨 <b>Activator</b>: detects conditions and acts: alerts by email or Teams, or runs a pipeline or a notebook.</li></ul>"""),
   "visual": "rtiFlow"},
  {"type": "match",
   "say": T("Une cada pieza con su trabajo.", "Pair each piece with its job."),
   "title": T("¿Quién hace qué en tiempo real?", "Who does what in real time?"),
   "pairs": [
     ["🌊 Eventstream", T("Recibir eventos de un IoT Hub y enviarlos a varios destinos", "Receive events from an IoT Hub and send them to several destinations")],
     ["🏠 Eventhouse", T("Guardar millones de eventos y consultarlos en segundos", "Store millions of events and query them in seconds")],
     ["📺 Real-Time Dashboard", T("Mostrar en una pantalla los eventos del último minuto", "Show the last minute's events on a screen")],
     ["🚨 Activator", T("Avisar por Teams cuando una máquina pase de 90 °C", "Alert on Teams when a machine goes above 90 °C")]]},
  {"type": "quiz",
   "say": T("No todo necesita tiempo real. Elige con criterio.", "Not everything needs real time. Choose wisely."),
   "q": T("¿Cuál de estos casos <b>sí</b> justifica Real-Time Intelligence?", "Which of these cases <b>does</b> justify Real-Time Intelligence?"),
   "opts": [
     opt(T("El reporte mensual de ventas para el consejo", "The monthly sales report for the board"), T("Un dato de hace unas horas basta. Batch es más simple y barato.", "Data from a few hours ago is enough. Batch is simpler and cheaper.")),
     opt(T("Detectar que la temperatura de un horno industrial sube fuera de rango", "Detect that an industrial oven's temperature is rising out of range"), T("¡Exacto! Cada minuto cuenta: un aviso tardío puede costar producción o seguridad.", "Exactly! Every minute counts: a late alert can cost production or safety."), True),
     opt(T("El cierre contable de fin de año", "The year-end accounting close"), T("Es un proceso batch por naturaleza.", "It's batch by nature."))]},
  {"type": "reveal", "kind": "brain",
   "say": T("Pregunta de arquitecto y de presupuesto. 💰", "An architect and budget question. 💰"),
   "prompt": T("Si el tiempo real es tan poderoso, ¿por qué no hacer <b>todo</b> en tiempo real?", "If real time is so powerful, why not do <b>everything</b> in real time?"),
   "answer": T("Porque tiene costo y complejidad. Un Eventhouse que recibe datos o consultas todo el tiempo se mantiene <b>siempre encendido</b> y consume capacidad sin parar. Si nadie va a actuar en segundos, un proceso batch cada hora o cada noche es más barato y más fácil de mantener. La pregunta clave es: <b>¿qué decisión cambia si sé esto un minuto antes?</b> Si la respuesta es “ninguna”, usa batch.",
               "Because it has cost and complexity. An Eventhouse that receives data or queries all the time stays <b>always on</b> and consumes capacity non-stop. If nobody will act within seconds, an hourly or nightly batch process is cheaper and easier to maintain. The key question is: <b>what decision changes if I know this a minute earlier?</b> If the answer is “none”, use batch.")}
 ]})

# ------------------------------------------------------------------ 5.2
L.append({
 "id": "l5-2", "icon": "🌊", "min": 25,
 "badge": {"e": "🚲", "n": T("Domador de streams", "Stream Tamer")},
 "title": T("Eventstream y Eventhouse: tu primer flujo en vivo", "Eventstream and Eventhouse: your first live stream"),
 "steps": [
  {"type": "concept",
   "say": T("Un Eventstream es como un sistema de tuberías inteligente: recibe, filtra y reparte.", "An Eventstream is like a smart plumbing system: it receives, filters and distributes."),
   "kicker": T("Capturar y enrutar", "Capture and route"),
   "title": T("Fuentes, transformaciones y destinos", "Sources, transformations and destinations"),
   "body": T(
    """<ul><li><b>Fuentes</b>: Azure Event Hubs, Azure IoT Hub, cambios (CDC) de bases de datos, Kafka, un endpoint propio para tus aplicaciones… y <b>datos de ejemplo</b> para practicar (bicicletas, taxis, bolsa de valores).</li>
    <li><b>Transformaciones sin código</b>: filtrar, elegir y renombrar campos, unir flujos y <b>agregar por ventanas de tiempo</b>.</li>
    <li><b>Destinos</b>: Eventhouse (lo más común), Lakehouse, Activator u otro stream derivado. Un mismo Eventstream puede enviar los eventos a varios destinos a la vez.</li></ul>
    <p>El <b>Eventhouse</b> es el hogar de los eventos: contiene bases de datos <b>KQL</b>, pensadas para datos con marca de tiempo que llegan sin parar. Ingiere millones de eventos y responde consultas en segundos.</p>""",
    """<ul><li><b>Sources</b>: Azure Event Hubs, Azure IoT Hub, database change data (CDC), Kafka, a custom endpoint for your apps… and <b>sample data</b> to practice with (bikes, taxis, stock market).</li>
    <li><b>No-code transformations</b>: filter, pick and rename fields, union streams and <b>aggregate over time windows</b>.</li>
    <li><b>Destinations</b>: Eventhouse (most common), Lakehouse, Activator or another derived stream. One Eventstream can send events to several destinations at once.</li></ul>
    <p>The <b>Eventhouse</b> is home for events: it holds <b>KQL</b> databases, built for timestamped data that never stops arriving. It ingests millions of events and answers queries in seconds.</p>""")},
  {"type": "concept",
   "say": T("Las ventanas de tiempo son el corazón del streaming. Mira bien el diagrama.", "Time windows are the heart of streaming. Look closely at the diagram."),
   "title": T("Ventanas de tiempo", "Time windows"),
   "body": T(
    """<p>Un stream nunca termina, así que no puedes “sumar todo”. En su lugar agregas por <b>ventanas</b>:</p>
    <ul><li><b>Tumbling</b>: bloques fijos que no se traslapan. “Total de eventos cada 5 minutos.”</li>
    <li><b>Hopping</b>: bloques fijos que sí se traslapan. “Promedio de los últimos 10 minutos, calculado cada 5.”</li>
    <li><b>Sliding</b>: la ventana avanza con cada evento. “Avísame si hay más de 3 errores en cualquier lapso de 1 minuto.”</li>
    <li><b>Session</b>: agrupa ráfagas de actividad separadas por silencios, como una sesión de usuario.</li></ul>""",
    """<p>A stream never ends, so you can't “sum everything”. Instead you aggregate over <b>windows</b>:</p>
    <ul><li><b>Tumbling</b>: fixed, non-overlapping blocks. “Total events every 5 minutes.”</li>
    <li><b>Hopping</b>: fixed blocks that overlap. “Average over the last 10 minutes, computed every 5.”</li>
    <li><b>Sliding</b>: the window moves with each event. “Alert me if there are more than 3 errors in any 1-minute span.”</li>
    <li><b>Session</b>: groups bursts of activity separated by silence, like a user session.</li></ul>"""),
   "visual": "windows"},
  {"type": "quiz",
   "say": T("Elige la ventana correcta.", "Pick the right window."),
   "q": T("El gerente quiere un conteo de bicicletas rentadas <b>cada 15 minutos exactos</b> (9:00, 9:15, 9:30…), sin que un evento cuente dos veces. ¿Qué ventana usas?",
          "The manager wants a count of rented bikes <b>every 15 minutes on the dot</b> (9:00, 9:15, 9:30…), with no event counted twice. Which window?"),
   "opts": [
     opt("Tumbling", T("¡Exacto! Bloques fijos sin traslape: cada evento cae en una sola ventana.", "Exactly! Fixed blocks with no overlap: each event lands in exactly one window."), True),
     opt("Hopping", T("Hopping se traslapa: un evento podría contar en dos ventanas.", "Hopping overlaps: one event could count in two windows.")),
     opt("Session", T("Session depende de los silencios entre eventos, no de horarios fijos.", "Session depends on gaps between events, not fixed times."))]},
  {"type": "lab",
   "say": T("¡A transmitir! En unos minutos verás eventos llegando en vivo. 🚲📡", "Let's stream! In a few minutes you'll see events arriving live. 🚲📡"),
   "title": T("Laboratorio: bicicletas en vivo hacia un Eventhouse", "Lab: live bikes into an Eventhouse"),
   "intro": T("Trabaja en <code>ws_tutor_fabric</code>. <i>Los nombres de los botones pueden variar un poco según tu versión de Fabric.</i>", "Work in <code>ws_tutor_fabric</code>. <i>Button names may vary slightly with your Fabric version.</i>"),
   "tasks": [
     {"t": T("<b>+ New item → Eventhouse</b>. Nómbralo <code>eh_bicis</code>. Se crea junto con una base de datos KQL del mismo nombre.", "<b>+ New item → Eventhouse</b>. Name it <code>eh_bicis</code>. A KQL database with the same name is created with it.")},
     {"t": T("<b>+ New item → Eventstream</b>. Nómbralo <code>es_bicis</code>.", "<b>+ New item → Eventstream</b>. Name it <code>es_bicis</code>.")},
     {"t": T("Elige <b>Use sample data</b> (o <i>Add source → Sample data</i>). Nombre de la fuente: <code>src_bicis</code>. Dataset: <b>Bicycles</b>.", "Choose <b>Use sample data</b> (or <i>Add source → Sample data</i>). Source name: <code>src_bicis</code>. Dataset: <b>Bicycles</b>.")},
     {"t": T("Agrega un destino <b>Eventhouse</b>: base de datos <code>eh_bicis</code>, nueva tabla <code>bicis</code>, formato JSON.", "Add an <b>Eventhouse</b> destination: database <code>eh_bicis</code>, new table <code>bicis</code>, JSON format.")},
     {"t": T("Pulsa <b>Publish</b>. Selecciona el nodo del stream y revisa <b>Data preview</b>: verás eventos llegando.", "Click <b>Publish</b>. Select the stream node and check <b>Data preview</b>: you'll see events arriving.")},
     {"t": T("Espera 2 o 3 minutos. Abre <code>eh_bicis</code> → base de datos KQL → tabla <code>bicis</code>: el conteo de filas va creciendo.", "Wait 2–3 minutes. Open <code>eh_bicis</code> → KQL database → <code>bicis</code> table: the row count keeps growing.")}],
   "expect": T("Un flujo vivo: <b>src_bicis → es_bicis → eh_bicis.bicis</b>, con filas nuevas cada pocos segundos. A diferencia de los niveles anteriores, <b>aquí no hay un número exacto que comparar</b>: los datos cambian mientras los miras. ¡Bienvenido al streaming! " + COLNOTE["es"],
               "A live flow: <b>src_bicis → es_bicis → eh_bicis.bicis</b>, with new rows every few seconds. Unlike earlier levels, <b>there's no exact number to check here</b>: the data changes while you look. Welcome to streaming! " + COLNOTE["en"])},
  {"type": "concept",
   "say": T("Dudas típicas de quien viene del mundo batch.", "Typical questions from people coming from batch."),
   "title": T("Dudas frecuentes", "Common questions"), "body": T("", ""),
   "callouts": [{"k": "nodumb", "qa": [
     {"q": T("¿Por qué Eventhouse y no un Lakehouse?", "Why an Eventhouse and not a Lakehouse?"),
      "a": T("El Lakehouse es excelente para lotes grandes, pero escribir miles de eventos pequeños por segundo genera muchísimos archivos diminutos. El Eventhouse está diseñado para ingerir así y para consultar por tiempo en segundos. Además, puedes exponer sus tablas en OneLake como Delta (lección 5.5).",
             "The Lakehouse is great for large batches, but writing thousands of small events per second creates tons of tiny files. The Eventhouse is built to ingest that way and to query by time in seconds. Plus, you can expose its tables in OneLake as Delta (lesson 5.5).")},
     {"q": T("¿El Eventhouse guarda los datos para siempre?", "Does the Eventhouse keep data forever?"),
      "a": T("Tú decides con dos políticas: <b>retención</b> (cuánto tiempo se conservan los datos) y <b>caché</b> (cuántos días recientes se mantienen “calientes” en almacenamiento rápido). Lo más consultado suele ser lo más reciente.",
             "You decide with two policies: <b>retention</b> (how long data is kept) and <b>caching</b> (how many recent days stay “hot” on fast storage). What's queried most is usually the most recent data.")}]}]}
 ]})

# ------------------------------------------------------------------ 5.3
L.append({
 "id": "l5-3", "icon": "🔎", "min": 25,
 "badge": {"e": "🧭", "n": T("Detective KQL", "KQL Detective")},
 "title": T("KQL: preguntas rápidas a millones de eventos", "KQL: fast questions over millions of events"),
 "steps": [
  {"type": "concept",
   "say": T("KQL se lee como una línea de producción: los datos entran por arriba y bajan por la tubería. 🏭", "KQL reads like an assembly line: data enters at the top and flows down the pipe. 🏭"),
   "kicker": T("Kusto Query Language", "Kusto Query Language"),
   "title": T("La tubería <code>|</code>", "The <code>|</code> pipe"),
   "body": T(
    """<p>Una consulta KQL empieza con una tabla y cada <code>|</code> pasa el resultado al siguiente operador, como una banda transportadora:</p>
    <ul><li><code>take 10</code>: dame 10 filas cualesquiera para explorar.</li>
    <li><code>where</code>: filtra filas.</li><li><code>project</code>: elige columnas.</li>
    <li><code>summarize … by …</code>: agrega, como GROUP BY.</li>
    <li><code>bin(tiempo, 1m)</code>: redondea el tiempo en cubetas de 1 minuto. Es el mejor amigo de las series de tiempo.</li>
    <li><code>render timechart</code>: dibuja la gráfica.</li></ul>
    <p>Hay una regla práctica: <span class="hl">filtra lo antes posible</span>, sobre todo por tiempo (<code>ago(1h)</code>), para que el motor lea menos datos.</p>""",
    """<p>A KQL query starts with a table and each <code>|</code> passes the result to the next operator, like a conveyor belt:</p>
    <ul><li><code>take 10</code>: give me any 10 rows to explore.</li>
    <li><code>where</code>: filters rows.</li><li><code>project</code>: picks columns.</li>
    <li><code>summarize … by …</code>: aggregates, like GROUP BY.</li>
    <li><code>bin(time, 1m)</code>: rounds time into 1-minute buckets. Best friend of time series.</li>
    <li><code>render timechart</code>: draws the chart.</li></ul>
    <p>A rule of thumb: <span class="hl">filter as early as possible</span>, especially by time (<code>ago(1h)</code>), so the engine reads less data.</p>"""),
   "callouts": [{"k": "key", "b": T("Si vienes de SQL, en una consulta KQL puedes escribir <code>explain</code> seguido de una consulta SQL y te devuelve su equivalente en KQL. Es una gran forma de aprender.",
                                     "If you come from SQL, in a KQL query you can write <code>explain</code> followed by a SQL query and it returns the KQL equivalent. A great way to learn.")}]},
  {"type": "match",
   "say": T("Traduce de SQL a KQL.", "Translate from SQL to KQL."),
   "title": T("Diccionario SQL → KQL", "SQL → KQL dictionary"),
   "pairs": [
     ["WHERE", "where"],
     ["SELECT col1, col2", "project col1, col2"],
     ["GROUP BY", "summarize … by"],
     ["ORDER BY … DESC", "sort by … desc"],
     ["TOP 10", "take 10 / top 10 by"]]},
  {"type": "fill",
   "say": T("Escribe tu primera consulta KQL de verdad.", "Write your first real KQL query."),
   "title": T("Estaciones casi vacías por barrio", "Nearly empty stations by neighbourhood"),
   "code": "bicis\n| {{0}} No_Bikes < 3\n| {{1}} estaciones = dcount(BikepointID) by Neighbourhood\n| top 5 by estaciones desc\n| render {{2}}",
   "blanks": [
     {"a": ["where"], "hint": T("El operador que filtra filas.", "The operator that filters rows.")},
     {"a": ["summarize"], "hint": T("El GROUP BY de KQL.", "KQL's GROUP BY.")},
     {"a": ["barchart", "columnchart"], "hint": T("Un tipo de gráfica de barras: bar + chart.", "A bar chart type: bar + chart.")}]},
  {"type": "lab",
   "say": T("Hazle preguntas a tu stream en vivo. Ejecuta cada consulta por separado.", "Ask your live stream some questions. Run each query separately."),
   "title": T("Laboratorio: explora tus bicicletas con KQL", "Lab: explore your bikes with KQL"),
   "intro": T("Abre <code>eh_bicis</code> → base de datos KQL → <b>Explore your data</b> (o crea un <b>KQL Queryset</b> llamado <code>qs_bicis</code>). Selecciona una consulta con el cursor y pulsa <b>Run</b>. " + COLNOTE["es"],
              "Open <code>eh_bicis</code> → KQL database → <b>Explore your data</b> (or create a <b>KQL Queryset</b> named <code>qs_bicis</code>). Put the cursor on a query and click <b>Run</b>. " + COLNOTE["en"]),
   "tasks": [
     {"t": T("Explora y cuenta:", "Explore and count:"), "code": "bicis\n| take 10\n\nbicis\n| count"},
     {"t": T("¿Qué barrios tienen más bicicletas en promedio?", "Which neighbourhoods have the most bikes on average?"), "code": "bicis\n| summarize promedio_bicis = avg(No_Bikes) by Neighbourhood\n| top 5 by promedio_bicis desc"},
     {"t": T("¿Cuántos eventos llegan por minuto? Mira la gráfica crecer:", "How many events arrive per minute? Watch the chart grow:"), "code": "bicis\n| where ingestion_time() > ago(30m)\n| summarize eventos = count() by bin(ingestion_time(), 1m)\n| render timechart"},
     {"t": T("Estaciones casi vacías (la consulta del ejercicio anterior):", "Nearly empty stations (the query from the previous exercise):"), "code": "bicis\n| where No_Bikes < 3\n| summarize estaciones = dcount(BikepointID) by Neighbourhood\n| top 5 by estaciones desc\n| render barchart"},
     {"t": T("Ejecuta <code>bicis | count</code> otra vez. ¿Cambió?", "Run <code>bicis | count</code> again. Did it change?")}],
   "expect": T("Las consultas responden en segundos, y el conteo crece cada vez que lo ejecutas: el stream nunca se detiene. La gráfica por minuto muestra una línea más o menos constante, que es el ritmo del generador de ejemplo. Los barrios y promedios exactos dependen de lo que llegue mientras haces el laboratorio.",
               "Queries answer in seconds, and the count grows every time you run it: the stream never stops. The per-minute chart shows a roughly steady line, the sample generator's pace. Exact neighbourhoods and averages depend on what arrives during your lab.")},
  {"type": "quiz",
   "say": T("Buenas prácticas de rendimiento en KQL.", "KQL performance good practice."),
   "q": T("Tu tabla tiene 3 años de eventos y solo te interesa la última hora. ¿Qué consulta es mejor?", "Your table has 3 years of events and you only care about the last hour. Which query is better?"),
   "opts": [
     opt(T("<code>bicis | summarize count() by Neighbourhood | where …última hora…</code>", "<code>bicis | summarize count() by Neighbourhood | where …last hour…</code>"), T("Agregas 3 años y después filtras. Mucho trabajo desperdiciado (y además ya no tendrías la columna de tiempo).", "You aggregate 3 years, then filter. Lots of wasted work (and you'd no longer have the time column).")),
     opt(T("<code>bicis | where ingestion_time() > ago(1h) | summarize count() by Neighbourhood</code>", "<code>bicis | where ingestion_time() > ago(1h) | summarize count() by Neighbourhood</code>"), T("¡Exacto! Filtrar por tiempo primero permite que el motor lea solo los datos recientes.", "Exactly! Filtering by time first lets the engine read only recent data."), True)]}
 ]})

# ------------------------------------------------------------------ 5.4
L.append({
 "id": "l5-4", "icon": "🚨", "min": 25,
 "badge": {"e": "🔔", "n": T("Centinela de alertas", "Alert Sentinel")},
 "title": T("Real-Time Dashboards y Activator: ver y actuar", "Real-Time Dashboards and Activator: see and act"),
 "steps": [
  {"type": "concept",
   "say": T("Ver en tiempo real está bien. <b>Actuar</b> en tiempo real es mejor. 🚨", "Seeing in real time is good. <b>Acting</b> in real time is better. 🚨"),
   "kicker": T("De la pantalla a la acción", "From screen to action"),
   "title": T("Tableros que se refrescan y reglas que actúan", "Dashboards that refresh and rules that act"),
   "body": T(
    """<p>Un <b>Real-Time Dashboard</b> está hecho de <b>tiles</b> (mosaicos). Cada tile es una consulta KQL con su visual, y el tablero puede refrescarse solo cada pocos segundos.</p>
    <p><b>Activator</b> es el motor de reglas: observa datos que cambian, evalúa condiciones y, cuando se cumplen, <b>actúa</b>:</p>
    <ul><li>Envía un correo o un mensaje de Teams.</li><li>Ejecuta un elemento de Fabric: pipeline, notebook, Dataflow, Copy job, función…</li></ul>
    <p>Activator lleva el estado <b>por objeto</b>. Por ejemplo, revisa cada estación de bicicletas por separado y avisa solo de la que cruzó el umbral, en lugar de una alerta general.</p>
    <p>Puedes crear reglas desde un tile del tablero (<b>Set alert</b>), desde una consulta KQL, desde un Eventstream, desde un reporte de Power BI o desde eventos de Fabric, como “un pipeline falló”.</p>""",
    """<p>A <b>Real-Time Dashboard</b> is made of <b>tiles</b>. Each tile is a KQL query with its visual, and the dashboard can refresh itself every few seconds.</p>
    <p><b>Activator</b> is the rules engine: it watches changing data, evaluates conditions and, when they're met, <b>acts</b>:</p>
    <ul><li>Sends an email or a Teams message.</li><li>Runs a Fabric item: pipeline, notebook, Dataflow, Copy job, function…</li></ul>
    <p>Activator tracks state <b>per object</b>. For example, it checks each bike station separately and alerts only on the one that crossed the threshold, instead of one generic alert.</p>
    <p>You can create rules from a dashboard tile (<b>Set alert</b>), a KQL query, an Eventstream, a Power BI report or Fabric events, such as “a pipeline failed”.</p>"""),
   "callouts": [{"k": "watch", "b": T("Una alerta basada en una consulta que corre cada 1 o 5 minutos mantiene el Eventhouse <b>siempre encendido</b>. Sin consultas ni ingesta durante varios minutos, el Eventhouse puede quedar inactivo y ahorrar capacidad. Elige la frecuencia que el negocio realmente necesita.",
                                       "An alert based on a query that runs every 1 or 5 minutes keeps the Eventhouse <b>always on</b>. With no queries or ingestion for several minutes, the Eventhouse can go idle and save capacity. Pick the frequency the business really needs.")}]},
  {"type": "order",
   "say": T("Ordena el ciclo completo: del evento a la acción.", "Order the full cycle: from event to action."),
   "title": T("Del evento a la acción", "From event to action"),
   "items": [T("Una estación de bicicletas reporta su estado", "A bike station reports its status"),
             T("Eventstream recibe el evento y lo envía al Eventhouse", "Eventstream receives the event and sends it to the Eventhouse"),
             T("El tile del tablero ejecuta su consulta KQL y se actualiza", "The dashboard tile runs its KQL query and refreshes"),
             T("Activator evalúa la regla: “menos de 2 bicicletas”", "Activator evaluates the rule: “fewer than 2 bikes”"),
             T("Llega un mensaje de Teams al equipo de logística", "A Teams message reaches the logistics team")]},
  {"type": "lab",
   "say": T("Tu primer tablero en vivo con una alerta. Esto impresiona en cualquier demo. 😎", "Your first live dashboard with an alert. This impresses in any demo. 😎"),
   "title": T("Laboratorio: tablero en vivo + alerta con Activator", "Lab: live dashboard + Activator alert"),
   "intro": T("Necesitas el Eventstream <code>es_bicis</code> en ejecución. " + COLNOTE["es"], "You need the <code>es_bicis</code> Eventstream running. " + COLNOTE["en"]),
   "tasks": [
     {"t": T("<b>+ New item → Real-Time Dashboard</b>. Nómbralo <code>rtd_bicis</code>.", "<b>+ New item → Real-Time Dashboard</b>. Name it <code>rtd_bicis</code>.")},
     {"t": T("<b>New tile</b> → fuente de datos: base de datos KQL <code>eh_bicis</code>. Consulta:", "<b>New tile</b> → data source: KQL database <code>eh_bicis</code>. Query:"), "code": "bicis\n| where ingestion_time() > ago(15m)\n| summarize eventos = count() by bin(ingestion_time(), 1m)"},
     {"t": T("Visual <b>Line chart</b>. Título: “Eventos por minuto”. <b>Apply changes</b>.", "Visual <b>Line chart</b>. Title: “Events per minute”. <b>Apply changes</b>.")},
     {"t": T("Agrega otro tile con las estaciones con menos bicicletas en este momento:", "Add another tile with the stations that have the fewest bikes right now:"), "code": "bicis\n| summarize arg_max(ingestion_time(), *) by BikepointID\n| project BikepointID, Street, Neighbourhood, No_Bikes\n| top 10 by No_Bikes asc"},
     {"t": T("En la configuración del tablero activa <b>Auto refresh</b> cada 30 segundos y guarda.", "In the dashboard settings turn on <b>Auto refresh</b> every 30 seconds and save.")},
     {"t": T("En el tile de “Eventos por minuto”, pulsa <b>… → Set alert</b>: condición <b>eventos</b> mayor que un valor un poco por debajo de lo que ves (para que se dispare), acción <b>Email</b> a ti mismo. Guárdalo en una Activator nueva: <code>act_bicis</code>.", "On the “Events per minute” tile, click <b>… → Set alert</b>: condition <b>eventos</b> greater than a value slightly below what you see (so it fires), action <b>Email</b> to yourself. Save it in a new Activator: <code>act_bicis</code>.")},
     {"t": T("Espera unos minutos y revisa tu correo. Después, <b>detén la regla</b> en <code>act_bicis</code> y el Eventstream, para no consumir capacidad.", "Wait a few minutes and check your email. Then <b>stop the rule</b> in <code>act_bicis</code> and the Eventstream, so they don't consume capacity.")}],
   "expect": T("Un tablero que se mueve solo y un correo de Activator con el valor que disparó la regla. <code>arg_max(ingestion_time(), *) by BikepointID</code> es un patrón clave: devuelve <b>el último estado de cada estación</b>. Úsalo siempre que necesites “cómo está cada cosa ahora mismo”.",
               "A dashboard that moves by itself and an Activator email with the value that fired the rule. <code>arg_max(ingestion_time(), *) by BikepointID</code> is a key pattern: it returns <b>each station's latest state</b>. Use it whenever you need “how is each thing right now”.")},
  {"type": "quiz",
   "say": T("¿Viste el truco de <code>arg_max</code>? Comprobemos.", "Did you catch the <code>arg_max</code> trick? Let's check."),
   "q": T("Cada estación envía su estado cada pocos segundos. Quieres saber cuántas bicicletas tiene <b>ahora</b> cada estación. ¿Qué haces?",
          "Each station sends its status every few seconds. You want to know how many bikes each station has <b>right now</b>. What do you do?"),
   "opts": [
     opt(T("<code>summarize sum(No_Bikes) by BikepointID</code>", "<code>summarize sum(No_Bikes) by BikepointID</code>"), T("Sumarías todas las lecturas históricas: números absurdamente grandes.", "You'd add up every historical reading: absurdly large numbers.")),
     opt(T("<code>summarize arg_max(ingestion_time(), *) by BikepointID</code>", "<code>summarize arg_max(ingestion_time(), *) by BikepointID</code>"), T("¡Exacto! Toma la fila más reciente de cada estación: su estado actual.", "Exactly! It takes each station's most recent row: its current state."), True),
     opt(T("<code>take 1</code>", "<code>take 1</code>"), T("Te da una fila cualquiera de una sola estación.", "It gives you one arbitrary row from a single station."))]},
  {"type": "quiz",
   "say": T("Activator también orquesta.", "Activator orchestrates too."),
   "q": T("Quieres que, si el pipeline nocturno de ventas falla, se reintente solo y se avise al equipo. ¿Qué combinación usas?",
          "If the nightly sales pipeline fails, you want it to retry automatically and notify the team. Which combination do you use?"),
   "opts": [
     opt(T("Activator escuchando eventos de trabajos de Fabric: al detectar la falla, ejecuta el pipeline y avisa por Teams", "Activator listening to Fabric job events: on failure it reruns the pipeline and notifies on Teams"),
         T("¡Correcto! Activator puede suscribirse a eventos de Fabric, como trabajos que fallan, y ejecutar elementos como acción.", "Correct! Activator can subscribe to Fabric events, such as failed jobs, and run items as an action."), True),
     opt(T("Revisar el Monitor hub cada mañana", "Check the Monitor hub every morning"), T("Funciona, pero es manual y reaccionas horas tarde.", "It works, but it's manual and you react hours late.")),
     opt(T("Un Real-Time Dashboard sin alertas", "A Real-Time Dashboard with no alerts"), T("Verías el problema solo si alguien está mirando la pantalla.", "You'd see the problem only if someone is watching the screen."))]}
 ]})

# ------------------------------------------------------------------ 5.5
L.append({
 "id": "l5-5", "icon": "🔀", "min": 20,
 "badge": {"e": "🏆", "n": T("Arquitecto del tiempo real", "Real-Time Architect")},
 "title": T("Batch + tiempo real juntos y el desafío final", "Batch + real time together, and the final challenge"),
 "steps": [
  {"type": "concept",
   "say": T("El mundo real no es solo batch ni solo streaming: es <b>los dos juntos</b>.", "The real world isn't just batch or just streaming: it's <b>both together</b>."),
   "kicker": T("Unir los dos mundos", "Joining both worlds"),
   "title": T("OneLake como punto de encuentro", "OneLake as the meeting point"),
   "body": T(
    """<ul><li><b>Disponibilidad en OneLake</b>: puedes activar que las tablas de una base de datos KQL se expongan en OneLake como <b>Delta</b>. Así Spark, el SQL endpoint y Power BI leen tus eventos sin copiarlos, y puedes cruzarlos con datos batch, como el catálogo de estaciones o las ventas.</li>
    <li><b>Shortcuts</b>: una base KQL también puede leer tablas Delta de un Lakehouse mediante shortcuts, por ejemplo para enriquecer eventos con una dimensión.</li>
    <li><b>Update policies y vistas materializadas</b>: transforman o agregan los eventos <b>al momento de llegar</b> dentro del Eventhouse. Es el equivalente en tiempo real de tus capas Plata y Oro.</li></ul>
    <p>A esto se le llama arquitectura <b>Lambda</b>: una ruta <b>rápida</b> (eventos, segundos) y una ruta <b>completa</b> (batch, horas), que se juntan para consumir. Cuando todo pasa por streaming, se le llama <b>Kappa</b>.</p>""",
    """<ul><li><b>OneLake availability</b>: you can have a KQL database's tables exposed in OneLake as <b>Delta</b>. Then Spark, the SQL endpoint and Power BI read your events without copying, and you can join them with batch data, like the station catalog or sales.</li>
    <li><b>Shortcuts</b>: a KQL database can also read Delta tables from a Lakehouse via shortcuts, for example to enrich events with a dimension.</li>
    <li><b>Update policies and materialized views</b>: transform or aggregate events <b>as they arrive</b> inside the Eventhouse. It's the real-time equivalent of your Silver and Gold layers.</li></ul>
    <p>This is called a <b>Lambda</b> architecture: a <b>fast</b> path (events, seconds) and a <b>complete</b> path (batch, hours), joined for consumption. When everything flows through streaming, it's called <b>Kappa</b>.</p>"""),
   "visual": "lambdaArch"},
  {"type": "quiz",
   "say": T("Une los dos mundos.", "Bring both worlds together."),
   "q": T("Quieres un reporte de Power BI que cruce los eventos de las bicicletas (Eventhouse) con el catálogo de estaciones y su zona comercial (Lakehouse). ¿Qué haces?",
          "You want a Power BI report joining bike events (Eventhouse) with the station catalog and its business zone (Lakehouse). What do you do?"),
   "opts": [
     opt(T("Exportar los eventos a CSV cada hora y cargarlos al Lakehouse", "Export events to CSV every hour and load them into the Lakehouse"), T("Duplicas datos, agregas latencia y piezas manuales.", "You duplicate data and add latency and manual parts.")),
     opt(T("Activar la disponibilidad en OneLake de la tabla KQL y unirla con el catálogo como cualquier tabla Delta", "Turn on OneLake availability for the KQL table and join it with the catalog like any Delta table"),
         T("¡Exacto! Una sola copia de los eventos, visible para todos los motores de Fabric.", "Exactly! One copy of the events, visible to every Fabric engine."), True),
     opt(T("No se puede: batch y tiempo real viven separados", "It can't be done: batch and real time live apart"), T("En Fabric, OneLake es justamente el punto de encuentro.", "In Fabric, OneLake is exactly the meeting point."))]},
  {"type": "reveal", "kind": "pencil",
   "say": T("Diseña con tus palabras. Piensa en una embotelladora.", "Design it in your own words. Think of a bottling plant."),
   "prompt": T("Una embotelladora quiere: (1) alertas en segundos si un sensor de presión sale de rango y (2) un reporte diario de eficiencia por línea. Dibuja mentalmente la arquitectura: ¿qué va por la ruta rápida y qué por la lenta?",
               "A bottling plant wants: (1) alerts within seconds if a pressure sensor goes out of range and (2) a daily efficiency report per line. Picture the architecture: what goes on the fast path and what on the slow one?"),
   "answer": T("<b>Ruta rápida</b>: sensores → IoT Hub → Eventstream → Eventhouse, con Activator para la alerta de presión y un Real-Time Dashboard para piso de planta. <b>Ruta lenta</b>: la tabla de eventos expuesta en OneLake + datos de producción del ERP → notebooks de Plata y Oro → Warehouse con modelo estrella → modelo semántico Direct Lake → reporte diario de eficiencia. Un solo dato de origen y dos velocidades de consumo.",
               "<b>Fast path</b>: sensors → IoT Hub → Eventstream → Eventhouse, with Activator for the pressure alert and a Real-Time Dashboard for the shop floor. <b>Slow path</b>: the event table exposed in OneLake + ERP production data → Silver and Gold notebooks → Warehouse star schema → Direct Lake semantic model → daily efficiency report. One source of data, two consumption speeds.")},
  {"type": "match",
   "say": T("🏁 <b>Desafío final del Nivel 5.</b> Necesidad → pieza.", "🏁 <b>Level 5 final challenge.</b> Need → piece."),
   "title": T("Desafío: el arquitecto del tiempo real", "Challenge: the real-time architect"),
   "pairs": [
     [T("Recibir 50,000 eventos por segundo de sensores IoT", "Receive 50,000 events per second from IoT sensors"), "Eventstream"],
     [T("Saber el estado actual de cada máquina", "Know each machine's current state"), "arg_max(…) by …"],
     [T("Pantalla en piso de planta que se refresca sola", "A shop-floor screen that refreshes itself"), "Real-Time Dashboard"],
     [T("Detener la línea si la temperatura pasa de 90 °C", "Stop the line if temperature exceeds 90 °C"), "Activator"],
     [T("Cruzar eventos con datos batch del ERP", "Join events with batch ERP data"), T("Disponibilidad en OneLake", "OneLake availability")]]},
  {"type": "quiz",
   "say": T("La última del nivel. ¡Ya casi! 🎓", "The level's last one. Almost there! 🎓"),
   "q": T("Un cliente pide “todo en tiempo real”, incluido el reporte mensual de cierre contable. ¿Qué le recomiendas?",
          "A client asks for “everything in real time”, including the monthly accounting close report. What do you recommend?"),
   "opts": [
     opt(T("Aceptar: si el cliente lo pide, se hace", "Accept: if the client asks, we build it"), T("Pagaría capacidad constante por algo que se consulta una vez al mes.", "They'd pay for constant capacity for something queried once a month.")),
     opt(T("Tiempo real solo donde una decisión cambia si se sabe antes; el cierre mensual, en batch", "Real time only where a decision changes if known sooner; the monthly close, in batch"),
         T("¡Criterio de arquitecto! Cada dato a la velocidad que el negocio necesita, ni más ni menos. 🏆", "Architect-grade judgment! Each piece of data at the speed the business needs, no more, no less. 🏆"), True)]}
 ]})

out = {"id": 5,
       "title": T("Real-Time Intelligence", "Real-Time Intelligence"),
       "desc": T("Eventstream, Eventhouse, KQL, Real-Time Dashboards, alertas con Activator y arquitecturas batch + tiempo real.", "Eventstream, Eventhouse, KQL, Real-Time Dashboards, Activator alerts and batch + real-time architectures."),
       "lessons": L}
dst = pathlib.Path(__file__).resolve().parent.parent / "content/level-5.json"
dst.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", dst, sum(len(l["steps"]) for l in L), "steps")
