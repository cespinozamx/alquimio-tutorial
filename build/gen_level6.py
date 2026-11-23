"""Genera content/level-6.json — Nivel 6: Modelado semántico y Direct Lake."""
import json, pathlib

def T(es, en): return {"es": es, "en": en}
def opt(t, why, ok=False):
    o = {"t": t, "why": why}
    if ok: o["ok"] = 1
    return o

L = []

# ------------------------------------------------------------------ 6.1
L.append({
 "id": "l6-1", "icon": "🧩", "min": 15,
 "badge": {"e": "📖", "n": T("Traductor del negocio", "Business Translator")},
 "title": T("¿Qué es un modelo semántico?", "What is a semantic model?"),
 "steps": [
  {"type": "story",
   "say": T("Nivel 6: aquí los datos se vuelven <b>decisiones</b>. Es mi nivel favorito. 📊", "Level 6: this is where data becomes <b>decisions</b>. My favorite level. 📊"),
   "kicker": T("La cocina y el menú", "The kitchen and the menu"),
   "title": T("El cliente no lee recetas: lee el menú", "Customers don't read recipes: they read the menu"),
   "body": T(
    """<p>En los niveles anteriores fuiste el cocinero: limpiaste ingredientes (Plata) y preparaste platillos (Oro). Pero el comensal no entra a la cocina. Lee un <b>menú</b> con nombres claros, precios y combinaciones que tienen sentido.</p>
    <p>El <b>modelo semántico</b> es ese menú. Se sienta sobre tus tablas Oro y les agrega <b>significado de negocio</b>:</p>
    <ul><li><b>Relaciones</b> entre hechos y dimensiones.</li><li><b>Medidas</b> calculadas una sola vez y bien: “Ventas Totales”, “Ticket Promedio”.</li>
    <li><b>Nombres y formatos</b> amigables: “Región” en lugar de <code>dim_cliente.region</code>, y montos con signo de pesos.</li><li><b>Seguridad</b>: quién ve qué filas.</li></ul>
    <p>Power BI, Excel, Copilot y los agentes de datos leen el menú, no la cocina. <span class="hl">Un buen modelo semántico es una sola versión de la verdad</span>.</p>""",
    """<p>In the previous levels you were the cook: you cleaned ingredients (Silver) and prepared dishes (Gold). But diners don't walk into the kitchen. They read a <b>menu</b> with clear names, prices and combinations that make sense.</p>
    <p>The <b>semantic model</b> is that menu. It sits on top of your Gold tables and adds <b>business meaning</b>:</p>
    <ul><li><b>Relationships</b> between facts and dimensions.</li><li><b>Measures</b> calculated once, correctly: “Total Sales”, “Average Ticket”.</li>
    <li>Friendly <b>names and formats</b>: “Region” instead of <code>dim_cliente.region</code>, and amounts with a currency sign.</li><li><b>Security</b>: who sees which rows.</li></ul>
    <p>Power BI, Excel, Copilot and data agents read the menu, not the kitchen. <span class="hl">A good semantic model is a single version of the truth</span>.</p>"""),
   "visual": "storageModes"},
  {"type": "concept",
   "say": T("Hay tres formas de que el modelo lea los datos. Una es exclusiva de Fabric.", "There are three ways the model can read data. One is exclusive to Fabric."),
   "title": T("Modos de almacenamiento", "Storage modes"),
   "body": T("", ""),
   "cards": [
     {"e": "📥", "n": "Import", "d": T("Copia los datos dentro del modelo. Muy rápido, pero hay que refrescar (copiar otra vez) y los datos se duplican.", "Copies data into the model. Very fast, but needs refreshing (copying again) and duplicates the data.")},
     {"e": "🔁", "n": "DirectQuery", "d": T("No copia nada: cada clic en el reporte envía una consulta a la fuente. Datos al día, pero más lento.", "Copies nothing: every report click sends a query to the source. Fresh data, but slower.")},
     {"e": "⚡", "n": "Direct Lake", "d": T("Lee los archivos Delta de OneLake directo a la memoria del motor, sin copiar. Velocidad cercana a Import con datos casi al día.", "Reads OneLake Delta files straight into engine memory, without copying. Near-Import speed with near-fresh data."), "star": True}],
   "callouts": [{"k": "key", "b": T("Desde septiembre de 2025, Fabric <b>ya no crea un modelo semántico por defecto</b> al crear un Lakehouse o un Warehouse. Tú decides qué tablas entran y cómo se relacionan.",
                                     "Since September 2025, Fabric <b>no longer creates a default semantic model</b> when you create a Lakehouse or Warehouse. You decide which tables go in and how they relate.")}]},
  {"type": "match",
   "say": T("Une cada situación con el modo de almacenamiento que mejor le queda.", "Pair each situation with the storage mode that fits best."),
   "title": T("¿Qué modo elegirías?", "Which mode would you pick?"),
   "pairs": [
     [T("Tablas Oro en OneLake y reportes rápidos sin copiar datos", "Gold tables in OneLake and fast reports without copying data"), "⚡ Direct Lake"],
     [T("Un Excel pequeño de metas que alguien actualiza a mano", "A small Excel of targets someone updates by hand"), "📥 Import"],
     [T("Consultar en vivo una base operacional fuera de Fabric", "Query a live operational database outside Fabric"), "🔁 DirectQuery"]]},
  {"type": "quiz",
   "say": T("Piensa en el problema de “varias versiones de la verdad”.", "Think about the “several versions of the truth” problem."),
   "q": T("Tres áreas calculan “Ventas Netas” en sus propios Excel y cada una obtiene un número distinto. ¿Qué resuelve un modelo semántico?",
          "Three departments calculate “Net Sales” in their own Excel files and each gets a different number. What does a semantic model solve?"),
   "opts": [
     opt(T("Nada: es solo una capa visual", "Nothing: it's just a visual layer"), T("Es mucho más que visual: define cálculos y reglas que todos reutilizan.", "It's much more than visual: it defines calculations and rules everyone reuses.")),
     opt(T("Define la medida “Ventas Netas” una sola vez y todos los reportes la reutilizan", "It defines the “Net Sales” measure once and every report reuses it"), T("¡Exacto! Una medida, una definición, un mismo número en todos los reportes.", "Exactly! One measure, one definition, the same number in every report."), True),
     opt(T("Obliga a todos a usar el mismo Excel", "It forces everyone to use the same Excel"), T("Excel puede conectarse al modelo, pero la clave es que la lógica vive en el modelo, no en el archivo.", "Excel can connect to the model, but the key is that the logic lives in the model, not in the file."))]}
 ]})

