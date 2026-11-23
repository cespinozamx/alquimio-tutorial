"""Genera content/level-4.json — Nivel 4: Data Warehouse y T-SQL."""
import json, pathlib

def T(es, en): return {"es": es, "en": en}
def opt(t, why, ok=False):
    o = {"t": t, "why": why}
    if ok: o["ok"] = 1
    return o

L = []

# ------------------------------------------------------------------ 4.1
L.append({
 "id": "l4-1", "icon": "🏛️", "min": 15,
 "badge": {"e": "⚖️", "n": T("Juez Lakehouse vs Warehouse", "Lakehouse vs Warehouse Judge")},
 "title": T("Warehouse vs Lakehouse: ¿cuándo cuál?", "Warehouse vs Lakehouse: which one when?"),
 "steps": [
  {"type": "story",
   "say": T("Nivel 4. Bienvenido al mundo de T-SQL. Si vienes de SQL Server, aquí te sentirás en casa. 🏠", "Level 4. Welcome to the world of T-SQL. If you come from SQL Server, you'll feel right at home. 🏠"),
   "kicker": T("El taller y la biblioteca", "The workshop and the library"),
   "title": T("Dos edificios sobre el mismo terreno", "Two buildings on the same land"),
   "body": T(
    """<p>Imagina un <b>taller</b> enorme donde cabe de todo: piezas sueltas, cajas, planos, prototipos. Trabajas con herramientas eléctricas (Spark) y construyes lo que quieras. Ese es el <b>Lakehouse</b>.</p>
    <p>Al lado hay una <b>biblioteca</b>: todo está catalogado en estantes con reglas claras, y cualquiera que sepa pedir un libro (T-SQL) lo encuentra, lo presta o lo actualiza. Ese es el <b>Warehouse</b>.</p>
    <p>La sorpresa: <span class="hl">los dos están construidos sobre el mismo terreno</span>. Ambos guardan sus tablas en <b>OneLake</b>, en formato <b>Delta</b>, y Power BI puede leer cualquiera de los dos.</p>""",
    """<p>Picture a huge <b>workshop</b> where everything fits: loose parts, boxes, blueprints, prototypes. You work with power tools (Spark) and build whatever you want. That's the <b>Lakehouse</b>.</p>
    <p>Next door is a <b>library</b>: everything is catalogued on shelves with clear rules, and anyone who knows how to ask for a book (T-SQL) can find it, borrow it or update it. That's the <b>Warehouse</b>.</p>
    <p>The surprise: <span class="hl">both are built on the same land</span>. Both keep their tables in <b>OneLake</b>, in <b>Delta</b> format, and Power BI can read either one.</p>"""),
   "visual": "whVsLh"},
  {"type": "concept",
   "say": T("La diferencia clave está en <b>cómo escribes</b> los datos.", "The key difference is <b>how you write</b> data."),
   "title": T("Lo que cambia y lo que no", "What changes and what doesn't"),
   "body": T("", ""),
   "cards": [
     {"e": "🏭", "n": "Lakehouse", "d": T("Archivos (Files) + tablas Delta. Escribes con Spark, Dataflows o pipelines. Su SQL analytics endpoint es de solo lectura.", "Files + Delta tables. You write with Spark, Dataflows or pipelines. Its SQL analytics endpoint is read-only.")},
     {"e": "🏛️", "n": "Warehouse", "d": T("Solo tablas. Escribes con T-SQL completo: INSERT, UPDATE, DELETE, MERGE, procedimientos almacenados y transacciones entre varias tablas.", "Tables only. You write with full T-SQL: INSERT, UPDATE, DELETE, MERGE, stored procedures and multi-table transactions."), "star": True},
     {"e": "🌊", "n": T("En común", "In common"), "d": T("OneLake, formato Delta, seguridad de Fabric, Direct Lake para Power BI y la misma capacidad.", "OneLake, Delta format, Fabric security, Direct Lake for Power BI and the same capacity.")}],
   "callouts": [{"k": "key", "b": T("Crear, modificar o borrar tablas y hacer INSERT, UPDATE o DELETE solo funciona en el <b>Warehouse</b>, no en el SQL analytics endpoint del Lakehouse.",
                                     "Creating, altering or dropping tables and running INSERT, UPDATE or DELETE only works in the <b>Warehouse</b>, not in the Lakehouse's SQL analytics endpoint.")}]},
  {"type": "match",
   "say": T("Une cada necesidad con el elemento que mejor la resuelve.", "Pair each need with the item that solves it best."),
   "title": T("¿Taller o biblioteca?", "Workshop or library?"),
   "pairs": [
     [T("Guardar imágenes, JSON y CSV crudos", "Store raw images, JSON and CSV"), T("🏭 Lakehouse (Files)", "🏭 Lakehouse (Files)")],
     [T("Un equipo de SQL con procedimientos almacenados", "A SQL team with stored procedures"), T("🏛️ Warehouse", "🏛️ Warehouse")],
     [T("Transformar 5 TB con PySpark", "Transform 5 TB with PySpark"), T("📓 Notebook sobre Lakehouse", "📓 Notebook on a Lakehouse")],
     [T("Actualizar varias tablas en una sola transacción", "Update several tables in a single transaction"), T("🔒 Transacción en el Warehouse", "🔒 Warehouse transaction")]]},
  {"type": "quiz",
   "say": T("Escenario de migración, muy común en LATAM.", "A migration scenario, very common in LATAM."),
   "q": T("Un banco migra su data warehouse de SQL Server: 300 procedimientos almacenados en T-SQL y un equipo que no programa en Python. ¿Qué destino recomiendas en Fabric?",
          "A bank is migrating its SQL Server data warehouse: 300 T-SQL stored procedures and a team that doesn't code in Python. Which Fabric destination do you recommend?"),
   "opts": [
     opt(T("Lakehouse y reescribir todo en PySpark", "Lakehouse and rewrite everything in PySpark"), T("Posible, pero tirarías años de conocimiento del equipo y alargarías mucho la migración.", "Possible, but you'd throw away years of team knowledge and stretch the migration a lot.")),
     opt(T("Warehouse: conserva T-SQL y procedimientos, con ajustes", "Warehouse: keeps T-SQL and procedures, with adjustments"), T("¡Exacto! El Warehouse habla T-SQL. Habrá que ajustar tipos de datos y algunas funciones, pero el conocimiento del equipo se aprovecha.", "Exactly! The Warehouse speaks T-SQL. You'll adjust data types and some features, but the team's knowledge carries over."), True),
     opt(T("Dejarlo en SQL Server y conectarlo con un shortcut", "Leave it in SQL Server and connect it with a shortcut"), T("Los shortcuts no apuntan a SQL Server. Para replicarlo existe Mirroring, pero eso no migra la lógica.", "Shortcuts don't point to SQL Server. Mirroring could replicate it, but that doesn't migrate the logic."))]},
  {"type": "reveal", "kind": "brain",
   "say": T("La respuesta de arquitecto casi nunca es “uno u otro”.", "The architect's answer is rarely “one or the other”."),
   "prompt": T("¿Pueden convivir Lakehouse y Warehouse en la misma solución? ¿Cómo los repartirías en una arquitectura Medallion?",
               "Can a Lakehouse and a Warehouse coexist in the same solution? How would you split them in a Medallion architecture?"),
   "answer": T("¡Sí, y es muy común! Un patrón típico: <b>Bronce y Plata en Lakehouse</b> (Spark maneja bien archivos crudos y grandes volúmenes) y <b>Oro en Warehouse</b> (modelo estrella cargado con T-SQL y procedimientos). El Warehouse lee las tablas del Lakehouse con <b>consultas entre bases de datos</b> usando nombres de tres partes, como <code>lh_tutor.dbo.silver_ventas_m</code>, sin copiar archivos. Lo harás en la lección 4.3.",
               "Yes, and it's very common! A typical pattern: <b>Bronze and Silver in a Lakehouse</b> (Spark handles raw files and large volumes well) and <b>Gold in a Warehouse</b> (a star schema loaded with T-SQL and procedures). The Warehouse reads Lakehouse tables with <b>cross-database queries</b> using three-part names, like <code>lh_tutor.dbo.silver_ventas_m</code>, without copying files. You'll do it in lesson 4.3.")}
 ]})

