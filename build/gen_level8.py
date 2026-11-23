"""Genera content/level-8.json — Nivel 8: Proyecto final integrador (BiciCiudad)."""
import json, pathlib

def T(es, en): return {"es": es, "en": en}
def opt(t, why, ok=False):
    o = {"t": t, "why": why}
    if ok: o["ok"] = 1
    return o

RENTAS = """id_renta,fecha,estacion,barrio,minutos,monto,metodo_pago
1,2026-02-02,EST-01,Centro,25,45.00,tarjeta
2,2026-02-02,EST-02,Norte,40,70.00,app
3,2026-02-02,EST-01,Centro,15,30.00,app
4,2026-02-03,EST-03,Sur,60,95.00,tarjeta
4,2026-02-03,EST-03,Sur,60,95.00,tarjeta
5,2026-02-03,EST-04,Poniente,-10,20.00,app
6,2026-02-04,EST-02,Norte,35,60.00,efectivo
7,2026-02-04,EST-05,Centro,50,85.00,app
8,2026-02-05,EST-04,Poniente,20,40.00,tarjeta
9,2026-02-05,EST-03,Sur,30,55.00,app
10,2026-02-06,EST-05,Centro,45,75.00,tarjeta
11,2026-02-06,EST-01,Centro,10,,app
12,2026-02-07,EST-02,Norte,55,90.00,app"""

DIA2 = """id_renta,fecha,estacion,barrio,minutos,monto,metodo_pago
9,2026-02-05,EST-03,Sur,30,65.00,app
13,2026-02-08,EST-04,Poniente,30,50.00,app"""

NB = """# ── Celda 1 · PARÁMETROS ──
p_archivo = "rentas.csv"

# ── Celda 2 · Bronce → Plata con MERGE y cifras de control ──
from pyspark.sql import functions as F
from delta.tables import DeltaTable

bronce = (spark.read.option("header", "true").option("inferSchema", "true")
               .csv(f"Files/{p_archivo}"))
print("Bronce:", bronce.count())

plata = (bronce.dropDuplicates()
               .filter((F.col("minutos") > 0) & F.col("monto").isNotNull())
               .withColumn("fecha", F.to_date("fecha"))
               .withColumn("_ingest_ts", F.current_timestamp()))

if not spark.catalog.tableExists("silver_rentas"):
    plata.write.format("delta").saveAsTable("silver_rentas")
else:
    (DeltaTable.forName(spark, "silver_rentas").alias("t")
        .merge(plata.alias("s"), "t.id_renta = s.id_renta")
        .whenMatchedUpdateAll()
        .whenNotMatchedInsertAll()
        .execute())

r = spark.sql("SELECT COUNT(*) AS filas, ROUND(SUM(monto), 2) AS total FROM silver_rentas").first()
print("Plata:", r.filas, r.total)
notebookutils.notebook.exit(f"{r.filas}|{r.total}")"""

WH_SOL = """CREATE TABLE dbo.dim_estacion (
    sk_estacion BIGINT IDENTITY,
    estacion    VARCHAR(10) NOT NULL,
    barrio      VARCHAR(30) NOT NULL
);

CREATE TABLE dbo.fact_rentas (
    id_renta    INT,
    sk_fecha    INT,
    sk_estacion BIGINT,
    metodo_pago VARCHAR(20),
    minutos     INT,
    monto       DECIMAL(10, 2)
);
GO

CREATE PROCEDURE dbo.usp_cargar_rentas AS
BEGIN
    MERGE dbo.dim_estacion AS t
    USING (SELECT DISTINCT estacion, barrio FROM lh_bici.dbo.silver_rentas) AS s
       ON t.estacion = s.estacion
    WHEN NOT MATCHED BY TARGET THEN
        INSERT (estacion, barrio) VALUES (s.estacion, s.barrio);

    MERGE dbo.fact_rentas AS t
    USING (SELECT r.id_renta,
                  YEAR(r.fecha) * 10000 + MONTH(r.fecha) * 100 + DAY(r.fecha) AS sk_fecha,
                  e.sk_estacion, r.metodo_pago, r.minutos,
                  CAST(r.monto AS DECIMAL(10, 2)) AS monto
           FROM lh_bici.dbo.silver_rentas AS r
           JOIN dbo.dim_estacion AS e ON e.estacion = r.estacion) AS s
       ON t.id_renta = s.id_renta
    WHEN MATCHED AND (t.monto <> s.monto OR t.minutos <> s.minutos) THEN
        UPDATE SET t.monto = s.monto, t.minutos = s.minutos
    WHEN NOT MATCHED BY TARGET THEN
        INSERT (id_renta, sk_fecha, sk_estacion, metodo_pago, minutos, monto)
        VALUES (s.id_renta, s.sk_fecha, s.sk_estacion, s.metodo_pago, s.minutos, s.monto);
END;"""

WH_CHECK = """EXEC dbo.usp_cargar_rentas;

SELECT e.barrio, COUNT(*) AS rentas, SUM(f.monto) AS ingresos
FROM dbo.fact_rentas f
JOIN dbo.dim_estacion e ON e.sk_estacion = f.sk_estacion
GROUP BY e.barrio
ORDER BY ingresos DESC;"""

KQL_SOL = """// Estado actual de cada estación
estado_estaciones
| summarize arg_max(ingestion_time(), *) by BikepointID
| where No_Bikes == 0
| project BikepointID, Street, Neighbourhood, No_Bikes, No_Empty_Docks

// Estaciones vacías por barrio, en este momento
estado_estaciones
| summarize arg_max(ingestion_time(), *) by BikepointID
| summarize vacias = countif(No_Bikes == 0) by Neighbourhood
| top 10 by vacias desc"""

DAX_SOL = """Ingresos = SUM(fact_rentas[monto])
Rentas = COUNTROWS(fact_rentas)
Minutos Promedio = DIVIDE(SUM(fact_rentas[minutos]), [Rentas])
Ingreso por Minuto = DIVIDE([Ingresos], SUM(fact_rentas[minutos]))
% Ingresos = DIVIDE([Ingresos], CALCULATE([Ingresos], ALL(dim_estacion)))"""

