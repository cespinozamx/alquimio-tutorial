"""Genera content/level-3.json — Nivel 3: Spark y Notebooks a fondo."""
import json, pathlib

def T(es, en): return {"es": es, "en": en}
def opt(t, why, ok=False):
    o = {"t": t, "why": why}
    if ok: o["ok"] = 1
    return o

L = []

# ------------------------------------------------------------------ 3.1
L.append({
 "id": "l3-1", "icon": "🧠", "min": 18,
 "badge": {"e": "🍳", "n": T("Jefe de cocina Spark", "Spark Head Chef")},
 "title": T("Cómo piensa Spark: driver, ejecutores y pereza", "How Spark thinks: driver, executors and laziness"),
 "steps": [
  {"type": "story",
   "say": T("Nivel 3. Hoy entramos a la cocina de Spark. Si entiendes esto, entiendes el 90% de los problemas de rendimiento.",
            "Level 3. Today we walk into Spark's kitchen. Understand this and you understand 90% of performance problems."),
   "kicker": T("Una cocina industrial", "An industrial kitchen"),
   "title": T("El chef, los cocineros y las comandas", "The chef, the cooks and the tickets"),
   "body": T(
    """<p>Imagina una cocina enorme. El <b>chef</b> (el <b>driver</b>) no cocina: lee el pedido, planea la receta y reparte el trabajo. Los <b>cocineros</b> (los <b>ejecutores</b>) cocinan en paralelo, cada uno con su porción de ingredientes. Cada porción es una <b>partición</b> de tus datos.</p>
    <p>Y aquí está el truco: el chef es <b>perezoso</b> (<i>lazy</i>). Mientras le dictas pasos (“filtra”, “agrega una columna”, “agrupa”), solo los anota en la comanda. <span class="hl">Nadie enciende la estufa hasta que alguien pide el plato</span>: un <code>count()</code>, un <code>display()</code> o un <code>write</code>.</p>
    <p>¿Por qué? Porque con la comanda completa el chef puede <b>optimizar</b>: juntar pasos, descartar columnas que nadie usa y filtrar lo antes posible.</p>""",
    """<p>Picture a huge kitchen. The <b>chef</b> (the <b>driver</b>) doesn't cook: they read the order, plan the recipe and hand out work. The <b>cooks</b> (the <b>executors</b>) cook in parallel, each with their own share of ingredients. Each share is a <b>partition</b> of your data.</p>
    <p>And here's the trick: the chef is <b>lazy</b>. While you dictate steps (“filter”, “add a column”, “group”), they just write them on the ticket. <span class="hl">Nobody turns on the stove until someone orders the dish</span>: a <code>count()</code>, a <code>display()</code> or a <code>write</code>.</p>
    <p>Why? Because with the full ticket the chef can <b>optimize</b>: merge steps, drop columns nobody uses and filter as early as possible.</p>"""),
   "visual": "sparkCluster"},
  {"type": "concept",
   "say": T("Dos familias de operaciones. Apréndelas de memoria.", "Two families of operations. Learn them by heart."),
   "title": T("Transformaciones vs acciones", "Transformations vs actions"),
   "body": T("<p>Las <b>transformaciones</b> crean un DataFrame nuevo y son perezosas. Las <b>acciones</b> piden un resultado y disparan el trabajo real.</p>",
             "<p><b>Transformations</b> create a new DataFrame and are lazy. <b>Actions</b> ask for a result and trigger real work.</p>"),
   "cards": [
     {"e": "📝", "n": T("Transformaciones (perezosas)", "Transformations (lazy)"), "d": "select, filter, withColumn, join, groupBy, orderBy, dropDuplicates"},
     {"e": "🔥", "n": T("Acciones (ejecutan)", "Actions (execute)"), "d": "count, display, show, collect, take, write / saveAsTable", "star": True}],
   "callouts": [
     {"k": "key", "b": T("Algunas transformaciones obligan a <b>reacomodar datos entre ejecutores</b> (<i>shuffle</i>): <code>groupBy</code>, <code>join</code>, <code>orderBy</code>, <code>dropDuplicates</code>. Son las más caras porque mueven datos por la red.",
                          "Some transformations force <b>data to move between executors</b> (a <i>shuffle</i>): <code>groupBy</code>, <code>join</code>, <code>orderBy</code>, <code>dropDuplicates</code>. They're the most expensive because they move data across the network.")},
     {"k": "watch", "b": T("<code>collect()</code> trae <b>todas</b> las filas al driver. Con una tabla grande, el chef se queda sin espacio en la mesa y el notebook falla por falta de memoria. Para explorar usa <code>display()</code> o <code>take(10)</code>.",
                           "<code>collect()</code> brings <b>every</b> row to the driver. With a big table, the chef runs out of counter space and the notebook fails with out-of-memory. For exploring, use <code>display()</code> or <code>take(10)</code>.")}]},
  {"type": "quiz",
   "say": T("Piensa: ¿cuál de estas líneas hace que Spark <b>trabaje de verdad</b>?", "Think: which of these lines makes Spark <b>actually work</b>?"),
   "q": T("Ejecutas estas líneas una por una. ¿En cuál empieza a procesar datos el clúster?", "You run these lines one by one. On which one does the cluster start processing data?"),
   "opts": [
     opt("<code>df2 = df.filter(F.col(\"monto\") > 0)</code>", T("Filter es una transformación: solo se anota en la comanda.", "Filter is a transformation: it only goes on the ticket.")),
     opt("<code>df3 = df2.withColumn(\"iva\", F.col(\"monto\") * 0.16)</code>", T("También es transformación. El chef sigue anotando.", "Also a transformation. The chef is still taking notes.")),
     opt("<code>df3.count()</code>", T("¡Exacto! <code>count()</code> es una acción: ahora sí se ejecutan el filtro, la columna nueva y el conteo, todo de una vez y optimizado.", "Exactly! <code>count()</code> is an action: now the filter, the new column and the count all run at once, optimized."), True)]},
  {"type": "quiz",
   "say": T("Ahora identifica la operación cara.", "Now spot the expensive operation."),
   "q": T("¿Cuál de estas operaciones provoca un <i>shuffle</i> (mover datos entre ejecutores)?", "Which of these operations causes a <i>shuffle</i> (moving data between executors)?"),
   "opts": [
     opt("<code>select(\"region\", \"monto\")</code>", T("Cada ejecutor elige columnas de su propia partición. No hay que mover nada.", "Each executor picks columns from its own partition. Nothing has to move.")),
     opt("<code>groupBy(\"region\").sum(\"monto\")</code>", T("Correcto: para sumar por región, todas las filas de “Norte” deben juntarse en el mismo lugar, vengan de la partición que vengan.", "Correct: to sum by region, every “Norte” row must end up in the same place, whatever partition it came from."), True),
     opt("<code>filter(F.col(\"monto\") > 0)</code>", T("Cada ejecutor filtra lo suyo, sin hablar con los demás.", "Each executor filters its own rows without talking to the others."))]},
  {"type": "order",
   "say": T("Ordena lo que pasa desde que escribes código hasta que ves el resultado.", "Order what happens from writing code to seeing the result."),
   "title": T("El viaje de una consulta Spark", "The journey of a Spark query"),
   "items": [T("Escribes transformaciones (filter, withColumn, groupBy…)", "You write transformations (filter, withColumn, groupBy…)"),
             T("Llamas una acción (count, display, write)", "You call an action (count, display, write)"),
             T("El driver arma y optimiza el plan de ejecución", "The driver builds and optimizes the execution plan"),
             T("El plan se divide en etapas y tareas", "The plan is split into stages and tasks"),
             T("Los ejecutores procesan sus particiones en paralelo", "Executors process their partitions in parallel"),
             T("El resultado llega al driver o se escribe en Delta", "The result reaches the driver or is written to Delta")]},
  {"type": "reveal", "kind": "brain",
   "say": T("Un clásico de entrevista. Piensa antes de revelar.", "An interview classic. Think before revealing."),
   "prompt": T("Si Spark es perezoso, ¿por qué un notebook con 20 celdas de transformaciones a veces tarda <b>solo</b> en la última celda?",
               "If Spark is lazy, why does a notebook with 20 cells of transformations sometimes take time <b>only</b> in the last cell?"),
   "answer": T("Porque las 19 primeras celdas solo construyen el plan; la última tiene la <b>acción</b> (por ejemplo, <code>write</code>) que ejecuta todo junto. Por eso, cuando depures, no culpes a la última celda: el trabajo real incluye todos los pasos anteriores. Un tip: si llamas varias acciones sobre el mismo DataFrame, Spark recalcula todo cada vez, salvo que uses <code>cache()</code>.",
               "Because the first 19 cells only build the plan; the last one holds the <b>action</b> (e.g. <code>write</code>) that runs everything together. So when debugging, don't blame the last cell: the real work includes every previous step. Tip: if you call several actions on the same DataFrame, Spark recomputes everything each time unless you use <code>cache()</code>.")}
 ]})

