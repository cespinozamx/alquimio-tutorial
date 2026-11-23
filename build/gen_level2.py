"""Genera site/content/level-2.json — Nivel 2: Ingesta de datos."""
import json, pathlib

def T(es, en): return {"es": es, "en": en}
def opt(t, why, ok=False):
    o = {"t": t, "why": why}
    if ok: o["ok"] = 1
    return o

lessons = []

# ------------------------------------------------------------------ 2.1
lessons.append({
 "id": "l2-1", "icon": "🧭", "min": 15,
 "badge": {"e": "🗺️", "n": T("Cartógrafo de datos", "Data Cartographer")},
 "title": T("El mapa de la ingesta: ¿qué herramienta uso?", "The ingestion map: which tool do I use?"),
 "steps": [
  {"type": "story",
   "say": T("Bienvenido al Nivel 2. Hoy aprendes a <b>elegir bien</b>, que vale más que saber usar una sola herramienta.",
            "Welcome to Level 2. Today you learn to <b>choose well</b>, which beats knowing just one tool."),
   "kicker": T("Una historia de mudanzas", "A moving-day story"),
   "title": T("Cinco formas de llevar tus cosas a casa nueva", "Five ways to get your stuff to a new home"),
   "body": T(
    """<p>Imagina que te mudas. Tienes varias opciones, y cada una sirve para algo distinto:</p>
    <ul><li>🔗 <b>Shortcut</b>: no te llevas nada; abres una <i>ventana</i> a la casa vieja y usas las cosas desde ahí.</li>
    <li>📦 <b>Copy job</b>: contratas una mudanza que, además, <span class="hl">regresa cada semana solo por lo nuevo</span>.</li>
    <li>🧹 <b>Dataflow Gen2</b>: una mudanza que limpia, dobla y etiqueta mientras empaca.</li>
    <li>🧭 <b>Pipeline</b>: el jefe de obra que coordina camiones, pintores y electricistas en el orden correcto.</li>
    <li>🪞 <b>Mirroring</b>: un espejo mágico: lo que cambia en la casa vieja aparece en la nueva casi al instante.</li></ul>
    <p>Este diagrama es tu brújula. Vuelve a él cada vez que dudes.</p>""",
    """<p>Imagine you're moving. You have several options, each good for something different:</p>
    <ul><li>🔗 <b>Shortcut</b>: you take nothing; you open a <i>window</i> into the old house and use things from there.</li>
    <li>📦 <b>Copy job</b>: you hire movers who also <span class="hl">come back every week for just the new stuff</span>.</li>
    <li>🧹 <b>Dataflow Gen2</b>: movers who clean, fold and label while they pack.</li>
    <li>🧭 <b>Pipeline</b>: the site foreman who coordinates trucks, painters and electricians in the right order.</li>
    <li>🪞 <b>Mirroring</b>: a magic mirror: whatever changes in the old house shows up in the new one almost instantly.</li></ul>
    <p>This diagram is your compass. Come back to it whenever you're unsure.</p>"""),
   "visual": "ingestMap"},
  {"type": "concept",
   "say": T("Fíjate: <b>todas</b> terminan escribiendo en OneLake, en Delta.", "Notice: <b>all</b> of them end up writing to OneLake, in Delta."),
   "title": T("Las herramientas de ingesta en una mirada", "Ingestion tools at a glance"),
   "body": T("<p>Todas viven en Fabric y todas consumen de la misma capacidad. La diferencia está en <b>cuánto control</b> necesitas y <b>quién</b> las usa.</p>",
             "<p>They all live in Fabric and all draw from the same capacity. The difference is <b>how much control</b> you need and <b>who</b> uses them.</p>"),
   "cards": [
     {"e": "🔗", "n": "Shortcut", "d": T("Lee datos donde ya están (OneLake, ADLS, S3, GCS…) sin copiarlos.", "Reads data where it already lives (OneLake, ADLS, S3, GCS…) without copying."), "star": True},
     {"e": "📦", "n": "Copy job", "d": T("Copia simple de muchas tablas, completa o incremental (watermark o CDC). Él guarda el estado.", "Simple copy of many tables, full or incremental (watermark or CDC). It keeps the state for you."), "star": True},
     {"e": "🧭", "n": "Pipeline", "d": T("Orquesta actividades: copiar, ejecutar notebooks, decidir, repetir, avisar.", "Orchestrates activities: copy, run notebooks, branch, loop, notify."), "star": True},
     {"e": "🧹", "n": "Dataflow Gen2", "d": T("Power Query en la nube: conecta y transforma con clics.", "Power Query in the cloud: connect and transform with clicks.")},
     {"e": "🪞", "n": "Mirroring", "d": T("Réplica continua de bases de datos completas hacia OneLake.", "Continuous replication of whole databases into OneLake.")},
     {"e": "📓", "n": "Notebook", "d": T("Código Spark: máxima flexibilidad (lo verás a fondo en el Nivel 3).", "Spark code: maximum flexibility (deep dive in Level 3).")}],
   "callouts": [{"k": "key", "b": T("<b>Regla de oro:</b> si no necesitas mover el dato, no lo muevas (shortcut). Si necesitas moverlo, usa la herramienta <b>más simple</b> que resuelva el problema.",
                                     "<b>Golden rule:</b> if you don't need to move the data, don't (shortcut). If you must move it, use the <b>simplest</b> tool that solves the problem.")}]},
  {"type": "match",
   "say": T("Une cada situación con su herramienta. Usa la brújula del paso 1 si dudas.", "Pair each situation with its tool. Use the compass from step 1 if unsure."),
   "title": T("Situación → herramienta", "Situation → tool"),
   "pairs": [
     [T("Consultar archivos de un partner en Amazon S3 sin duplicarlos", "Query a partner's files in Amazon S3 without duplicating them"), T("🔗 Shortcut", "🔗 Shortcut")],
     [T("Copiar 40 tablas cada noche, solo lo que cambió", "Copy 40 tables every night, only what changed"), T("📦 Copy job", "📦 Copy job")],
     [T("Copiar, luego transformar y avisar si algo falla", "Copy, then transform, and alert if anything fails"), T("🧭 Pipeline", "🧭 Pipeline")],
     [T("Un analista limpia un Excel con clics", "An analyst cleans an Excel file with clicks"), T("🧹 Dataflow Gen2", "🧹 Dataflow Gen2")],
     [T("Ver en Fabric los cambios de Azure SQL casi al instante", "See Azure SQL changes in Fabric almost instantly"), T("🪞 Mirroring", "🪞 Mirroring")]]},
  {"type": "quiz",
   "say": T("Caso típico de cliente. Piensa en lo <b>simple</b>.", "Classic client case. Think <b>simple</b>."),
   "q": T("Debes copiar 25 tablas de un SQL Server en el centro de datos del cliente hacia el Lakehouse cada noche, solo con los cambios y sin lógica adicional. ¿Qué eliges?",
          "You must copy 25 tables from a SQL Server in the client's data center to the Lakehouse every night, only the changes, with no extra logic. What do you pick?"),
   "opts": [
     opt(T("Un notebook con un bucle en PySpark", "A notebook with a PySpark loop"), T("Funciona, pero escribes y mantienes código para algo que una herramienta ya resuelve.", "It works, but you'd write and maintain code for something a tool already solves.")),
     opt(T("Copy job en modo incremental, usando un gateway de datos on-premises", "Copy job in incremental mode, through an on-premises data gateway"),
         T("¡Exacto! Copy job lleva el control del watermark por ti, y el <b>on-premises data gateway</b> le da acceso seguro al servidor dentro de la red del cliente.",
           "Exactly! Copy job tracks the watermark for you, and the <b>on-premises data gateway</b> gives it secure access to the server inside the client's network."), True),
     opt(T("Un shortcut al SQL Server", "A shortcut to the SQL Server"), T("Los shortcuts apuntan a almacenamiento de archivos/tablas (OneLake, ADLS, S3…), no a un SQL Server.", "Shortcuts point to file/table storage (OneLake, ADLS, S3…), not to a SQL Server.")),
     opt(T("Exportar a CSV y subirlos a mano", "Export to CSV and upload by hand"), T("Cada noche, 25 tablas, a mano… tu yo del futuro llora. 😅", "Every night, 25 tables, by hand… future you is crying. 😅"))]},
  {"type": "quiz",
   "say": T("Ahora piensa en <b>quién</b> va a usar la herramienta.", "Now think about <b>who</b> will use the tool."),
   "q": T("El área de Finanzas (no programa, pero domina Excel y Power BI) quiere limpiar un archivo de SharePoint y dejarlo como tabla en el Lakehouse. ¿Qué le recomiendas?",
          "The Finance team (they don't code, but they master Excel and Power BI) wants to clean a SharePoint file and land it as a Lakehouse table. What do you recommend?"),
   "opts": [
     opt(T("Dataflow Gen2", "Dataflow Gen2"), T("Sí: es Power Query, la misma experiencia que ya conocen de Excel y Power BI, con destino al Lakehouse.", "Yes: it's Power Query, the same experience they know from Excel and Power BI, with the Lakehouse as destination."), True),
     opt(T("Notebook en PySpark", "PySpark notebook"), T("Potente, pero los obliga a programar.", "Powerful, but it forces them to code.")),
     opt(T("Mirroring", "Mirroring"), T("Mirroring replica bases de datos, no archivos de SharePoint.", "Mirroring replicates databases, not SharePoint files."))]},
  {"type": "concept",
   "say": T("Estas preguntas me las hacen en <b>todos</b> los cursos.", "I get these questions in <b>every</b> class."),
   "title": T("Dudas frecuentes", "Common questions"), "body": T("", ""),
   "callouts": [{"k": "nodumb", "qa": [
     {"q": T("¿Copy job o pipeline?", "Copy job or pipeline?"),
      "a": T("Si solo necesitas mover datos (completo o incremental), Copy job es más simple. Si necesitas pasos encadenados, condiciones, bucles o avisos, usa un pipeline. Y un pipeline puede ejecutar un Copy job como una de sus actividades.",
             "If you only need to move data (full or incremental), Copy job is simpler. If you need chained steps, conditions, loops or alerts, use a pipeline. A pipeline can also run a Copy job as one of its activities.")},
     {"q": T("¿Qué es el on-premises data gateway?", "What is the on-premises data gateway?"),
      "a": T("Un agente que instalas en un servidor dentro de la red del cliente. Abre un canal seguro de salida hacia Fabric para que este pueda leer fuentes que no están expuestas a internet.",
             "An agent you install on a server inside the client's network. It opens a secure outbound channel to Fabric so it can read sources that aren't exposed to the internet.")},
     {"q": T("¿Puedo combinar herramientas?", "Can I combine tools?"),
      "a": T("¡Claro! Lo normal en un proyecto real: shortcuts para lo que ya está en la nube, Mirroring para bases operacionales, Copy job para cargas masivas y un pipeline que orquesta los notebooks de transformación.",
             "Of course! That's normal in real projects: shortcuts for what's already in the cloud, Mirroring for operational databases, Copy job for bulk loads and a pipeline orchestrating the transformation notebooks.")}]}]}
 ]})