# ------------------------------------------------------------------ 4.2
L.append({
 "id": "l4-2", "icon": "⭐", "min": 18,
 "badge": {"e": "🌟", "n": T("Arquitecto de estrellas", "Star Architect")},
 "title": T("Modelado dimensional: el esquema estrella", "Dimensional modeling: the star schema"),
 "steps": [
  {"type": "story",
   "say": T("Toma un ticket de supermercado. Ahí está todo el modelado dimensional. 🧾", "Grab a supermarket receipt. All of dimensional modeling is right there. 🧾"),
   "kicker": T("El ticket del súper", "The supermarket receipt"),
   "title": T("Hechos en el centro, contexto alrededor", "Facts in the middle, context around them"),
   "body": T(
    """<p>Cada línea de un ticket es un <b>hecho</b>: algo que pasó y que se puede medir (cantidad, importe). Pero un número solo no dice nada. Para entenderlo necesitas el contexto: <b>quién</b> compró, <b>qué</b> producto, <b>cuándo</b> y <b>dónde</b>. Cada pieza de contexto es una <b>dimensión</b>.</p>
    <p>Si dibujas la tabla de hechos en el centro y las dimensiones alrededor, te queda una <b>estrella</b>. Es el modelo favorito de Power BI y de los motores analíticos porque las consultas son simples y rápidas: unes la tabla de hechos con sus dimensiones, filtras y agregas.</p>""",
    """<p>Every line on a receipt is a <b>fact</b>: something that happened and can be measured (quantity, amount). But a number alone says nothing. To understand it you need context: <b>who</b> bought, <b>which</b> product, <b>when</b> and <b>where</b>. Each piece of context is a <b>dimension</b>.</p>
    <p>Draw the fact table in the middle with the dimensions around it and you get a <b>star</b>. It's the favorite model of Power BI and analytical engines because queries are simple and fast: join the facts to their dimensions, filter and aggregate.</p>"""),
   "visual": "starSchema"},
  {"type": "concept",
   "say": T("Cuatro conceptos que vas a usar toda tu carrera.", "Four concepts you'll use for your whole career."),
   "title": T("El vocabulario del modelador", "The modeler's vocabulary"),
   "body": T(
    """<ul><li><b>Granularidad (grano)</b>: qué representa <i>una fila</i> de la tabla de hechos. Por ejemplo, “una línea de venta”. Es la decisión más importante del diseño.</li>
    <li><b>Medidas</b>: los números de los hechos que se suman o promedian (<code>monto</code>, <code>cantidad</code>).</li>
    <li><b>Llave sustituta</b> (<i>surrogate key</i>): un número interno del warehouse, como <code>sk_cliente</code>, distinto del ID que trae el sistema origen (la <b>llave de negocio</b>). Te protege si el origen cambia o si mezclas varios sistemas.</li>
    <li><b>Dimensión de fecha</b>: una fila por día con año, mes, trimestre, día de la semana… Así el reporte no tiene que calcularlos.</li></ul>""",
    """<ul><li><b>Grain</b>: what <i>one row</i> of the fact table represents. For example, “one sales line”. It's the most important design decision.</li>
    <li><b>Measures</b>: the fact numbers you sum or average (<code>monto</code>, <code>quantity</code>).</li>
    <li><b>Surrogate key</b>: an internal warehouse number, like <code>sk_cliente</code>, separate from the source system's ID (the <b>business key</b>). It protects you if the source changes or when you mix several systems.</li>
    <li><b>Date dimension</b>: one row per day with year, month, quarter, weekday… so the report doesn't have to compute them.</li></ul>"""),
   "callouts": [{"k": "watch", "b": T("Si mezclas granos en una misma tabla de hechos (por ejemplo, líneas de venta y totales mensuales), las sumas se duplican sin que nadie lo note. <b>Un grano por tabla de hechos.</b>",
                                       "If you mix grains in the same fact table (say, sales lines and monthly totals), sums get doubled without anyone noticing. <b>One grain per fact table.</b>")}]},
  {"type": "order",
   "say": T("Estos son los cuatro pasos clásicos de Ralph Kimball. Ordénalos.", "These are Ralph Kimball's four classic steps. Put them in order."),
   "title": T("Los 4 pasos del diseño dimensional", "The 4 steps of dimensional design"),
   "items": [T("Elegir el proceso de negocio (por ejemplo, ventas)", "Choose the business process (e.g. sales)"),
             T("Declarar la granularidad (una fila = una línea de venta)", "Declare the grain (one row = one sales line)"),
             T("Identificar las dimensiones (cliente, producto, fecha)", "Identify the dimensions (customer, product, date)"),
             T("Identificar los hechos o medidas (monto, cantidad)", "Identify the facts or measures (amount, quantity)")]},
  {"type": "match",
   "say": T("Clasifica cada columna de nuestro modelo de ventas.", "Classify each column in our sales model."),
   "title": T("¿Qué papel juega cada columna?", "What role does each column play?"),
   "pairs": [
     [T("<code>monto</code> en fact_ventas", "<code>monto</code> in fact_ventas"), T("Medida", "Measure")],
     [T("<code>sk_cliente</code> en fact_ventas", "<code>sk_cliente</code> in fact_ventas"), T("Llave foránea hacia una dimensión", "Foreign key to a dimension")],
     [T("<code>region</code> en dim_cliente", "<code>region</code> in dim_cliente"), T("Atributo descriptivo", "Descriptive attribute")],
     [T("El ID del cliente en el ERP", "The customer ID in the ERP"), T("Llave de negocio", "Business key")]]},
  {"type": "quiz",
   "say": T("Pregunta de granularidad. Piensa qué representa una fila.", "Grain question. Think about what one row represents."),
   "q": T("En <code>fact_ventas</code> cada fila es una venta individual. Alguien quiere agregar ahí la <b>meta mensual</b> de cada región. ¿Qué haces?",
          "In <code>fact_ventas</code> each row is one individual sale. Someone wants to add each region's <b>monthly target</b> there. What do you do?"),
   "opts": [
     opt(T("Agregar una columna <code>meta_mensual</code> a cada venta", "Add a <code>meta_mensual</code> column to each sale"), T("La meta se repetiría en cada venta del mes y al sumarla se multiplicaría. Grano mezclado.", "The target would repeat on every sale of the month and be multiplied when summed. Mixed grain.")),
     opt(T("Crear otra tabla de hechos <code>fact_metas</code> con grano región-mes", "Create another fact table <code>fact_metas</code> with a region-month grain"), T("¡Exacto! Cada tabla de hechos tiene su propio grano. Las dos comparten dimensiones (región, fecha) y Power BI las compara sin problema.", "Exactly! Each fact table has its own grain. Both share dimensions (region, date) and Power BI compares them easily."), True)]},
  {"type": "reveal", "kind": "pencil",
   "say": T("Escríbelo como se lo explicarías a un cliente.", "Write it the way you'd explain it to a client."),
   "prompt": T("¿Por qué no hacer una sola tabla gigante con todas las columnas (cliente, producto, fecha, monto) en lugar de una estrella?",
               "Why not build one giant table with every column (customer, product, date, amount) instead of a star?"),
   "answer": T("Una tabla ancha repite el texto de cliente y producto en cada fila: ocupa más y, si un cliente cambia de región, tienes que actualizar millones de filas. La estrella guarda cada atributo <b>una sola vez</b> en su dimensión, mantiene la tabla de hechos delgada (solo llaves y números) y es la forma que Power BI optimiza mejor: filtros simples, relaciones claras y medidas DAX más fáciles.",
               "A wide table repeats customer and product text on every row: it takes more space and, if a customer changes region, you have to update millions of rows. The star stores each attribute <b>just once</b> in its dimension, keeps the fact table slim (keys and numbers only) and is the shape Power BI optimizes best: simple filters, clear relationships and easier DAX measures.")}
 ]})