# ------------------------------------------------------------------ 6.2
L.append({
 "id": "l6-2", "icon": "🔌", "min": 20,
 "badge": {"e": "⚡", "n": T("Domador de Direct Lake", "Direct Lake Tamer")},
 "title": T("Direct Lake por dentro", "Direct Lake under the hood"),
 "steps": [
  {"type": "concept",
   "say": T("Aquí se conecta todo lo que aprendiste: Delta, V-Order, OPTIMIZE… 🔗", "This is where everything connects: Delta, V-Order, OPTIMIZE… 🔗"),
   "kicker": T("Cómo funciona", "How it works"),
   "title": T("Cargar columnas a demanda y “enmarcar” versiones", "Loading columns on demand and “framing” versions"),
   "body": T(
    """<ul><li><b>Carga de columnas a demanda</b>: cuando un visual necesita <code>monto</code> y <code>region</code>, el motor lee <i>solo esas columnas</i> de los archivos Parquet y las sube a memoria. La primera consulta tarda un poco más; las siguientes vuelan.</li>
    <li><b>Framing (enmarcado)</b>: el modelo apunta a una <b>versión</b> concreta de cada tabla Delta. Si cargas datos nuevos, el reporte los verá cuando el modelo haga un nuevo <i>framing</i>, ya sea automático o con un <b>refresh</b>. Un refresh de Direct Lake no copia datos: solo actualiza a qué versión apunta. Tarda segundos.</li>
    <li>Recuerda el Nivel 3: <b>V-Order</b> y <b>OPTIMIZE</b> en las tablas Oro hacen que esta lectura sea más rápida.</li></ul>""",
    """<ul><li><b>On-demand column loading</b>: when a visual needs <code>monto</code> and <code>region</code>, the engine reads <i>only those columns</i> from the Parquet files into memory. The first query takes a bit longer; the next ones fly.</li>
    <li><b>Framing</b>: the model points to a specific <b>version</b> of each Delta table. When you load new data, the report sees it when the model does a new <i>framing</i>, either automatically or via a <b>refresh</b>. A Direct Lake refresh doesn't copy data: it only updates which version it points to. It takes seconds.</li>
    <li>Remember Level 3: <b>V-Order</b> and <b>OPTIMIZE</b> on Gold tables make this read faster.</li></ul>"""),
   "visual": "directLakeFlow"},
  {"type": "concept",
   "say": T("Dos sabores de Direct Lake, con un comportamiento distinto cuando algo no se puede leer directo.", "Two flavors of Direct Lake, with different behavior when something can't be read directly."),
   "title": T("Direct Lake sobre SQL vs sobre OneLake", "Direct Lake on SQL vs on OneLake"),
   "body": T(
    """<ul><li><b>Direct Lake sobre SQL endpoints</b>: usa el SQL endpoint del Lakehouse o Warehouse para encontrar tablas y revisar permisos. Si algo no se puede leer en Direct Lake (por ejemplo, una <b>vista SQL</b> o seguridad definida en SQL), la consulta <b>cae a DirectQuery</b> (<i>fallback</i>): sigue funcionando, pero más lento.</li>
    <li><b>Direct Lake sobre OneLake</b>: lee las tablas Delta directo de OneLake y usa la seguridad de OneLake. <b>No tiene fallback a DirectQuery</b>: o se puede en Direct Lake, o la consulta falla.</li></ul>
    <p>Además existen <b>límites por SKU</b> (<i>guardrails</i>): filas por tabla, archivos Parquet por tabla, grupos de filas y memoria. Por ejemplo, una F2 admite hasta 300 millones de filas por tabla y una F64 hasta 1,500 millones.</p>""",
    """<ul><li><b>Direct Lake on SQL endpoints</b>: uses the Lakehouse or Warehouse SQL endpoint to discover tables and check permissions. If something can't be read in Direct Lake (e.g. a <b>SQL view</b> or SQL-defined security), the query <b>falls back to DirectQuery</b>: it still works, but slower.</li>
    <li><b>Direct Lake on OneLake</b>: reads Delta tables straight from OneLake and uses OneLake security. <b>No fallback to DirectQuery</b>: either it runs in Direct Lake, or the query fails.</li></ul>
    <p>There are also <b>per-SKU limits</b> (<i>guardrails</i>): rows per table, Parquet files per table, row groups and memory. For example, an F2 allows up to 300 million rows per table and an F64 up to 1.5 billion.</p>"""),
   "callouts": [{"k": "watch", "b": T("Construir el modelo sobre <b>vistas SQL</b> parece cómodo, pero en Direct Lake sobre SQL provoca fallback a DirectQuery. Para Direct Lake, prefiere <b>tablas físicas</b> en Oro.",
                                       "Building the model on <b>SQL views</b> looks convenient, but in Direct Lake on SQL it triggers DirectQuery fallback. For Direct Lake, prefer <b>physical tables</b> in Gold.")}]},
  {"type": "order",
   "say": T("Ordena lo que pasa desde que cargas datos nuevos hasta que el gerente los ve.", "Order what happens from loading new data to the manager seeing it."),
   "title": T("De la carga al reporte", "From load to report"),
   "items": [T("El procedimiento de carga escribe en las tablas Oro (nueva versión Delta)", "The load procedure writes to the Gold tables (new Delta version)"),
             T("El modelo hace framing y apunta a la nueva versión", "The model frames and points to the new version"),
             T("El usuario abre el reporte y un visual pide columnas", "The user opens the report and a visual asks for columns"),
             T("El motor carga a memoria solo esas columnas desde OneLake", "The engine loads only those columns from OneLake into memory"),
             T("El visual muestra el resultado", "The visual shows the result")]},
  {"type": "quiz",
   "say": T("Problema típico de soporte el lunes por la mañana. ☕", "Classic Monday-morning support ticket. ☕"),
   "q": T("El procedimiento de carga terminó bien, pero el reporte en Direct Lake sigue mostrando los datos de ayer. ¿Qué revisas primero?",
          "The load procedure finished fine, but the Direct Lake report still shows yesterday's data. What do you check first?"),
   "opts": [
     opt(T("Que el modelo se haya actualizado (framing): actualización automática activa o un refresh después de la carga", "That the model was updated (framing): automatic updates on, or a refresh after the load"),
         T("¡Exacto! Un patrón común: en el pipeline, después del procedimiento de carga, agregar una actividad que refresque el modelo semántico.", "Exactly! A common pattern: in the pipeline, after the load procedure, add an activity that refreshes the semantic model."), True),
     opt(T("Volver a importar todos los datos", "Re-import all the data"), T("En Direct Lake no hay nada que importar; solo hay que apuntar a la versión nueva.", "In Direct Lake there's nothing to import; you just point to the new version.")),
     opt(T("Comprar una capacidad más grande", "Buy a bigger capacity"), T("No tiene que ver con el tamaño: el modelo sigue apuntando a la versión anterior.", "Size isn't the issue: the model still points to the old version."))]},
  {"type": "quiz",
   "say": T("Diagnóstico de rendimiento.", "Performance diagnosis."),
   "q": T("Un reporte en Direct Lake sobre SQL va lento, y el Performance analyzer muestra consultas DirectQuery. El modelo usa la vista SQL <code>vw_ventas_completas</code>. ¿Qué propones?",
          "A Direct Lake on SQL report is slow, and Performance analyzer shows DirectQuery queries. The model uses the SQL view <code>vw_ventas_completas</code>. What do you propose?"),
   "opts": [
     opt(T("Materializar la vista como tabla en Oro y usar esa tabla en el modelo", "Materialize the view as a Gold table and use that table in the model"), T("¡Correcto! Las vistas SQL provocan fallback a DirectQuery. Una tabla física se lee en Direct Lake.", "Correct! SQL views trigger DirectQuery fallback. A physical table is read in Direct Lake."), True),
     opt(T("Agregar más visuales para repartir la carga", "Add more visuals to spread the load"), T("Más visuales = más consultas en DirectQuery. Empeora.", "More visuals = more DirectQuery queries. Worse.")),
     opt(T("Cambiar a Import y refrescar cada 5 minutos", "Switch to Import and refresh every 5 minutes"), T("Funcionaría, pero copias datos y gastas capacidad en refrescos constantes. Ataca la causa: la vista.", "It would work, but you'd copy data and burn capacity on constant refreshes. Fix the cause: the view."))]}
 ]})