# ------------------------------------------------------------------ 2.2
lessons.append({
 "id": "l2-2", "icon": "🎼", "min": 25,
 "badge": {"e": "🎻", "n": T("Director de orquesta", "Orchestra Conductor")},
 "title": T("Pipelines: el director de orquesta", "Pipelines: the orchestra conductor"),
 "steps": [
  {"type": "concept",
   "say": T("Un pipeline no transforma datos por sí mismo: <b>dirige</b> a quienes lo hacen.", "A pipeline doesn't transform data by itself: it <b>directs</b> those who do."),
   "kicker": T("Orquestación", "Orchestration"),
   "title": T("Actividades + dependencias", "Activities + dependencies"),
   "body": T(
    """<p>Un <b>pipeline</b> es un flujo de <b>actividades</b> conectadas por <b>dependencias</b>. Cada flecha dice <i>cuándo</i> corre la siguiente actividad:</p>
    <ul><li>✅ <b>On success</b>: solo si la anterior terminó bien.</li><li>❌ <b>On failure</b>: solo si falló.</li>
    <li>🔁 <b>On completion</b>: en cualquier caso, haya terminado bien o mal.</li><li>⏭️ <b>On skip</b>: si la anterior no se ejecutó.</li></ul>
    <p>Además tiene <b>parámetros</b> (valores que recibe al iniciar), <b>variables</b> (valores que cambian durante la ejecución) y <b>programaciones</b> (cuándo corre).</p>""",
    """<p>A <b>pipeline</b> is a flow of <b>activities</b> connected by <b>dependencies</b>. Each arrow says <i>when</i> the next activity runs:</p>
    <ul><li>✅ <b>On success</b>: only if the previous one succeeded.</li><li>❌ <b>On failure</b>: only if it failed.</li>
    <li>🔁 <b>On completion</b>: either way, success or failure.</li><li>⏭️ <b>On skip</b>: if the previous one didn't run.</li></ul>
    <p>It also has <b>parameters</b> (values received at start), <b>variables</b> (values that change during the run) and <b>schedules</b> (when it runs).</p>"""),
   "visual": "pipelineFlow"},
  {"type": "concept",
   "say": T("No memorices la lista: aprende las <b>familias</b>.", "Don't memorize the list: learn the <b>families</b>."),
   "title": T("Las familias de actividades", "Activity families"),
   "body": T("", ""),
   "cards": [
     {"e": "🚚", "n": T("Mover", "Move"), "d": T("Copy data, Copy job", "Copy data, Copy job"), "star": True},
     {"e": "⚗️", "n": T("Transformar", "Transform"), "d": T("Notebook, Dataflow, Stored procedure, Script", "Notebook, Dataflow, Stored procedure, Script"), "star": True},
     {"e": "🔀", "n": T("Controlar el flujo", "Control flow"), "d": T("Lookup, ForEach, If Condition, Set variable, Get Metadata, Invoke pipeline, Wait", "Lookup, ForEach, If Condition, Set variable, Get Metadata, Invoke pipeline, Wait")},
     {"e": "📣", "n": T("Avisar", "Notify"), "d": T("Teams, Office 365 Outlook", "Teams, Office 365 Outlook")}],
   "callouts": [{"k": "watch", "b": T("Si conectas tu notificación de error con <b>On completion</b>, ¡te llegará un correo también cuando todo salga bien! Para alertas de error usa <b>On failure</b>.",
                                       "If you wire your error notification with <b>On completion</b>, you'll get an email even when everything goes fine! For error alerts use <b>On failure</b>.")}]},
  {"type": "order",
   "say": T("Este patrón se llama <b>metadata-driven</b>: una tabla de control dice qué copiar. Ordénalo.", "This pattern is called <b>metadata-driven</b>: a control table says what to copy. Put it in order."),
   "title": T("Arma una ingesta metadata-driven", "Build a metadata-driven ingestion"),
   "items": [T("Lookup: leer la lista de tablas desde una tabla de control", "Lookup: read the list of tables from a control table"),
             T("ForEach: recorrer cada tabla de la lista", "ForEach: loop over each table in the list"),
             T("Copy data (dentro del ForEach): fuente → Bronce", "Copy data (inside the ForEach): source → Bronze"),
             T("Notebook: Bronce → Plata → Oro", "Notebook: Bronze → Silver → Gold"),
             T("Teams/Outlook: avisar el resultado", "Teams/Outlook: report the result")]},
  {"type": "fill",
   "say": T("Las <b>expresiones</b> dan vida a un pipeline. Todas empiezan con <code>@</code>.", "<b>Expressions</b> bring a pipeline to life. They all start with <code>@</code>."),
   "title": T("Completa las expresiones del pipeline", "Complete the pipeline expressions"),
   "code": "-- Nombre de la tabla que llega como parámetro\n@pipeline().{{0}}.p_tabla\n\n-- Filas que copió la actividad Copy_ventas\n@activity('Copy_ventas').{{1}}.rowsCopied\n\n-- Fecha y hora actual en UTC\n@{{2}}()",
   "blanks": [
     {"a": ["parameters"], "hint": T("Plural, en inglés: los valores que recibe el pipeline al iniciar.", "Plural, in English: the values the pipeline receives at start.")},
     {"a": ["output"], "hint": T("Lo que una actividad devuelve cuando termina.", "What an activity returns when it finishes.")},
     {"a": ["utcnow"], "hint": T("Función de fecha/hora actual en tiempo universal: utc + Now.", "Current date/time function in universal time: utc + Now.")}]},
  {"type": "lab",
   "say": T("A construir tu primer pipeline. Al final tendrás <b>orquestación real</b>: copiar y luego transformar.", "Let's build your first pipeline. At the end you'll have <b>real orchestration</b>: copy, then transform."),
   "title": T("Laboratorio: copiar datos y encadenar tu notebook", "Lab: copy data and chain your notebook"),
   "intro": T("Usa el workspace <code>ws_tutor_fabric</code>, el Lakehouse <code>lh_tutor</code> y el notebook <code>nb_ventas_medallion</code> del Nivel 1. <i>Los nombres de los botones pueden variar un poco según tu versión de Fabric.</i>",
              "Use the <code>ws_tutor_fabric</code> workspace, the <code>lh_tutor</code> Lakehouse and the <code>nb_ventas_medallion</code> notebook from Level 1. <i>Button names may vary slightly with your Fabric version.</i>"),
   "tasks": [
     {"t": T("<b>+ New item → Pipeline</b> (en algunas versiones se llama <i>Data pipeline</i>). Nómbralo <code>pl_ingesta_tutor</code>.", "<b>+ New item → Pipeline</b> (called <i>Data pipeline</i> in some versions). Name it <code>pl_ingesta_tutor</code>.")},
     {"t": T("En el lienzo elige <b>Copy data assistant</b> (o <i>Copy data → Use copy assistant</i>).", "On the canvas choose <b>Copy data assistant</b> (or <i>Copy data → Use copy assistant</i>).")},
     {"t": T("Origen: pestaña <b>Sample data</b> → elige <b>Public Holidays</b>. Si no aparece, elige cualquier otro dataset de ejemplo pequeño.", "Source: <b>Sample data</b> tab → pick <b>Public Holidays</b>. If it's not listed, pick any other small sample dataset.")},
     {"t": T("Destino: <b>Lakehouse</b> → <code>lh_tutor</code> → <b>Tables</b> → nueva tabla <code>bronze_public_holidays</code>. Termina el asistente.", "Destination: <b>Lakehouse</b> → <code>lh_tutor</code> → <b>Tables</b> → new table <code>bronze_public_holidays</code>. Finish the assistant.")},
     {"t": T("Agrega la actividad <b>Notebook</b> (pestaña <i>Activities</i>) y en <i>Settings</i> selecciona <code>nb_ventas_medallion</code>.", "Add a <b>Notebook</b> activity (<i>Activities</i> tab) and in <i>Settings</i> select <code>nb_ventas_medallion</code>.")},
     {"t": T("Arrastra el conector verde <b>✓ On success</b> de la actividad Copy hacia el Notebook.", "Drag the green <b>✓ On success</b> connector from the Copy activity to the Notebook.")},
     {"t": T("<b>Save → Run</b>. En la pestaña <b>Output</b> espera a que ambas actividades digan <i>Succeeded</i>. Abre el detalle de Copy y revisa <i>Rows read / Rows written</i>.", "<b>Save → Run</b>. In the <b>Output</b> tab wait for both activities to say <i>Succeeded</i>. Open the Copy details and check <i>Rows read / Rows written</i>.")},
     {"t": T("En el SQL analytics endpoint de <code>lh_tutor</code> ejecuta:", "In the <code>lh_tutor</code> SQL analytics endpoint run:"), "code": "SELECT COUNT(*) AS filas FROM bronze_public_holidays;"},
     {"t": T("Opcional: <b>Schedule</b> → diario a las 06:00. Después <b>desactívalo</b> para no consumir capacidad de tu prueba.", "Optional: <b>Schedule</b> → daily at 06:00. Then <b>turn it off</b> so it doesn't eat your trial capacity.")}],
   "expect": T("Ambas actividades en verde y un conteo mayor a cero (el número depende del dataset de ejemplo). Las <b>Rows written</b> del Copy deben coincidir con tu <code>COUNT(*)</code>: así se valida una ingesta.",
               "Both activities green and a count above zero (the number depends on the sample dataset). The Copy's <b>Rows written</b> must match your <code>COUNT(*)</code>: that's how you validate an ingestion.")},
  {"type": "quiz",
   "say": T("Pregunta sobre lo que acabas de construir.", "A question about what you just built."),
   "q": T("Si mañana la actividad Copy falla, ¿qué pasa con el Notebook conectado con <b>On success</b>?", "If tomorrow the Copy activity fails, what happens to the Notebook wired with <b>On success</b>?"),
   "opts": [
     opt(T("Se ejecuta igual, con los datos de ayer", "It runs anyway, with yesterday's data"), T("Eso pasaría con <b>On completion</b>.", "That would happen with <b>On completion</b>.")),
     opt(T("No se ejecuta y la corrida del pipeline queda marcada como fallida", "It doesn't run and the pipeline run is marked as failed"), T("Correcto. Por eso conviene agregar una rama <b>On failure</b> con una alerta.", "Correct. That's why you should add an <b>On failure</b> branch with an alert."), True),
     opt(T("Fabric reintenta el Copy para siempre", "Fabric retries the Copy forever"), T("Puedes configurar reintentos por actividad, pero son un número limitado que tú defines.", "You can configure per-activity retries, but it's a limited number you define."))]}
 ]})