# ------------------------------------------------------------------ 4.3
DIMS = """-- Dimensión cliente: llave sustituta IDENTITY (siempre BIGINT en Fabric)
CREATE TABLE dbo.dim_cliente (
    sk_cliente BIGINT IDENTITY,
    cliente    VARCHAR(100) NOT NULL,
    region     VARCHAR(30)  NOT NULL
);
INSERT INTO dbo.dim_cliente (cliente, region)
SELECT DISTINCT cliente, region
FROM lh_tutor.dbo.silver_ventas_m;

-- Dimensión producto
CREATE TABLE dbo.dim_producto (
    sk_producto BIGINT IDENTITY,
    producto    VARCHAR(100) NOT NULL
);
INSERT INTO dbo.dim_producto (producto)
SELECT DISTINCT producto
FROM lh_tutor.dbo.silver_ventas_m;

-- Dimensión fecha con CTAS (CREATE TABLE AS SELECT)
CREATE TABLE dbo.dim_fecha AS
SELECT DISTINCT
       YEAR(fecha) * 10000 + MONTH(fecha) * 100 + DAY(fecha) AS sk_fecha,
       fecha,
       YEAR(fecha)  AS anio,
       MONTH(fecha) AS mes,
       DAY(fecha)   AS dia
FROM lh_tutor.dbo.silver_ventas_m;"""

FACT = """CREATE TABLE dbo.fact_ventas (
    id_venta    INT,
    sk_fecha    INT,
    sk_cliente  BIGINT,
    sk_producto BIGINT,
    monto       DECIMAL(12, 2)
);

INSERT INTO dbo.fact_ventas
SELECT v.id,
       YEAR(v.fecha) * 10000 + MONTH(v.fecha) * 100 + DAY(v.fecha),
       c.sk_cliente,
       p.sk_producto,
       CAST(v.monto AS DECIMAL(12, 2))
FROM lh_tutor.dbo.silver_ventas_m AS v
JOIN dbo.dim_cliente  AS c ON c.cliente = v.cliente AND c.region = v.region
JOIN dbo.dim_producto AS p ON p.producto = v.producto;"""

CHECK = """SELECT 'dim_cliente' AS tabla, COUNT(*) AS filas FROM dbo.dim_cliente
UNION ALL SELECT 'dim_producto', COUNT(*) FROM dbo.dim_producto
UNION ALL SELECT 'dim_fecha',    COUNT(*) FROM dbo.dim_fecha
UNION ALL SELECT 'fact_ventas',  COUNT(*) FROM dbo.fact_ventas;

SELECT c.region, COUNT(*) AS ventas, SUM(f.monto) AS total
FROM dbo.fact_ventas f
JOIN dbo.dim_cliente c ON c.sk_cliente = f.sk_cliente
GROUP BY c.region
ORDER BY total DESC;"""