# ------------------------------------------------------------------ 6.3
L.append({
 "id": "l6-3", "icon": "🕸️", "min": 25,
 "badge": {"e": "🔗", "n": T("Tejedor de relaciones", "Relationship Weaver")},
 "title": T("Laboratorio: tu modelo semántico sobre el Warehouse", "Lab: your semantic model on the Warehouse"),
 "steps": [
  {"type": "concept",
   "say": T("Antes de hacer clic, tres reglas de oro del modelado en Power BI.", "Before clicking, three golden rules of Power BI modeling."),
   "kicker": T("Reglas de oro", "Golden rules"),
   "title": T("Relaciones bien hechas, modelo feliz", "Good relationships, happy model"),
   "body": T(
    """<ul><li><b>Uno a muchos, de la dimensión a los hechos</b>: un cliente (1) tiene muchas ventas (*). La relación va de <code>dim_cliente[sk_cliente]</code> a <code>fact_ventas[sk_cliente]</code>.</li>
    <li><b>Filtro en una sola dirección</b>: la dimensión filtra a los hechos, no al revés. Las relaciones bidireccionales generan ambigüedad y resultados sorprendentes.</li>
    <li><b>Oculta lo técnico</b>: las llaves sustitutas (<code>sk_*</code>) e IDs no le sirven al usuario de negocio. Ocúltalas y deja visibles solo atributos y medidas.</li></ul>""",
    """<ul><li><b>One-to-many, from dimension to facts</b>: one customer (1) has many sales (*). The relationship goes from <code>dim_cliente[sk_cliente]</code> to <code>fact_ventas[sk_cliente]</code>.</li>
    <li><b>Single-direction filtering</b>: the dimension filters the facts, not the other way around. Bidirectional relationships create ambiguity and surprising results.</li>
    <li><b>Hide the technical bits</b>: surrogate keys (<code>sk_*</code>) and IDs mean nothing to business users. Hide them and leave only attributes and measures visible.</li></ul>"""),
   "callouts": [{"k": "key", "b": T("Marca <code>dim_fecha</code> como <b>tabla de fechas</b>. Así funcionan las funciones de inteligencia de tiempo de DAX (acumulado del año, mismo periodo del año anterior…). La columna de fecha debe tener valores únicos, sin vacíos y continuos.",
                                     "Mark <code>dim_fecha</code> as a <b>date table</b>. That's what makes DAX time-intelligence functions work (year-to-date, same period last year…). The date column must have unique, non-blank, contiguous values.")}]},
  {"type": "quiz",
   "say": T("Pregunta de modelado.", "Modeling question."),
   "q": T("¿Qué cardinalidad y dirección de filtro debe tener la relación entre <code>dim_producto</code> y <code>fact_ventas</code>?",
          "What cardinality and filter direction should the relationship between <code>dim_producto</code> and <code>fact_ventas</code> have?"),
   "opts": [
     opt(T("Muchos a muchos, bidireccional", "Many-to-many, bidirectional"), T("Muchos a muchos solo se usa en casos especiales; aquí cada venta tiene un único producto.", "Many-to-many is for special cases; here each sale has exactly one product.")),
     opt(T("Uno (dim_producto) a muchos (fact_ventas), filtro en una dirección", "One (dim_producto) to many (fact_ventas), single-direction filter"), T("¡Exacto! El patrón de estrella clásico.", "Exactly! The classic star pattern."), True),
     opt(T("Uno a uno", "One-to-one"), T("Un producto aparece en muchas ventas, así que no es uno a uno.", "A product appears in many sales, so it's not one-to-one."))]},
  {"type": "lab",
   "say": T("A construir. Trabajarás desde el navegador, sin instalar nada. 🧑‍💻", "Let's build. You'll work in the browser, no installs needed. 🧑‍💻"),
   "title": T("Laboratorio: modelo semántico Direct Lake sobre wh_ventas", "Lab: Direct Lake semantic model on wh_ventas"),
   "intro": T("Usa el Warehouse <code>wh_ventas</code> del Nivel 4. <i>Los nombres de los botones pueden variar un poco según tu versión de Fabric.</i>", "Use the <code>wh_ventas</code> Warehouse from Level 4. <i>Button names may vary slightly with your Fabric version.</i>"),
   "tasks": [
     {"t": T("Abre <code>wh_ventas</code> y elige <b>New semantic model</b>. Nómbralo <code>sm_ventas</code> y marca <code>fact_ventas</code>, <code>dim_cliente</code>, <code>dim_producto</code> y <code>dim_fecha</code>. <b>No</b> marques <code>fact_ventas_dev</code>.",
             "Open <code>wh_ventas</code> and choose <b>New semantic model</b>. Name it <code>sm_ventas</code> and tick <code>fact_ventas</code>, <code>dim_cliente</code>, <code>dim_producto</code> and <code>dim_fecha</code>. Do <b>not</b> tick <code>fact_ventas_dev</code>.")},
     {"t": T("Se abre el editor del modelo en el navegador. Si no aparece, revisa el bloqueador de ventanas emergentes o usa <b>Open data model</b> desde el workspace.", "The model editor opens in the browser. If it doesn't, check your pop-up blocker or use <b>Open data model</b> from the workspace.")},
     {"t": T("Crea las 3 relaciones arrastrando cada llave de la dimensión sobre su columna en la tabla de hechos: <code>sk_cliente</code>, <code>sk_producto</code> y <code>sk_fecha</code>. Verifica que digan <b>1 → *</b> y dirección <b>Single</b>.", "Create the 3 relationships by dragging each dimension key onto its column in the fact table: <code>sk_cliente</code>, <code>sk_producto</code> and <code>sk_fecha</code>. Check they show <b>1 → *</b> and <b>Single</b> direction.")},
     {"t": T("Oculta las columnas técnicas: clic derecho → <b>Hide</b> en todas las <code>sk_*</code> y en <code>id_venta</code>.", "Hide the technical columns: right-click → <b>Hide</b> on every <code>sk_*</code> and on <code>id_venta</code>.")},
     {"t": T("Selecciona <code>dim_fecha</code> → <b>Mark as date table</b> → columna <code>fecha</code>.", "Select <code>dim_fecha</code> → <b>Mark as date table</b> → column <code>fecha</code>.")},
     {"t": T("Renombra para el negocio: <code>region</code> → <b>Región</b>, <code>cliente</code> → <b>Cliente</b>, <code>producto</code> → <b>Producto</b>. Formatea <code>monto</code> como moneda.", "Rename for the business: <code>region</code> → <b>Región</b>, <code>cliente</code> → <b>Cliente</b>, <code>producto</code> → <b>Producto</b>. Format <code>monto</code> as currency.")}],
   "expect": T("Una estrella con 4 tablas y 3 relaciones uno a muchos. El usuario de negocio solo ve nombres claros: Región, Cliente, Producto, fecha y monto. Las llaves quedan ocultas, pero siguen trabajando.",
               "A star with 4 tables and 3 one-to-many relationships. Business users only see clear names: Región, Cliente, Producto, fecha and monto. The keys are hidden but still doing their job.")},
  {"type": "reveal", "kind": "brain",
   "say": T("Piensa en Copilot y los agentes de datos.", "Think about Copilot and data agents."),
   "prompt": T("¿Por qué renombrar columnas y escribir descripciones en el modelo importa todavía más en la era de Copilot y de los agentes de datos?",
               "Why does renaming columns and writing descriptions in the model matter even more in the era of Copilot and data agents?"),
   "answer": T("Porque la IA <b>lee tu modelo semántico</b> para entender la pregunta. Si la columna se llama <code>mnt_vta_nt</code> y no tiene descripción, la IA adivina. Si se llama “Ventas Netas” y su descripción dice “importe sin IVA ni devoluciones”, responde bien. Un modelo bien nombrado y documentado es la base de respuestas confiables en lenguaje natural.",
               "Because AI <b>reads your semantic model</b> to understand the question. If the column is called <code>mnt_vta_nt</code> with no description, the AI guesses. If it's called “Net Sales” and its description says “amount excluding tax and returns”, it answers correctly. A well-named, documented model is the foundation for trustworthy natural-language answers.")}
 ]})