# ------------------------------------------------------------------ 3.2
L.append({
 "id": "l3-2", "icon": "🗣️", "min": 22,
 "badge": {"e": "🌐", "n": T("Bilingüe de Spark", "Spark Bilingual")},
 "title": T("DataFrames y Spark SQL: dos idiomas, un motor", "DataFrames and Spark SQL: two languages, one engine"),
 "steps": [
  {"type": "concept",
   "say": T("¿Eres más de SQL o de Python? Buenas noticias: <b>no tienes que elegir</b>.", "More of a SQL or a Python person? Good news: <b>you don't have to choose</b>."),
   "kicker": T("Dos idiomas", "Two languages"),
   "title": T("El mismo plan, escrito de dos formas", "The same plan, written two ways"),
   "body": T(
    """<p>En un notebook de Fabric puedes escribir la misma lógica con la API de <b>DataFrames</b> (PySpark) o con <b>Spark SQL</b>. Las dos generan <b>el mismo plan de ejecución</b>, así que rinden igual. Elige la que se lea mejor para cada paso.</p>
    <ul><li><code>spark.sql("SELECT …")</code> ejecuta SQL desde Python y devuelve un DataFrame.</li>
    <li>Una celda que empieza con <code>%%sql</code> es una celda completa de SQL.</li>
    <li><code>df.createOrReplaceTempView("v_nombre")</code> le pone nombre a un DataFrame para usarlo desde SQL. Esa vista vive solo en tu sesión.</li></ul>""",
    """<p>In a Fabric notebook you can write the same logic with the <b>DataFrame</b> API (PySpark) or with <b>Spark SQL</b>. Both produce <b>the same execution plan</b>, so they perform the same. Pick whichever reads better for each step.</p>
    <ul><li><code>spark.sql("SELECT …")</code> runs SQL from Python and returns a DataFrame.</li>
    <li>A cell that starts with <code>%%sql</code> is a whole SQL cell.</li>
    <li><code>df.createOrReplaceTempView("v_name")</code> names a DataFrame so you can use it from SQL. That view lives only in your session.</li></ul>"""),
   "callouts": [{"k": "key", "b": T("Las tablas del Lakehouse adjunto se leen directo por nombre: <code>spark.read.table(\"silver_ventas\")</code> o <code>SELECT * FROM silver_ventas</code>.",
                                     "Tables in the attached Lakehouse are read straight by name: <code>spark.read.table(\"silver_ventas\")</code> or <code>SELECT * FROM silver_ventas</code>.")}]},
  {"type": "fill",
   "say": T("Escribe la misma idea en los dos idiomas.", "Write the same idea in both languages."),
   "title": T("Traduce entre Python y SQL", "Translate between Python and SQL"),
   "code": "df = spark.read.table(\"silver_ventas\")\n\n# 1) Registrar el DataFrame como vista temporal\ndf.{{0}}(\"v_ventas\")\n\n# 2) Versión SQL\ntotal_sql = spark.{{1}}(\"SELECT region, SUM(monto) AS total FROM v_ventas GROUP BY region\")\n\n# 3) Versión DataFrame (mismo plan)\ntotal_df = df.{{2}}(\"region\").agg(F.sum(\"monto\").alias(\"total\"))",
   "blanks": [
     {"a": ["createorreplacetempview", "createtempview"], "hint": T("create + OrReplace + TempView, todo junto.", "create + OrReplace + TempView, all together.")},
     {"a": ["sql"], "hint": T("Tres letras: el método que ejecuta una consulta SQL.", "Three letters: the method that runs a SQL query.")},
     {"a": ["groupby"], "hint": T("El equivalente de GROUP BY en la API de DataFrames.", "The DataFrame API equivalent of GROUP BY.")}]},
  {"type": "lab",
   "say": T("Vamos a usar SQL de verdad: una dimensión, un JOIN y una función de ventana.", "Let's use real SQL: a dimension, a JOIN and a window function."),
   "title": T("Laboratorio: ranking de clientes por región", "Lab: customer ranking by region"),
   "intro": T("Crea un notebook nuevo <code>nb_sql_ranking</code> y adjunta <code>lh_tutor</code>. Pega cada bloque en su propia celda.",
              "Create a new notebook <code>nb_sql_ranking</code> and attach <code>lh_tutor</code>. Paste each block into its own cell."),
   "tasks": [
     {"t": T("Celda 1: crea una pequeña tabla de dimensión con SQL.", "Cell 1: create a small dimension table with SQL."),
      "code": "%%sql\nCREATE OR REPLACE TABLE dim_region USING DELTA AS\nSELECT * FROM VALUES\n  ('Norte', 'Monterrey'),\n  ('Centro', 'CDMX'),\n  ('Sur', 'Merida'),\n  ('Occidente', 'Guadalajara')\nAS t(region, ciudad_hub);"},
     {"t": T("Celda 2: une ventas con la dimensión y calcula el lugar de cada cliente en su región con <code>RANK()</code>.", "Cell 2: join sales with the dimension and rank each customer within their region using <code>RANK()</code>."),
      "code": "%%sql\nSELECT v.region,\n       d.ciudad_hub,\n       v.cliente,\n       SUM(v.monto) AS total,\n       RANK() OVER (PARTITION BY v.region ORDER BY SUM(v.monto) DESC) AS lugar\nFROM silver_ventas v\nJOIN dim_region d ON v.region = d.region\nGROUP BY v.region, d.ciudad_hub, v.cliente\nORDER BY v.region, lugar;"},
     {"t": T("Celda 3: obtén lo mismo en PySpark y compara.", "Cell 3: get the same result in PySpark and compare."),
      "code": "from pyspark.sql import functions as F, Window\n\nv = spark.read.table(\"silver_ventas\")\nd = spark.read.table(\"dim_region\")\nw = Window.partitionBy(\"region\").orderBy(F.desc(\"total\"))\n\nranking = (v.join(d, \"region\")\n             .groupBy(\"region\", \"ciudad_hub\", \"cliente\")\n             .agg(F.sum(\"monto\").alias(\"total\"))\n             .withColumn(\"lugar\", F.rank().over(w))\n             .orderBy(\"region\", \"lugar\"))\ndisplay(ranking)"}],
   "expect": T("Las dos versiones devuelven <b>5 filas</b>. En Norte, <b>Abarrotes Luna</b> queda en primer lugar con <b>3030.75</b> y <b>Mini Market Eco</b> en segundo con 705.00. La venta negativa de este cliente ya se había filtrado en Plata.",
               "Both versions return <b>5 rows</b>. In Norte, <b>Abarrotes Luna</b> ranks first with <b>3030.75</b> and <b>Mini Market Eco</b> second with 705.00. This customer's negative sale had already been filtered out in Silver.")},
  {"type": "quiz",
   "say": T("Pregunta de rendimiento.", "Performance question."),
   "q": T("Tu compañero dice: “Siempre uso SQL porque es más rápido que PySpark”. ¿Qué le respondes?", "Your teammate says: “I always use SQL because it's faster than PySpark.” What do you answer?"),
   "opts": [
     opt(T("Tiene razón: SQL siempre es más rápido", "They're right: SQL is always faster"), T("Para la misma lógica, ambos pasan por el mismo optimizador y generan el mismo plan.", "For the same logic, both go through the same optimizer and produce the same plan.")),
     opt(T("Para la misma lógica rinden igual: ambos generan el mismo plan. Elige por legibilidad", "For the same logic they perform the same: both produce the same plan. Choose for readability"), T("¡Exacto! La diferencia real está en la lógica (filtrar temprano, evitar shuffles), no en el idioma.", "Exactly! The real difference is in the logic (filter early, avoid shuffles), not the language."), True),
     opt(T("PySpark siempre es más rápido porque es Python", "PySpark is always faster because it's Python"), T("Con la API de DataFrames, el trabajo pesado no corre en Python: lo hace el motor de Spark.", "With the DataFrame API, the heavy lifting doesn't run in Python: the Spark engine does it."))]},
  {"type": "concept",
   "say": T("Dudas que salen siempre en esta lección.", "Questions that always come up in this lesson."),
   "title": T("Dudas frecuentes", "Common questions"), "body": T("", ""),
   "callouts": [{"k": "nodumb", "qa": [
     {"q": T("¿Una vista temporal ocupa espacio en el Lakehouse?", "Does a temp view take space in the Lakehouse?"),
      "a": T("No. Es solo un nombre para un plan dentro de tu sesión de Spark. Cuando la sesión termina, desaparece. Si quieres algo permanente, guarda una tabla.", "No. It's just a name for a plan inside your Spark session. When the session ends, it's gone. If you want something permanent, save a table.")},
     {"q": T("¿Y las UDF de Python?", "What about Python UDFs?"),
      "a": T("Úsalas solo si no existe una función nativa en <code>pyspark.sql.functions</code>. Las UDF sacan los datos del motor hacia Python fila por fila y suelen ser mucho más lentas.", "Use them only if no native function exists in <code>pyspark.sql.functions</code>. UDFs pull data out of the engine into Python row by row and are usually much slower.")}]}]}
 ]})