L.append({
 "id": "l4-3", "icon": "🛠️", "min": 30,
 "badge": {"e": "🏗️", "n": T("Constructor de Warehouses", "Warehouse Builder")},
 "title": T("T-SQL en el Warehouse: construye tu estrella", "T-SQL in the Warehouse: build your star"),
 "steps": [
  {"type": "concept",
   "say": T("Antes del laboratorio, las <b>diferencias</b> con SQL Server. Te ahorrarán horas de errores.", "Before the lab, the <b>differences</b> from SQL Server. They'll save you hours of errors."),
   "kicker": T("T-SQL con acento Fabric", "T-SQL with a Fabric accent"),
   "title": T("Lo que cambia respecto a SQL Server", "What's different from SQL Server"),
   "body": T(
    """<ul><li><b>Tipos de datos</b>: no hay <code>nvarchar</code>; usa <code>varchar</code>, que en Fabric guarda texto en UTF-8. Tampoco hay <code>datetime</code>: usa <code>datetime2</code>.</li>
    <li><b>IDENTITY</b>: solo con <code>BIGINT</code>. No defines valor inicial ni incremento, los valores son únicos pero <span class="hl">no consecutivos</span> (puede haber huecos) y no existe <code>IDENTITY_INSERT</code>.</li>
    <li><b>Llaves primarias y foráneas</b>: se declaran como <code>NOT ENFORCED</code>. Sirven como documentación y para el optimizador, pero <b>no impiden duplicados</b>.</li>
    <li><b>Consultas entre bases de datos</b>: lees tablas de un Lakehouse o de otro Warehouse del workspace con nombres de tres partes: <code>lh_tutor.dbo.silver_ventas_m</code>.</li>
    <li>Sí tienes <b>CTAS</b> (<code>CREATE TABLE … AS SELECT</code>), tablas temporales <code>#temp</code>, <code>TRUNCATE</code>, vistas, funciones y procedimientos.</li></ul>""",
    """<ul><li><b>Data types</b>: there's no <code>nvarchar</code>; use <code>varchar</code>, which in Fabric stores text as UTF-8. No <code>datetime</code> either: use <code>datetime2</code>.</li>
    <li><b>IDENTITY</b>: <code>BIGINT</code> only. You can't set the seed or increment, values are unique but <span class="hl">not consecutive</span> (there can be gaps) and there's no <code>IDENTITY_INSERT</code>.</li>
    <li><b>Primary and foreign keys</b>: declared as <code>NOT ENFORCED</code>. They document the model and help the optimizer, but <b>don't prevent duplicates</b>.</li>
    <li><b>Cross-database queries</b>: you read tables from a Lakehouse or another Warehouse in the workspace with three-part names: <code>lh_tutor.dbo.silver_ventas_m</code>.</li>
    <li>You do get <b>CTAS</b> (<code>CREATE TABLE … AS SELECT</code>), <code>#temp</code> tables, <code>TRUNCATE</code>, views, functions and procedures.</li></ul>""")},
  {"type": "fill",
   "say": T("Completa las tres piezas que más se olvidan.", "Fill in the three pieces people forget most."),
   "title": T("T-SQL estilo Fabric", "Fabric-style T-SQL"),
   "code": "CREATE TABLE dbo.dim_cliente (\n    sk_cliente BIGINT {{0}},\n    cliente    VARCHAR(100) NOT NULL\n);\n\nALTER TABLE dbo.dim_cliente\n  ADD CONSTRAINT pk_dim_cliente\n  PRIMARY KEY NONCLUSTERED (sk_cliente) NOT {{1}};\n\nSELECT * FROM lh_tutor.{{2}}.silver_ventas_m;",
   "blanks": [
     {"a": ["identity"], "hint": T("La propiedad que genera números automáticos.", "The property that auto-generates numbers.")},
     {"a": ["enforced"], "hint": T("NOT ______: la llave se declara pero no se valida.", "NOT ______: the key is declared but not validated.")},
     {"a": ["dbo"], "hint": T("El esquema por defecto de las tablas.", "The default schema for tables.")}]},
  {"type": "lab",
   "say": T("Vas a construir un <b>modelo estrella completo</b> con T-SQL, leyendo directo del Lakehouse. 🌟", "You'll build a <b>complete star schema</b> with T-SQL, reading straight from the Lakehouse. 🌟"),
   "title": T("Laboratorio: tu primer modelo estrella en el Warehouse", "Lab: your first star schema in the Warehouse"),
   "intro": T("Usaremos <code>silver_ventas_m</code> (11 filas, lección 3.3) como fuente. <i>Los nombres de los botones pueden variar un poco según tu versión de Fabric.</i>",
              "We'll use <code>silver_ventas_m</code> (11 rows, lesson 3.3) as the source. <i>Button names may vary slightly with your Fabric version.</i>"),
   "tasks": [
     {"t": T("En <code>ws_tutor_fabric</code>: <b>+ New item → Warehouse</b>. Nómbralo <code>wh_ventas</code>.", "In <code>ws_tutor_fabric</code>: <b>+ New item → Warehouse</b>. Name it <code>wh_ventas</code>.")},
     {"t": T("En el <b>Explorer</b> del Warehouse, agrega <code>lh_tutor</code> como fuente (<b>+ Warehouses</b> o <b>+ Data sources</b>). Así podrás leer sus tablas con nombres de tres partes.", "In the Warehouse <b>Explorer</b>, add <code>lh_tutor</code> as a source (<b>+ Warehouses</b> or <b>+ Data sources</b>). That lets you read its tables with three-part names.")},
     {"t": T("<b>New SQL query</b>. Crea y carga las tres dimensiones:", "<b>New SQL query</b>. Create and load the three dimensions:"), "code": DIMS},
     {"t": T("Crea y carga la tabla de hechos:", "Create and load the fact table:"), "code": FACT},
     {"t": T("Valida con cifras de control:", "Validate with control totals:"), "code": CHECK},
     {"t": T("Curiosidad: ejecuta <code>SELECT * FROM dbo.dim_cliente;</code> y observa los valores de <code>sk_cliente</code>.", "Curiosity: run <code>SELECT * FROM dbo.dim_cliente;</code> and look at the <code>sk_cliente</code> values.")}],
   "expect": T("""<p>Conteos: <b>dim_cliente 5 · dim_producto 4 · dim_fecha 7 · fact_ventas 11</b>. Totales por región:</p>
     <table class="res"><tr><th>region</th><th>ventas</th><th>total</th></tr><tr><td>Norte</td><td>3</td><td>3735.75</td></tr><tr><td>Sur</td><td>3</td><td>1860.75</td></tr><tr><td>Centro</td><td>2</td><td>1670.00</td></tr><tr><td>Occidente</td><td>3</td><td>1325.50</td></tr></table>
     <p>Suma = <b>8592.00</b>, igual que en Plata. ¡El dato llegó entero de Bronce a Oro!</p>""",
     """<p>Counts: <b>dim_cliente 5 · dim_producto 4 · dim_fecha 7 · fact_ventas 11</b>. Totals by region:</p>
     <table class="res"><tr><th>region</th><th>ventas</th><th>total</th></tr><tr><td>Norte</td><td>3</td><td>3735.75</td></tr><tr><td>Sur</td><td>3</td><td>1860.75</td></tr><tr><td>Centro</td><td>2</td><td>1670.00</td></tr><tr><td>Occidente</td><td>3</td><td>1325.50</td></tr></table>
     <p>Sum = <b>8592.00</b>, same as Silver. The data made it whole from Bronze to Gold!</p>""")},
  {"type": "quiz",
   "say": T("¿Viste los valores de <code>sk_cliente</code>? Probablemente no eran 1, 2, 3, 4, 5. 🤔", "Did you see the <code>sk_cliente</code> values? They probably weren't 1, 2, 3, 4, 5. 🤔"),
   "q": T("Tus <code>sk_cliente</code> salieron como números grandes y con saltos. ¿Qué significa?", "Your <code>sk_cliente</code> values came out as large numbers with gaps. What does it mean?"),
   "opts": [
     opt(T("Error: hay que borrar la tabla y repetir la carga", "An error: drop the table and reload"), T("No es error. Si repites la carga, saldrán otros números igual de “raros”.", "Not an error. Reload and you'll get other equally “weird” numbers.")),
     opt(T("Es normal: IDENTITY en Fabric garantiza valores únicos, pero no consecutivos", "It's normal: IDENTITY in Fabric guarantees unique values, but not consecutive ones"), T("¡Exacto! El Warehouse es distribuido: genera rangos en paralelo. Una llave sustituta solo necesita ser única; su valor no debe significar nada.", "Exactly! The Warehouse is distributed: it generates ranges in parallel. A surrogate key only needs to be unique; its value shouldn't mean anything."), True),
     opt(T("Hay que usar <code>IDENTITY(1,1)</code>", "You need <code>IDENTITY(1,1)</code>"), T("En Fabric no se puede definir valor inicial ni incremento.", "In Fabric you can't set the seed or increment."))]},
  {"type": "quiz",
   "say": T("Ojo con esta: le pasa a gente con mucha experiencia en SQL Server.", "Careful with this one: it trips up people with lots of SQL Server experience."),
   "q": T("Declaraste <code>PRIMARY KEY … NOT ENFORCED</code> en <code>dim_cliente</code>. Si cargas por error el mismo cliente dos veces, ¿qué pasa?",
          "You declared <code>PRIMARY KEY … NOT ENFORCED</code> on <code>dim_cliente</code>. If you accidentally load the same customer twice, what happens?"),
   "opts": [
     opt(T("El INSERT falla por violación de llave", "The INSERT fails with a key violation"), T("Eso pasaría en SQL Server. Aquí la llave <b>no se valida</b>.", "That's what SQL Server would do. Here the key <b>isn't validated</b>.")),
     opt(T("Se insertan los duplicados sin avisar; tu proceso de carga debe evitarlos", "The duplicates get inserted silently; your load process must prevent them"), T("Correcto. Por eso las cargas usan <code>MERGE</code> o <code>WHERE NOT EXISTS</code>, y las cifras de control comparan conteos. Lo verás en la lección 4.4.", "Correct. That's why loads use <code>MERGE</code> or <code>WHERE NOT EXISTS</code>, and control totals compare counts. You'll see it in lesson 4.4."), True)]}
 ]})

