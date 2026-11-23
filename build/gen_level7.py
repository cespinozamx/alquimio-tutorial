"""Genera content/level-7.json — Nivel 7: Gobierno, seguridad y CI/CD."""
import json, pathlib

def T(es, en): return {"es": es, "en": en}
def opt(t, why, ok=False):
    o = {"t": t, "why": why}
    if ok: o["ok"] = 1
    return o

L = []

# ------------------------------------------------------------------ 7.1
L.append({
 "id": "l7-1", "icon": "🗺️", "min": 20,
 "badge": {"e": "🏙️", "n": T("Urbanista de datos", "Data City Planner")},
 "title": T("Gobierno: dominios, endosos, etiquetas y linaje", "Governance: domains, endorsement, labels and lineage"),
 "steps": [
  {"type": "story",
   "say": T("Nivel 7. Tu plataforma ya funciona. Ahora hay que hacer que <b>siga funcionando</b> con 200 usuarios. 🏙️", "Level 7. Your platform works. Now it has to <b>keep working</b> with 200 users. 🏙️"),
   "kicker": T("De pueblo a ciudad", "From village to city"),
   "title": T("Cuando la plataforma crece, necesita reglas de ciudad", "As the platform grows, it needs city rules"),
   "body": T(
    """<p>En un pueblo todos se conocen: sabes quién hizo cada tabla y si confías en ella. En una ciudad de miles de habitantes necesitas <b>orden</b>:</p>
    <ul><li>🏘️ <b>Dominios</b>: los barrios. Agrupan workspaces por área de negocio (Finanzas, Comercial, RR. HH.) y permiten delegar la administración a cada área.</li>
    <li>🏅 <b>Endosos</b>: el sello de calidad. <i>Promoted</i> (“lo recomiendo”), <i>Certified</i> (revisado por alguien autorizado) y <i>Master data</i> (la fuente oficial de un dato clave).</li>
    <li>🏷️ <b>Etiquetas de sensibilidad</b> de Microsoft Purview: “Confidencial” o “Uso interno”. Viajan con el dato, incluso si se exporta a Excel o PDF.</li>
    <li>🧭 <b>Linaje</b>: el mapa de tuberías. De dónde viene cada dato y qué se rompe si cambias algo.</li></ul>""",
    """<p>In a village everyone knows each other: you know who built each table and whether to trust it. In a city of thousands you need <b>order</b>:</p>
    <ul><li>🏘️ <b>Domains</b>: the neighborhoods. They group workspaces by business area (Finance, Sales, HR) and let you delegate administration to each area.</li>
    <li>🏅 <b>Endorsement</b>: the quality seal. <i>Promoted</i> (“I recommend it”), <i>Certified</i> (reviewed by an authorized person) and <i>Master data</i> (the official source of a key data point).</li>
    <li>🏷️ Microsoft Purview <b>sensitivity labels</b>: “Confidential” or “Internal use”. They travel with the data, even when exported to Excel or PDF.</li>
    <li>🧭 <b>Lineage</b>: the pipe map. Where each piece of data comes from and what breaks if you change something.</li></ul>"""),
   "visual": "govCity"},
  {"type": "match",
   "say": T("Une cada necesidad con su herramienta de gobierno.", "Pair each need with its governance tool."),
   "title": T("¿Qué herramienta de gobierno uso?", "Which governance tool do I use?"),
   "pairs": [
     [T("Que todos sepan cuál es el modelo oficial de ventas", "Everyone should know which sales model is the official one"), T("🏅 Endoso Certified", "🏅 Certified endorsement")],
     [T("Saber qué reportes se rompen si borro una columna", "Know which reports break if I drop a column"), T("🧭 Linaje", "🧭 Lineage")],
     [T("Que un Excel exportado siga marcado como confidencial", "An exported Excel file stays marked as confidential"), T("🏷️ Etiqueta de sensibilidad", "🏷️ Sensitivity label")],
     [T("Que Finanzas administre sus propios workspaces", "Finance manages its own workspaces"), T("🏘️ Dominio", "🏘️ Domain")]]},
  {"type": "lab",
   "say": T("Vamos a ver el mapa completo de lo que construiste en el curso. Te va a gustar. 🗺️", "Let's look at the full map of what you built during the course. You'll like it. 🗺️"),
   "title": T("Laboratorio: linaje y endoso de tu solución", "Lab: lineage and endorsement of your solution"),
   "intro": T("Trabaja en <code>ws_tutor_fabric</code>. <i>Los nombres de los botones pueden variar un poco según tu versión de Fabric.</i>", "Work in <code>ws_tutor_fabric</code>. <i>Button names may vary slightly with your Fabric version.</i>"),
   "tasks": [
     {"t": T("En el workspace, cambia la vista de <b>List</b> a <b>Lineage</b> (ícono arriba a la derecha).", "In the workspace, switch the view from <b>List</b> to <b>Lineage</b> (top-right icon).")},
     {"t": T("Sigue las flechas: <code>lh_tutor</code> → <code>wh_ventas</code> → <code>sm_ventas</code> → <code>rpt_ventas</code>. Haz clic en <code>sm_ventas</code> y usa <b>Show impact across workspaces</b> (o <i>Impact analysis</i>).", "Follow the arrows: <code>lh_tutor</code> → <code>wh_ventas</code> → <code>sm_ventas</code> → <code>rpt_ventas</code>. Click <code>sm_ventas</code> and use <b>Show impact across workspaces</b> (or <i>Impact analysis</i>).")},
     {"t": T("Abre la configuración de <code>sm_ventas</code> → <b>Endorsement</b> → marca <b>Promoted</b> y agrega una descripción: “Modelo de ventas del tutor Alquimio”.", "Open <code>sm_ventas</code> settings → <b>Endorsement</b> → choose <b>Promoted</b> and add a description: “Alquimio tutor sales model”.")},
     {"t": T("Si tu organización tiene etiquetas de Purview, asigna una a <code>sm_ventas</code> (por ejemplo, <i>General</i> o <i>Internal</i>). Si no aparece la opción, tu tenant aún no las tiene configuradas: márcalo como hecho.", "If your organization has Purview labels, assign one to <code>sm_ventas</code> (e.g. <i>General</i> or <i>Internal</i>). If the option doesn't show, your tenant hasn't configured them yet: mark it done.")}],
   "expect": T("En la vista de linaje verás la cadena completa del curso: del Lakehouse al reporte. <code>sm_ventas</code> mostrará el sello <b>Promoted</b>, y en el OneLake catalog aparecerá antes que los modelos sin endoso.",
               "In lineage view you'll see the course's whole chain: from the Lakehouse to the report. <code>sm_ventas</code> will show the <b>Promoted</b> badge, and in the OneLake catalog it will rank above unendorsed models.")},
  {"type": "quiz",
   "say": T("Diferencia clave entre endosos.", "A key difference between endorsements."),
   "q": T("¿Cuál es la diferencia principal entre <b>Promoted</b> y <b>Certified</b>?", "What's the main difference between <b>Promoted</b> and <b>Certified</b>?"),
   "opts": [
     opt(T("Ninguna, son sinónimos", "None, they're synonyms"), T("Tienen distinto nivel de confianza y distintos permisos.", "They carry different trust levels and permissions.")),
     opt(T("Cualquier colaborador puede promover; certificar solo lo hacen revisores que el administrador autoriza", "Any contributor can promote; only reviewers the admin authorizes can certify"),
         T("¡Exacto! Promoted dice “yo lo recomiendo”. Certified dice “la organización lo revisó y lo respalda”.", "Exactly! Promoted says “I recommend it”. Certified says “the organization reviewed and backs it”."), True),
     opt(T("Certified hace que la tabla sea más rápida", "Certified makes the table faster"), T("Los endosos son de confianza y descubrimiento, no de rendimiento.", "Endorsements are about trust and discovery, not performance."))]}
 ]})