L = []

# ------------------------------------------------------------------ 8.1
L.append({
 "id": "l8-1", "icon": "🗺️", "min": 20,
 "badge": {"e": "📐", "n": T("Arquitecto del proyecto", "Project Architect")},
 "title": T("El encargo: BiciCiudad necesita una plataforma de datos", "The brief: BiciCiudad needs a data platform"),
 "steps": [
  {"type": "story",
   "say": T("¡Llegaste al proyecto final! 🎓 Aquí ya no hay recetas paso a paso: tú decides. Yo solo te doy pistas… y soluciones escondidas por si te atoras.",
            "You made it to the capstone! 🎓 No more step-by-step recipes here: you decide. I'll just give hints… and hidden solutions in case you get stuck."),
   "kicker": T("Tu primer cliente", "Your first client"),
   "title": T("El correo de BiciCiudad", "The email from BiciCiudad"),
   "body": T(
    """<p><b>BiciCiudad</b> es una empresa (ficticia) de renta de bicicletas. Su directora de operaciones te escribe:</p>
    <blockquote style="border-left:4px solid var(--copper);margin:0 0 14px;padding:8px 14px;background:#fff;border-radius:0 12px 12px 0">
    “Necesitamos dos cosas. <b>Primero</b>, un reporte confiable de ingresos por barrio, estación y método de pago. Hoy cada área tiene su Excel y nunca cuadran. <b>Segundo</b>, saber <b>en este momento</b> qué estaciones se quedaron sin bicicletas, y que logística reciba un aviso para reabastecerlas. Ah, y TI pide que todo quede versionado y con seguridad: cada gerente de barrio debe ver solo lo suyo.”</blockquote>
    <p>Vas a construir la solución completa en Fabric, uniendo <b>todo</b> lo que aprendiste: Lakehouse, Spark y MERGE, pipelines, Warehouse, Direct Lake, Real-Time Intelligence, seguridad y Git.</p>""",
    """<p><b>BiciCiudad</b> is a (fictional) bike-rental company. Its operations director writes to you:</p>
    <blockquote style="border-left:4px solid var(--copper);margin:0 0 14px;padding:8px 14px;background:#fff;border-radius:0 12px 12px 0">
    “We need two things. <b>First</b>, a reliable revenue report by neighbourhood, station and payment method. Today every department has its own Excel and they never match. <b>Second</b>, to know <b>right now</b> which stations ran out of bikes, with logistics getting an alert to restock them. Oh, and IT wants everything versioned and secured: each neighbourhood manager should see only their own data.”</blockquote>
    <p>You'll build the complete solution in Fabric, bringing together <b>everything</b> you learned: Lakehouse, Spark and MERGE, pipelines, Warehouse, Direct Lake, Real-Time Intelligence, security and Git.</p>"""),
   "visual": "capstoneArch"},
  {"type": "match",
   "say": T("Traduce cada requisito del cliente a una pieza de Fabric. Es lo primero que hace un arquitecto.", "Translate each client requirement into a Fabric piece. It's the first thing an architect does."),
   "title": T("Requisito → solución", "Requirement → solution"),
   "pairs": [
     [T("“Los Excel nunca cuadran”", "“The Excel files never match”"), T("Modelo semántico con medidas únicas", "Semantic model with single measures")],
     [T("“Saber en este momento qué estaciones están vacías”", "“Know right now which stations are empty”"), T("Eventstream + Eventhouse + KQL", "Eventstream + Eventhouse + KQL")],
     [T("“Que logística reciba un aviso”", "“Logistics gets an alert”"), "Activator"],
     [T("“Cada gerente ve solo lo suyo”", "“Each manager sees only their own”"), T("RLS en el modelo semántico", "RLS in the semantic model")],
     [T("“Todo versionado”", "“Everything versioned”"), T("Integración con Git", "Git integration")]]},
  {"type": "order",
   "say": T("Planea el orden de construcción. Primero los cimientos.", "Plan the build order. Foundations first."),
   "title": T("Plan de trabajo del proyecto", "Project work plan"),
   "items": [T("Crear el workspace y conectarlo a Git", "Create the workspace and connect it to Git"),
             T("Ruta batch: Lakehouse, notebook de Plata con MERGE y pipeline", "Batch path: Lakehouse, Silver notebook with MERGE and pipeline"),
             T("Oro en Warehouse: modelo estrella y procedimiento de carga", "Gold in Warehouse: star schema and load procedure"),
             T("Ruta en tiempo real: Eventstream, Eventhouse y alerta", "Real-time path: Eventstream, Eventhouse and alert"),
             T("Consumo: modelo semántico, reporte, RLS y endoso", "Consumption: semantic model, report, RLS and endorsement")]},
  {"type": "lab",
   "say": T("Prepara el terreno. Usa un workspace nuevo para que el proyecto quede limpio y presentable.", "Prepare the ground. Use a new workspace so the project stays clean and presentable."),
   "title": T("Reto 0: el workspace del proyecto", "Challenge 0: the project workspace"),
   "intro": T("A partir de aquí, los pasos dicen <b>qué</b> lograr. Si necesitas recordar el <b>cómo</b>, vuelve a la lección del nivel correspondiente.", "From here on, the steps say <b>what</b> to achieve. If you need to remember <b>how</b>, revisit the lesson from the matching level."),
   "tasks": [
     {"t": T("Crea el workspace <code>ws_biciudad_dev</code> con capacidad Trial o Fabric. <i>(Nivel 1)</i>", "Create the <code>ws_biciudad_dev</code> workspace with a Trial or Fabric capacity. <i>(Level 1)</i>")},
     {"t": T("Crea el Lakehouse <code>lh_bici</code>, el Warehouse <code>wh_bici</code> y el Eventhouse <code>eh_bici</code>. <i>(Niveles 1, 4 y 5)</i>", "Create the <code>lh_bici</code> Lakehouse, the <code>wh_bici</code> Warehouse and the <code>eh_bici</code> Eventhouse. <i>(Levels 1, 4 and 5)</i>")},
     {"t": T("Conecta el workspace a un repositorio nuevo <code>biciudad-fabric</code>, en la carpeta <code>fabric</code>. <i>(Nivel 7)</i>", "Connect the workspace to a new <code>biciudad-fabric</code> repository, folder <code>fabric</code>. <i>(Level 7)</i>")},
     {"t": T("Haz tu primer commit: <code>chore: estructura inicial del proyecto</code>.", "Make your first commit: <code>chore: initial project structure</code>.")}],
   "expect": T("Un workspace con tres elementos vacíos y un repositorio con su primer commit. Parece poco, pero así empiezan los proyectos profesionales: con estructura y trazabilidad desde el día uno.",
               "A workspace with three empty items and a repository with its first commit. It looks small, but that's how professional projects start: with structure and traceability from day one.")}
 ]})