# ------------------------------------------------------------------ 4.4
PROC = """CREATE PROCEDURE dbo.usp_cargar_ventas
AS
BEGIN
    -- 1) Clientes nuevos
    MERGE dbo.dim_cliente AS t
    USING (SELECT DISTINCT cliente, region FROM lh_tutor.dbo.silver_ventas_m) AS s
       ON t.cliente = s.cliente AND t.region = s.region
    WHEN NOT MATCHED BY TARGET THEN
        INSERT (cliente, region) VALUES (s.cliente, s.region);

    -- 2) Productos nuevos
    MERGE dbo.dim_producto AS t
    USING (SELECT DISTINCT producto FROM lh_tutor.dbo.silver_ventas_m) AS s
       ON t.producto = s.producto
    WHEN NOT MATCHED BY TARGET THEN
        INSERT (producto) VALUES (s.producto);

    -- 3) Fechas nuevas
    MERGE dbo.dim_fecha AS t
    USING (SELECT DISTINCT YEAR(fecha) * 10000 + MONTH(fecha) * 100 + DAY(fecha) AS sk_fecha,
                           fecha, YEAR(fecha) AS anio, MONTH(fecha) AS mes, DAY(fecha) AS dia
           FROM lh_tutor.dbo.silver_ventas_m) AS s
       ON t.sk_fecha = s.sk_fecha
    WHEN NOT MATCHED BY TARGET THEN
        INSERT (sk_fecha, fecha, anio, mes, dia) VALUES (s.sk_fecha, s.fecha, s.anio, s.mes, s.dia);

    -- 4) Hechos: actualiza montos que cambiaron e inserta ventas nuevas
    MERGE dbo.fact_ventas AS t
    USING (SELECT v.id,
                  YEAR(v.fecha) * 10000 + MONTH(v.fecha) * 100 + DAY(v.fecha) AS sk_fecha,
                  c.sk_cliente, p.sk_producto,
                  CAST(v.monto AS DECIMAL(12, 2)) AS monto
           FROM lh_tutor.dbo.silver_ventas_m AS v
           JOIN dbo.dim_cliente  AS c ON c.cliente = v.cliente AND c.region = v.region
           JOIN dbo.dim_producto AS p ON p.producto = v.producto) AS s
       ON t.id_venta = s.id
    WHEN MATCHED AND t.monto <> s.monto THEN
        UPDATE SET t.monto = s.monto
    WHEN NOT MATCHED BY TARGET THEN
        INSERT (id_venta, sk_fecha, sk_cliente, sk_producto, monto)
        VALUES (s.id, s.sk_fecha, s.sk_cliente, s.sk_producto, s.monto);
END;"""