# ------------------------------------------------------------------ 3.3
MERGE_CODE = """from pyspark.sql import functions as F
from delta.tables import DeltaTable

# 1) Punto de partida: copia de silver_ventas (9 filas)
spark.read.table("silver_ventas").write.mode("overwrite").saveAsTable("silver_ventas_m")

# 2) Los cambios de hoy: el id 2 corrige su monto y llegan dos ventas nuevas
cambios = (spark.createDataFrame(
      [(2,  "2026-01-05", "Super Sol",   "Centro",    "Refresco 600ml", 1050.00),
       (11, "2026-01-11", "Tienda Rosa", "Sur",       "Agua 1L",         520.00),
       (12, "2026-01-11", "La Esquina",  "Occidente", "Te frio 500ml",   610.00)],
      "id INT, fecha STRING, cliente STRING, region STRING, producto STRING, monto DOUBLE")
    .withColumn("fecha", F.to_date("fecha"))
    .withColumn("_ingest_ts", F.current_timestamp()))

# 3) MERGE: actualiza lo que existe, inserta lo nuevo
destino = DeltaTable.forName(spark, "silver_ventas_m")
(destino.alias("t")
   .merge(cambios.alias("s"), "t.id = s.id")
   .whenMatchedUpdateAll()
   .whenNotMatchedInsertAll()
   .execute())

display(spark.sql("SELECT COUNT(*) AS filas, ROUND(SUM(monto), 2) AS total FROM silver_ventas_m"))"""