# ------------------------------------------------------------------ 8.2
L.append({
 "id": "l8-2", "icon": "🚲", "min": 35,
 "badge": {"e": "🧪", "n": T("Ingeniero de la ruta batch", "Batch Path Engineer")},
 "title": T("Reto 1: la ruta batch, de Bronce a Plata con MERGE", "Challenge 1: the batch path, Bronze to Silver with MERGE"),
 "steps": [
  {"type": "reveal", "kind": "pencil",
   "say": T("Antes de escribir código, haz lo que hace un profesional: <b>calcula las cifras de control a mano</b>.", "Before writing code, do what a professional does: <b>compute the control totals by hand</b>."),
   "prompt": T(f"""Este es el archivo de rentas del día 1. Las reglas de calidad dicen que se eliminan los duplicados exactos, las rentas con minutos ≤ 0 y las que no tienen monto.<br><b>¿Cuántas filas quedarán en Plata y cuál será el total de <code>monto</code>?</b><pre style="margin-top:10px">{RENTAS}</pre>""",
               f"""This is the day-1 rentals file. Data quality rules say exact duplicates are removed, as are rentals with minutes ≤ 0 and those with no amount.<br><b>How many rows will remain in Silver, and what will the <code>monto</code> total be?</b><pre style="margin-top:10px">{RENTAS}</pre>"""),
   "answer": T("13 filas en Bronce → se quita el duplicado del id 4 (12) → se quitan el id 5 (minutos −10) y el id 11 (sin monto) → <b>10 filas</b> en Plata. Total: 45 + 70 + 30 + 95 + 60 + 85 + 40 + 55 + 75 + 90 = <b>645.00</b>. Guarda estos números: son tu contrato con el cliente.",
               "13 rows in Bronze → remove id 4's duplicate (12) → remove id 5 (−10 minutes) and id 11 (no amount) → <b>10 rows</b> in Silver. Total: 45 + 70 + 30 + 95 + 60 + 85 + 40 + 55 + 75 + 90 = <b>645.00</b>. Keep these numbers: they're your contract with the client.")},
  {"type": "lab",
   "say": T("Construye la ruta batch. Intenta escribir el notebook tú solo; la solución está escondida por si la necesitas.", "Build the batch path. Try writing the notebook yourself; the solution is hidden in case you need it."),
   "title": T("Reto 1: notebook parametrizado con MERGE", "Challenge 1: parameterized notebook with MERGE"),
   "intro": T("Requisitos: un notebook que reciba el nombre del archivo como <b>parámetro</b>, aplique las reglas de calidad, cree <code>silver_rentas</code> la primera vez y haga <b>MERGE por <code>id_renta</code></b> las siguientes. Debe imprimir y devolver las cifras de control. <i>(Niveles 1, 3 y 4 del curso)</i>",
              "Requirements: a notebook that takes the file name as a <b>parameter</b>, applies the quality rules, creates <code>silver_rentas</code> the first time and does a <b>MERGE on <code>id_renta</code></b> afterwards. It must print and return the control totals. <i>(Course levels 1, 3 and 4)</i>"),
   "tasks": [
     {"t": T("Guarda este contenido como <code>rentas.csv</code> y súbelo a <b>Files</b> de <code>lh_bici</code>:", "Save this content as <code>rentas.csv</code> and upload it to <b>Files</b> in <code>lh_bici</code>:"), "code": RENTAS},
     {"t": T("Guarda este otro como <code>rentas_dia2.csv</code> y súbelo también (lo usarás en el paso 5):", "Save this one as <code>rentas_dia2.csv</code> and upload it too (you'll use it in step 5):"), "code": DIA2},
     {"t": T("Crea el notebook <code>nb_rentas_silver</code>, adjunta <code>lh_bici</code>, marca la primera celda como parámetros y escribe tu solución.", "Create the <code>nb_rentas_silver</code> notebook, attach <code>lh_bici</code>, mark the first cell as parameters and write your solution."), "solution": NB},
     {"t": T("Ejecútalo con <code>p_archivo = \"rentas.csv\"</code>. Compara contra tus cifras de control.", "Run it with <code>p_archivo = \"rentas.csv\"</code>. Compare against your control totals.")},
     {"t": T("Crea el pipeline <code>pl_bici_diario</code> con una actividad Notebook que llame a <code>nb_rentas_silver</code> con el parámetro base <code>p_archivo = rentas_dia2.csv</code>. Ejecútalo. <i>(Nivel 2)</i>", "Create the <code>pl_bici_diario</code> pipeline with a Notebook activity calling <code>nb_rentas_silver</code> with base parameter <code>p_archivo = rentas_dia2.csv</code>. Run it. <i>(Level 2)</i>")}],
   "expect": T("Primera ejecución: <b>Bronce 13 · Plata 10 · total 645.0</b>. Después del pipeline con el día 2 (el id 9 corrige su monto de 55 a 65 y llega el id 13 con 50): <b>Plata 11 · total 705.0</b>. Si vuelves a ejecutar el pipeline, los números no cambian: tu carga es <b>idempotente</b>.",
               "First run: <b>Bronze 13 · Silver 10 · total 645.0</b>. After the pipeline with day 2 (id 9 corrects its amount from 55 to 65 and id 13 arrives with 50): <b>Silver 11 · total 705.0</b>. Run the pipeline again and the numbers don't change: your load is <b>idempotent</b>.")},
  {"type": "quiz",
   "say": T("Comprueba que entiendes lo que acabas de construir.", "Check you understand what you just built."),
   "q": T("¿Por qué después del día 2 hay 11 filas y no 12, si el archivo traía 2 filas nuevas?", "Why are there 11 rows after day 2, not 12, if the file brought 2 rows?"),
   "opts": [
     opt(T("Porque el filtro de calidad eliminó una", "Because the quality filter removed one"), T("Las dos filas del día 2 pasan las reglas de calidad.", "Both day-2 rows pass the quality rules.")),
     opt(T("Porque el id 9 ya existía: MERGE lo <b>actualizó</b> y solo <b>insertó</b> el id 13", "Because id 9 already existed: MERGE <b>updated</b> it and only <b>inserted</b> id 13"), T("¡Exacto! 10 + 1 nueva = 11, y el total sube 10 (corrección) + 50 (nueva) = 705.", "Exactly! 10 + 1 new = 11, and the total rises by 10 (correction) + 50 (new) = 705."), True),
     opt(T("Porque Spark perdió una fila", "Because Spark lost a row"), T("Spark no pierde filas. 😉 Las cifras de control lo demuestran.", "Spark doesn't lose rows. 😉 The control totals prove it."))]}
 ]})