L.append({
 "id": "l4-4", "icon": "🔁", "min": 28,
 "badge": {"e": "⚙️", "n": T("Maestro de procedimientos", "Stored Procedure Master")},
 "title": T("Cargas en el Warehouse: MERGE y procedimientos almacenados", "Warehouse loads: MERGE and stored procedures"),
 "steps": [
  {"type": "concept",
   "say": T("Ya tienes tu estrella. Ahora hay que <b>mantenerla al día</b> cada noche, sin duplicar nada.", "You have your star. Now you need to <b>keep it up to date</b> every night without duplicating anything."),
   "kicker": T("Cargas repetibles", "Repeatable loads"),
   "title": T("Cómo entran los datos al Warehouse", "How data gets into the Warehouse"),
   "body": T(
    """<ul><li><b>INSERT … SELECT / CTAS entre bases de datos</b>: lees de un Lakehouse y escribes en el Warehouse. Es lo más común en una arquitectura Medallion.</li>
    <li><b>Pipelines y Copy job</b> con el Warehouse como destino, para traer datos de fuentes externas.</li>
    <li><b>COPY INTO</b>: carga masiva de archivos (CSV, Parquet) desde una cuenta de almacenamiento.</li></ul>
    <p>Para que la carga sea repetible usamos <b>MERGE</b> en T-SQL, que <span class="hl">en el Warehouse de Fabric es GA desde enero de 2026</span>, y la envolvemos en un <b>procedimiento almacenado</b>. Un pipeline lo ejecuta con la actividad <i>Stored procedure</i>.</p>""",
    """<ul><li><b>Cross-database INSERT … SELECT / CTAS</b>: read from a Lakehouse and write into the Warehouse. The most common approach in a Medallion architecture.</li>
    <li><b>Pipelines and Copy job</b> with the Warehouse as destination, to bring data from external sources.</li>
    <li><b>COPY INTO</b>: bulk-load files (CSV, Parquet) from a storage account.</li></ul>
    <p>To make the load repeatable we use T-SQL <b>MERGE</b>, <span class="hl">generally available in the Fabric Warehouse since January 2026</span>, and wrap it in a <b>stored procedure</b>. A pipeline runs it with the <i>Stored procedure</i> activity.</p>"""),
   "callouts": [{"k": "key", "b": T("Carga primero las <b>dimensiones</b> y después los <b>hechos</b>: la tabla de hechos necesita encontrar las llaves sustitutas de clientes y productos nuevos.",
                                     "Load the <b>dimensions</b> first, then the <b>facts</b>: the fact table needs to find the surrogate keys of new customers and products.")}]},
  {"type": "order",
   "say": T("Ordena el procedimiento de carga nocturna.", "Order the nightly load procedure."),
   "title": T("El orden correcto de una carga dimensional", "The right order for a dimensional load"),
   "items": [T("Insertar en las dimensiones los clientes, productos y fechas nuevos", "Insert new customers, products and dates into the dimensions"),
             T("Buscar las llaves sustitutas de cada venta con JOIN a las dimensiones", "Look up each sale's surrogate keys by joining to the dimensions"),
             T("MERGE en la tabla de hechos: actualizar lo que cambió e insertar lo nuevo", "MERGE into the fact table: update what changed and insert what's new"),
             T("Comparar conteos y totales contra Plata (cifras de control)", "Compare counts and totals against Silver (control totals)")]},
  {"type": "fill",
   "say": T("MERGE en T-SQL tiene sus propias palabras. Complétalas.", "T-SQL MERGE has its own keywords. Fill them in."),
   "title": T("MERGE en T-SQL", "T-SQL MERGE"),
   "code": "CREATE {{0}} dbo.usp_cargar_clientes AS\nBEGIN\n  MERGE dbo.dim_cliente AS t\n  USING (SELECT DISTINCT cliente, region\n         FROM lh_tutor.dbo.silver_ventas_m) AS s\n     ON t.cliente = s.cliente\n  WHEN MATCHED AND t.region <> s.region THEN\n      {{1}} SET t.region = s.region\n  WHEN NOT MATCHED BY {{2}} THEN\n      INSERT (cliente, region) VALUES (s.cliente, s.region);\nEND;",
   "blanks": [
     {"a": ["procedure", "proc"], "hint": T("CREATE ______: un procedimiento almacenado.", "CREATE ______: a stored procedure.")},
     {"a": ["update"], "hint": T("Lo que haces con una fila que ya existe y cambió.", "What you do to a row that exists and changed.")},
     {"a": ["target"], "hint": T("NOT MATCHED BY ______: no existe en el destino.", "NOT MATCHED BY ______: missing in the destination.")}]},
  {"type": "lab",
   "say": T("Vas a crear un procedimiento que <b>se cura solo</b>: si alguien daña un dato, la siguiente ejecución lo corrige. 🩹", "You'll create a procedure that <b>heals itself</b>: if someone damages a value, the next run fixes it. 🩹"),
   "title": T("Laboratorio: procedimiento de carga idempotente", "Lab: idempotent load procedure"),
   "intro": T("Trabaja en <code>wh_ventas</code>, con las tablas de la lección 4.3.", "Work in <code>wh_ventas</code>, with the tables from lesson 4.3."),
   "tasks": [
     {"t": T("Crea el procedimiento:", "Create the procedure:"), "code": PROC},
     {"t": T("Ejecútalo y revisa que nada cambie, porque los datos ya estaban cargados:", "Run it and check that nothing changes, since the data was already loaded:"), "code": "EXEC dbo.usp_cargar_ventas;\nSELECT COUNT(*) AS filas, SUM(monto) AS total FROM dbo.fact_ventas;"},
     {"t": T("Ahora “daña” un dato a propósito y vuelve a cargar:", "Now “damage” a value on purpose and reload:"), "code": "UPDATE dbo.fact_ventas SET monto = 0 WHERE id_venta = 1;\nSELECT SUM(monto) AS total_danado FROM dbo.fact_ventas;\n\nEXEC dbo.usp_cargar_ventas;\nSELECT SUM(monto) AS total_reparado FROM dbo.fact_ventas;"}],
   "expect": T("Tras el primer EXEC: <b>11 filas y 8592.00</b>. Después del UPDATE: <b>total_danado = 7341.50</b> (faltan los 1250.50 de la venta 1). Tras el segundo EXEC: <b>total_reparado = 8592.00</b>. El MERGE detectó la diferencia contra Plata y la corrigió.",
               "After the first EXEC: <b>11 rows and 8592.00</b>. After the UPDATE: <b>total_danado = 7341.50</b> (missing the 1250.50 from sale 1). After the second EXEC: <b>total_reparado = 8592.00</b>. The MERGE found the difference against Silver and fixed it.")},
  {"type": "quiz",
   "say": T("Conecta lo que aprendiste en el Nivel 2.", "Connect it to what you learned in Level 2."),
   "q": T("Quieres que <code>usp_cargar_ventas</code> se ejecute cada noche, justo después del notebook que actualiza Plata. ¿Cómo lo orquestas?",
          "You want <code>usp_cargar_ventas</code> to run every night, right after the notebook that refreshes Silver. How do you orchestrate it?"),
   "opts": [
     opt(T("Un pipeline: Notebook → (On success) → actividad Stored procedure", "A pipeline: Notebook → (On success) → Stored procedure activity"), T("¡Exacto! El pipeline garantiza el orden y puedes agregar una rama On failure con una alerta.", "Exactly! The pipeline guarantees the order, and you can add an On failure branch with an alert."), True),
     opt(T("Dos programaciones separadas: el notebook a las 2:00 y el procedimiento a las 3:00", "Two separate schedules: the notebook at 2:00 and the procedure at 3:00"), T("Si un día el notebook tarda más de una hora, el procedimiento cargará datos incompletos. Usa dependencias, no horarios.", "If the notebook ever takes more than an hour, the procedure will load incomplete data. Use dependencies, not clock times.")),
     opt(T("Llamar al procedimiento desde Power BI", "Call the procedure from Power BI"), T("Power BI consume datos; no orquesta cargas.", "Power BI consumes data; it doesn't orchestrate loads."))]},
  {"type": "concept",
   "say": T("Estas dudas aparecen en todas las migraciones.", "These questions come up in every migration."),
   "title": T("Dudas frecuentes", "Common questions"), "body": T("", ""),
   "callouts": [{"k": "nodumb", "qa": [
     {"q": T("¿El Warehouse soporta transacciones?", "Does the Warehouse support transactions?"),
      "a": T("Sí. Puedes envolver varias operaciones en <code>BEGIN TRAN … COMMIT</code>, incluso sobre varias tablas del mismo Warehouse: o se aplican todas o ninguna.", "Yes. You can wrap several operations in <code>BEGIN TRAN … COMMIT</code>, even across multiple tables in the same Warehouse: either all apply or none do.")},
     {"q": T("¿Puedo escribir en el Lakehouse desde el Warehouse?", "Can I write to the Lakehouse from the Warehouse?"),
      "a": T("No. Desde el Warehouse <b>lees</b> las tablas del Lakehouse; las escrituras en el Lakehouse se hacen con Spark, pipelines o Dataflows.", "No. From the Warehouse you <b>read</b> Lakehouse tables; writes to the Lakehouse go through Spark, pipelines or Dataflows.")},
     {"q": T("¿Y si vengo de Synapse dedicated SQL pool?", "What if I'm coming from a Synapse dedicated SQL pool?"),
      "a": T("Vas a encontrar mucho familiar, pero sin distribuciones ni índices que administrar: el Warehouse de Fabric los maneja solo. Revisa los tipos de datos y las funciones que uses antes de migrar.", "You'll find a lot that's familiar, but with no distributions or indexes to manage: the Fabric Warehouse handles them for you. Check the data types and features you use before migrating.")}]}]}
 ]})