L.append({
 "id": "l3-3", "icon": "🧬", "min": 25,
 "badge": {"e": "🧪", "n": T("Maestro del MERGE", "MERGE Master")},
 "title": T("MERGE: el antídoto contra los duplicados", "MERGE: the antidote to duplicates"),
 "steps": [
  {"type": "story",
   "say": T("¿Recuerdas las 18 filas de la lección 2.4? Hoy las curamos. 💊", "Remember the 18 rows from lesson 2.4? Today we cure them. 💊"),
   "kicker": T("Upsert", "Upsert"),
   "title": T("Actualiza lo que existe, inserta lo que falta", "Update what exists, insert what's missing"),
   "body": T(
    """<p>Con <b>Append</b>, cada fila que llega se agrega, aunque ya existiera. Con <b>Overwrite</b>, reescribes todo. Lo que casi siempre quieres en Plata es otra cosa: un <b>upsert</b>.</p>
    <p><b>MERGE</b> compara las filas nuevas (<i>source</i>) con la tabla destino (<i>target</i>) usando una <b>clave</b>, como <code>id</code>:</p>
    <ul><li>Si la clave <b>ya existe</b> → <b>actualiza</b> la fila.</li><li>Si <b>no existe</b> → la <b>inserta</b>.</li><li>Opcional: si la fuente marca la fila como borrada → la <b>elimina</b>.</li></ul>
    <p>Resultado: puedes ejecutar la misma carga varias veces y la tabla <span class="hl">queda igual</span>. Eso es ser <b>idempotente</b>.</p>""",
    """<p>With <b>Append</b>, every incoming row is added, even if it already existed. With <b>Overwrite</b>, you rewrite everything. What you almost always want in Silver is something else: an <b>upsert</b>.</p>
    <p><b>MERGE</b> compares the new rows (<i>source</i>) to the destination table (<i>target</i>) using a <b>key</b>, like <code>id</code>:</p>
    <ul><li>If the key <b>already exists</b> → <b>update</b> the row.</li><li>If it <b>doesn't</b> → <b>insert</b> it.</li><li>Optional: if the source flags the row as deleted → <b>delete</b> it.</li></ul>
    <p>Result: you can run the same load several times and the table <span class="hl">stays the same</span>. That's being <b>idempotent</b>.</p>"""),
   "visual": "mergeFlow"},
  {"type": "quiz",
   "say": T("Haz la cuenta antes del laboratorio. Usa el diagrama.", "Do the math before the lab. Use the diagram."),
   "q": T("El destino tiene 9 filas (ids 1, 2, 3, 5, 6, 7, 8, 9, 10). Llegan 3 filas: id 2 (monto corregido), id 11 e id 12. Después del MERGE, ¿cuántas filas tiene el destino?",
          "The target has 9 rows (ids 1, 2, 3, 5, 6, 7, 8, 9, 10). 3 rows arrive: id 2 (corrected amount), id 11 and id 12. After the MERGE, how many rows does the target have?"),
   "opts": [
     opt("12", T("Eso pasaría con Append: el id 2 quedaría duplicado.", "That's what Append would do: id 2 would be duplicated.")),
     opt("11", T("¡Exacto! 1 actualizada (id 2) + 2 insertadas (11 y 12) → 9 + 2 = 11.", "Exactly! 1 updated (id 2) + 2 inserted (11 and 12) → 9 + 2 = 11."), True),
     opt("3", T("Eso pasaría con Overwrite usando solo los cambios. ¡Perderías 8 ventas!", "That's what Overwrite with just the changes would do. You'd lose 8 sales!"))]},
  {"type": "fill",
   "say": T("MERGE también se escribe en SQL. Completa las palabras clave.", "MERGE can be written in SQL too. Fill in the keywords."),
   "title": T("MERGE INTO en Spark SQL", "MERGE INTO in Spark SQL"),
   "code": "MERGE INTO silver_ventas_m AS t\nUSING cambios AS s\n{{0}} t.id = s.id\nWHEN {{1}} THEN\n  UPDATE SET *\nWHEN NOT MATCHED THEN\n  {{2}} *",
   "blanks": [
     {"a": ["on"], "hint": T("Igual que en un JOIN: la condición de la clave va después de…", "Just like a JOIN: the key condition goes after…")},
     {"a": ["matched"], "hint": T("“Cuando coincide”, en inglés.", "“When it matches”.")},
     {"a": ["insert"], "hint": T("Lo que haces con una fila nueva.", "What you do with a new row.")}]},
  {"type": "lab",
   "say": T("Ejecuta el MERGE y luego <b>vuelve a ejecutarlo</b>. Si nada cambia, lo lograste.", "Run the MERGE and then <b>run it again</b>. If nothing changes, you nailed it."),
   "title": T("Laboratorio: upsert idempotente con Delta", "Lab: idempotent upsert with Delta"),
   "intro": T("Crea el notebook <code>nb_merge_ventas</code> y adjunta <code>lh_tutor</code>.", "Create the <code>nb_merge_ventas</code> notebook and attach <code>lh_tutor</code>."),
   "tasks": [
     {"t": T("Pega y ejecuta esta celda:", "Paste and run this cell:"), "code": MERGE_CODE},
     {"t": T("Anota el resultado: <code>filas</code> y <code>total</code>.", "Write down the result: <code>filas</code> and <code>total</code>.")},
     {"t": T("Ejecuta la celda <b>otra vez</b> y compara. ¿Cambió algo?", "Run the cell <b>again</b> and compare. Did anything change?")}],
   "expect": T("Las dos veces: <b>filas = 11</b> y <b>total = 8592.00</b>. Eso es idempotencia: 7392.00 original + 70 de la corrección del id 2 + 520 + 610.",
               "Both times: <b>filas = 11</b> and <b>total = 8592.00</b>. That's idempotency: the original 7392.00 + 70 from the id 2 correction + 520 + 610.")},
  {"type": "quiz",
   "say": T("Este error le pasa a todo el mundo la primera vez. 😅", "Everyone hits this error the first time. 😅"),
   "q": T("Tu MERGE falla con un mensaje de que <b>varias filas de la fuente coinciden con la misma fila del destino</b>. ¿Qué pasó?",
          "Your MERGE fails with a message that <b>multiple source rows matched the same target row</b>. What happened?"),
   "opts": [
     opt(T("La tabla destino está dañada", "The target table is corrupted"), T("El destino está bien; el problema viene de la fuente.", "The target is fine; the problem comes from the source.")),
     opt(T("La fuente trae la misma clave repetida, y Delta no sabe cuál versión usar", "The source has the same key repeated, and Delta doesn't know which version to use"),
         T("¡Correcto! Antes del MERGE, deja una sola fila por clave: <code>dropDuplicates([\"id\"])</code> o, mejor, la más reciente con una ventana <code>row_number()</code> ordenada por fecha.",
           "Correct! Before the MERGE, keep one row per key: <code>dropDuplicates([\"id\"])</code> or, better, the latest one with a <code>row_number()</code> window ordered by date."), True),
     opt(T("MERGE no funciona con más de 10 filas", "MERGE doesn't work with more than 10 rows"), T("MERGE maneja millones de filas sin problema.", "MERGE handles millions of rows just fine."))]}
 ]})