# ------------------------------------------------------------------ 6.4
L.append({
 "id": "l6-4", "icon": "🧮", "min": 28,
 "badge": {"e": "🔮", "n": T("Hechicero de DAX", "DAX Sorcerer")},
 "title": T("DAX esencial: medidas que cuentan la historia", "Essential DAX: measures that tell the story"),
 "steps": [
  {"type": "concept",
   "say": T("DAX parece Excel, pero piensa distinto. La clave es una sola idea: el <b>contexto de filtro</b>.", "DAX looks like Excel, but thinks differently. The key is one idea: <b>filter context</b>."),
   "kicker": T("Medidas", "Measures"),
   "title": T("Una fórmula, mil respuestas", "One formula, a thousand answers"),
   "body": T(
    """<p>Una <b>medida</b> es una fórmula que se calcula <b>en el momento</b>, según lo que el usuario está viendo. <code>Total Ventas = SUM(fact_ventas[monto])</code> da 8592 en una tarjeta, pero en una tabla por región da un número distinto en cada fila. Es la misma fórmula: cambia el <b>contexto de filtro</b>, es decir, qué filas están visibles en esa celda.</p>
    <ul><li><code>SUM</code>, <code>COUNTROWS</code>, <code>AVERAGE</code>: agregaciones básicas.</li>
    <li><code>DIVIDE(a, b)</code>: divide y, si <code>b</code> es cero, devuelve vacío en lugar de error.</li>
    <li><code>CALCULATE(medida, filtro)</code>: <span class="hl">la función más importante de DAX</span>. Calcula una medida <b>cambiando el contexto de filtro</b>.</li></ul>""",
    """<p>A <b>measure</b> is a formula computed <b>on the fly</b>, based on what the user is looking at. <code>Total Sales = SUM(fact_ventas[monto])</code> gives 8592 on a card, but in a table by region it gives a different number on each row. Same formula: what changes is the <b>filter context</b>, i.e. which rows are visible in that cell.</p>
    <ul><li><code>SUM</code>, <code>COUNTROWS</code>, <code>AVERAGE</code>: basic aggregations.</li>
    <li><code>DIVIDE(a, b)</code>: divides and, if <code>b</code> is zero, returns blank instead of an error.</li>
    <li><code>CALCULATE(measure, filter)</code>: <span class="hl">the most important DAX function</span>. It computes a measure <b>while changing the filter context</b>.</li></ul>"""),
   "callouts": [{"k": "watch", "b": T("Prefiere <b>medidas</b> sobre columnas calculadas para los números de negocio: se calculan al consultar, no ocupan memoria fila por fila y respetan los filtros del reporte.",
                                       "Prefer <b>measures</b> over calculated columns for business numbers: they compute at query time, don't take memory row by row and respect report filters.")}]},
  {"type": "fill",
   "say": T("Escribe tus primeras cuatro medidas.", "Write your first four measures."),
   "title": T("Completa las medidas DAX", "Complete the DAX measures"),
   "code": "Total Ventas   = {{0}}(fact_ventas[monto])\n\nNum Ventas     = {{1}}(fact_ventas)\n\nTicket Promedio = {{2}}([Total Ventas], [Num Ventas])\n\nVentas Norte   = {{3}}([Total Ventas], dim_cliente[Región] = \"Norte\")",
   "blanks": [
     {"a": ["sum"], "hint": T("Suma una columna.", "Sums a column.")},
     {"a": ["countrows"], "hint": T("Cuenta las filas de una tabla: COUNT + ROWS.", "Counts a table's rows: COUNT + ROWS.")},
     {"a": ["divide"], "hint": T("División segura que no truena con cero.", "Safe division that won't blow up on zero.")},
     {"a": ["calculate"], "hint": T("La reina de DAX: calcula cambiando filtros.", "The queen of DAX: computes while changing filters.")}]},
  {"type": "lab",
   "say": T("¡El momento que esperabas! Tu primer reporte sobre datos que tú mismo llevaste de un CSV hasta Oro. 🎉", "The moment you've been waiting for! Your first report on data you took yourself from a CSV all the way to Gold. 🎉"),
   "title": T("Laboratorio: medidas y tu primer reporte Direct Lake", "Lab: measures and your first Direct Lake report"),
   "intro": T("Abre <code>sm_ventas</code> en modo de edición. Crea cada medida en la tabla <code>fact_ventas</code> con <b>New measure</b>. Ojo: como en la lección 6.3 renombraste la columna a <b>Región</b>, en DAX se escribe <code>dim_cliente[Región]</code>.", "Open <code>sm_ventas</code> in edit mode. Create each measure on the <code>fact_ventas</code> table with <b>New measure</b>. Note: since you renamed the column to <b>Región</b> in lesson 6.3, in DAX you write <code>dim_cliente[Región]</code>."),
   "tasks": [
     {"t": T("Crea las medidas:", "Create the measures:"),
      "code": "Total Ventas = SUM(fact_ventas[monto])\nNum Ventas = COUNTROWS(fact_ventas)\nTicket Promedio = DIVIDE([Total Ventas], [Num Ventas])\nVentas Norte = CALCULATE([Total Ventas], dim_cliente[Región] = \"Norte\")\n% del Total = DIVIDE([Total Ventas], CALCULATE([Total Ventas], ALL(dim_cliente)))"},
     {"t": T("Formatea <b>Total Ventas</b>, <b>Ticket Promedio</b> y <b>Ventas Norte</b> como moneda con 2 decimales, y <b>% del Total</b> como porcentaje.", "Format <b>Total Ventas</b>, <b>Ticket Promedio</b> and <b>Ventas Norte</b> as currency with 2 decimals, and <b>% del Total</b> as a percentage.")},
     {"t": T("Elige <b>New report</b>. Agrega 3 tarjetas: Total Ventas, Num Ventas y Ticket Promedio.", "Choose <b>New report</b>. Add 3 cards: Total Ventas, Num Ventas and Ticket Promedio.")},
     {"t": T("Agrega una <b>tabla</b> con Región, Total Ventas, Ventas Norte y % del Total.", "Add a <b>table</b> with Región, Total Ventas, Ventas Norte and % del Total.")},
     {"t": T("Agrega un <b>gráfico de barras</b> de Total Ventas por Producto. Guarda el reporte como <code>rpt_ventas</code>.", "Add a <b>bar chart</b> of Total Ventas by Producto. Save the report as <code>rpt_ventas</code>.")}],
   "expect": T("""<p>Tarjetas: <b>8592.00 · 11 · 781.09</b>. Tabla por región:</p>
     <table class="res"><tr><th>Región</th><th>Total Ventas</th><th>Ventas Norte</th><th>% del Total</th></tr>
     <tr><td>Norte</td><td>3735.75</td><td>3735.75</td><td>43.48%</td></tr><tr><td>Sur</td><td>1860.75</td><td>3735.75</td><td>21.66%</td></tr>
     <tr><td>Centro</td><td>1670.00</td><td>3735.75</td><td>19.44%</td></tr><tr><td>Occidente</td><td>1325.50</td><td>3735.75</td><td>15.43%</td></tr></table>
     <p>Barras por producto: Refresco 600ml 3720.25 · Agua 1L 2070.50 · Te frio 500ml 1935.00 · Jugo 1L 866.25. ¿Te llamó la atención que <b>Ventas Norte</b> repite 3735.75 en todas las filas? La siguiente pregunta lo explica.</p>""",
     """<p>Cards: <b>8592.00 · 11 · 781.09</b>. Table by region:</p>
     <table class="res"><tr><th>Región</th><th>Total Ventas</th><th>Ventas Norte</th><th>% del Total</th></tr>
     <tr><td>Norte</td><td>3735.75</td><td>3735.75</td><td>43.48%</td></tr><tr><td>Sur</td><td>1860.75</td><td>3735.75</td><td>21.66%</td></tr>
     <tr><td>Centro</td><td>1670.00</td><td>3735.75</td><td>19.44%</td></tr><tr><td>Occidente</td><td>1325.50</td><td>3735.75</td><td>15.43%</td></tr></table>
     <p>Bars by product: Refresco 600ml 3720.25 · Agua 1L 2070.50 · Te frio 500ml 1935.00 · Jugo 1L 866.25. Did you notice <b>Ventas Norte</b> repeats 3735.75 on every row? The next question explains why.</p>""")},
  {"type": "quiz",
   "say": T("Esta pregunta es el “clic” de DAX. Cuando la entiendes, todo cambia. 💡", "This question is DAX's “aha” moment. Once you get it, everything changes. 💡"),
   "q": T("¿Por qué <b>Ventas Norte</b> muestra 3735.75 incluso en la fila de “Sur”?", "Why does <b>Ventas Norte</b> show 3735.75 even on the “Sur” row?"),
   "opts": [
     opt(T("Es un error de la relación entre tablas", "It's a relationship error"), T("Las relaciones están bien: Total Ventas sí cambia por fila.", "The relationships are fine: Total Ventas does change per row.")),
     opt(T("CALCULATE <b>reemplaza</b> el filtro de región de la fila por region = \"Norte\"", "CALCULATE <b>replaces</b> the row's region filter with region = \"Norte\""),
         T("¡Exacto! En la fila “Sur”, el contexto dice region = Sur, pero CALCULATE lo sobrescribe con Norte. Por eso <b>% del Total</b> usa <code>ALL(dim_cliente)</code>: quita el filtro de región para obtener el gran total como denominador.",
           "Exactly! On the “Sur” row, the context says region = Sur, but CALCULATE overrides it with Norte. That's why <b>% del Total</b> uses <code>ALL(dim_cliente)</code>: it removes the region filter to get the grand total as the denominator."), True),
     opt(T("Direct Lake no soporta filtros por fila", "Direct Lake doesn't support row filters"), T("Direct Lake soporta DAX completo; esto es comportamiento de CALCULATE.", "Direct Lake supports full DAX; this is CALCULATE behavior."))]},
  {"type": "quiz",
   "say": T("Haz la cuenta.", "Do the math."),
   "q": T("Si filtras el reporte para ver solo el producto <b>Agua 1L</b>, ¿qué muestra la tarjeta <b>Num Ventas</b>?", "If you filter the report to show only <b>Agua 1L</b>, what does the <b>Num Ventas</b> card show?"),
   "opts": [
     opt("11", T("Eso es sin filtro. El filtro de producto cambia el contexto.", "That's unfiltered. The product filter changes the context.")),
     opt("3", T("¡Correcto! Ventas 1, 7 y 11: 1250.50 + 300.00 + 520.00 = 2070.50.", "Correct! Sales 1, 7 and 11: 1250.50 + 300.00 + 520.00 = 2070.50."), True),
     opt("4", T("Revisa: las ventas de Agua 1L son los ids 1, 7 y 11. La del id 4 se filtró en Plata por monto negativo.", "Check: Agua 1L sales are ids 1, 7 and 11. Id 4 was filtered out in Silver for its negative amount."))]}
 ]})