# ------------------------------------------------------------------ 4.5
CLONE = """-- 1) Clon zero-copy para pruebas: solo copia metadatos
CREATE TABLE dbo.fact_ventas_dev AS CLONE OF dbo.fact_ventas;

-- 2) Experimenta en el clon sin tocar producción
UPDATE dbo.fact_ventas_dev SET monto = monto * 2;

SELECT 'produccion' AS tabla, SUM(monto) AS total FROM dbo.fact_ventas
UNION ALL
SELECT 'dev', SUM(monto) FROM dbo.fact_ventas_dev;"""

TT = """-- 3) Anota la hora actual (UTC) y copia el resultado
SELECT CONVERT(VARCHAR(23), SYSUTCDATETIME(), 126) AS ahora_utc;

-- 4) Borra todo el clon… ¡uy!
DELETE FROM dbo.fact_ventas_dev;

-- 5) Viaja al pasado: pega la hora que copiaste en el paso 3
SELECT COUNT(*) AS filas_en_el_pasado
FROM dbo.fact_ventas_dev
OPTION (FOR TIMESTAMP AS OF 'PEGA_AQUI_LA_HORA');"""

L.append({
 "id": "l4-5", "icon": "🛡️", "min": 25,
 "badge": {"e": "🏆", "n": T("Guardián del Warehouse", "Warehouse Guardian")},
 "title": T("Clones, time travel, seguridad y el desafío final", "Clones, time travel, security and the final challenge"),
 "steps": [
  {"type": "concept",
   "say": T("Dos superpoderes que muchos warehouses tradicionales envidian. 🦸", "Two superpowers many traditional warehouses envy. 🦸"),
   "kicker": T("Clones y viajes en el tiempo", "Clones and time travel"),
   "title": T("Copiar sin copiar y consultar el pasado", "Copy without copying, and query the past"),
   "body": T(
    """<ul><li><b>Clon zero-copy</b>: <code>CREATE TABLE nueva AS CLONE OF original</code> crea una tabla nueva copiando solo los <b>metadatos</b>; los archivos Parquet se comparten. Es casi instantáneo y casi no ocupa espacio. Ideal para pruebas, desarrollo o “congelar” una foto para auditoría. Con <code>AT</code> puedes clonar la tabla como estaba en un momento anterior.</li>
    <li><b>Time travel</b>: agrega <code>OPTION (FOR TIMESTAMP AS OF '…')</code> a un SELECT y verás los datos como estaban en ese momento. El Warehouse conserva versiones por defecto hasta <span class="hl">30 días</span>. La hora siempre va en <b>UTC</b>.</li></ul>""",
    """<ul><li><b>Zero-copy clone</b>: <code>CREATE TABLE new AS CLONE OF original</code> creates a new table by copying only the <b>metadata</b>; the Parquet files are shared. It's nearly instant and takes almost no space. Ideal for testing, development or “freezing” a snapshot for audit. With <code>AT</code> you can clone the table as it was at an earlier moment.</li>
    <li><b>Time travel</b>: add <code>OPTION (FOR TIMESTAMP AS OF '…')</code> to a SELECT and you'll see the data as it was at that moment. The Warehouse keeps versions for up to <span class="hl">30 days</span> by default. Times are always in <b>UTC</b>.</li></ul>"""),
   "callouts": [{"k": "watch", "b": T("Las consultas con time travel son de solo lectura: no puedes hacer INSERT, UPDATE ni DELETE “en el pasado”. Para recuperar datos, clona la tabla <code>AT</code> el momento correcto o inserta desde un SELECT con time travel.",
                                       "Time-travel queries are read-only: you can't INSERT, UPDATE or DELETE “in the past”. To recover data, clone the table <code>AT</code> the right moment or insert from a time-travel SELECT.")}]},
  {"type": "lab",
   "say": T("Vas a romper algo… y a rescatarlo del pasado. 🕰️", "You'll break something… and rescue it from the past. 🕰️"),
   "title": T("Laboratorio: clon zero-copy y rescate con time travel", "Lab: zero-copy clone and time-travel rescue"),
   "intro": T("En <code>wh_ventas</code>. Ejecuta cada bloque por separado.", "In <code>wh_ventas</code>. Run each block separately."),
   "tasks": [
     {"t": T("Crea un clon y experimenta en él:", "Create a clone and experiment on it:"), "code": CLONE},
     {"t": T("Anota la hora, borra el clon y viaja al pasado:", "Note the time, wipe the clone and travel to the past:"), "code": TT},
     {"t": T("Comprueba el presente:", "Check the present:"), "code": "SELECT COUNT(*) AS filas_hoy FROM dbo.fact_ventas_dev;"}],
   "expect": T("Clon: producción <b>8592.00</b> y dev <b>17184.00</b>: producción no se tocó. Después del DELETE: <b>filas_en_el_pasado = 11</b> y <b>filas_hoy = 0</b>. Los datos “borrados” siguen accesibles en el pasado.",
               "Clone: production <b>8592.00</b> and dev <b>17184.00</b>: production wasn't touched. After the DELETE: <b>filas_en_el_pasado = 11</b> and <b>filas_hoy = 0</b>. The “deleted” data is still reachable in the past.")},
  {"type": "quiz",
   "say": T("Pregunta de costos para tu cliente.", "A cost question for your client."),
   "q": T("Clonas una tabla de hechos de 2 TB para que el equipo de QA haga pruebas. ¿Cuánto almacenamiento extra ocupa el clon en el momento de crearlo?",
          "You clone a 2 TB fact table so the QA team can test. How much extra storage does the clone take at creation time?"),
   "opts": [
     opt(T("Otros 2 TB", "Another 2 TB"), T("Eso sería una copia tradicional. El clon zero-copy comparte los archivos.", "That would be a traditional copy. A zero-copy clone shares the files.")),
     opt(T("Casi nada: solo los metadatos. Crece únicamente con los cambios que QA haga en el clon", "Almost nothing: just metadata. It only grows with the changes QA makes to the clone"), T("¡Exacto! Por eso los clones son perfectos para ambientes de prueba.", "Exactly! That's why clones are perfect for test environments."), True)]},
  {"type": "concept",
   "say": T("La seguridad no es opcional, menos con datos de clientes.", "Security isn't optional, least of all with customer data."),
   "title": T("Seguridad granular en el Warehouse", "Granular security in the Warehouse"),
   "body": T("<p>Además de los roles del workspace, el Warehouse permite seguridad fina con T-SQL:</p>", "<p>Beyond workspace roles, the Warehouse supports fine-grained security with T-SQL:</p>"),
   "cards": [
     {"e": "🔐", "n": "GRANT / DENY", "d": T("Permisos por objeto: quién puede leer qué tabla o vista.", "Object permissions: who can read which table or view.")},
     {"e": "🧱", "n": T("Seguridad por columna", "Column-level security"), "d": T("Permitir SELECT solo sobre ciertas columnas.", "Allow SELECT on specific columns only.")},
     {"e": "🧭", "n": T("Seguridad por fila (RLS)", "Row-level security (RLS)"), "d": T("Una función de filtro y una política: cada usuario ve solo sus filas.", "A filter function plus a policy: each user sees only their rows."), "star": True},
     {"e": "🎭", "n": T("Enmascaramiento dinámico", "Dynamic data masking"), "d": T("Mostrar datos sensibles parcialmente ocultos (por ejemplo, XXXX1234).", "Show sensitive data partially hidden (e.g. XXXX1234).")}]},
  {"type": "match",
   "say": T("🏁 <b>Desafío final del Nivel 4.</b> Necesidad → funcionalidad.", "🏁 <b>Level 4 final challenge.</b> Need → feature."),
   "title": T("Desafío: el guardián del Warehouse", "Challenge: the Warehouse guardian"),
   "pairs": [
     [T("Ambiente de pruebas sin duplicar 5 TB", "A test environment without duplicating 5 TB"), T("Clon zero-copy", "Zero-copy clone")],
     [T("Ver cómo estaba una tabla ayer a las 9:00", "See how a table looked yesterday at 9:00"), "OPTION (FOR TIMESTAMP AS OF …)"],
     [T("Cada gerente ve solo las ventas de su región", "Each manager sees only their region's sales"), T("Seguridad por fila (RLS)", "Row-level security (RLS)")],
     [T("Mostrar el RFC como XXXX-1234", "Show the tax ID as XXXX-1234"), T("Enmascaramiento dinámico", "Dynamic data masking")],
     [T("Carga nocturna repetible sin duplicados", "Repeatable nightly load with no duplicates"), T("Procedimiento con MERGE", "Procedure with MERGE")]]},
  {"type": "quiz",
   "say": T("La pregunta de arquitecto que cierra el nivel. ¡Ya casi!", "The architect question that closes the level. Almost there!"),
   "q": T("Diseñas Oro para una cadena de restaurantes. El equipo de BI domina T-SQL, ingeniería usa PySpark y los reportes van en Power BI. ¿Qué propones?",
          "You're designing Gold for a restaurant chain. The BI team masters T-SQL, engineering uses PySpark and reports run in Power BI. What do you propose?"),
   "opts": [
     opt(T("Todo en un solo Lakehouse y que BI aprenda PySpark", "Everything in a single Lakehouse and BI learns PySpark"), T("Ignoras la fortaleza del equipo de BI y alargas el proyecto.", "You ignore the BI team's strengths and stretch the project.")),
     opt(T("Bronce y Plata en Lakehouse con Spark; Oro en Warehouse con modelo estrella y procedimientos T-SQL; Power BI en Direct Lake",
           "Bronze and Silver in a Lakehouse with Spark; Gold in a Warehouse with a star schema and T-SQL procedures; Power BI in Direct Lake"),
         T("¡Arquitectura de nivel profesional! Cada equipo trabaja con su herramienta, todo vive en OneLake y Power BI lee Oro sin importar datos.", "Professional-grade architecture! Each team uses its own tool, everything lives in OneLake and Power BI reads Gold without importing data."), True),
     opt(T("Exportar Oro a Excel cada día", "Export Gold to Excel every day"), T("Adiós gobierno, adiós una sola versión de la verdad. 😬", "Goodbye governance, goodbye single version of the truth. 😬"))]}
 ]})

out = {"id": 4,
       "title": T("Data Warehouse y T-SQL", "Data Warehouse and T-SQL"),
       "desc": T("Warehouse vs Lakehouse, modelo estrella, T-SQL en Fabric, MERGE y procedimientos, clones, time travel y seguridad.", "Warehouse vs Lakehouse, star schema, T-SQL in Fabric, MERGE and procedures, clones, time travel and security."),
       "lessons": L}
dst = pathlib.Path(__file__).resolve().parent.parent / "content/level-4.json"
dst.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", dst, sum(len(l["steps"]) for l in L), "steps")