# ------------------------------------------------------------------ 7.2
L.append({
 "id": "l7-2", "icon": "🧅", "min": 20,
 "badge": {"e": "🛡️", "n": T("Guardián por capas", "Layered Guardian")},
 "title": T("Seguridad por capas: de Entra ID a OneLake security", "Layered security: from Entra ID to OneLake security"),
 "steps": [
  {"type": "concept",
   "say": T("La seguridad en Fabric es como una cebolla: varias capas, y cada una protege algo distinto. 🧅", "Security in Fabric is like an onion: several layers, each protecting something different. 🧅"),
   "kicker": T("Defensa en profundidad", "Defense in depth"),
   "title": T("Las capas de seguridad de Fabric", "Fabric's security layers"),
   "body": T(
    """<ol><li><b>Identidad (Microsoft Entra ID)</b>: quién eres, MFA y acceso condicional. Si no pasas esta puerta, no entras.</li>
    <li><b>Roles de workspace</b>: Admin, Member, Contributor, Viewer. Deciden quién edita y quién solo consume.</li>
    <li><b>Permisos por elemento</b>: compartir un reporte o un modelo sin dar acceso a todo el workspace.</li>
    <li><b>OneLake security</b>: roles sobre los datos de un Lakehouse (tablas, carpetas, filas y columnas) que se aplican en todos los motores que leen OneLake.</li>
    <li><b>Seguridad del motor</b>: GRANT y RLS en el Warehouse (Nivel 4) y RLS en el modelo semántico (Nivel 6).</li>
    <li><b>Etiquetas de sensibilidad</b>: protegen el dato incluso fuera de Fabric.</li></ol>""",
    """<ol><li><b>Identity (Microsoft Entra ID)</b>: who you are, MFA and conditional access. If you don't pass this gate, you're not in.</li>
    <li><b>Workspace roles</b>: Admin, Member, Contributor, Viewer. They decide who edits and who only consumes.</li>
    <li><b>Item permissions</b>: share a report or model without granting the whole workspace.</li>
    <li><b>OneLake security</b>: roles over a Lakehouse's data (tables, folders, rows and columns) enforced across every engine that reads OneLake.</li>
    <li><b>Engine security</b>: GRANT and RLS in the Warehouse (Level 4) and RLS in the semantic model (Level 6).</li>
    <li><b>Sensitivity labels</b>: protect the data even outside Fabric.</li></ol>"""),
   "visual": "securityLayers",
   "callouts": [{"k": "key", "b": T("OneLake security funciona con <b>denegación por defecto</b>: cuando la activas en un Lakehouse, quien no pertenece a un rol no ve datos. Los roles los crean usuarios Admin o Member del workspace y dan acceso a usuarios con rol Viewer.",
                                     "OneLake security is <b>deny-by-default</b>: once enabled on a Lakehouse, anyone outside a role sees no data. Roles are created by workspace Admins or Members and grant access to users with the Viewer role.")}]},
  {"type": "match",
   "say": T("Elige la capa correcta para cada caso.", "Pick the right layer for each case."),
   "title": T("¿En qué capa lo resuelvo?", "Which layer solves it?"),
   "pairs": [
     [T("Bloquear el acceso desde dispositivos no administrados", "Block access from unmanaged devices"), T("Acceso condicional de Entra ID", "Entra ID conditional access")],
     [T("El equipo de QA puede editar notebooks, pero no administrar el workspace", "The QA team can edit notebooks but not manage the workspace"), T("Rol Contributor", "Contributor role")],
     [T("Un científico de datos lee solo la tabla de clientes del Lakehouse desde Spark", "A data scientist reads only the customers table of the Lakehouse from Spark"), "OneLake security"],
     [T("El gerente ve solo su región en el reporte", "The manager sees only their region in the report"), T("RLS en el modelo semántico", "RLS in the semantic model")]]},
  {"type": "quiz",
   "say": T("El principio de mínimo privilegio, aplicado.", "Least privilege, applied."),
   "q": T("Un auditor externo debe revisar un solo reporte durante dos semanas. ¿Qué le das?", "An external auditor must review a single report for two weeks. What do you give them?"),
   "opts": [
     opt(T("Rol Member en el workspace", "Member role on the workspace"), T("Le darías permiso de editar y compartir todo. Demasiado.", "You'd let them edit and share everything. Too much.")),
     opt(T("Compartir solo ese reporte (permiso por elemento) y quitar el acceso al terminar", "Share just that report (item permission) and revoke it when done"), T("¡Exacto! Mínimo privilegio y por tiempo limitado.", "Exactly! Least privilege, time-boxed."), True),
     opt(T("Exportar el reporte a PDF y enviarlo por correo", "Export the report to PDF and email it"), T("Pierdes control y trazabilidad, y el PDF puede reenviarse sin límite.", "You lose control and traceability, and the PDF can be forwarded endlessly."))]},
  {"type": "quiz",
   "say": T("Ojo con esta trampa clásica.", "Watch out for this classic trap."),
   "q": T("Configuraste RLS en el modelo semántico para que cada gerente vea su región. Pero agregaste a los gerentes como <b>Members</b> del workspace. ¿Qué pasa?",
          "You set up RLS in the semantic model so each manager sees their region. But you added the managers as workspace <b>Members</b>. What happens?"),
   "opts": [
     opt(T("RLS funciona igual", "RLS works the same"), T("No: quienes pueden editar el modelo no quedan filtrados por RLS.", "No: people who can edit the model aren't filtered by RLS.")),
     opt(T("Ven todas las regiones: RLS solo aplica a quienes tienen permiso de lectura", "They see every region: RLS only applies to people with read permission"),
         T("Correcto. Los consumidores deben ser <b>Viewers</b> o recibir el reporte compartido o una app, nunca Members ni Contributors.", "Correct. Consumers should be <b>Viewers</b> or get the report via sharing or an app, never Members or Contributors."), True)]},
  {"type": "reveal", "kind": "brain",
   "say": T("Pregunta de arquitecto.", "Architect question."),
   "prompt": T("Si ya tienes RLS en el modelo semántico, ¿para qué querrías también OneLake security en el Lakehouse?",
               "If you already have RLS in the semantic model, why would you also want OneLake security on the Lakehouse?"),
   "answer": T("Porque RLS en el modelo solo protege a quien entra <b>por el modelo</b>. Un científico de datos con un notebook, un usuario del SQL endpoint o una herramienta externa que lee OneLake se saltaría el modelo. OneLake security define las reglas <b>en el dato</b>, así que aplican sin importar el motor. Defensa en profundidad: proteges el dato en su origen y también en cada punto de consumo.",
               "Because model RLS only protects people who come in <b>through the model</b>. A data scientist with a notebook, a SQL endpoint user or an external tool reading OneLake would bypass the model. OneLake security defines rules <b>on the data</b>, so they apply regardless of the engine. Defense in depth: you protect the data at its source and at every point of consumption.")}
 ]})