# ------------------------------------------------------------------ 3.4
L.append({
 "id": "l3-4", "icon": "⏳", "min": 22,
 "badge": {"e": "🕰️", "n": T("Viajero del tiempo Delta", "Delta Time Traveler")},
 "title": T("Delta a fondo: time travel, OPTIMIZE, V-Order y VACUUM", "Delta deep dive: time travel, OPTIMIZE, V-Order and VACUUM"),
 "steps": [
  {"type": "concept",
   "say": T("Delta tiene memoria. Hoy aprendes a usarla… y a limpiarla.", "Delta has a memory. Today you learn to use it… and to clean it up."),
   "kicker": T("El diario de la tabla", "The table's diary"),
   "title": T("Cada escritura es una versión", "Every write is a version"),
   "body": T(
    """<p>Una tabla Delta es una carpeta con archivos Parquet <b>más</b> un diario: la carpeta <code>_delta_log</code>. Cada escritura (insert, merge, overwrite, optimize) agrega una entrada y crea una <b>versión</b> nueva.</p>
    <p>Gracias a ese diario puedes:</p>
    <ul><li>Ver la historia: <code>DESCRIBE HISTORY tabla</code></li><li>Consultar el pasado: <code>SELECT … FROM tabla VERSION AS OF 3</code> o <code>TIMESTAMP AS OF '2026-01-10'</code></li><li>Deshacer un error: <code>RESTORE TABLE tabla TO VERSION AS OF 3</code></li></ul>""",
    """<p>A Delta table is a folder of Parquet files <b>plus</b> a diary: the <code>_delta_log</code> folder. Every write (insert, merge, overwrite, optimize) adds an entry and creates a new <b>version</b>.</p>
    <p>Thanks to that diary you can:</p>
    <ul><li>See the history: <code>DESCRIBE HISTORY table</code></li><li>Query the past: <code>SELECT … FROM table VERSION AS OF 3</code> or <code>TIMESTAMP AS OF '2026-01-10'</code></li><li>Undo a mistake: <code>RESTORE TABLE table TO VERSION AS OF 3</code></li></ul>"""),
   "visual": "deltaLog"},
  {"type": "concept",
   "say": T("Ahora el mantenimiento. Aquí es donde se ahorra dinero de verdad. 💰", "Now maintenance. This is where you really save money. 💰"),
   "title": T("OPTIMIZE, V-Order y VACUUM", "OPTIMIZE, V-Order and VACUUM"),
   "body": T(
    """<ul><li><b>OPTIMIZE</b> junta muchos archivos pequeños en pocos grandes. Las cargas frecuentes dejan “migajas” y leer miles de archivos pequeños es lento.</li>
    <li><b>V-Order</b> ordena y comprime los Parquet con una técnica compatible con el motor de Power BI. Acelera mucho las lecturas de <b>Direct Lake</b> y del SQL endpoint, pero hace más lentas las escrituras.</li>
    <li><b>VACUUM</b> borra físicamente los archivos viejos que ninguna versión reciente usa. Ahorra almacenamiento, pero <span class="hl">después ya no puedes viajar a esas versiones</span>. Por defecto protege los últimos 7 días.</li></ul>""",
    """<ul><li><b>OPTIMIZE</b> merges many small files into a few large ones. Frequent loads leave “crumbs”, and reading thousands of small files is slow.</li>
    <li><b>V-Order</b> sorts and compresses the Parquet files with a technique compatible with the Power BI engine. It greatly speeds up <b>Direct Lake</b> and SQL endpoint reads, but makes writes slower.</li>
    <li><b>VACUUM</b> physically deletes old files that no recent version uses. It saves storage, but <span class="hl">afterwards you can't travel back to those versions</span>. By default it protects the last 7 days.</li></ul>"""),
   "callouts": [
     {"k": "watch", "b": T("En los workspaces nuevos de Fabric, <b>V-Order está desactivado por defecto</b> (perfil de recursos <code>writeHeavy</code>) para escribir más rápido. Actívalo donde se lee mucho: típicamente las tablas <b>Oro</b> que consume Power BI.",
                           "In new Fabric workspaces, <b>V-Order is disabled by default</b> (<code>writeHeavy</code> resource profile) to write faster. Turn it on where reads dominate: typically the <b>Gold</b> tables Power BI consumes.")},
     {"k": "key", "b": T("Regla práctica: escrituras rápidas en Bronce y Plata, lecturas rápidas en Oro.", "Rule of thumb: fast writes in Bronze and Silver, fast reads in Gold.")}]},
  {"type": "match",
   "say": T("Une cada comando con su superpoder.", "Pair each command with its superpower."),
   "title": T("La caja de herramientas Delta", "The Delta toolbox"),
   "pairs": [
     ["DESCRIBE HISTORY", T("Ver quién cambió la tabla, cuándo y con qué operación", "See who changed the table, when and with which operation")],
     ["VERSION AS OF", T("Consultar la tabla como estaba en una versión anterior", "Query the table as it was at an earlier version")],
     ["RESTORE TABLE", T("Regresar la tabla a una versión anterior", "Roll the table back to an earlier version")],
     ["OPTIMIZE", T("Compactar muchos archivos pequeños", "Compact many small files")],
     ["VACUUM", T("Borrar archivos viejos que ya no se usan", "Delete old files that are no longer used")]]},
  {"type": "lab",
   "say": T("Vamos a viajar en el tiempo con la tabla del MERGE. 🕰️", "Let's time-travel with the MERGE table. 🕰️"),
   "title": T("Laboratorio: historia, viaje en el tiempo y OPTIMIZE", "Lab: history, time travel and OPTIMIZE"),
   "intro": T("Usa <code>silver_ventas_m</code> de la lección anterior, en un notebook con <code>lh_tutor</code> adjunto.", "Use <code>silver_ventas_m</code> from the previous lesson, in a notebook with <code>lh_tutor</code> attached."),
   "tasks": [
     {"t": T("Mira la historia de la tabla:", "Look at the table's history:"), "code": "%%sql\nDESCRIBE HISTORY silver_ventas_m;"},
     {"t": T("Viaja a la versión 0, cuando la tabla se creó:", "Travel to version 0, when the table was created:"), "code": "%%sql\nSELECT COUNT(*) AS filas, ROUND(SUM(monto), 2) AS total\nFROM silver_ventas_m VERSION AS OF 0;"},
     {"t": T("Compacta la tabla aplicando V-Order (Fabric lo permite en el mismo comando):", "Compact the table applying V-Order (Fabric allows it in the same command):"), "code": "%%sql\nOPTIMIZE silver_ventas_m VORDER;"},
     {"t": T("Vuelve a ejecutar <code>DESCRIBE HISTORY</code> y busca la operación <b>OPTIMIZE</b> en la parte de arriba.", "Run <code>DESCRIBE HISTORY</code> again and look for the <b>OPTIMIZE</b> operation at the top.")}],
   "expect": T("La versión 0 tiene <b>9 filas y 7392.00</b>: la tabla antes del MERGE. En la historia verás <b>CREATE OR REPLACE TABLE AS SELECT</b> (o <b>WRITE</b>), <b>MERGE</b> y, al final, <b>OPTIMIZE</b>. Con tan pocas filas OPTIMIZE casi no tiene nada que compactar; en tablas reales la diferencia es enorme.",
               "Version 0 has <b>9 rows and 7392.00</b>: the table before the MERGE. In the history you'll see <b>CREATE OR REPLACE TABLE AS SELECT</b> (or <b>WRITE</b>), <b>MERGE</b> and finally <b>OPTIMIZE</b>. With so few rows OPTIMIZE has little to compact; on real tables the difference is huge.")},
  {"type": "quiz",
   "say": T("Caso de soporte a las 9 de la mañana. ☕", "A 9 a.m. support ticket. ☕"),
   "q": T("Ejecutas <code>VACUUM</code> con la retención por defecto (7 días). Al día siguiente, auditoría pide los datos <b>como estaban hace 30 días</b>. ¿Qué pasa?",
          "You run <code>VACUUM</code> with the default retention (7 days). The next day, audit asks for the data <b>as it was 30 days ago</b>. What happens?"),
   "opts": [
     opt(T("Funciona: el diario guarda todo para siempre", "It works: the diary keeps everything forever"), T("El diario sigue ahí, pero los <b>archivos de datos</b> de esas versiones ya se borraron.", "The diary is still there, but the <b>data files</b> for those versions were deleted.")),
     opt(T("Falla: VACUUM borró los archivos que esas versiones necesitaban", "It fails: VACUUM deleted the files those versions needed"), T("Correcto. Si necesitas historia larga, ajusta la retención <b>antes</b> de hacer VACUUM, o guarda snapshots en otra tabla.", "Correct. If you need long history, adjust retention <b>before</b> running VACUUM, or keep snapshots in another table."), True)]},
  {"type": "quiz",
   "say": T("¿Dónde activas V-Order?", "Where do you turn V-Order on?"),
   "q": T("¿En cuál de estas tablas tiene más sentido activar V-Order?", "On which of these tables does V-Order make the most sense?"),
   "opts": [
     opt(T("Bronce: recibe cargas cada 5 minutos y casi nadie la consulta", "Bronze: gets loads every 5 minutes and is rarely queried"), T("Ahí pagarías escrituras más lentas sin aprovechar las lecturas.", "You'd pay for slower writes without benefiting from reads.")),
     opt(T("Oro: tabla de hechos que leen todos los reportes de Power BI en Direct Lake", "Gold: fact table read by every Power BI report in Direct Lake"), T("¡Exacto! Se escribe pocas veces y se lee muchísimas. Ahí V-Order brilla.", "Exactly! Written rarely, read constantly. That's where V-Order shines."), True)]}
 ]})