# ------------------------------------------------------------------ 2.3
lessons.append({
 "id": "l2-3", "icon": "🧹", "min": 20,
 "badge": {"e": "🧽", "n": T("Domador de Power Query", "Power Query Tamer")},
 "title": T("Dataflows Gen2: transformar sin código", "Dataflows Gen2: transform without code"),
 "steps": [
  {"type": "concept",
   "say": T("Si alguna vez usaste Power Query en Excel o Power BI, ya sabes la mitad de esta lección.", "If you've ever used Power Query in Excel or Power BI, you already know half of this lesson."),
   "kicker": T("Low-code", "Low-code"),
   "title": T("Power Query, ahora con destino", "Power Query, now with a destination"),
   "body": T(
    """<p>Un <b>Dataflow Gen2</b> es Power Query en la nube: te conectas a una fuente, transformas con clics y <b>escribes el resultado en un destino</b> de Fabric, como un Lakehouse o un Warehouse.</p>
    <p>Cada clic se guarda como un <b>paso aplicado</b> (en lenguaje M). Es una receta reproducible: el dataflow repite los mismos pasos en cada ejecución.</p>
    <p>En el destino eliges el <b>método de actualización</b>:</p>
    <ul><li><b>Replace</b>: borra y vuelve a escribir la tabla completa.</li><li><b>Append</b>: agrega las filas nuevas a lo que ya existe.</li></ul>""",
    """<p>A <b>Dataflow Gen2</b> is Power Query in the cloud: you connect to a source, transform with clicks and <b>write the result to a Fabric destination</b>, such as a Lakehouse or a Warehouse.</p>
    <p>Every click is saved as an <b>applied step</b> (in the M language). It's a reproducible recipe: the dataflow repeats the same steps on every run.</p>
    <p>At the destination you pick the <b>update method</b>:</p>
    <ul><li><b>Replace</b>: deletes and rewrites the whole table.</li><li><b>Append</b>: adds the new rows to what's already there.</li></ul>"""),
   "callouts": [{"k": "watch", "b": T("Los dataflows consumen capacidad como todo en Fabric. Para volúmenes muy grandes o lógica compleja, un notebook o un Copy job suelen ser más eficientes.",
                                       "Dataflows consume capacity like everything in Fabric. For very large volumes or complex logic, a notebook or a Copy job is usually more efficient.")}]},
  {"type": "quiz",
   "say": T("Elige el método de actualización correcto.", "Pick the right update method."),
   "q": T("Cada día recibes el catálogo <b>completo</b> de productos (todas las filas, no solo cambios). ¿Qué método usas en el destino?",
          "Every day you receive the <b>complete</b> product catalog (all rows, not just changes). Which method do you use at the destination?"),
   "opts": [
     opt(T("Append", "Append"), T("Con Append, cada día se sumaría otra copia completa del catálogo: duplicados garantizados.", "With Append, a full copy of the catalog would pile up every day: guaranteed duplicates.")),
     opt(T("Replace", "Replace"), T("Correcto: si recibes todo, reemplazas todo. La tabla siempre refleja el catálogo de hoy.", "Correct: if you receive everything, you replace everything. The table always reflects today's catalog."), True)]},
  {"type": "match",
   "say": T("Une cada transformación de Power Query con lo que hace.", "Pair each Power Query transformation with what it does."),
   "title": T("El cinturón de herramientas de Power Query", "The Power Query tool belt"),
   "pairs": [
     [T("Merge queries", "Merge queries"), T("Combinar dos tablas por una clave (JOIN)", "Combine two tables on a key (JOIN)")],
     [T("Append queries", "Append queries"), T("Apilar tablas con las mismas columnas (UNION)", "Stack tables with the same columns (UNION)")],
     [T("Change type", "Change type"), T("Convertir texto a fecha o a número", "Convert text to date or number")],
     [T("Remove duplicates", "Remove duplicates"), T("Eliminar filas repetidas", "Delete repeated rows")],
     [T("Group by", "Group by"), T("Sumar ventas por región", "Sum sales by region")]]},
  {"type": "lab",
   "say": T("Vamos a repetir la limpieza de la lección 1.5, pero <b>sin escribir código</b>. Compara las dos experiencias.", "We'll repeat the cleanup from lesson 1.5, but <b>without writing code</b>. Compare both experiences."),
   "title": T("Laboratorio: limpia las ventas con Dataflow Gen2", "Lab: clean the sales data with Dataflow Gen2"),
   "intro": T("Partimos de la tabla <code>ventas</code> que cargaste en la lección 1.3 (11 filas, con un duplicado y un monto negativo).", "We start from the <code>ventas</code> table you loaded in lesson 1.3 (11 rows, with one duplicate and one negative amount)."),
   "tasks": [
     {"t": T("<b>+ New item → Dataflow Gen2</b>. Nómbralo <code>df_ventas_silver</code>.", "<b>+ New item → Dataflow Gen2</b>. Name it <code>df_ventas_silver</code>.")},
     {"t": T("<b>Get data</b> → busca <b>Lakehouse</b> → <code>lh_tutor</code> → <b>Tables</b> → marca <code>ventas</code> → <b>Create</b>.", "<b>Get data</b> → search <b>Lakehouse</b> → <code>lh_tutor</code> → <b>Tables</b> → tick <code>ventas</code> → <b>Create</b>.")},
     {"t": T("Selecciona todas las columnas (Ctrl+A en los encabezados) → <b>Home → Remove rows → Remove duplicates</b>.", "Select all columns (Ctrl+A on the headers) → <b>Home → Remove rows → Remove duplicates</b>.")},
     {"t": T("En la columna <code>monto</code>: flecha del filtro → <b>Number filters → Greater than</b> → <code>0</code>.", "On the <code>monto</code> column: filter arrow → <b>Number filters → Greater than</b> → <code>0</code>.")},
     {"t": T("Si <code>fecha</code> no es de tipo fecha, cámbiala: clic en el ícono de tipo del encabezado → <b>Date</b>. Revisa el panel <b>Applied steps</b>: ahí está tu receta.", "If <code>fecha</code> isn't a date type, change it: click the type icon in the header → <b>Date</b>. Check the <b>Applied steps</b> pane: that's your recipe.")},
     {"t": T("Abajo a la derecha, en <b>Data destination</b> → <b>Lakehouse</b> → <code>lh_tutor</code> → nueva tabla <code>silver_ventas_df</code>, método <b>Replace</b>.", "Bottom right, in <b>Data destination</b> → <b>Lakehouse</b> → <code>lh_tutor</code> → new table <code>silver_ventas_df</code>, method <b>Replace</b>.")},
     {"t": T("<b>Guarda y ejecuta</b> (según tu versión: <i>Publish</i> o <i>Save & run</i>). Luego consulta en el SQL analytics endpoint:", "<b>Save and run</b> (depending on your version: <i>Publish</i> or <i>Save & run</i>). Then query in the SQL analytics endpoint:"),
      "code": "SELECT COUNT(*) AS filas, MIN(monto) AS minimo\nFROM silver_ventas_df;"}],
   "expect": T("<b>filas = 9</b> y <b>minimo = 300.00</b>. ¡El mismo resultado que con PySpark en la lección 1.5! Dos caminos, un mismo destino.",
               "<b>filas = 9</b> and <b>minimo = 300.00</b>. The same result as with PySpark in lesson 1.5! Two paths, one destination.")},
  {"type": "reveal", "kind": "brain",
   "say": T("Ya probaste los dos caminos. ¿Cuál elegirías y cuándo?", "You've tried both paths. Which would you pick, and when?"),
   "prompt": T("¿Cuándo conviene un Dataflow Gen2 y cuándo un notebook de PySpark?", "When is a Dataflow Gen2 the better choice, and when is a PySpark notebook?"),
   "answer": T("<b>Dataflow Gen2</b>: equipos que no programan, muchos conectores de negocio (SharePoint, Excel, APIs), volúmenes moderados y transformaciones visuales. <b>Notebook</b>: grandes volúmenes, lógica compleja o reutilizable, pruebas unitarias, control de versiones del código y máximo rendimiento. En proyectos grandes conviven: los analistas usan dataflows y el equipo de ingeniería usa notebooks.",
               "<b>Dataflow Gen2</b>: teams that don't code, many business connectors (SharePoint, Excel, APIs), moderate volumes and visual transformations. <b>Notebook</b>: large volumes, complex or reusable logic, unit tests, code version control and top performance. In big projects both coexist: analysts use dataflows and the engineering team uses notebooks.")}
 ]})