# ------------------------------------------------------------------ 7.3
L.append({
 "id": "l7-3", "icon": "🌿", "min": 30,
 "badge": {"e": "🌳", "n": T("Jardinero de Git", "Git Gardener")},
 "title": T("Integración con Git: tu workspace bajo control de versiones", "Git integration: your workspace under version control"),
 "steps": [
  {"type": "concept",
   "say": T("“¿Quién cambió este notebook y por qué?” Con Git, esa pregunta tiene respuesta. 🌿", "“Who changed this notebook, and why?” With Git, that question has an answer. 🌿"),
   "kicker": T("Control de versiones", "Version control"),
   "title": T("Un workspace conectado a un repositorio", "A workspace connected to a repository"),
   "body": T(
    """<p>La <b>integración con Git</b> conecta un workspace con una rama de un repositorio en <b>Azure DevOps</b>, <b>GitHub</b> o <b>GitHub Enterprise</b>. Cada elemento se guarda como archivos de texto: un notebook como código, un pipeline como JSON, un modelo semántico en formato TMDL, un reporte en PBIR.</p>
    <ul><li><b>Commit</b>: envías tus cambios del workspace al repositorio.</li><li><b>Update</b>: traes al workspace los cambios que otros hicieron en el repositorio.</li>
    <li><b>Ramas</b>: cada desarrollador trabaja en su propia rama y su propio workspace, y luego integra con un <i>pull request</i>.</li></ul>""",
    """<p><b>Git integration</b> connects a workspace to a branch of a repository in <b>Azure DevOps</b>, <b>GitHub</b> or <b>GitHub Enterprise</b>. Each item is stored as text files: a notebook as code, a pipeline as JSON, a semantic model in TMDL format, a report in PBIR.</p>
    <ul><li><b>Commit</b>: send your workspace changes to the repository.</li><li><b>Update</b>: bring changes others made in the repository into the workspace.</li>
    <li><b>Branches</b>: each developer works on their own branch and workspace, then merges via a <i>pull request</i>.</li></ul>"""),
   "visual": "gitFlow",
   "callouts": [{"k": "watch", "b": T("A Git viajan las <b>definiciones</b> de los elementos, <b>no los datos</b>. Las tablas Delta de tu Lakehouse no se guardan en el repositorio (y qué bueno: serían gigabytes).",
                                       "Git stores item <b>definitions</b>, <b>not data</b>. Your Lakehouse's Delta tables don't go into the repository (thankfully: they'd be gigabytes).")}]},
  {"type": "quiz",
   "say": T("Confirma que entendiste qué viaja a Git.", "Confirm you understand what goes to Git."),
   "q": T("Haces commit de <code>ws_tutor_fabric</code>. ¿Qué encontrarás en el repositorio?", "You commit <code>ws_tutor_fabric</code>. What will you find in the repository?"),
   "opts": [
     opt(T("Las 11 filas de silver_ventas_m en formato Parquet", "The 11 rows of silver_ventas_m in Parquet"), T("Los datos se quedan en OneLake; Git guarda definiciones.", "Data stays in OneLake; Git stores definitions.")),
     opt(T("El código de los notebooks, la definición de pipelines, modelos y reportes, y los metadatos de los elementos", "Notebook code, pipeline, model and report definitions, plus item metadata"), T("¡Exacto! Todo lo necesario para <b>recrear</b> la solución, no sus datos.", "Exactly! Everything needed to <b>recreate</b> the solution, not its data."), True),
     opt(T("Solo los reportes de Power BI", "Only the Power BI reports"), T("Git soporta muchos tipos de elementos: notebooks, pipelines, lakehouses, warehouses, modelos y más.", "Git supports many item types: notebooks, pipelines, lakehouses, warehouses, models and more."))]},
  {"type": "order",
   "say": T("El flujo de trabajo de un equipo profesional. Ordénalo.", "A professional team's workflow. Put it in order."),
   "title": T("El ciclo de un cambio con Git", "The lifecycle of a change with Git"),
   "items": [T("Crear una rama de trabajo y su workspace de desarrollo", "Create a feature branch and its development workspace"),
             T("Hacer el cambio en el notebook y probarlo", "Make the change in the notebook and test it"),
             T("Commit con un mensaje que explique el porqué", "Commit with a message that explains why"),
             T("Abrir un pull request y pedir revisión", "Open a pull request and ask for review"),
             T("Fusionar a main y actualizar el workspace principal", "Merge to main and update the main workspace")]},
  {"type": "lab",
   "say": T("Conecta tu workspace a GitHub y mira tu código aparecer en el repositorio. 🐙", "Connect your workspace to GitHub and watch your code appear in the repository. 🐙"),
   "title": T("Laboratorio: conecta ws_tutor_fabric a GitHub", "Lab: connect ws_tutor_fabric to GitHub"),
   "intro": T("Necesitas una cuenta de GitHub y ser Admin del workspace. El administrador de tu tenant debe tener habilitada la sincronización con GitHub. Si usas Azure DevOps, los pasos son equivalentes.",
              "You need a GitHub account and to be workspace Admin. Your tenant admin must have GitHub sync enabled. If you use Azure DevOps, the steps are equivalent."),
   "tasks": [
     {"t": T("En GitHub, crea un repositorio privado vacío llamado <code>alquimio-fabric</code>, con un README para que tenga la rama <code>main</code>.", "In GitHub, create an empty private repository called <code>alquimio-fabric</code>, with a README so it has a <code>main</code> branch.")},
     {"t": T("Crea un <b>fine-grained personal access token</b> limitado a ese repositorio, con permiso de lectura y escritura en <b>Contents</b>.", "Create a <b>fine-grained personal access token</b> limited to that repository, with read and write permission on <b>Contents</b>.")},
     {"t": T("En Fabric: <b>Workspace settings → Git integration → GitHub</b>. Agrega tu cuenta con el token y la URL del repositorio.", "In Fabric: <b>Workspace settings → Git integration → GitHub</b>. Add your account with the token and the repository URL.")},
     {"t": T("Elige la rama <code>main</code>, escribe la carpeta <code>fabric</code> y pulsa <b>Connect and sync</b>.", "Choose the <code>main</code> branch, type the folder <code>fabric</code> and click <b>Connect and sync</b>.")},
     {"t": T("En GitHub, abre <code>fabric/nb_ventas_medallion.Notebook/</code> y mira el archivo de contenido: es tu código de PySpark.", "In GitHub, open <code>fabric/nb_ventas_medallion.Notebook/</code> and look at the content file: it's your PySpark code.")},
     {"t": T("En Fabric, agrega una línea de comentario al principio del notebook:", "In Fabric, add a comment line at the top of the notebook:"), "code": "# v2 · revisado en el Nivel 7 del tutor Alquimio"},
     {"t": T("Abre <b>Source control</b> (en la barra del workspace): verás el notebook como modificado. Haz <b>Commit</b> con el mensaje <code>docs: comentario de versión</code>.", "Open <b>Source control</b> (in the workspace bar): the notebook shows as modified. <b>Commit</b> with the message <code>docs: version comment</code>.")}],
   "expect": T("En GitHub verás una carpeta por elemento (<code>.Notebook</code>, <code>.Lakehouse</code>, <code>.Warehouse</code>, <code>.SemanticModel</code>, <code>.Report</code>…) y, en el historial, tu commit con el diff de una sola línea. Ya tienes trazabilidad: quién, qué, cuándo y por qué.",
               "In GitHub you'll see a folder per item (<code>.Notebook</code>, <code>.Lakehouse</code>, <code>.Warehouse</code>, <code>.SemanticModel</code>, <code>.Report</code>…) and, in the history, your commit with a one-line diff. You now have traceability: who, what, when and why.")},
  {"type": "quiz",
   "say": T("Seguridad en Git: muy importante.", "Security in Git: very important."),
   "q": T("Un notebook tiene escrita la contraseña de una base de datos y haces commit a GitHub. ¿Qué es lo correcto?", "A notebook has a database password hardcoded and you commit it to GitHub. What's the right move?"),
   "opts": [
     opt(T("Borrar la línea en un nuevo commit y listo", "Delete the line in a new commit and move on"), T("La contraseña sigue en el historial de Git. Hay que rotarla.", "The password is still in Git history. It must be rotated.")),
     opt(T("Rotar la contraseña de inmediato y guardar los secretos en Azure Key Vault o en conexiones de Fabric, nunca en el código", "Rotate the password immediately and keep secrets in Azure Key Vault or Fabric connections, never in code"),
         T("¡Correcto! Asume que el secreto ya se filtró. A partir de ahí, los secretos se leen en tiempo de ejecución, por ejemplo con <code>notebookutils.credentials.getSecret()</code> desde Key Vault.", "Correct! Assume the secret has leaked. From then on, secrets are read at runtime, e.g. with <code>notebookutils.credentials.getSecret()</code> from Key Vault."), True),
     opt(T("Hacer el repositorio privado", "Make the repository private"), T("Ayuda, pero no basta: cualquiera con acceso al repo, hoy o mañana, puede verla.", "It helps, but isn't enough: anyone with repo access, now or later, can see it."))]}
 ]})