# ------------------------------------------------------------------ 8.3
L.append({
 "id": "l8-3", "icon": "🏛️", "min": 30,
 "badge": {"e": "⭐", "n": T("Constructor del Oro", "Gold Builder")},
 "title": T("Reto 2: Oro en el Warehouse", "Challenge 2: Gold in the Warehouse"),
 "steps": [
  {"type": "quiz",
   "say": T("Primero el diseño. Declara el grano.", "Design first. Declare the grain."),
   "q": T("¿Cuál es la granularidad correcta para <code>fact_rentas</code>?", "What's the right grain for <code>fact_rentas</code>?"),
   "opts": [
     opt(T("Una fila por barrio por día", "One row per neighbourhood per day"), T("Es un agregado: perderías el detalle por estación y método de pago.", "That's an aggregate: you'd lose detail by station and payment method.")),
     opt(T("Una fila por renta", "One row per rental"), T("¡Exacto! El grano más fino posible. Cualquier agregado se calcula después en el modelo.", "Exactly! The finest possible grain. Any aggregate gets computed later in the model."), True),
     opt(T("Una fila por estación", "One row per station"), T("Eso es una dimensión, no un hecho.", "That's a dimension, not a fact."))]},
  {"type": "lab",
   "say": T("Construye la estrella con T-SQL. Recuerda las diferencias de Fabric: BIGINT IDENTITY, VARCHAR y nombres de tres partes.", "Build the star with T-SQL. Remember Fabric's differences: BIGINT IDENTITY, VARCHAR and three-part names."),
   "title": T("Reto 2: estrella + procedimiento idempotente", "Challenge 2: star schema + idempotent procedure"),
   "intro": T("Requisitos: <code>dim_estacion</code> con llave sustituta y <code>fact_rentas</code> con grano de una fila por renta, cargadas por un procedimiento <code>usp_cargar_rentas</code> que use MERGE y lea <code>lh_bici.dbo.silver_rentas</code>. <i>(Nivel 4)</i>",
              "Requirements: <code>dim_estacion</code> with a surrogate key and <code>fact_rentas</code> at one row per rental, loaded by a <code>usp_cargar_rentas</code> procedure that uses MERGE and reads <code>lh_bici.dbo.silver_rentas</code>. <i>(Level 4)</i>"),
   "tasks": [
     {"t": T("En <code>wh_bici</code>, agrega <code>lh_bici</code> al Explorer para poder leerlo.", "In <code>wh_bici</code>, add <code>lh_bici</code> to the Explorer so you can read it.")},
     {"t": T("Crea las tablas y el procedimiento. Si usas un solo script, ejecuta primero los CREATE TABLE y después el CREATE PROCEDURE.", "Create the tables and the procedure. If you use one script, run the CREATE TABLE statements first, then the CREATE PROCEDURE."), "solution": WH_SOL},
     {"t": T("Ejecuta el procedimiento y valida:", "Run the procedure and validate:"), "code": WH_CHECK},
     {"t": T("Agrega al pipeline <code>pl_bici_diario</code> una actividad <b>Stored procedure</b> después del notebook (On success). Agrega también una rama <b>On failure</b> con un aviso por Teams o correo. <i>(Nivel 2)</i>", "Add a <b>Stored procedure</b> activity to <code>pl_bici_diario</code> after the notebook (On success). Also add an <b>On failure</b> branch with a Teams or email alert. <i>(Level 2)</i>")}],
   "expect": T("""<p><b>dim_estacion: 5 filas · fact_rentas: 11 filas · total 705.00</b>. Por barrio:</p>
     <table class="res"><tr><th>barrio</th><th>rentas</th><th>ingresos</th></tr><tr><td>Centro</td><td>4</td><td>235.00</td></tr><tr><td>Norte</td><td>3</td><td>220.00</td></tr><tr><td>Sur</td><td>2</td><td>160.00</td></tr><tr><td>Poniente</td><td>2</td><td>90.00</td></tr></table>
     <p>Igual que en Plata. El dato viajó entero de Bronce a Oro.</p>""",
     """<p><b>dim_estacion: 5 rows · fact_rentas: 11 rows · total 705.00</b>. By neighbourhood:</p>
     <table class="res"><tr><th>barrio</th><th>rentas</th><th>ingresos</th></tr><tr><td>Centro</td><td>4</td><td>235.00</td></tr><tr><td>Norte</td><td>3</td><td>220.00</td></tr><tr><td>Sur</td><td>2</td><td>160.00</td></tr><tr><td>Poniente</td><td>2</td><td>90.00</td></tr></table>
     <p>Same as Silver. The data traveled whole from Bronze to Gold.</p>""")},
  {"type": "quiz",
   "say": T("Pregunta de cifras de control.", "A control-totals question."),
   "q": T("Ingresos de <b>Sur</b> en Oro: 160.00. En el archivo original el id 9 decía 55.00. ¿Es un error?", "<b>Sur</b> revenue in Gold: 160.00. In the original file id 9 said 55.00. Is it an error?"),
   "opts": [
     opt(T("Sí: debería ser 150.00", "Yes: it should be 150.00"), T("Esa era la cifra del día 1. El día 2 llegó una corrección.", "That was the day-1 figure. A correction arrived on day 2.")),
     opt(T("No: 95.00 (id 4) + 65.00 (id 9 corregido el día 2) = 160.00", "No: 95.00 (id 4) + 65.00 (id 9 corrected on day 2) = 160.00"), T("¡Correcto! El MERGE propagó la corrección de Plata a Oro. Eso es una plataforma confiable.", "Correct! The MERGE carried the correction from Silver to Gold. That's a trustworthy platform."), True)]}
 ]})