# ------------------------------------------------------------------ 3.5
CHILD = """# ── Celda 1 · márcala como celda de PARÁMETROS ──
p_region = "Norte"

# ── Celda 2 ──
import uuid
from pyspark.sql import functions as F

exec_id = str(uuid.uuid4())
df = spark.read.table("silver_ventas_m").filter(F.col("region") == p_region)
filas = df.count()
total = df.agg(F.sum("monto")).first()[0] or 0.0

# Cifra de control: una fila de auditoría por ejecución
(spark.createDataFrame([(exec_id, p_region, filas, float(total))],
                       "execution_id STRING, region STRING, filas LONG, total DOUBLE")
      .withColumn("ts", F.current_timestamp())
      .write.mode("append").saveAsTable("ctl_ejecuciones"))

notebookutils.notebook.exit(f"{p_region}:{filas}")"""

PARENT = """regiones = ["Norte", "Centro", "Sur", "Occidente"]

for r in regiones:
    resultado = notebookutils.notebook.run("nb_carga_region", 600, {"p_region": r})
    print("✔", resultado)

display(spark.sql(\"\"\"
    SELECT region, filas, ROUND(total, 2) AS total
    FROM ctl_ejecuciones
    ORDER BY ts DESC
    LIMIT 4\"\"\"))"""