# ------------------------------------------------------------------ 6.5
L.append({
 "id": "l6-5", "icon": "🔐", "min": 22,
 "badge": {"e": "🏆", "n": T("Maestro del modelo semántico", "Semantic Model Master")},
 "title": T("Seguridad, rendimiento y el desafío final", "Security, performance and the final challenge"),
 "steps": [
  {"type": "concept",
   "say": T("Mismo reporte, distintos ojos: cada gerente ve solo lo suyo. 👀", "Same report, different eyes: each manager sees only their own data. 👀"),
   "kicker": T("Seguridad en el modelo", "Model security"),
   "title": T("Seguridad por fila (RLS) en el modelo semántico", "Row-level security (RLS) in the semantic model"),
   "body": T(
    """<p>Con <b>RLS</b> defines <b>roles</b> con un filtro DAX. Por ejemplo, el rol “Gerente Norte” tiene el filtro <code>[Región] = "Norte"</code> en <code>dim_cliente</code>. Gracias a las relaciones, ese filtro baja a <code>fact_ventas</code> y el gerente solo ve ventas del Norte, en <b>todos</b> los visuales.</p>
    <p>Para no crear un rol por persona se usa <b>RLS dinámica</b>: una tabla de seguridad relaciona correos con regiones, y el filtro usa <code>USERPRINCIPALNAME()</code> para saber quién está viendo.</p>""",
    """<p>With <b>RLS</b> you define <b>roles</b> with a DAX filter. For example, the “Gerente Norte” role has the filter <code>[Región] = "Norte"</code> on <code>dim_cliente</code>. Thanks to the relationships, that filter flows down to <code>fact_ventas</code> and the manager only sees Norte sales, in <b>every</b> visual.</p>
    <p>To avoid one role per person, use <b>dynamic RLS</b>: a security table maps emails to regions, and the filter uses <code>USERPRINCIPALNAME()</code> to know who's viewing.</p>"""),
   "callouts": [{"k": "watch", "b": T("RLS filtra a quienes <b>leen</b> el reporte. Los administradores, miembros y colaboradores del workspace pueden ver todos los datos. Comparte con lectores, no los agregues como miembros del workspace.",
                                       "RLS filters people who <b>read</b> the report. Workspace admins, members and contributors can see all the data. Share with viewers; don't add them as workspace members.")}]},
  {"type": "lab",
   "say": T("Vas a crear un rol y verlo con los ojos del gerente. 🕶️", "You'll create a role and see the report through the manager's eyes. 🕶️"),
   "title": T("Laboratorio: rol “Gerente Norte”", "Lab: “Gerente Norte” role"),
   "intro": T("En <code>sm_ventas</code>, modo de edición.", "In <code>sm_ventas</code>, edit mode."),
   "tasks": [
     {"t": T("<b>Manage roles → New role</b>: nómbralo <code>Gerente Norte</code>. En la tabla <code>dim_cliente</code>, agrega el filtro DAX:", "<b>Manage roles → New role</b>: name it <code>Gerente Norte</code>. On the <code>dim_cliente</code> table, add the DAX filter:"), "code": "[Región] = \"Norte\""},
     {"t": T("Guarda. Abre <code>rpt_ventas</code> y usa <b>View as</b> (o <i>Test as role</i>) con el rol <code>Gerente Norte</code>.", "Save. Open <code>rpt_ventas</code> and use <b>View as</b> (or <i>Test as role</i>) with the <code>Gerente Norte</code> role.")},
     {"t": T("Observa las tarjetas, la tabla y las barras. Luego sal de la vista del rol.", "Look at the cards, the table and the bars. Then exit the role view.")}],
   "expect": T("Con el rol: <b>Total Ventas 3735.75 · Num Ventas 3 · Ticket Promedio 1245.25</b>. La tabla solo muestra Norte (y su <b>% del Total</b> es 100%, porque el rol limita incluso al “gran total”). Las barras solo muestran Agua 1L (1250.50), Refresco 600ml (1780.25) y Te frio 500ml (705.00).",
               "With the role: <b>Total Ventas 3735.75 · Num Ventas 3 · Ticket Promedio 1245.25</b>. The table only shows Norte (and its <b>% del Total</b> is 100%, because the role limits even the “grand total”). The bars only show Agua 1L (1250.50), Refresco 600ml (1780.25) and Te frio 500ml (705.00).")},
  {"type": "concept",
   "say": T("Para cerrar, la lista de revisión de rendimiento que uso con mis clientes.", "To wrap up, the performance checklist I use with my clients."),
   "title": T("Checklist de un modelo Direct Lake sano", "Checklist for a healthy Direct Lake model"),
   "body": T("", ""),
   "cards": [
     {"e": "⭐", "n": T("Modelo estrella", "Star schema"), "d": T("Hechos delgados, dimensiones descriptivas y relaciones 1 → * en una dirección.", "Slim facts, descriptive dimensions and single-direction 1 → * relationships."), "star": True},
     {"e": "🧱", "n": T("Tablas, no vistas", "Tables, not views"), "d": T("Vistas SQL = fallback a DirectQuery en Direct Lake sobre SQL.", "SQL views = DirectQuery fallback in Direct Lake on SQL.")},
     {"e": "🗜️", "n": "V-Order + OPTIMIZE", "d": T("En las tablas Oro: menos archivos y lectura más rápida.", "On Gold tables: fewer files and faster reads.")},
     {"e": "✂️", "n": T("Solo las columnas necesarias", "Only the columns you need"), "d": T("Cada columna extra ocupa memoria. Si nadie la usa, no la incluyas.", "Every extra column takes memory. If nobody uses it, leave it out.")},
     {"e": "📏", "n": "Guardrails", "d": T("Revisa filas y archivos por tabla contra los límites de tu SKU.", "Check rows and files per table against your SKU's limits.")},
     {"e": "🔄", "n": T("Framing tras la carga", "Framing after the load"), "d": T("Refresca el modelo al final del pipeline de carga.", "Refresh the model at the end of the load pipeline.")}]},
  {"type": "match",
   "say": T("🏁 <b>Desafío final del Nivel 6.</b> Síntoma → solución.", "🏁 <b>Level 6 final challenge.</b> Symptom → fix."),
   "title": T("Desafío: el médico del modelo", "Challenge: the model doctor"),
   "pairs": [
     [T("El reporte no muestra la carga de esta mañana", "The report doesn't show this morning's load"), T("Refresh (framing) del modelo", "Model refresh (framing)")],
     [T("Consultas en DirectQuery por una vista SQL", "DirectQuery queries because of a SQL view"), T("Materializar la vista como tabla", "Materialize the view as a table")],
     [T("Cada gerente debe ver solo su región", "Each manager must see only their region"), T("RLS con USERPRINCIPALNAME()", "RLS with USERPRINCIPALNAME()")],
     [T("Tres áreas calculan distinto “Ventas Netas”", "Three departments compute “Net Sales” differently"), T("Una medida única en el modelo", "A single measure in the model")],
     [T("El % del total sale 100% en cada fila", "% of total shows 100% on every row"), T("ALL() en el denominador", "ALL() in the denominator")]]},
  {"type": "quiz",
   "say": T("Última pregunta del nivel… y del recorrido completo de datos. 🎓", "Last question of the level… and of the full data journey. 🎓"),
   "q": T("Repasemos el viaje completo del curso. ¿Cuál es el orden correcto?", "Let's review the course's full journey. What's the right order?"),
   "opts": [
     opt(T("CSV → Lakehouse (Bronce) → PySpark y MERGE (Plata) → Warehouse con estrella (Oro) → modelo semántico Direct Lake → reporte con RLS",
           "CSV → Lakehouse (Bronze) → PySpark and MERGE (Silver) → Warehouse with a star schema (Gold) → Direct Lake semantic model → report with RLS"),
         T("¡Exacto! Y en cada paso validaste con cifras de control: 11 → 9 → 11 filas y 8592.00 de principio a fin. Eso es ingeniería de datos profesional. 🏆",
           "Exactly! And at every step you validated with control totals: 11 → 9 → 11 rows and 8592.00 end to end. That's professional data engineering. 🏆"), True),
     opt(T("Reporte → modelo semántico → Warehouse → CSV", "Report → semantic model → Warehouse → CSV"), T("¡Al revés! Los datos fluyen desde la fuente hacia el consumo.", "Backwards! Data flows from source to consumption.")),
     opt(T("CSV → Power BI Import directamente", "CSV → Power BI Import directly"), T("Funciona para un prototipo, pero sin capas, sin validación y sin una sola versión de la verdad.", "Fine for a prototype, but no layers, no validation and no single version of the truth."))]}
 ]})

out = {"id": 6,
       "title": T("Modelado semántico y Direct Lake", "Semantic modeling and Direct Lake"),
       "desc": T("Modelos semánticos, Direct Lake por dentro, relaciones, DAX esencial, RLS y tu primer reporte sobre datos propios.", "Semantic models, Direct Lake under the hood, relationships, essential DAX, RLS and your first report on your own data."),
       "lessons": L}
dst = pathlib.Path(__file__).resolve().parent.parent / "content/level-6.json"
dst.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", dst, sum(len(l["steps"]) for l in L), "steps")