# ------------------------------------------------------------------ 8.4
L.append({
 "id": "l8-4", "icon": "⚡", "min": 30,
 "badge": {"e": "📡", "n": T("Operador del tiempo real", "Real-Time Operator")},
 "title": T("Reto 3: la ruta en tiempo real", "Challenge 3: the real-time path"),
 "steps": [
  {"type": "concept",
   "say": T("Ahora la segunda petición del cliente: ver y actuar <b>en este momento</b>.", "Now the client's second request: see and act <b>right now</b>."),
   "kicker": T("Ruta rápida", "Fast path"),
   "title": T("Estaciones vacías, al instante", "Empty stations, instantly"),
   "body": T(
    """<p>Para el proyecto usaremos el dataset de ejemplo <b>Bicycles</b> de Eventstream como si fueran los sensores de las estaciones de BiciCiudad. En un proyecto real, las estaciones enviarían su estado a un Azure IoT Hub o a Event Hubs, y el resto de la arquitectura sería idéntico.</p>
    <p>La pregunta clave es: <b>¿cómo está cada estación ahora mismo?</b> Ya conoces el patrón: <code>arg_max(ingestion_time(), *) by BikepointID</code>.</p>""",
    """<p>For the project we'll use Eventstream's <b>Bicycles</b> sample dataset as if it were BiciCiudad's station sensors. In a real project, stations would send their status to an Azure IoT Hub or Event Hubs, and the rest of the architecture would be identical.</p>
    <p>The key question is: <b>how is each station right now?</b> You already know the pattern: <code>arg_max(ingestion_time(), *) by BikepointID</code>.</p>"""),
   "callouts": [{"k": "watch", "b": T("Al terminar el reto, <b>detén el Eventstream y las reglas de Activator</b>. Un flujo en vivo que nadie mira sigue consumiendo capacidad.", "When you finish the challenge, <b>stop the Eventstream and the Activator rules</b>. A live stream nobody watches keeps consuming capacity.")}]},
  {"type": "lab",
   "say": T("Arma la ruta rápida completa. Esta parte luce muchísimo en una demo. 😎", "Build the full fast path. This part looks amazing in a demo. 😎"),
   "title": T("Reto 3: stream, KQL, tablero y alerta", "Challenge 3: stream, KQL, dashboard and alert"),
   "intro": T("Requisitos: eventos de estaciones en <code>eh_bici</code>, una consulta del estado actual, un tablero que se refresque solo, una alerta a logística y los eventos disponibles en OneLake. <i>(Nivel 5)</i>",
              "Requirements: station events in <code>eh_bici</code>, a current-state query, a self-refreshing dashboard, an alert to logistics and the events available in OneLake. <i>(Level 5)</i>"),
   "tasks": [
     {"t": T("Crea el Eventstream <code>es_estaciones</code> con el ejemplo <b>Bicycles</b> y destino <code>eh_bici</code>, tabla <code>estado_estaciones</code>. Publícalo.", "Create the <code>es_estaciones</code> Eventstream with the <b>Bicycles</b> sample and destination <code>eh_bici</code>, table <code>estado_estaciones</code>. Publish it.")},
     {"t": T("Escribe en KQL: (a) las estaciones que <b>ahora</b> tienen 0 bicicletas y (b) cuántas estaciones vacías hay por barrio.", "Write in KQL: (a) the stations that <b>now</b> have 0 bikes and (b) how many empty stations there are per neighbourhood."), "solution": KQL_SOL},
     {"t": T("Crea el Real-Time Dashboard <code>rtd_biciudad</code> con dos tiles (eventos por minuto y estaciones vacías por barrio) y refresco automático cada 30 segundos.", "Create the <code>rtd_biciudad</code> Real-Time Dashboard with two tiles (events per minute and empty stations per neighbourhood) and auto-refresh every 30 seconds.")},
     {"t": T("En el tile de estaciones vacías, crea una alerta de Activator (<code>act_logistica</code>) que te envíe un correo cuando un barrio tenga más de un umbral que elijas.", "On the empty-stations tile, create an Activator alert (<code>act_logistica</code>) that emails you when a neighbourhood goes above a threshold you choose.")},
     {"t": T("Activa la <b>disponibilidad en OneLake</b> de la base KQL (o de la tabla <code>estado_estaciones</code>), para que los eventos también existan como Delta.", "Turn on <b>OneLake availability</b> for the KQL database (or the <code>estado_estaciones</code> table), so events also exist as Delta.")},
     {"t": T("Haz commit en Git: <code>feat: ruta en tiempo real</code>. Luego detén el Eventstream y la regla.", "Commit to Git: <code>feat: real-time path</code>. Then stop the Eventstream and the rule.")}],
   "expect": T("Un tablero vivo, un correo de Activator con el barrio que cruzó el umbral y la tabla de eventos disponible en OneLake. No hay cifras exactas que comparar porque los datos son en vivo. Lo que se valida es que <b>el ciclo evento → acción funciona</b>.",
               "A live dashboard, an Activator email naming the neighbourhood that crossed the threshold, and the events table available in OneLake. There are no exact figures to check because the data is live. What you validate is that <b>the event → action loop works</b>.")},
  {"type": "reveal", "kind": "brain",
   "say": T("Pregunta para tu presentación con el cliente.", "A question for your client presentation."),
   "prompt": T("La directora pregunta: “¿Por qué el reporte de ingresos y el tablero de estaciones están en lugares distintos? ¿No sería mejor todo junto?”. ¿Qué le respondes?",
               "The director asks: “Why are the revenue report and the stations dashboard in different places? Wouldn't it be better all together?” What do you answer?"),
   "answer": T("Porque responden preguntas a <b>velocidades distintas</b>. Los ingresos se consultan con datos validados y conciliados (ruta batch, cifras de control, una sola versión de la verdad). Las estaciones vacías necesitan segundos (ruta rápida). Ambos viven en la misma plataforma y en OneLake: si mañana quieren cruzar disponibilidad con ingresos, los eventos ya están como Delta y se pueden unir con el modelo batch. Es una arquitectura <b>Lambda</b>: dos velocidades, un solo lago.",
               "Because they answer questions at <b>different speeds</b>. Revenue is consulted with validated, reconciled data (batch path, control totals, single version of the truth). Empty stations need seconds (fast path). Both live on the same platform and in OneLake: if tomorrow they want to cross availability with revenue, the events are already Delta and can be joined with the batch model. It's a <b>Lambda</b> architecture: two speeds, one lake.")}
 ]})