L.append({
 "id": "l3-5", "icon": "🏗️", "min": 30,
 "badge": {"e": "🏆", "n": T("Ingeniero Spark profesional", "Professional Spark Engineer")},
 "title": T("Notebooks profesionales: parámetros, orquestación y rendimiento", "Professional notebooks: parameters, orchestration and performance"),
 "steps": [
  {"type": "concept",
   "say": T("Un notebook de producción no se edita a mano cada día: <b>recibe parámetros</b>.", "A production notebook isn't edited by hand every day: it <b>receives parameters</b>."),
   "kicker": T("De experimento a producción", "From experiment to production"),
   "title": T("Parámetros y orquestación entre notebooks", "Parameters and notebook orchestration"),
   "body": T(
    """<ul><li><b>Celda de parámetros</b>: una celda con valores por defecto que marcas como parámetros desde el menú de la celda. Cuando un pipeline o un notebook padre te llama, sus valores <b>reemplazan</b> a los de esa celda.</li>
    <li><code>notebookutils.notebook.run("nb", timeout, {…})</code> ejecuta otro notebook con parámetros y devuelve el texto que el hijo envía con <code>notebookutils.notebook.exit(valor)</code>.</li>
    <li><code>notebookutils.notebook.runMultiple(…)</code> ejecuta varios notebooks en paralelo, o en un orden de dependencias, compartiendo la misma sesión de Spark.</li></ul>""",
    """<ul><li><b>Parameter cell</b>: a cell with default values that you mark as parameters from the cell menu. When a pipeline or parent notebook calls you, its values <b>replace</b> those in that cell.</li>
    <li><code>notebookutils.notebook.run("nb", timeout, {…})</code> runs another notebook with parameters and returns the text the child sends with <code>notebookutils.notebook.exit(value)</code>.</li>
    <li><code>notebookutils.notebook.runMultiple(…)</code> runs several notebooks in parallel, or in a dependency order, sharing the same Spark session.</li></ul>"""),
   "callouts": [{"k": "watch", "b": T("No pongas <code>notebookutils.notebook.exit()</code> dentro de un <code>try/except</code>: ahí no surte efecto.", "Don't put <code>notebookutils.notebook.exit()</code> inside a <code>try/except</code>: it won't take effect there.")}]},
  {"type": "concept",
   "say": T("Ahora el motor. Estas perillas cambian la factura de tu cliente.", "Now the engine. These knobs change your client's bill."),
   "title": T("Cómputo y rendimiento en Fabric Spark", "Compute and performance in Fabric Spark"),
   "body": T("<p>No tienes que dominarlas todas hoy, pero sí saber que existen:</p>", "<p>You don't need to master them all today, but you should know they exist:</p>"),
   "cards": [
     {"e": "🏊", "n": T("Starter pool", "Starter pool"), "d": T("Sesiones que arrancan en segundos. Ideal para empezar.", "Sessions that start in seconds. Ideal for getting started.")},
     {"e": "🛠️", "n": T("Custom pool", "Custom pool"), "d": T("Tú eliges el tamaño de nodos y el autoescalado.", "You choose node size and autoscale.")},
     {"e": "📦", "n": "Environment", "d": T("Agrupa versión de runtime, librerías y propiedades de Spark para reutilizarlas.", "Bundles runtime version, libraries and Spark properties for reuse.")},
     {"e": "🚀", "n": "Native Execution Engine", "d": T("Motor vectorizado en C++ que acelera Spark sin cambiar tu código. Se activa en el Environment.", "A vectorized C++ engine that speeds up Spark without code changes. Enabled in the Environment."), "star": True},
     {"e": "🎚️", "n": T("Perfiles de recursos", "Resource profiles"), "d": T("Configuraciones listas: writeHeavy (por defecto en workspaces nuevos), readHeavyForSpark, readHeavyForPBI.", "Ready-made configs: writeHeavy (default in new workspaces), readHeavyForSpark, readHeavyForPBI.")},
     {"e": "🧬", "n": "Runtime", "d": T("Versión de Spark y Delta. Revisa cuál usa tu workspace en Workspace settings → Spark settings.", "Spark and Delta version. Check which one your workspace uses in Workspace settings → Spark settings.")}]},
  {"type": "fill",
   "say": T("Completa el contrato entre el notebook padre y el hijo.", "Complete the contract between the parent and child notebooks."),
   "title": T("notebookutils y %%configure", "notebookutils and %%configure"),
   "code": "# Notebook padre: ejecuta el hijo con un parámetro\nres = notebookutils.notebook.{{0}}(\"nb_carga_region\", 600, {\"p_region\": \"Sur\"})\n\n# Notebook hijo: devuelve un valor al padre\nnotebookutils.notebook.{{1}}(f\"{p_region}:{filas}\")\n\n# Primera celda de una sesión: activar el Native Execution Engine\n%%{{2}}\n{ \"conf\": { \"spark.native.enabled\": \"true\" } }",
   "blanks": [
     {"a": ["run"], "hint": T("Tres letras: ejecutar.", "Three letters: execute.")},
     {"a": ["exit"], "hint": T("Salir del notebook devolviendo un valor.", "Leave the notebook returning a value.")},
     {"a": ["configure"], "hint": T("El comando mágico que configura la sesión de Spark.", "The magic command that configures the Spark session.")}]},
  {"type": "lab",
   "say": T("Último laboratorio del nivel: un notebook parametrizado, un orquestador y <b>cifras de control</b>, como en un proyecto real.",
            "Last lab of the level: a parameterized notebook, an orchestrator and <b>control totals</b>, like in a real project."),
   "title": T("Laboratorio: notebook parametrizado + orquestador", "Lab: parameterized notebook + orchestrator"),
   "intro": T("Crearás dos notebooks. <b>Adjunta <code>lh_tutor</code> a los dos.</b>", "You'll create two notebooks. <b>Attach <code>lh_tutor</code> to both.</b>"),
   "tasks": [
     {"t": T("Crea <code>nb_carga_region</code> con estas dos celdas. En la primera, abre el menú <b>…</b> de la celda y elige <b>Toggle parameter cell</b> (o <i>Mark cell as parameters</i>).", "Create <code>nb_carga_region</code> with these two cells. On the first one, open the cell's <b>…</b> menu and pick <b>Toggle parameter cell</b> (or <i>Mark cell as parameters</i>)."), "code": CHILD},
     {"t": T("Ejecútalo una vez a mano para probarlo. Debe terminar devolviendo <code>Norte:3</code>.", "Run it once by hand to test it. It should finish returning <code>Norte:3</code>.")},
     {"t": T("Crea <code>nb_orquestador</code> con esta celda y ejecútala:", "Create <code>nb_orquestador</code> with this cell and run it:"), "code": PARENT}],
   "expect": T("""<p>Verás <code>✔ Norte:3</code>, <code>✔ Centro:2</code>, <code>✔ Sur:3</code> y <code>✔ Occidente:3</code>: suman las 11 filas de <code>silver_ventas_m</code>. En <code>ctl_ejecuciones</code>:</p>
     <table class="res"><tr><th>region</th><th>filas</th><th>total</th></tr><tr><td>Norte</td><td>3</td><td>3735.75</td></tr><tr><td>Centro</td><td>2</td><td>1670.00</td></tr><tr><td>Sur</td><td>3</td><td>1860.75</td></tr><tr><td>Occidente</td><td>3</td><td>1325.50</td></tr></table>
     <p>Suma de totales = <b>8592.00</b>, igual que en la lección 3.3. Así se demuestra que no se perdió ni se duplicó nada.</p>""",
     """<p>You'll see <code>✔ Norte:3</code>, <code>✔ Centro:2</code>, <code>✔ Sur:3</code> and <code>✔ Occidente:3</code>: together, the 11 rows of <code>silver_ventas_m</code>. In <code>ctl_ejecuciones</code>:</p>
     <table class="res"><tr><th>region</th><th>filas</th><th>total</th></tr><tr><td>Norte</td><td>3</td><td>3735.75</td></tr><tr><td>Centro</td><td>2</td><td>1670.00</td></tr><tr><td>Sur</td><td>3</td><td>1860.75</td></tr><tr><td>Occidente</td><td>3</td><td>1325.50</td></tr></table>
     <p>Sum of totals = <b>8592.00</b>, same as in lesson 3.3. That's how you prove nothing was lost or duplicated.</p>""")},
  {"type": "quiz",
   "say": T("Problema real de producción.", "A real production problem."),
   "q": T("Un pipeline llama a tu notebook con <code>p_region = \"Sur\"</code>, pero el notebook siempre procesa “Norte”. ¿Qué es lo más probable?",
          "A pipeline calls your notebook with <code>p_region = \"Sur\"</code>, but the notebook always processes “Norte”. What's most likely?"),
   "opts": [
     opt(T("La celda con <code>p_region</code> no está marcada como celda de parámetros", "The cell with <code>p_region</code> isn't marked as a parameter cell"), T("¡Exacto! Sin esa marca, Fabric no sabe dónde inyectar el valor y se queda el valor por defecto.", "Exactly! Without that mark, Fabric doesn't know where to inject the value, so the default stays."), True),
     opt(T("Los pipelines no pueden enviar parámetros a notebooks", "Pipelines can't send parameters to notebooks"), T("Sí pueden: la actividad Notebook tiene <i>base parameters</i>.", "They can: the Notebook activity has <i>base parameters</i>.")),
     opt(T("Hay que reiniciar la capacidad", "You need to restart the capacity"), T("No tiene relación. 😄", "Unrelated. 😄"))]},
  {"type": "match",
   "say": T("🏁 <b>Desafío final del Nivel 3.</b> Problema → solución.", "🏁 <b>Level 3 final challenge.</b> Problem → solution."),
   "title": T("Desafío: el doctor de Spark", "Challenge: the Spark doctor"),
   "pairs": [
     [T("Recargar el mismo archivo duplica filas en Plata", "Reloading the same file duplicates rows in Silver"), T("MERGE por clave", "MERGE on a key")],
     [T("Ayer alguien borró datos por error", "Yesterday someone deleted data by mistake"), "RESTORE TABLE … TO VERSION AS OF"],
     [T("Miles de archivos pequeños y lecturas lentas", "Thousands of small files and slow reads"), "OPTIMIZE"],
     [T("Procesar 4 regiones en paralelo en una sola sesión", "Process 4 regions in parallel in a single session"), "notebookutils.notebook.runMultiple"],
     [T("Acelerar Spark sin tocar el código", "Speed up Spark without touching the code"), "Native Execution Engine"]]},
  {"type": "quiz",
   "say": T("La última. ¡Ya casi eres Ingeniero Spark profesional!", "The last one. You're almost a Professional Spark Engineer!"),
   "q": T("Un notebook hace <code>df = spark.read.table(\"ventas_10TB\")</code> y luego <code>datos = df.collect()</code> para recorrer las filas con un <code>for</code>. Falla por memoria. ¿Qué recomiendas?",
          "A notebook does <code>df = spark.read.table(\"ventas_10TB\")</code> and then <code>datos = df.collect()</code> to loop over the rows with a <code>for</code>. It fails with out-of-memory. What do you recommend?"),
   "opts": [
     opt(T("Un nodo driver más grande", "A bigger driver node"), T("Solo pospone el problema: 10 TB no caben en una sola máquina.", "It only postpones the problem: 10 TB don't fit on one machine.")),
     opt(T("Expresar la lógica con transformaciones de DataFrame/SQL y escribir el resultado, sin traer los datos al driver", "Express the logic with DataFrame/SQL transformations and write the result, without bringing data to the driver"),
         T("¡Exacto! Deja que los ejecutores trabajen en paralelo. Un <code>for</code> sobre <code>collect()</code> convierte un clúster en una sola computadora.", "Exactly! Let the executors work in parallel. A <code>for</code> over <code>collect()</code> turns a cluster into a single computer."), True),
     opt(T("Usar <code>cache()</code> antes de <code>collect()</code>", "Use <code>cache()</code> before <code>collect()</code>"), T("cache guarda los datos en los ejecutores; collect igual los manda todos al driver.", "cache keeps data on the executors; collect still sends all of it to the driver."))]}
 ]})

out = {"id": 3,
       "title": T("Spark y Notebooks a fondo", "Spark and Notebooks deep dive"),
       "desc": T("Cómo piensa Spark, DataFrames y SQL, MERGE, mantenimiento Delta y notebooks de producción.", "How Spark thinks, DataFrames and SQL, MERGE, Delta maintenance and production notebooks."),
       "lessons": L}
dst = pathlib.Path(__file__).resolve().parent.parent / "content/level-3.json"
dst.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", dst, sum(len(l["steps"]) for l in L), "steps")