# ------------------------------------------------------------------ 7.4
L.append({
 "id": "l7-4", "icon": "🚀", "min": 28,
 "badge": {"e": "🛰️", "n": T("Controlador de despliegues", "Deployment Controller")},
 "title": T("Deployment pipelines y variable libraries", "Deployment pipelines and variable libraries"),
 "steps": [
  {"type": "concept",
   "say": T("Nunca se edita directo en producción. Nunca. 🚫", "You never edit directly in production. Never. 🚫"),
   "kicker": T("Dev → Test → Prod", "Dev → Test → Prod"),
   "title": T("Promover contenido entre ambientes", "Promoting content across environments"),
   "body": T(
    """<p>Un <b>deployment pipeline</b> conecta varios workspaces como <b>etapas</b>, normalmente Desarrollo, Pruebas y Producción. Con un clic <b>comparas</b> qué cambió entre etapas y <b>despliegas</b> solo lo que quieras.</p>
    <ul><li>Se despliegan <b>definiciones</b>, no datos: un Lakehouse llega vacío a Pruebas y se llena con sus propias cargas.</li>
    <li>Las <b>reglas de despliegue</b> cambian configuraciones por etapa, como la fuente de datos de un modelo semántico.</li>
    <li>Las <b>variable libraries</b> guardan valores por ambiente (nombre de un Lakehouse, una conexión, un umbral). Cada etapa tiene su propio <b>conjunto de valores activo</b>, así que el mismo notebook o pipeline usa los valores correctos según el ambiente.</li></ul>""",
    """<p>A <b>deployment pipeline</b> links several workspaces as <b>stages</b>, typically Development, Test and Production. With one click you <b>compare</b> what changed between stages and <b>deploy</b> only what you want.</p>
    <ul><li>It deploys <b>definitions</b>, not data: a Lakehouse arrives empty in Test and fills up with its own loads.</li>
    <li><b>Deployment rules</b> change settings per stage, such as a semantic model's data source.</li>
    <li><b>Variable libraries</b> store per-environment values (a Lakehouse name, a connection, a threshold). Each stage has its own <b>active value set</b>, so the same notebook or pipeline uses the right values for each environment.</li></ul>"""),
   "visual": "deployFlow"},
  {"type": "quiz",
   "say": T("Escenario real de un cliente.", "A real client scenario."),
   "q": T("En Desarrollo, tu pipeline lee de <code>lh_bronze_dev</code>; en Producción debe leer de <code>lh_bronze_prod</code>. ¿Cómo lo resuelves sin editar el pipeline en cada ambiente?",
          "In Development, your pipeline reads from <code>lh_bronze_dev</code>; in Production it must read from <code>lh_bronze_prod</code>. How do you solve it without editing the pipeline in each environment?"),
   "opts": [
     opt(T("Editar el pipeline a mano después de cada despliegue", "Edit the pipeline by hand after every deployment"), T("Propenso a errores y sin trazabilidad. Justo lo que queremos evitar.", "Error-prone and untraceable. Exactly what we want to avoid.")),
     opt(T("Una variable library con un conjunto de valores por etapa, y que el pipeline lea la variable", "A variable library with one value set per stage, with the pipeline reading the variable"), T("¡Exacto! El pipeline es idéntico en todos los ambientes; solo cambia el conjunto de valores activo.", "Exactly! The pipeline is identical in every environment; only the active value set changes."), True),
     opt(T("Tener un solo Lakehouse para todos los ambientes", "Use a single Lakehouse for every environment"), T("Las pruebas mezclarían datos con producción. Riesgo alto.", "Tests would mix data with production. High risk."))]},
  {"type": "order",
   "say": T("Ordena un despliegue seguro.", "Order a safe deployment."),
   "title": T("Un despliegue responsable", "A responsible deployment"),
   "items": [T("Fusionar el cambio aprobado a la rama main (workspace de Desarrollo)", "Merge the approved change into main (Development workspace)"),
             T("Comparar Desarrollo contra Pruebas y revisar las diferencias", "Compare Development against Test and review the differences"),
             T("Desplegar a Pruebas y ejecutar las validaciones (cifras de control)", "Deploy to Test and run the validations (control totals)"),
             T("Aprobar y desplegar a Producción", "Approve and deploy to Production"),
             T("Monitorear la primera ejecución en Producción", "Monitor the first run in Production")]},
  {"type": "lab",
   "say": T("Vas a promover tu solución a un ambiente de pruebas. Fíjate bien en qué llega… y qué no. 👀", "You'll promote your solution to a test environment. Pay attention to what arrives… and what doesn't. 👀"),
   "title": T("Laboratorio: tu primer deployment pipeline", "Lab: your first deployment pipeline"),
   "intro": T("Necesitas capacidad para un workspace más. <i>La interfaz de deployment pipelines tiene una versión nueva; si ves otra distribución, busca los mismos botones por nombre.</i>",
              "You need capacity for one more workspace. <i>The deployment pipelines UI has a new version; if your layout differs, look for the same buttons by name.</i>"),
   "tasks": [
     {"t": T("En la barra lateral: <b>Workspaces → Deployment pipelines → New pipeline</b>. Nómbralo <code>dp_tutor</code> y deja dos etapas: <b>Development</b> y <b>Test</b>.", "In the sidebar: <b>Workspaces → Deployment pipelines → New pipeline</b>. Name it <code>dp_tutor</code> and keep two stages: <b>Development</b> and <b>Test</b>.")},
     {"t": T("Asigna <code>ws_tutor_fabric</code> a la etapa <b>Development</b>.", "Assign <code>ws_tutor_fabric</code> to the <b>Development</b> stage.")},
     {"t": T("En <b>Test</b>, crea o asigna un workspace nuevo: <code>ws_tutor_fabric_test</code>.", "In <b>Test</b>, create or assign a new workspace: <code>ws_tutor_fabric_test</code>.")},
     {"t": T("Selecciona <code>lh_tutor</code>, <code>nb_ventas_medallion</code> y <code>pl_ingesta_tutor</code> y pulsa <b>Deploy</b> hacia Test.", "Select <code>lh_tutor</code>, <code>nb_ventas_medallion</code> and <code>pl_ingesta_tutor</code> and click <b>Deploy</b> to Test.")},
     {"t": T("Abre <code>ws_tutor_fabric_test</code> → <code>lh_tutor</code>. ¿Qué tablas tiene?", "Open <code>ws_tutor_fabric_test</code> → <code>lh_tutor</code>. Which tables does it have?")},
     {"t": T("Regresa al deployment pipeline y usa <b>Compare</b> entre etapas: los elementos desplegados aparecen como iguales y el resto como “solo en Development”.", "Go back to the deployment pipeline and use <b>Compare</b> between stages: deployed items show as identical and the rest as “only in Development”.")}],
   "expect": T("El Lakehouse de Test llega <b>vacío</b>: sin tablas ni archivos. Llegaron las <b>definiciones</b>, no los datos. Para llenarlo, Test necesita su propia carga: subir el CSV y ejecutar el pipeline y el notebook en ese ambiente. Así trabajan los equipos reales: cada ambiente con sus propios datos.",
               "Test's Lakehouse arrives <b>empty</b>: no tables, no files. The <b>definitions</b> arrived, not the data. To fill it, Test needs its own load: upload the CSV and run the pipeline and notebook in that environment. That's how real teams work: each environment with its own data.")},
  {"type": "concept",
   "say": T("Para equipos grandes, todo esto se automatiza.", "For large teams, all of this gets automated."),
   "title": T("Automatizar el CI/CD", "Automating CI/CD"),
   "body": T("<p>Los deployment pipelines son ideales para empezar. Cuando el equipo crece, el despliegue se automatiza desde GitHub Actions o Azure Pipelines con estas herramientas:</p>",
             "<p>Deployment pipelines are ideal to start with. As the team grows, deployment is automated from GitHub Actions or Azure Pipelines with these tools:</p>"),
   "cards": [
     {"e": "🐍", "n": "fabric-cicd", "d": T("Librería de Python para desplegar elementos de un repositorio a workspaces. Es la herramienta de despliegue más adoptada.", "A Python library that deploys items from a repository to workspaces. It's the most widely adopted deployment tool."), "star": True},
     {"e": "⌨️", "n": "Fabric CLI", "d": T("Línea de comandos de código abierto para scripts y runners de CI.", "An open-source command line for scripts and CI runners.")},
     {"e": "🏗️", "n": "Terraform", "d": T("Infraestructura como código: capacidades, workspaces y permisos.", "Infrastructure as code: capacities, workspaces and permissions.")},
     {"e": "🔌", "n": "Fabric REST APIs", "d": T("La base de todo lo anterior. Se autentican con un service principal.", "The foundation of all the above. Authenticated with a service principal.")}]}
 ]})