# ------------------------------------------------------------------ 2.4
lessons.append({
 "id": "l2-4", "icon": "⏱️", "min": 25,
 "badge": {"e": "⌛", "n": T("Guardián del watermark", "Watermark Keeper")},
 "title": T("Cargas incrementales y Copy job", "Incremental loads and Copy job"),
 "steps": [
  {"type": "story",
   "say": T("Esta lección separa a los principiantes de los profesionales. 😎", "This lesson separates beginners from professionals. 😎"),
   "kicker": T("El periódico de cada mañana", "The morning newspaper"),
   "title": T("No releas todo el archivo histórico cada día", "Don't reread the whole archive every day"),
   "body": T(
    """<p>Cada mañana lees el periódico <b>de hoy</b>, no todos los periódicos desde 1950. Con los datos es igual:</p>
    <ul><li><b>Carga completa (full)</b>: copias toda la tabla en cada ejecución. Simple, pero lenta y cara cuando la tabla crece.</li>
    <li><b>Carga incremental</b>: copias <span class="hl">solo lo nuevo o lo que cambió</span> desde la última vez.</li></ul>
    <p>Para saber “desde la última vez” necesitas una marca: el <b>watermark</b>. Normalmente es una columna como <code>fecha_mod</code> o un ID que siempre crece. En cada carga copias las filas cuyo valor es <b>mayor</b> que el último que copiaste.</p>""",
    """<p>Every morning you read <b>today's</b> newspaper, not every issue since 1950. Data works the same way:</p>
    <ul><li><b>Full load</b>: you copy the whole table on every run. Simple, but slow and expensive as the table grows.</li>
    <li><b>Incremental load</b>: you copy <span class="hl">only what's new or changed</span> since last time.</li></ul>
    <p>To know “since last time” you need a marker: the <b>watermark</b>. It's usually a column like <code>fecha_mod</code> or an ever-increasing ID. On each load you copy the rows whose value is <b>greater</b> than the last one you copied.</p>"""),
   "visual": "watermark"},
  {"type": "quiz",
   "say": T("Usa el diagrama. Fíjate bien en la palabra <b>mayor</b>.", "Use the diagram. Pay close attention to the word <b>greater</b>."),
   "q": T("El último watermark guardado es <code>01-08</code>. La fuente tiene filas con <code>fecha_mod</code> 01-05, 01-06, 01-08, 01-09, 01-11 y 01-12. ¿Cuántas filas copia la carga incremental de hoy?",
          "The last saved watermark is <code>01-08</code>. The source has rows with <code>fecha_mod</code> 01-05, 01-06, 01-08, 01-09, 01-11 and 01-12. How many rows does today's incremental load copy?"),
   "opts": [
     opt(T("6", "6"), T("Eso sería una carga completa.", "That would be a full load.")),
     opt(T("4", "4"), T("Incluiste la fila de 01-08, pero esa ya se copió: la condición es <b>mayor que</b>, no mayor o igual.", "You included the 01-08 row, but it was already copied: the condition is <b>greater than</b>, not greater-or-equal.")),
     opt(T("3", "3"), T("¡Exacto! 01-09, 01-11 y 01-12. Después de copiarlas, el nuevo watermark será 01-12.", "Exactly! 01-09, 01-11 and 01-12. After copying them, the new watermark becomes 01-12."), True)]},
  {"type": "concept",
   "say": T("Hay dos formas de detectar cambios. Y una de ellas <b>no ve los borrados</b>.", "There are two ways to detect changes. And one of them <b>can't see deletes</b>."),
   "title": T("Watermark vs CDC, y cómo lo resuelve Copy job", "Watermark vs CDC, and how Copy job handles it"),
   "body": T(
    """<ul><li><b>Watermark</b>: compara una columna que crece (fecha o ID). Funciona con casi cualquier fuente, pero <b>no detecta filas borradas</b>.</li>
    <li><b>CDC</b> (<i>Change Data Capture</i>): la base de datos registra cada insert, update y delete. Si la fuente lo tiene activado, captura también los borrados.</li></ul>
    <p><b>Copy job</b> hace el trabajo pesado por ti: en modo <i>incremental</i> la primera ejecución copia todo y las siguientes solo los cambios. <span class="hl">Él guarda el estado</span>, y si una ejecución falla, la siguiente retoma desde la última exitosa.</p>
    <p>En el destino eliges cómo escribir: <b>Append</b> (agregar), <b>Overwrite</b> (sobrescribir) o <b>Merge</b> (insertar o actualizar por clave). Qué opciones ves depende del conector.</p>""",
    """<ul><li><b>Watermark</b>: compares a growing column (date or ID). Works with almost any source, but <b>doesn't detect deleted rows</b>.</li>
    <li><b>CDC</b> (<i>Change Data Capture</i>): the database logs every insert, update and delete. If the source has it enabled, it captures deletes too.</li></ul>
    <p><b>Copy job</b> does the heavy lifting: in <i>incremental</i> mode the first run copies everything and later runs copy only changes. <span class="hl">It keeps the state</span>, and if a run fails, the next one resumes from the last successful run.</p>
    <p>At the destination you choose how to write: <b>Append</b>, <b>Overwrite</b> or <b>Merge</b> (insert or update by key). Which options you see depends on the connector.</p>"""),
   "callouts": [{"k": "watch", "b": T("Incremental + Append + filas que vuelven a llegar = <b>duplicados</b>. Si la fuente puede reenviar una fila ya copiada, usa <b>Merge</b> con una clave o deduplica en Plata.",
                                       "Incremental + Append + rows that arrive again = <b>duplicates</b>. If the source can resend a row you already copied, use <b>Merge</b> with a key or deduplicate in Silver.")}]},
  {"type": "order",
   "say": T("Antes de Copy job, esto se construía a mano en un pipeline. Ordena el patrón clásico.", "Before Copy job, this was hand-built in a pipeline. Order the classic pattern."),
   "title": T("El patrón watermark hecho a mano", "The hand-built watermark pattern"),
   "items": [T("Lookup: leer el último watermark guardado", "Lookup: read the last saved watermark"),
             T("Lookup: obtener el valor máximo actual de fecha_mod en la fuente", "Lookup: get the current max fecha_mod in the source"),
             T("Copy: copiar las filas entre el watermark viejo y el nuevo", "Copy: copy rows between the old and new watermark"),
             T("Script: guardar el nuevo watermark para la próxima vez", "Script: save the new watermark for next time")]},
  {"type": "lab",
   "say": T("En este laboratorio vas a <b>provocar un error a propósito</b>. Es la mejor forma de no cometerlo en producción.", "In this lab you'll <b>cause a bug on purpose</b>. It's the best way to avoid it in production."),
   "title": T("Laboratorio: Copy job incremental (y su trampa)", "Lab: incremental Copy job (and its trap)"),
   "intro": T("Usaremos como fuente <code>silver_ventas</code> (lección 1.5), que tiene la columna <code>_ingest_ts</code> con la hora de carga.", "We'll use <code>silver_ventas</code> (lesson 1.5) as the source; it has an <code>_ingest_ts</code> column with the load time."),
   "tasks": [
     {"t": T("<b>+ New item → Copy job</b>. Nómbralo <code>cj_ventas_incremental</code>.", "<b>+ New item → Copy job</b>. Name it <code>cj_ventas_incremental</code>.")},
     {"t": T("Origen: <b>Lakehouse</b> <code>lh_tutor</code> → tabla <code>silver_ventas</code>.", "Source: <b>Lakehouse</b> <code>lh_tutor</code> → table <code>silver_ventas</code>.")},
     {"t": T("Destino: <b>Lakehouse</b> <code>lh_tutor</code> → nueva tabla <code>bronze_ventas_cj</code>, escritura <b>Append</b>.", "Destination: <b>Lakehouse</b> <code>lh_tutor</code> → new table <code>bronze_ventas_cj</code>, write mode <b>Append</b>.")},
     {"t": T("Modo de copia: <b>Incremental copy</b>. Columna incremental: <code>_ingest_ts</code>. Si te ofrece usar CDF, elige watermark para este ejercicio.", "Copy mode: <b>Incremental copy</b>. Incremental column: <code>_ingest_ts</code>. If it offers CDF, choose watermark for this exercise.")},
     {"t": T("Guarda y <b>ejecuta</b>. Primera corrida: debe copiar <b>9</b> filas.", "Save and <b>run</b>. First run: it should copy <b>9</b> rows.")},
     {"t": T("<b>Ejecútalo otra vez</b>. Ahora debe copiar <b>0</b> filas: no hay nada nuevo. ✨", "<b>Run it again</b>. Now it should copy <b>0</b> rows: nothing is new. ✨")},
     {"t": T("Ahora vuelve a ejecutar el notebook <code>nb_ventas_medallion</code> y después el Copy job una vez más. Cuenta las filas del destino:", "Now rerun the <code>nb_ventas_medallion</code> notebook, then the Copy job once more. Count the destination rows:"),
      "code": "SELECT COUNT(*) AS filas, COUNT(DISTINCT id) AS ids_unicos\nFROM bronze_ventas_cj;"}],
   "expect": T("Verás <b>filas = 18</b> pero <b>ids_unicos = 9</b>. ¡Duplicados! La siguiente pregunta te explica por qué.", "You'll see <b>filas = 18</b> but <b>ids_unicos = 9</b>. Duplicates! The next question explains why.")},
  {"type": "quiz",
   "say": T("Detective de datos: ¿quién fue el culpable? 🔍", "Data detective: who's the culprit? 🔍"),
   "q": T("¿Por qué <code>bronze_ventas_cj</code> terminó con 18 filas?", "Why did <code>bronze_ventas_cj</code> end up with 18 rows?"),
   "opts": [
     opt(T("Copy job tiene un error", "Copy job has a bug"), T("Copy job hizo exactamente lo que le pediste. 😉", "Copy job did exactly what you asked. 😉")),
     opt(T("El notebook reescribió las 9 filas con un <code>_ingest_ts</code> nuevo; el watermark las vio como nuevas y Append las agregó otra vez",
           "The notebook rewrote all 9 rows with a new <code>_ingest_ts</code>; the watermark saw them as new and Append added them again"),
         T("¡Exacto! El watermark debe reflejar <b>cambios reales del negocio</b> (como <code>fecha_mod</code>), no la hora de un proceso que reescribe todo. Y con Append, cualquier reenvío duplica. Soluciones: un watermark de negocio, Merge por <code>id</code>, o deduplicar en Plata.",
           "Exactly! The watermark should reflect <b>real business changes</b> (like <code>fecha_mod</code>), not the time of a process that rewrites everything. And with Append, any resend duplicates. Fixes: a business watermark, Merge on <code>id</code>, or deduplicate in Silver."), True),
     opt(T("El Lakehouse duplica datos al leerlos", "The Lakehouse duplicates data when reading"), T("No: el Lakehouse no inventa filas.", "No: the Lakehouse doesn't invent rows."))]},
  {"type": "reveal", "kind": "pencil",
   "say": T("Escribe tu respuesta. Esta aparece en entrevistas técnicas.", "Write your answer. This one shows up in technical interviews."),
   "prompt": T("Un vendedor <b>borra</b> una venta en el ERP. Tu carga incremental usa watermark por <code>fecha_mod</code>. ¿Tu Lakehouse se entera? ¿Qué harías?",
               "A salesperson <b>deletes</b> a sale in the ERP. Your incremental load uses a watermark on <code>fecha_mod</code>. Does your Lakehouse find out? What would you do?"),
   "answer": T("<b>No se entera</b>: una fila borrada ya no existe en la fuente, así que no tiene <code>fecha_mod</code> que comparar. Opciones: activar <b>CDC</b> en la fuente (captura deletes), pedir un <b>borrado lógico</b> (columna <code>es_borrado</code>) en lugar de borrar la fila, o hacer una <b>conciliación completa</b> periódica, por ejemplo semanal.",
               "<b>It doesn't</b>: a deleted row no longer exists in the source, so there's no <code>fecha_mod</code> to compare. Options: enable <b>CDC</b> on the source (captures deletes), ask for a <b>soft delete</b> (an <code>is_deleted</code> column) instead of removing the row, or run a periodic <b>full reconciliation</b>, e.g. weekly.")}
 ]})