# ------------------------------------------------------------------ 8.5
L.append({
 "id": "l8-5", "icon": "📊", "min": 30,
 "badge": {"e": "🎯", "n": T("Entregador de valor", "Value Deliverer")},
 "title": T("Reto 4: consumo, seguridad y entrega", "Challenge 4: consumption, security and delivery"),
 "steps": [
  {"type": "lab",
   "say": T("La recta final: el reporte que verá la directora. 🏁", "The home stretch: the report the director will see. 🏁"),
   "title": T("Reto 4: modelo semántico, DAX, RLS y gobierno", "Challenge 4: semantic model, DAX, RLS and governance"),
   "intro": T("Requisitos: un modelo Direct Lake sobre <code>wh_bici</code>, cinco medidas, un reporte, un rol por barrio, endoso y un commit final. <i>(Niveles 6 y 7)</i>",
              "Requirements: a Direct Lake model on <code>wh_bici</code>, five measures, a report, a role per neighbourhood, endorsement and a final commit. <i>(Levels 6 and 7)</i>"),
   "tasks": [
     {"t": T("Crea el modelo <code>sm_biciudad</code> con <code>fact_rentas</code> y <code>dim_estacion</code>. Relación 1 → * en una dirección. Oculta las llaves y <code>id_renta</code>.", "Create the <code>sm_biciudad</code> model with <code>fact_rentas</code> and <code>dim_estacion</code>. A single-direction 1 → * relationship. Hide the keys and <code>id_renta</code>.")},
     {"t": T("Crea las medidas: Ingresos, Rentas, Minutos Promedio, Ingreso por Minuto y % Ingresos.", "Create the measures: Ingresos, Rentas, Minutos Promedio, Ingreso por Minuto and % Ingresos."), "solution": DAX_SOL},
     {"t": T("Crea el reporte <code>rpt_biciudad</code>: tarjetas (Ingresos, Rentas, Minutos Promedio), tabla por barrio con % Ingresos y barras por método de pago.", "Create the <code>rpt_biciudad</code> report: cards (Ingresos, Rentas, Minutos Promedio), a table by neighbourhood with % Ingresos and bars by payment method.")},
     {"t": T("Crea el rol <code>Gerente Centro</code> con el filtro <code>[barrio] = \"Centro\"</code> en <code>dim_estacion</code> y pruébalo con <b>View as</b>.", "Create the <code>Gerente Centro</code> role with the filter <code>[barrio] = \"Centro\"</code> on <code>dim_estacion</code> and test it with <b>View as</b>.")},
     {"t": T("Marca <code>sm_biciudad</code> como <b>Promoted</b> con una descripción, revisa el linaje completo del workspace y haz commit: <code>feat: modelo y reporte BiciCiudad</code>.", "Mark <code>sm_biciudad</code> as <b>Promoted</b> with a description, review the workspace's full lineage and commit: <code>feat: BiciCiudad model and report</code>.")}],
   "expect": T("""<p>Tarjetas: <b>Ingresos 705.00 · Rentas 11 · Minutos Promedio 36.82</b> (405 minutos / 11). Ingreso por Minuto: <b>1.74</b>.</p>
     <table class="res"><tr><th>barrio</th><th>Ingresos</th><th>% Ingresos</th></tr><tr><td>Centro</td><td>235.00</td><td>33.33%</td></tr><tr><td>Norte</td><td>220.00</td><td>31.21%</td></tr><tr><td>Sur</td><td>160.00</td><td>22.70%</td></tr><tr><td>Poniente</td><td>90.00</td><td>12.77%</td></tr></table>
     <p>Por método de pago: app 390.00 · tarjeta 255.00 · efectivo 60.00. Con el rol <b>Gerente Centro</b>: Ingresos 235.00 y 4 rentas.</p>""",
     """<p>Cards: <b>Ingresos 705.00 · Rentas 11 · Minutos Promedio 36.82</b> (405 minutes / 11). Ingreso por Minuto: <b>1.74</b>.</p>
     <table class="res"><tr><th>barrio</th><th>Ingresos</th><th>% Ingresos</th></tr><tr><td>Centro</td><td>235.00</td><td>33.33%</td></tr><tr><td>Norte</td><td>220.00</td><td>31.21%</td></tr><tr><td>Sur</td><td>160.00</td><td>22.70%</td></tr><tr><td>Poniente</td><td>90.00</td><td>12.77%</td></tr></table>
     <p>By payment method: app 390.00 · tarjeta 255.00 · efectivo 60.00. With the <b>Gerente Centro</b> role: Ingresos 235.00 and 4 rentals.</p>""")},
  {"type": "reveal", "kind": "pencil",
   "say": T("Último ejercicio práctico: preséntalo como en la vida real.", "Last hands-on exercise: present it like in real life."),
   "prompt": T("Escribe en 4 o 5 líneas el resumen que le enviarías a la directora de BiciCiudad para entregar el proyecto.", "Write, in 4 or 5 lines, the summary you'd send the BiciCiudad director to deliver the project."),
   "answer": T("Un ejemplo: “Entregamos la plataforma de datos de BiciCiudad en Fabric. (1) Ingresos: un solo modelo certificable con 11 rentas validadas y $705.00, conciliados contra el origen con cifras de control; cada gerente ve solo su barrio. (2) Estaciones: tablero en vivo y alertas automáticas a logística cuando un barrio se queda sin bicicletas. (3) Todo está versionado en Git y la carga diaria es automática e idempotente. Siguiente paso propuesto: promover a producción con un deployment pipeline.” Fíjate: habla de <b>valor y confianza</b>, no de tecnología.",
               "An example: “We delivered BiciCiudad's data platform on Fabric. (1) Revenue: a single certifiable model with 11 validated rentals and $705.00, reconciled to source with control totals; each manager sees only their neighbourhood. (2) Stations: a live dashboard and automatic alerts to logistics when a neighbourhood runs out of bikes. (3) Everything is versioned in Git and the daily load is automated and idempotent. Proposed next step: promote to production with a deployment pipeline.” Notice: it talks about <b>value and trust</b>, not technology.")}
 ]})