# ------------------------------------------------------------------ 7.5
L.append({
 "id": "l7-5", "icon": "📈", "min": 22,
 "badge": {"e": "🏆", "n": T("Guardián de la plataforma", "Platform Guardian")},
 "title": T("Monitoreo, capacidad y el desafío final", "Monitoring, capacity and the final challenge"),
 "steps": [
  {"type": "concept",
   "say": T("Lo que no se mide, no se puede mejorar… ni defender ante el director de finanzas. 💸", "What isn't measured can't be improved… or defended to the CFO. 💸"),
   "kicker": T("Operación", "Operations"),
   "title": T("¿Quién está consumiendo mi capacidad?", "Who's eating my capacity?"),
   "body": T(
    """<ul><li><b>Monitor hub</b> (Monitoreo): el historial de ejecuciones de pipelines, notebooks, Dataflows y Copy jobs, con estado y duración.</li>
    <li><b>Capacity Metrics app</b>: cuántas <i>Capacity Units</i> (CU) consume cada elemento y operación, y si hubo limitación (<i>throttling</i>).</li>
    <li><b>Workspace monitoring</b>: envía registros y métricas detalladas a una base de datos KQL dentro del workspace para analizarlas y crear alertas.</li></ul>
    <p>Fabric <b>suaviza</b> el consumo en el tiempo: puedes tener picos por encima de tu capacidad y se “pagan” en los minutos u horas siguientes. Pero si te excedes demasiado y por mucho tiempo, Fabric primero <b>retrasa</b> y después <b>rechaza</b> operaciones nuevas.</p>""",
    """<ul><li><b>Monitor hub</b>: the run history of pipelines, notebooks, Dataflows and Copy jobs, with status and duration.</li>
    <li><b>Capacity Metrics app</b>: how many <i>Capacity Units</i> (CU) each item and operation consumes, and whether throttling happened.</li>
    <li><b>Workspace monitoring</b>: sends detailed logs and metrics to a KQL database inside the workspace so you can analyze them and set alerts.</li></ul>
    <p>Fabric <b>smooths</b> consumption over time: you can spike above your capacity and “pay it back” over the following minutes or hours. But if you overshoot too much for too long, Fabric first <b>delays</b> and then <b>rejects</b> new operations.</p>"""),
   "callouts": [{"k": "key", "b": T("Antes de comprar una capacidad más grande, abre la Capacity Metrics app y busca el elemento que más consume. A menudo es un notebook sin optimizar o un Dataflow que se refresca cada 15 minutos sin necesidad.",
                                     "Before buying a bigger capacity, open the Capacity Metrics app and find the top consumer. It's often an unoptimized notebook or a Dataflow refreshing every 15 minutes for no reason.")}]},
  {"type": "quiz",
   "say": T("Diagnóstico de costos.", "Cost diagnosis."),
   "q": T("Todos los días a las 9:00 los reportes van lentos. La Capacity Metrics app muestra que a esa hora corre la carga completa de un Dataflow de 40 millones de filas. ¿Qué propones primero?",
          "Every day at 9:00 reports are slow. The Capacity Metrics app shows a full load of a 40-million-row Dataflow running at that hour. What do you propose first?"),
   "opts": [
     opt(T("Subir de F64 a F128", "Upgrade from F64 to F128"), T("Duplicas el costo sin atacar la causa.", "You double the cost without fixing the cause.")),
     opt(T("Mover la carga a la madrugada y volverla incremental (Copy job o notebook con MERGE)", "Move the load to the early morning and make it incremental (Copy job or notebook with MERGE)"), T("¡Exacto! Menos datos y en otro horario: la capacidad queda libre para los reportes en horario laboral.", "Exactly! Less data, at a different time: capacity stays free for reports during business hours."), True),
     opt(T("Pedir a los usuarios que no abran reportes a las 9:00", "Ask users not to open reports at 9:00"), T("😅 Mejor que la plataforma se adapte al negocio, no al revés.", "😅 Better for the platform to adapt to the business, not the other way around."))]},
  {"type": "match",
   "say": T("🏁 <b>Desafío final del Nivel 7.</b> Problema → herramienta.", "🏁 <b>Level 7 final challenge.</b> Problem → tool."),
   "title": T("Desafío: el guardián de la plataforma", "Challenge: the platform guardian"),
   "pairs": [
     [T("Alguien cambió un notebook en producción y nadie sabe qué hizo", "Someone changed a production notebook and nobody knows what they did"), T("Integración con Git", "Git integration")],
     [T("Pasar cambios probados de Test a Prod", "Move tested changes from Test to Prod"), "Deployment pipeline"],
     [T("El mismo pipeline debe leer un Lakehouse distinto por ambiente", "The same pipeline must read a different Lakehouse per environment"), "Variable library"],
     [T("Saber qué reportes se rompen si borro una tabla", "Know which reports break if I drop a table"), T("Linaje / análisis de impacto", "Lineage / impact analysis")],
     [T("Encontrar qué está saturando la capacidad", "Find what's saturating the capacity"), "Capacity Metrics app"]]},
  {"type": "quiz",
   "say": T("La pregunta final del nivel. Piensa como líder técnico. 🎓", "The level's final question. Think like a tech lead. 🎓"),
   "q": T("Te contratan para ordenar la plataforma Fabric de una empresa con 30 workspaces, sin control de versiones y con cambios directos en producción. ¿Por dónde empiezas?",
          "You're hired to tidy up a company's Fabric platform: 30 workspaces, no version control and direct changes in production. Where do you start?"),
   "opts": [
     opt(T("Borrar todo y empezar desde cero", "Delete everything and start from scratch"), T("Rompes la operación del negocio. Nunca.", "You break the business. Never.")),
     opt(T("Inventario con linaje y Capacity Metrics, conectar los workspaces críticos a Git, separar Dev/Test/Prod con deployment pipelines y aplicar roles de mínimo privilegio",
           "Inventory with lineage and Capacity Metrics, connect critical workspaces to Git, separate Dev/Test/Prod with deployment pipelines and apply least-privilege roles"),
         T("¡Plan de nivel profesional! Primero entiendes y aseguras lo que hay; después ordenas el ciclo de vida, sin detener la operación. 🏆", "A professional-grade plan! First you understand and secure what exists; then you organize the lifecycle, without stopping operations. 🏆"), True),
     opt(T("Comprar la capacidad más grande para que nada falle", "Buy the biggest capacity so nothing fails"), T("No resuelve gobierno, seguridad ni trazabilidad.", "It doesn't solve governance, security or traceability."))]}
 ]})

out = {"id": 7,
       "title": T("Gobierno, seguridad y CI/CD", "Governance, security and CI/CD"),
       "desc": T("Dominios, endosos, linaje, seguridad por capas, OneLake security, Git, deployment pipelines, variable libraries y monitoreo.", "Domains, endorsement, lineage, layered security, OneLake security, Git, deployment pipelines, variable libraries and monitoring."),
       "lessons": L}
dst = pathlib.Path(__file__).resolve().parent.parent / "content/level-7.json"
dst.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", dst, sum(len(l["steps"]) for l in L), "steps")