# ------------------------------------------------------------------ 2.5
lessons.append({
 "id": "l2-5", "icon": "🪞", "min": 20,
 "badge": {"e": "🏆", "n": T("Maestro de la Ingesta", "Ingestion Master")},
 "title": T("Mirroring y el desafío final del nivel", "Mirroring and the level's final challenge"),
 "steps": [
  {"type": "concept",
   "say": T("Mirroring es lo más parecido a magia que tiene Fabric. 🪄", "Mirroring is the closest thing to magic Fabric has. 🪄"),
   "kicker": T("Réplica continua", "Continuous replication"),
   "title": T("Mirroring: un espejo de tu base de datos en OneLake", "Mirroring: a mirror of your database in OneLake"),
   "body": T(
    """<p><b>Mirroring</b> replica de forma <b>continua y casi en tiempo real</b> tablas de una base de datos hacia OneLake, en formato Delta. No construyes ETL: lo configuras y Fabric mantiene la copia al día.</p>
    <p>Fuentes de base de datos: Azure SQL Database, Azure SQL Managed Instance, SQL Server, Azure Cosmos DB, Snowflake y Azure Database for PostgreSQL, entre otras. Con <b>Open Mirroring</b>, partners y soluciones propias pueden escribir cambios en una zona de aterrizaje.</p>
    <p>El costo es amigable: el cómputo para replicar no se cobra, y el almacenamiento de la réplica es gratuito hasta <span class="hl">1 TB por cada Capacity Unit</span> de tu capacidad.</p>""",
    """<p><b>Mirroring</b> replicates database tables into OneLake <b>continuously and in near real time</b>, in Delta format. You don't build ETL: you configure it and Fabric keeps the copy up to date.</p>
    <p>Database sources include Azure SQL Database, Azure SQL Managed Instance, SQL Server, Azure Cosmos DB, Snowflake and Azure Database for PostgreSQL, among others. With <b>Open Mirroring</b>, partners and custom solutions can write changes to a landing zone.</p>
    <p>The cost is friendly: compute for replication isn't charged, and replica storage is free up to <span class="hl">1 TB per Capacity Unit</span> of your capacity.</p>"""),
   "callouts": [
     {"k": "watch", "b": T("Mirroring replica <b>tablas</b>, no vistas, y la réplica es de solo lectura. Es tu capa <b>Bronce</b> automática: todavía necesitas Plata y Oro.",
                           "Mirroring replicates <b>tables</b>, not views, and the replica is read-only. It's your automatic <b>Bronze</b> layer: you still need Silver and Gold.")},
     {"k": "key", "b": T("¿La base está detrás de un firewall? Usa un <b>on-premises data gateway</b> o un <b>VNet data gateway</b>, según la fuente.",
                         "Is the database behind a firewall? Use an <b>on-premises data gateway</b> or a <b>VNet data gateway</b>, depending on the source.")}]},
  {"type": "quiz",
   "say": T("Haz la cuenta: 1 TB por cada CU.", "Do the math: 1 TB per CU."),
   "q": T("Tu cliente tiene una capacidad <b>F8</b>. ¿Cuánto almacenamiento de réplica de Mirroring tiene sin costo?", "Your client has an <b>F8</b> capacity. How much free Mirroring replica storage do they get?"),
   "opts": [
     opt(T("1 TB", "1 TB"), T("Es 1 TB <b>por cada CU</b>, no 1 TB en total.", "It's 1 TB <b>per CU</b>, not 1 TB in total.")),
     opt(T("8 TB", "8 TB"), T("¡Correcto! F8 = 8 CU → 8 TB. Una F64 tendría 64 TB.", "Correct! F8 = 8 CU → 8 TB. An F64 would get 64 TB."), True),
     opt(T("Ilimitado", "Unlimited"), T("Hay un límite; al pasarlo, OneLake cobra el almacenamiento normal.", "There's a limit; beyond it, OneLake bills storage normally."))]},
  {"type": "reveal", "kind": "brain",
   "say": T("Pregunta de arquitecto: ¿Mirroring o Copy job?", "Architect question: Mirroring or Copy job?"),
   "prompt": T("Si Copy job también puede copiar cambios con CDC, ¿cuándo elegirías Mirroring?", "If Copy job can also copy changes with CDC, when would you pick Mirroring?"),
   "answer": T("<b>Mirroring</b>: quieres una réplica casi en tiempo real de una base soportada, sin programar ejecuciones y sin administrar estado. Fabric la mantiene sincronizada sola. <b>Copy job</b>: necesitas elegir cuándo corre (por ejemplo, cada noche), el destino o el modo de escritura (Append, Merge), o la fuente no es compatible con Mirroring. Ambos terminan en OneLake; cambia el control que tienes.",
               "<b>Mirroring</b>: you want a near-real-time replica of a supported database, with no run schedule and no state to manage. Fabric keeps it in sync on its own. <b>Copy job</b>: you need to choose when it runs (e.g. nightly), the destination or the write mode (Append, Merge), or the source isn't supported by Mirroring. Both land in OneLake; what changes is how much control you have.")},
  {"type": "match",
   "say": T("🏁 <b>Desafío final del Nivel 2.</b> Sin pistas esta vez… bueno, quizá una si fallas.", "🏁 <b>Level 2 final challenge.</b> No hints this time… well, maybe one if you miss."),
   "title": T("Desafío: el arquitecto de ingesta", "Challenge: the ingestion architect"),
   "pairs": [
     [T("Ventas de Snowflake en Power BI con minutos de retraso, sin construir ETL", "Snowflake sales in Power BI minutes behind, with no ETL"), T("🪞 Mirroring", "🪞 Mirroring")],
     [T("Parquet de un partner en Google Cloud Storage que no quieres duplicar", "A partner's Parquet in Google Cloud Storage you don't want to duplicate"), T("🔗 Shortcut", "🔗 Shortcut")],
     [T("Proceso nocturno: copiar, transformar y avisar por Teams si falla", "Nightly process: copy, transform and alert on Teams if it fails"), T("🧭 Pipeline", "🧭 Pipeline")],
     [T("Copiar 60 tablas de Oracle cada hora, solo cambios", "Copy 60 Oracle tables every hour, only changes"), T("📦 Copy job", "📦 Copy job")],
     [T("Recursos Humanos limpia una lista de SharePoint con clics", "HR cleans a SharePoint list with clicks"), T("🧹 Dataflow Gen2", "🧹 Dataflow Gen2")]]},
  {"type": "quiz",
   "say": T("Última pregunta del nivel. Piensa en todo lo que aprendiste.", "Final question of the level. Think about everything you learned."),
   "q": T("Diseñas la ingesta de un ERP en SQL Server on-premises. Los usuarios necesitan los datos con pocos minutos de retraso y el negocio borra pedidos cancelados. ¿Cuál es la mejor propuesta inicial?",
          "You're designing ingestion for an on-premises SQL Server ERP. Users need the data a few minutes behind, and the business deletes cancelled orders. What's the best initial proposal?"),
   "opts": [
     opt(T("Copy job incremental por watermark cada noche", "Nightly watermark-based incremental Copy job"), T("Nocturno no cumple los “pocos minutos”, y el watermark no ve los pedidos borrados.", "Nightly doesn't meet “a few minutes”, and the watermark can't see deleted orders.")),
     opt(T("Mirroring de SQL Server con un gateway, y Plata/Oro con notebooks orquestados por un pipeline", "SQL Server Mirroring through a gateway, with Silver/Gold notebooks orchestrated by a pipeline"),
         T("¡Arquitectura de nivel profesional! Mirroring da baja latencia y refleja también los borrados en la réplica. El gateway resuelve el acceso on-premises, y Plata/Oro siguen siendo tu responsabilidad.",
           "Professional-grade architecture! Mirroring gives low latency and also reflects deletes in the replica. The gateway solves on-premises access, and Silver/Gold are still your job."), True),
     opt(T("Exportar CSV cada 5 minutos a SharePoint y leerlos con un Dataflow", "Export CSVs every 5 minutes to SharePoint and read them with a Dataflow"), T("Frágil, costoso y lleno de piezas manuales. 😬", "Fragile, costly and full of manual parts. 😬"))]}
 ]})

out = {"id": 2,
       "title": T("Ingesta de datos", "Data ingestion"),
       "desc": T("Shortcuts, Copy job, pipelines, Dataflows Gen2, cargas incrementales y Mirroring.", "Shortcuts, Copy job, pipelines, Dataflows Gen2, incremental loads and Mirroring."),
       "lessons": lessons}
dst = pathlib.Path(__file__).resolve().parent.parent / "content/level-2.json"
dst.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", dst, sum(len(l["steps"]) for l in lessons), "steps")
