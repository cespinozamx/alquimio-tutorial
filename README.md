# Alquimio · Tutor de Microsoft Fabric

Sitio estático (HTML + CSS + JS + JSON). No necesita backend ni compilación.

```
site/
├── index.html            ← cascarón de la página
├── assets/
│   ├── app.css           ← estilos (paleta, tipografía, mascota)
│   └── app.js            ← motor: mascota, rutas, ejercicios, XP, visuales
└── content/
    ├── course.json       ← índice de niveles (qué existe y en qué orden)
    ├── level-1.json      ← Nivel 1 · Fundamentos
    ├── level-2.json      ← Nivel 2 · Ingesta
    ├── level-3.json      ← Nivel 3 · Spark y Notebooks
    ├── level-4.json      ← Nivel 4 · Data Warehouse y T-SQL
    ├── level-5.json      ← Nivel 5 · Real-Time Intelligence
    ├── level-6.json      ← Nivel 6 · Modelado semántico y Direct Lake
    ├── level-7.json      ← Nivel 7 · Gobierno, seguridad y CI/CD
    └── level-8.json      ← Nivel 8 · Proyecto final + examen
```

## Probar en tu computadora

El contenido se carga con `fetch`, así que **no funciona abriendo el archivo con doble clic** (file://). Usa un servidor local:

```bash
cd site
python -m http.server 8000
# abre http://localhost:8000
```

## Publicar

Sube la carpeta `site/` tal cual a cualquier hosting estático: GitHub Pages, Azure Static Web Apps, Netlify o un bucket con sitio web estático.

Este repositorio publica en Azure Static Web Apps mediante GitHub Actions al
subir cambios a `main`. El workflow usa `app_location: "/"`,
`skip_app_build: true` y `output_location: ""`: no instala paquetes ni compila
el sitio. El token de despliegue se mantiene en GitHub Secrets y el workflow
solicita un token OIDC de GitHub para la política de autenticación del recurso.

## Agregar un nivel

1. Crea `content/level-3.json` con la misma forma que `level-2.json`.
2. En `course.json`, cambia el nivel 3 de `"locked": true` a `"file": "level-3.json"`.

El progreso de cada alumno se guarda por `id` de lección (`l3-1`, `l3-2`…). **No cambies los `id` de lecciones ya publicadas**, porque los alumnos perderían su avance en esas lecciones.

## Textos bilingües

Cualquier texto puede ser:
- un objeto `{"es": "…", "en": "…"}`, o
- una cadena simple, si es igual en los dos idiomas (por ejemplo, código).

Se permite HTML básico: `<b>`, `<i>`, `<code>`, `<ul><li>`, `<span class="hl">` (resaltador amarillo).

## Estructura de una lección

```json
{
  "id": "l3-1",
  "icon": "🐍",
  "min": 20,
  "badge": { "e": "🪄", "n": {"es": "Nombre insignia", "en": "Badge name"} },
  "title": {"es": "…", "en": "…"},
  "steps": [ … ]
}
```

## Tipos de paso (`type`)

Todos aceptan `say`: lo que dice Alquimio al llegar al paso.

| type | Para qué | Campos |
|---|---|---|
| `story` / `concept` | Explicar (pasivo) | `kicker`, `title`, `body`, `cards`, `visual`, `svg`, `callouts` |
| `quiz` | Opción múltiple con explicación por opción | `q`, `opts: [{t, why, ok}]` (una con `"ok": 1`) |
| `match` | Relacionar parejas | `title`, `pairs: [[izq, der], …]` (se barajan solas) |
| `order` | Ordenar pasos | `title`, `items` **en el orden correcto** (se barajan solos) |
| `fill` | Completar código | `title`, `code` con huecos `{{0}}`, `{{1}}`…, `blanks: [{a: ["respuesta"], hint}]` |
| `reveal` | Pensar y luego revelar | `kind` (`brain` o `pencil`), `prompt`, `answer` |
| `lab` | Laboratorio con casillas | `title`, `intro`, `tasks: [{t, code?, solution?}]`, `expect` (`solution` se muestra oculta, para retos) |

### Recuadros Head First (`callouts`)

```json
"callouts": [
  {"k": "key",    "b": {"es": "…", "en": "…"}},
  {"k": "watch",  "b": {"es": "…", "en": "…"}},
  {"k": "brain",  "b": {"es": "…", "en": "…"}},
  {"k": "pencil", "b": {"es": "…", "en": "…"}},
  {"k": "nodumb", "qa": [{"q": {…}, "a": {…}}]}
]
```

`key` = Punto clave · `watch` = ¡Cuidado! · `brain` = Poder cerebral · `pencil` = Afila tu lápiz · `nodumb` = No hay preguntas tontas.

### Tarjetas (`cards`)

```json
"cards": [{"e": "⚙️", "n": "Data Engineering", "d": {"es": "…", "en": "…"}, "star": true}]
```

### Visuales

- `"visual": "medallion"` usa un diagrama ya incluido en `app.js`: `beforeAfter`, `hierarchy`, `medallion`, `ingestMap`, `pipelineFlow`, `watermark`, `sparkCluster`, `mergeFlow`, `deltaLog`, `whVsLh`, `starSchema`, `storageModes`, `directLakeFlow`, `govCity`, `securityLayers`, `gitFlow`, `deployFlow`, `rtiFlow`, `windows`, `lambdaArch`, `capstoneArch`.
- `"svg": "<svg viewBox='…'>…</svg>"` inserta tu propio SVG. Puede ser bilingüe: `{"es": "<svg…>", "en": "<svg…>"}`.

## XP

| Acción | XP |
|---|---|
| Quiz | 20 al primer intento · 10 al segundo · 5 después |
| match, order, fill | 30, menos 5 por error (mínimo 10) |
| reveal | 10 |
| lab | 40 |
| Lección terminada | 50 |

Los rangos están en `RANKS`, dentro de `app.js`.

## Certificado

La ruta `#certificado` se desbloquea cuando el alumno completa **todas** las lecciones publicadas. El alumno escribe su nombre, ve su certificado y puede copiar un texto para LinkedIn. El botón **Descargar PNG** solo aparece cuando el sitio se abre directamente, no dentro de un iframe. El código del certificado es un identificador de cortesía, no una verificación criptográfica.