# ------------------------------------------------------------------ 8.6 · Examen final
L.append({
 "id": "l8-6", "icon": "🎓", "min": 20,
 "badge": {"e": "🎓", "n": T("Alquimista de datos certificado", "Certified Data Alchemist")},
 "title": T("Examen final", "Final exam"),
 "steps": [
  {"type": "story",
   "say": T("Diez preguntas, una por cada gran idea del curso. Respira. Ya sabes todo esto. 🧘", "Ten questions, one for each big idea in the course. Breathe. You already know all of this. 🧘"),
   "kicker": T("La última prueba", "The final test"),
   "title": T("Antes del certificado", "Before the certificate"),
   "body": T("<p>Este examen repasa todo el programa, del Nivel 1 al 7. No hay tiempo límite y puedes volver a intentar cada pregunta, pero obtienes más XP si aciertas a la primera. Al terminar, se desbloquea tu <b>certificado de finalización</b>.</p>",
             "<p>This exam reviews the whole program, from Level 1 to 7. There's no time limit and you can retry each question, but you get more XP for getting it right on the first try. When you finish, your <b>certificate of completion</b> unlocks.</p>")},
  {"type": "quiz", "q": T("<b>Nivel 1</b> · ¿En qué formato guarda OneLake las tablas que leen Spark, SQL y Power BI?", "<b>Level 1</b> · In which format does OneLake store the tables read by Spark, SQL and Power BI?"),
   "opts": [opt("CSV", T("CSV se usa en Files, no para las tablas.", "CSV is for Files, not tables.")), opt("Delta Parquet", T("Correcto: un formato abierto, una sola copia para todos los motores.", "Correct: an open format, one copy for every engine."), True), opt("JSON", T("JSON es para datos semiestructurados en Files.", "JSON is for semi-structured data in Files."))]},
  {"type": "quiz", "q": T("<b>Nivel 1</b> · ¿Qué capa Medallion debe conservar el dato tal como llegó de la fuente?", "<b>Level 1</b> · Which Medallion layer must keep the data exactly as it arrived?"),
   "opts": [opt(T("Bronce", "Bronze"), T("Correcto: es tu seguro para reprocesar y auditar.", "Correct: it's your insurance to reprocess and audit."), True), opt(T("Plata", "Silver"), T("Plata limpia y deduplica.", "Silver cleans and deduplicates.")), opt(T("Oro", "Gold"), T("Oro modela para el negocio.", "Gold models for the business."))]},
  {"type": "quiz", "q": T("<b>Nivel 2</b> · Quieres consultar 3 TB que están en Amazon S3 sin copiarlos. ¿Qué usas?", "<b>Level 2</b> · You want to query 3 TB in Amazon S3 without copying them. What do you use?"),
   "opts": [opt("Copy job", T("Copiaría los 3 TB.", "It would copy the 3 TB.")), opt("Shortcut", T("Correcto: los datos se quedan donde están.", "Correct: the data stays where it is."), True), opt("Mirroring", T("Mirroring replica bases de datos.", "Mirroring replicates databases."))]},
  {"type": "quiz", "q": T("<b>Nivel 2</b> · ¿Qué limitación tiene una carga incremental basada solo en watermark?", "<b>Level 2</b> · What's the limitation of a watermark-only incremental load?"),
   "opts": [opt(T("No detecta filas borradas en la fuente", "It doesn't detect rows deleted at the source"), T("Correcto: para eso necesitas CDC, borrado lógico o una conciliación periódica.", "Correct: for that you need CDC, soft deletes or periodic reconciliation."), True), opt(T("No funciona con fechas", "It doesn't work with dates"), T("Las fechas son el watermark más común.", "Dates are the most common watermark.")), opt(T("Siempre copia todo", "It always copies everything"), T("Eso sería una carga completa.", "That would be a full load."))]},
  {"type": "quiz", "q": T("<b>Nivel 3</b> · ¿Cuál de estas operaciones obliga a Spark a ejecutar el plan?", "<b>Level 3</b> · Which of these operations forces Spark to run the plan?"),
   "opts": [opt("filter", T("Es una transformación perezosa.", "It's a lazy transformation.")), opt("withColumn", T("También es perezosa.", "Also lazy.")), opt("count", T("Correcto: es una acción.", "Correct: it's an action."), True)]},
  {"type": "quiz", "q": T("<b>Nivel 3</b> · Ejecutas la misma carga dos veces y quieres que la tabla quede igual. ¿Qué usas en Plata?", "<b>Level 3</b> · You run the same load twice and want the table unchanged. What do you use in Silver?"),
   "opts": [opt(T("Append", "Append"), T("Duplicaría filas.", "It would duplicate rows.")), opt(T("MERGE por clave", "MERGE on a key"), T("Correcto: upsert idempotente.", "Correct: an idempotent upsert."), True), opt(T("VACUUM", "VACUUM"), T("VACUUM limpia archivos viejos; no carga datos.", "VACUUM cleans old files; it doesn't load data."))]},
  {"type": "quiz", "q": T("<b>Nivel 4</b> · En el Warehouse de Fabric, ¿qué tipo de dato admite IDENTITY?", "<b>Level 4</b> · In the Fabric Warehouse, which data type supports IDENTITY?"),
   "opts": [opt("INT", T("En Fabric, IDENTITY solo admite BIGINT.", "In Fabric, IDENTITY only supports BIGINT.")), opt("BIGINT", T("Correcto, y sus valores son únicos pero no consecutivos.", "Correct, and its values are unique but not consecutive."), True), opt("NVARCHAR", T("Ni siquiera existe nvarchar en el Warehouse de Fabric.", "nvarchar doesn't even exist in the Fabric Warehouse."))]},
  {"type": "quiz", "q": T("<b>Nivel 5</b> · ¿Qué patrón KQL devuelve el estado más reciente de cada máquina?", "<b>Level 5</b> · Which KQL pattern returns each machine's latest state?"),
   "opts": [opt("take 1", T("Devuelve una fila cualquiera.", "It returns one arbitrary row.")), opt("summarize arg_max(ingestion_time(), *) by id", T("Correcto: la fila más reciente por objeto.", "Correct: the most recent row per object."), True), opt("summarize sum(valor) by id", T("Sumaría todas las lecturas históricas.", "It would add up every historical reading."))]},
  {"type": "quiz", "q": T("<b>Nivel 6</b> · Un reporte en Direct Lake sobre SQL va lento porque el modelo usa una vista SQL. ¿Qué pasa?", "<b>Level 6</b> · A Direct Lake on SQL report is slow because the model uses a SQL view. What's happening?"),
   "opts": [opt(T("Fallback a DirectQuery", "DirectQuery fallback"), T("Correcto: materializa la vista como tabla en Oro.", "Correct: materialize the view as a Gold table."), True), opt(T("Se está importando todo", "Everything is being imported"), T("Direct Lake no importa datos.", "Direct Lake doesn't import data.")), opt(T("Falta V-Order en Bronce", "Bronze is missing V-Order"), T("Bronce no lo lee el reporte.", "The report doesn't read Bronze."))]},
  {"type": "quiz", "q": T("<b>Nivel 7</b> · ¿Qué viaja a Git y en un deployment pipeline?", "<b>Level 7</b> · What travels to Git and through a deployment pipeline?"),
   "opts": [opt(T("Las definiciones de los elementos, no los datos", "Item definitions, not data"), T("Correcto: cada ambiente tiene sus propios datos.", "Correct: each environment has its own data."), True), opt(T("Los datos de las tablas", "Table data"), T("Los datos se quedan en OneLake.", "Data stays in OneLake.")), opt(T("Solo los reportes", "Only reports"), T("Viajan muchos tipos de elementos.", "Many item types travel."))]},
  {"type": "story",
   "say": T("🎉 ¡Terminaste el examen! Pulsa <b>Terminar lección</b> y reclama tu certificado. Estoy muy orgulloso de ti, colega.", "🎉 You finished the exam! Click <b>Finish lesson</b> and claim your certificate. I'm very proud of you, colleague."),
   "kicker": T("¡Lo lograste!", "You did it!"),
   "title": T("De un CSV con errores a una plataforma completa", "From a messy CSV to a complete platform"),
   "body": T("<p>Empezaste sin saber qué era OneLake. Hoy sabes ingerir, limpiar, modelar, servir, vigilar en tiempo real, asegurar y versionar una plataforma de datos completa, y demostrar con cifras de control que el dato es confiable de principio a fin.</p><p>Al terminar esta lección se desbloquea tu certificado. Si te faltó alguna lección, la página del certificado te dirá cuál.</p>",
             "<p>You started without knowing what OneLake was. Today you can ingest, clean, model, serve, monitor in real time, secure and version a complete data platform, and prove with control totals that the data is trustworthy end to end.</p><p>When you finish this lesson, your certificate unlocks. If you missed a lesson, the certificate page will tell you which one.</p>")}
 ]})

out = {"id": 8,
       "title": T("Proyecto final integrador", "Capstone project"),
       "desc": T("BiciCiudad: una plataforma completa con ruta batch, Oro en Warehouse, tiempo real, modelo semántico, seguridad y Git. Examen final y certificado.", "BiciCiudad: a complete platform with a batch path, Gold in a Warehouse, real time, a semantic model, security and Git. Final exam and certificate."),
       "lessons": L}
dst = pathlib.Path(__file__).resolve().parent.parent / "content/level-8.json"
dst.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", dst, sum(len(l["steps"]) for l in L), "steps")
