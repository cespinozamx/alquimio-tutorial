/* =========================================================
   1) i18n + estado
   ========================================================= */
const T = (es, en) => ({ es, en });
const KEY = "alquimio-fabric-v1";
function load() { try { return JSON.parse(localStorage.getItem(KEY)) || null; } catch (e) { return null; } }
function save() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} }
const S = Object.assign({
  lang: (navigator.language || "es").toLowerCase().startsWith("es") ? "es" : "en",
  xp: 0, done: {}, awarded: {}, dock: "open"
}, load() || {});
const tr = x => (x && typeof x === "object" && "es" in x) ? x[S.lang] : (x || "");
const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

const UI = {
  tagline: T("Tutor de datos", "Data tutor"),
  heroTitle: T(`Aprende <span class="mark">Microsoft Fabric</span> con un mago que no te deja dormir`, `Learn <span class="mark">Microsoft Fabric</span> with a wizard who won't let you nod off`),
  heroLead: T("Ingeniería de Datos explicada al estilo Head First: historias, analogías, ejercicios que te hacen pensar y laboratorios paso a paso. Gratis, en español e inglés.",
              "Data Engineering explained Head First style: stories, analogies, exercises that make you think, and step-by-step labs. Free, in Spanish and English."),
  heroSay: T("¡Hola! Soy <b>Alquimio</b>, alquimista de datos. Convierto datos crudos en oro… y te voy a enseñar a hacerlo. Haz clic en mí cuando necesites una pista.",
             "Hi! I'm <b>Alquimio</b>, a data alchemist. I turn raw data into gold… and I'll teach you how. Click me whenever you need a hint."),
  start: T("Comenzar el Nivel 1", "Start Level 1"),
  cont: T("Continuar donde me quedé", "Pick up where I left off"),
  handNote: T("← empieza aquí, sin saber nada", "← start here, zero experience needed"),
  xp: T("XP", "XP"), lessonsDone: T("lecciones completadas", "lessons completed"), badges: T("insignias", "badges"), rankLbl: T("rango actual", "current rank"),
  path: T("Tu ruta de aprendizaje", "Your learning path"),
  pathSub: T("De lo elemental a lo complejo. Cada nivel desbloquea una insignia.", "From the basics to the advanced. Every level unlocks a badge."),
  level: T("Nivel", "Level"), min: T("min", "min"), done: T("¡Hecha!", "Done!"), next: T("Siguiente", "Next up"),
  soon: T("Próximamente", "Coming soon"),
  step: T("Paso", "Step"), of: T("de", "of"),
  back: T("← Anterior", "← Back"), fwd: T("Siguiente →", "Next →"), finish: T("Terminar lección ✓", "Finish lesson ✓"),
  home: T("Ruta", "Path"),
  check: T("Revisar", "Check"), reveal: T("Revelar respuesta", "Reveal answer"), thinkPh: T("Escribe tu idea aquí antes de revelar…", "Jot your idea here before revealing…"),
  copy: T("Copiar", "Copy"), copied: T("¡Copiado!", "Copied!"),
  lessonComplete: T("¡Lección completada!", "Lesson complete!"),
  earned: T("Ganaste", "You earned"), badgeGot: T("Nueva insignia", "New badge"),
  nextLesson: T("Siguiente lección →", "Next lesson →"), backPath: T("Volver a la ruta", "Back to path"),
  certTitle: T("Tu certificado de finalización", "Your certificate of completion"),
  certCard: T("Completa todas las lecciones y el examen final para obtener tu certificado de finalización.", "Complete every lesson and the final exam to earn your certificate of completion."),
  certView: T("Ver mi certificado 🎓", "View my certificate 🎓"), certProgress: T("Progreso hacia el certificado", "Progress toward the certificate"),
  certLocked: T("Aún te faltan estas lecciones:", "You still need these lessons:"),
  certName: T("Escribe tu nombre como quieres que aparezca", "Type your name as you want it to appear"),
  certCopy: T("Copiar texto para LinkedIn", "Copy text for LinkedIn"), certPng: T("Descargar PNG", "Download PNG"),
  certNote: T("Este es un certificado de finalización de un curso gratuito e independiente. No es una certificación oficial de Microsoft.", "This is a certificate of completion for a free, independent course. It is not an official Microsoft certification."),
  certShot: T("Tip: si el botón de descarga no aparece aquí, toma una captura de pantalla del certificado o ábrelo desde el sitio publicado.", "Tip: if the download button doesn't show here, take a screenshot of the certificate or open it from the published site."),
  levelDone: T("¡Completaste el Nivel {n}! Insignia de nivel desbloqueada.", "You finished Level {n}! Level badge unlocked."),
  allDone: T("¡Completaste todo lo publicado hasta ahora! Pronto llegan más niveles.", "You've finished everything published so far! More levels are coming soon."),
  loadErr: T("No pude cargar el contenido del curso.", "I couldn't load the course content."),
  loadHelp: T("Si abriste el archivo directamente (file://), sírvelo con un servidor local, por ejemplo: <code>python -m http.server</code> dentro de la carpeta del sitio.", "If you opened the file directly (file://), serve it with a local web server, e.g. <code>python -m http.server</code> inside the site folder."),
  reset: T("Reiniciar mi progreso", "Reset my progress"), sure: T("¿Seguro? Se borrará tu XP.", "Sure? Your XP will be erased."), yes: T("Sí, borrar", "Yes, erase"), no: T("Cancelar", "Cancel"),
  footer: T("Contenido educativo gratuito e independiente. Microsoft Fabric es una marca de Microsoft; este sitio no está afiliado a Microsoft.", "Free, independent educational content. Microsoft Fabric is a Microsoft trademark; this site is not affiliated with Microsoft."),
  hideWiz: T("Ocultar a Alquimio", "Hide Alquimio"), showWiz: T("Mostrar a Alquimio", "Show Alquimio"),
  tasksLeft: T("Marca cada paso cuando lo hayas hecho en Fabric.", "Tick each step once you've done it in Fabric."),
  matchHelp: T("Haz clic en un elemento de la izquierda y luego en su pareja de la derecha.", "Click an item on the left, then its partner on the right."),
  orderHelp: T("Usa las flechas para ordenar y luego revisa.", "Use the arrows to reorder, then check."),
  fillHelp: T("Escribe lo que falta en cada hueco amarillo.", "Type what's missing in each yellow blank."),
  cl: { key: T("Punto clave", "Key point"), brain: T("Poder cerebral", "Brain power"), watch: T("¡Cuidado!", "Watch it!"), pencil: T("Afila tu lápiz", "Sharpen your pencil"), nodumb: T("No hay preguntas tontas", "There are no dumb questions") }
};
const PRAISE = [
  T("¡Exacto! Eso es pensar como ingeniero de datos. ✨", "Exactly! That's thinking like a data engineer. ✨"),
  T("¡Bingo! Tu cerebro acaba de guardar eso en Delta. 🧠", "Bingo! Your brain just saved that in Delta. 🧠"),
  T("¡Perfecto! Convertiste plomo en oro. 🪄", "Perfect! You turned lead into gold. 🪄"),
  T("¡Muy bien! Sigue así, aprendiz.", "Well done! Keep it up, apprentice.")
];
const OOPS = [T("Casi… lee la explicación y vuelve a intentarlo.", "Almost… read the explanation and try again."), T("Hmm, ese hechizo no funcionó. Otra vez.", "Hmm, that spell fizzled. Try again.")];
const RANKS = [[0, T("Aprendiz", "Apprentice")], [150, T("Iniciado", "Initiate")], [400, T("Alquimista", "Alchemist")], [700, T("Hechicero de Datos", "Data Sorcerer")], [1100, T("Maestro de Pipelines", "Pipeline Master")], [1600, T("Archimago", "Archmage")], [2100, T("Gran Alquimista de Datos", "Grand Data Alchemist")], [2700, T("Archimago del Warehouse", "Warehouse Archmage")], [3300, T("Gran Maestro Alquimista", "Grand Master Alchemist")], [4000, T("Guardián Supremo de la Plataforma", "Supreme Platform Guardian")], [4700, T("Archimago del Tiempo Real", "Real-Time Archmage")], [5300, T("Alquimista de Datos Legendario", "Legendary Data Alchemist")]];
const rank = () => RANKS.filter(r => S.xp >= r[0]).pop()[1];
const pick = a => a[Math.floor(Math.random() * a.length)];

/* =========================================================
   2) Mascota original: Alquimio
   ========================================================= */
let wizN = 0;
function wizardSVG(noFx) {
  const p = "w" + (++wizN);
  return `<svg class="wiz" viewBox="0 0 200 250" aria-hidden="true">
  <defs>
    <radialGradient id="${p}g"><stop offset="0" stop-color="#fff6cf"/><stop offset=".45" stop-color="#ffb547" stop-opacity=".9"/><stop offset="1" stop-color="#ffb547" stop-opacity="0"/></radialGradient>
    <linearGradient id="${p}r" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#138080"/><stop offset="1" stop-color="#0a4c4d"/></linearGradient>
    <linearGradient id="${p}h" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#11706f"/><stop offset="1" stop-color="#073a3b"/></linearGradient>
  </defs>
  <ellipse cx="100" cy="242" rx="58" ry="7" fill="#000" opacity=".13"/>
  <g class="wz-all">
    <g class="wz-staff">
      <line x1="40" y1="70" x2="48" y2="234" stroke="#7a4a26" stroke-width="6" stroke-linecap="round"/>
      <circle class="gem-glow" cx="38" cy="58" r="24" fill="url(#${p}g)"/>
      <polygon points="38,43 49,51 49,65 38,73 27,65 27,51" fill="#ffc861" stroke="#a8661b" stroke-width="2"/>
      <polygon points="38,43 49,51 38,57 27,51" fill="#fff2bf"/>
      <line x1="38" y1="57" x2="38" y2="73" stroke="#a8661b" stroke-width="1.5"/>
    </g>
    <path d="M64 118 Q100 104 136 118 L166 234 Q100 246 34 234 Z" fill="url(#${p}r)"/>
    <path d="M34 234 Q100 246 166 234" stroke="#c46f35" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path d="M100 150 L100 240" stroke="#c46f35" stroke-width="4"/>
    <g stroke="#8fe0d2" stroke-width="1.4" opacity=".85" fill="none"><path d="M66 178 L80 196 L72 216 M80 196 L90 208"/><path d="M118 172 L132 190 L124 214 M132 190 L146 200"/></g>
    <g fill="#ffd77a"><circle cx="66" cy="178" r="2.6"/><circle cx="80" cy="196" r="2.6"/><circle cx="72" cy="216" r="2.6"/><circle cx="90" cy="208" r="2.2"/><circle cx="118" cy="172" r="2.6"/><circle cx="132" cy="190" r="2.6"/><circle cx="124" cy="214" r="2.6"/><circle cx="146" cy="200" r="2.2"/></g>
    <g class="wz-arm-l"><path d="M74 124 Q52 134 40 156 L54 166 Q64 148 82 140 Z" fill="#0c5a5a"/><circle cx="46" cy="160" r="8" fill="#f2c39b"/></g>
    <g class="wz-arm-r"><path d="M126 124 Q150 134 162 158 L148 167 Q138 148 118 140 Z" fill="#0c5a5a"/><circle cx="156" cy="162" r="8" fill="#f2c39b"/></g>
    <g class="wz-top">
      <circle cx="100" cy="92" r="30" fill="#f2c39b"/>
      <circle cx="78" cy="101" r="5" fill="#ef9f86" opacity=".55"/><circle cx="122" cy="101" r="5" fill="#ef9f86" opacity=".55"/>
      <path d="M70 96 Q70 140 100 160 Q130 140 130 96 Q118 113 100 113 Q82 113 70 96 Z" fill="#fbfaf4" stroke="#ddd6c7" stroke-width="1.5"/>
      <ellipse class="wz-mouth" cx="100" cy="118" rx="6" ry="3.2" fill="#7a3b2e"/>
      <path d="M83 107 Q92 100 100 106 Q108 100 117 107 Q108 113 100 109 Q92 113 83 107 Z" fill="#fff" stroke="#ddd6c7" stroke-width="1.2"/>
      <ellipse cx="100" cy="98" rx="6" ry="5" fill="#e6a684"/>
      <g class="wz-eyes" fill="#1d2330"><circle cx="88" cy="86" r="3.3"/><circle cx="112" cy="86" r="3.3"/><circle cx="89.2" cy="84.8" r="1" fill="#fff"/><circle cx="113.2" cy="84.8" r="1" fill="#fff"/></g>
      <g fill="none" stroke="#3a2a1f" stroke-width="2.2"><circle cx="88" cy="86" r="8.5"/><circle cx="112" cy="86" r="8.5"/><path d="M96.5 85 h7"/></g>
      <path d="M78 74 Q88 68 96 74 M104 74 Q112 68 122 74" stroke="#fff" stroke-width="5" stroke-linecap="round" fill="none"/>
      <ellipse cx="100" cy="66" rx="46" ry="9" fill="#073a3b"/>
      <path d="M62 66 C78 44 88 24 104 12 C112 6 122 4 132 10 C120 12 114 18 112 26 C118 40 128 54 138 66 Z" fill="url(#${p}h)"/>
      <path d="M64 60 Q100 50 136 60 L138 66 Q100 57 62 66 Z" fill="#e3a234"/>
      <g stroke="#8fe0d2" stroke-width="1.3" fill="none"><path d="M90 44 L101 32 L114 42 L104 52 Z"/></g>
      <g fill="#ffd77a"><circle cx="90" cy="44" r="2.4"/><circle cx="101" cy="32" r="2.4"/><circle cx="114" cy="42" r="2.4"/><circle cx="104" cy="52" r="2.4"/></g>
      <path d="M132 10 l3 -6 l2 6 l6 2 l-6 2 l-2 6 l-3 -6 l-6 -2 Z" fill="#ffd77a"/>
    </g>
    ${noFx ? "" : `<g class="wz-dots" fill="#fff" stroke="#1d2330" stroke-width="1.5"><circle cx="150" cy="70" r="4"/><circle cx="162" cy="56" r="5.5"/><circle cx="176" cy="38" r="7.5"/></g>`}
  </g>
  ${noFx ? "" : `  <g fill="#ffc861" stroke="#a8661b" stroke-width="1">
    <path class="wz-spark" d="M20 110 l4 -9 l4 9 l9 4 l-9 4 l-4 9 l-4 -9 l-9 -4 Z"/>
    <path class="wz-spark" style="animation-delay:.2s" d="M176 104 l3 -7 l3 7 l7 3 l-7 3 l-3 7 l-3 -7 l-7 -3 Z"/>
    <path class="wz-spark" style="animation-delay:.35s" d="M160 24 l3 -6 l3 6 l6 3 l-6 3 l-3 6 l-3 -6 l-6 -3 Z"/>
    <path class="wz-spark" style="animation-delay:.1s" d="M14 30 l3 -6 l3 6 l6 3 l-6 3 l-3 6 l-3 -6 l-6 -3 Z"/>
  </g>`}
</svg>`;
}

const M = { el: null, bubble: null, text: null, timers: [] };
function bindMascot(el, bubble, text) { M.el = el; M.bubble = bubble; M.text = text; }
function mood(m, ms = 1900) {
  if (!M.el) return;
  M.el.classList.remove("happy", "think", "oops");
  void M.el.offsetWidth;
  if (m) { M.el.classList.add(m); M.timers.push(setTimeout(() => M.el.classList.remove(m), ms)); }
}
function say(html, m) {
  if (!M.el) return;
  M.timers.forEach(clearTimeout); M.timers = [];
  M.text.innerHTML = html;
  if (M.bubble.classList) M.bubble.classList.add("show");
  M.el.classList.add("talk");
  const plain = html.replace(/<[^>]+>/g, "");
  M.timers.push(setTimeout(() => M.el.classList.remove("talk"), Math.min(4500, 600 + plain.length * 32)));
  if (m) mood(m, m === "think" ? 3500 : 1900);
  if (M.bubble.id === "bubble" && innerWidth < 760) M.timers.push(setTimeout(() => M.bubble.classList.remove("show"), Math.max(5000, plain.length * 70)));
}

/* =========================================================
   3) Visuales (SVG bilingües)
   ========================================================= */
const box = (x, y, w, h, fill, label, sub, fs = 14) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="10" fill="${fill}" stroke="#1d2330" stroke-width="2"/>
  <text x="${x + w / 2}" y="${y + (sub ? h / 2 - 3 : h / 2 + 5)}" text-anchor="middle" font-size="${fs}" font-weight="700">${label}</text>${sub ? `<text x="${x + w / 2}" y="${y + h / 2 + 15}" text-anchor="middle" font-size="12" fill="#5d6372">${sub}</text>` : ""}`;
const arrow = (d, c = "#1d2330") => `<path d="${d}" stroke="${c}" stroke-width="2.5" fill="none" marker-end="url(#ah)"/>`;
const DEFS = `<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#1d2330"/></marker></defs>`;
const VIS = {
  capstoneArch: () => `<svg viewBox="0 0 680 330">${DEFS}
    <text x="340" y="24" text-anchor="middle" font-size="16" font-weight="800">🚲 BiciCiudad · ws_biciudad_dev</text>
    ${box(14, 60, 120, 56, "#fff", "📄 rentas.csv", tr(T("diario", "daily")))}
    ${box(160, 60, 120, 56, "#e9f5f3", "🏭 lh_bici", tr(T("Bronce → Plata", "Bronze → Silver")))}
    ${box(306, 60, 120, 56, "#f1ecff", "🏛️ wh_bici", tr(T("Oro · estrella", "Gold · star")))}
    ${box(452, 60, 120, 56, "#fff8d6", "🧩 sm_biciudad", "Direct Lake · RLS")}
    ${box(590, 60, 78, 56, "#fff", "📊", "rpt")}
    ${arrow("M134 88 H154")}${arrow("M280 88 H300")}${arrow("M426 88 H446")}${arrow("M572 88 H584")}
    <text x="220" y="138" text-anchor="middle" font-size="11" fill="#5d6372">nb_rentas_silver · MERGE</text>
    <text x="366" y="138" text-anchor="middle" font-size="11" fill="#5d6372">usp_cargar_rentas</text>
    <rect x="150" y="146" width="290" height="26" rx="8" fill="#fff" stroke="#0e6b6b" stroke-width="1.5" stroke-dasharray="5 4"/><text x="295" y="164" text-anchor="middle" font-size="12" fill="#0e6b6b">🧭 pl_bici_diario</text>
    ${box(14, 210, 120, 56, "#fff", "📟 " + tr(T("Estaciones", "Stations")), "Bicycles")}
    ${box(160, 210, 120, 56, "#fbe6e3", "🌊 es_estaciones", "Eventstream")}
    ${box(306, 210, 120, 56, "#fbe6e3", "🏠 eh_bici", "KQL")}
    ${box(452, 190, 216, 40, "#fff", "📺 rtd_biciudad", "", 13)}${box(452, 244, 216, 40, "#fbe6e3", "🚨 act_logistica → " + tr(T("correo", "email")), "", 12)}
    ${arrow("M134 238 H154")}${arrow("M280 238 H300")}${arrow("M426 230 L446 212")}${arrow("M426 246 L446 262")}
    <path d="M366 210 V122" stroke="#c46f35" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#ah)"/><text x="374" y="190" font-size="11" fill="#c46f35">OneLake</text>
    <text x="14" y="318" class="hw" font-size="19" fill="#0e6b6b">${tr(T("🐙 todo versionado en Git: biciudad-fabric", "🐙 everything versioned in Git: biciudad-fabric"))}</text>
  </svg>`,
  rtiFlow: () => `<svg viewBox="0 0 680 250">${DEFS}
    ${box(14, 70, 110, 70, "#fff", "📟 " + tr(T("Fuentes", "Sources")), "IoT · Event Hubs")}
    ${box(150, 70, 120, 70, "#e9f5f3", "🌊 Eventstream", tr(T("captura y enruta", "capture & route")))}
    ${box(296, 70, 120, 70, "#fff8d6", "🏠 Eventhouse", "KQL")}
    ${box(450, 14, 216, 56, "#fff", "📺 Real-Time Dashboard", tr(T("se refresca solo", "auto-refresh")))}
    ${box(450, 84, 216, 56, "#fbe6e3", "🚨 Activator", tr(T("correo · Teams · pipeline", "email · Teams · pipeline")))}
    ${box(450, 154, 216, 56, "#f1ecff", "🌊 OneLake (Delta)", tr(T("Spark · SQL · Power BI", "Spark · SQL · Power BI")))}
    ${arrow("M124 105 H144")}${arrow("M270 105 H290")}
    <path d="M416 95 C432 60 432 44 444 42" stroke="#1d2330" stroke-width="2.5" fill="none" marker-end="url(#ah)"/>
    ${arrow("M416 108 H444")}
    <path d="M416 120 C432 150 432 180 444 182" stroke="#1d2330" stroke-width="2.5" fill="none" marker-end="url(#ah)"/>
    <text x="20" y="40" class="hw" font-size="19" fill="#c46f35">📡 Real-Time hub</text>
    <text x="20" y="238" class="hw" font-size="19" fill="#0e6b6b">${tr(T("segundos entre el evento y la acción", "seconds between event and action"))}</text>
  </svg>`,
  windows: () => { const row = (y, label, segs, c) => `<text x="14" y="${y + 20}" font-size="13" font-weight="700">${label}</text>
      ${segs.map(([a, b, dy]) => `<rect x="${120 + a * 5.2}" y="${y + (dy || 0)}" width="${(b - a) * 5.2 - 4}" height="22" rx="6" fill="${c}" stroke="#1d2330" stroke-width="1.5" opacity=".85"/>`).join("")}`;
    const ev = [8, 14, 22, 31, 37, 52, 55, 58, 71, 86, 90, 94];
    return `<svg viewBox="0 0 680 300">
    <line x1="120" y1="40" x2="660" y2="40" stroke="#1d2330" stroke-width="2"/>
    ${ev.map(t => `<circle cx="${120 + t * 5.2}" cy="40" r="5" fill="#c46f35"/>`).join("")}
    <text x="14" y="45" font-size="13" font-weight="700">${tr(T("eventos", "events"))}</text>
    ${row(70, "Tumbling", [[0, 25], [25, 50], [50, 75], [75, 100]], "#9fe3d6")}
    ${row(120, "Hopping", [[0, 50, 0], [25, 75, 14], [50, 100, 0]], "#ffe680")}
    ${row(182, "Sliding", [[17, 37], [41, 61], [70, 90]], "#d9ccff")}
    ${row(232, "Session", [[6, 40], [50, 60], [69, 97]], "#ffc9b8")}
    <text x="340" y="292" text-anchor="middle" class="hw" font-size="18" fill="#5d6372">${tr(T("tiempo →", "time →"))}</text>
  </svg>`; },
  lambdaArch: () => `<svg viewBox="0 0 680 270">${DEFS}
    ${box(14, 100, 120, 64, "#fff", "🏭 " + tr(T("Fuentes", "Sources")), tr(T("sensores · ERP", "sensors · ERP")))}
    <text x="200" y="40" font-size="14" font-weight="700" fill="#c2473b">⚡ ${tr(T("Ruta rápida (segundos)", "Fast path (seconds)"))}</text>
    ${box(170, 50, 140, 50, "#fbe6e3", "Eventstream", "→ Eventhouse", 13)}${box(340, 50, 150, 50, "#fbe6e3", "Activator", "+ Real-Time Dashboard", 13)}
    <text x="200" y="250" font-size="14" font-weight="700" fill="#0e6b6b">🐢 ${tr(T("Ruta completa (horas)", "Complete path (hours)"))}</text>
    ${box(170, 168, 140, 56, "#e9f5f3", tr(T("Lakehouse · notebooks", "Lakehouse · notebooks")), tr(T("Bronce → Plata", "Bronze → Silver")), 12)}${box(340, 168, 150, 56, "#e9f5f3", tr(T("Warehouse · Oro", "Warehouse · Gold")), tr(T("modelo estrella", "star schema")), 12)}
    ${box(530, 100, 136, 64, "#fff8d6", "📊 " + tr(T("Consumo", "Consumption")), tr(T("Power BI · IA", "Power BI · AI")))}
    ${arrow("M134 120 C150 90 152 76 164 76")}${arrow("M134 145 C150 176 152 196 164 196")}
    ${arrow("M310 75 H334")}${arrow("M310 196 H334")}
    ${arrow("M490 75 C512 80 516 100 524 112")}${arrow("M490 196 C512 190 516 166 524 152")}
    <path d="M240 100 V162" stroke="#c46f35" stroke-width="2.5" stroke-dasharray="6 4" marker-end="url(#ah)"/><text x="248" y="136" font-size="11" fill="#c46f35">OneLake</text>
  </svg>`,
  govCity: () => `<svg viewBox="0 0 680 280">
    ${[[20, "🏘️ " + tr(T("Dominio Comercial", "Sales domain")), "#e9f5f3", ["ws_ventas", "ws_marketing"]], [350, "🏘️ " + tr(T("Dominio Finanzas", "Finance domain")), "#f1ecff", ["ws_contabilidad", "ws_tesoreria"]]].map(([x, n, c, ws]) =>
      `<rect x="${x}" y="14" width="310" height="180" rx="14" fill="${c}" stroke="#1d2330" stroke-width="2"/><text x="${x + 16}" y="40" font-size="15" font-weight="700">${n}</text>
       ${ws.map((w, i) => `<rect x="${x + 16 + i * 146}" y="56" width="132" height="120" rx="10" fill="#fff" stroke="#1d2330" stroke-width="1.5"/><text x="${x + 82 + i * 146}" y="78" text-anchor="middle" font-size="12" font-weight="700">${w}</text>
         <text x="${x + 82 + i * 146}" y="104" text-anchor="middle" font-size="12">${i === 0 ? "🏅 Certified" : "🏅 Promoted"}</text><text x="${x + 82 + i * 146}" y="128" text-anchor="middle" font-size="12">🏷️ ${i === 0 ? tr(T("Confidencial", "Confidential")) : tr(T("Interno", "Internal"))}</text>
         <text x="${x + 82 + i * 146}" y="152" text-anchor="middle" font-size="12">🧭 ${tr(T("linaje", "lineage"))}</text>`).join("")}`).join("")}
    <rect x="20" y="210" width="640" height="48" rx="12" fill="#fff8d6" stroke="#1d2330" stroke-width="2"/>
    <text x="340" y="240" text-anchor="middle" font-size="14" font-weight="700">🔎 Microsoft Purview · OneLake catalog · ${tr(T("gobierno de todo el tenant", "tenant-wide governance"))}</text>
  </svg>`,
  securityLayers: () => { const layers = [["#1d2330", "#fff", T("1 · Identidad: Entra ID, MFA, acceso condicional", "1 · Identity: Entra ID, MFA, conditional access")], ["#0e6b6b", "#fff", T("2 · Roles de workspace", "2 · Workspace roles")], ["#138686", "#fff", T("3 · Permisos por elemento", "3 · Item permissions")], ["#e3a234", "#1d2330", T("4 · OneLake security (tablas, filas, columnas)", "4 · OneLake security (tables, rows, columns)")], ["#f2c76b", "#1d2330", T("5 · Motor: SQL GRANT/RLS · RLS del modelo", "5 · Engine: SQL GRANT/RLS · model RLS")]];
    return `<svg viewBox="0 0 680 320">${layers.map(([c, tc, t], i) => `<rect x="${20 + i * 34}" y="${14 + i * 30}" width="${640 - i * 68}" height="${290 - i * 50}" rx="${22 - i * 2}" fill="${c}" stroke="#1d2330" stroke-width="1.5"/>
      <text x="${38 + i * 34}" y="${36 + i * 30}" font-size="13" font-weight="700" fill="${tc}">${tr(t)}</text>`).join("")}
      <text x="340" y="190" text-anchor="middle" font-size="22">💎</text><text x="340" y="214" text-anchor="middle" font-size="14" font-weight="700">${tr(T("tus datos", "your data"))}</text>
      <rect x="420" y="276" width="240" height="34" rx="8" fill="#fbe6e3" stroke="#c2473b" stroke-width="2"/><text x="540" y="298" text-anchor="middle" font-size="12" font-weight="700" fill="#c2473b">🏷️ ${tr(T("6 · Etiquetas: viajan con el dato", "6 · Labels: travel with the data"))}</text>
    </svg>`; },
  gitFlow: () => `<svg viewBox="0 0 680 280">${DEFS}
    ${box(20, 40, 200, 150, "#e9f5f3", "", "")}<text x="120" y="66" text-anchor="middle" font-size="15" font-weight="700">🧪 ${tr(T("Workspace de Fabric", "Fabric workspace"))}</text>
    ${["📓 nb_ventas_medallion", "🧭 pl_ingesta_tutor", "🧩 sm_ventas", "📊 rpt_ventas"].map((n, i) => `<text x="40" y="${94 + i * 24}" font-size="12">${n}</text>`).join("")}
    ${box(460, 40, 200, 150, "#f4efe3", "", "")}<text x="560" y="66" text-anchor="middle" font-size="15" font-weight="700">🐙 ${tr(T("Repositorio Git", "Git repository"))}</text>
    ${[".Notebook/  → .py", ".DataPipeline/ → .json", ".SemanticModel/ → TMDL", ".Report/ → PBIR"].map((n, i) => `<text x="474" y="${94 + i * 24}" font-size="12" font-family="JetBrains Mono, monospace">${n}</text>`).join("")}
    <path d="M222 90 H452" stroke="#2f8f5b" stroke-width="3" marker-end="url(#ah)"/><text x="337" y="82" text-anchor="middle" font-size="13" font-weight="700" fill="#2f8f5b">Commit ⬆</text>
    <path d="M458 140 H228" stroke="#0e6b6b" stroke-width="3" marker-end="url(#ah)"/><text x="337" y="160" text-anchor="middle" font-size="13" font-weight="700" fill="#0e6b6b">⬇ Update</text>
    <line x1="470" y1="226" x2="660" y2="226" stroke="#1d2330" stroke-width="3"/><text x="470" y="216" font-size="12" font-weight="700">main</text>
    <path d="M500 226 C520 256 600 256 620 226" stroke="#c46f35" stroke-width="2.5" fill="none" stroke-dasharray="6 4"/><text x="560" y="266" text-anchor="middle" font-size="12" fill="#c46f35">feature/… → pull request</text>
    <text x="20" y="236" class="hw" font-size="19" fill="#c2473b">${tr(T("a Git van definiciones, ¡no datos!", "definitions go to Git, not data!"))}</text>
  </svg>`,
  deployFlow: () => `<svg viewBox="0 0 680 270">${DEFS}
    ${[["🛠️ Development", "ws_tutor_fabric", "#e9f5f3", "vl: lh_bronze_dev"], ["🧪 Test", "ws_tutor_fabric_test", "#fff8d6", "vl: lh_bronze_test"], ["🏭 Production", "ws_tutor_fabric_prod", "#e3f4e9", "vl: lh_bronze_prod"]].map(([n, w, c, v], i) => { const x = 20 + i * 225;
      return `${box(x, 40, 190, 110, c, "", "")}<text x="${x + 95}" y="70" text-anchor="middle" font-size="15" font-weight="700">${n}</text><text x="${x + 95}" y="96" text-anchor="middle" font-size="12" font-family="JetBrains Mono, monospace">${w}</text>
        <rect x="${x + 20}" y="110" width="150" height="26" rx="6" fill="#fff" stroke="#c46f35" stroke-width="1.5"/><text x="${x + 95}" y="128" text-anchor="middle" font-size="11" fill="#c46f35">${v}</text>
        ${i < 2 ? `<path d="M${x + 192} 95 H${x + 219}" stroke="#1d2330" stroke-width="3" marker-end="url(#ah)"/><text x="${x + 206}" y="84" text-anchor="middle" font-size="11" font-weight="700">Deploy</text>` : ""}`; }).join("")}
    <text x="340" y="190" text-anchor="middle" font-size="13">📦 ${tr(T("viajan: notebooks, pipelines, modelos, reportes, definiciones de Lakehouse", "travels: notebooks, pipelines, models, reports, Lakehouse definitions"))}</text>
    <text x="340" y="214" text-anchor="middle" font-size="13" fill="#c2473b">🚫 ${tr(T("no viajan: los datos de las tablas", "doesn't travel: table data"))}</text>
    <text x="340" y="252" text-anchor="middle" class="hw" font-size="19" fill="#0e6b6b">${tr(T("vl = variable library: el mismo pipeline, distintos valores por etapa", "vl = variable library: same pipeline, different values per stage"))}</text>
  </svg>`,
  storageModes: () => `<svg viewBox="0 0 680 290">${DEFS}
    <ellipse cx="340" cy="250" rx="300" ry="12" fill="#e3a234"/><rect x="40" y="250" width="600" height="26" fill="#e3a234"/><ellipse cx="340" cy="276" rx="300" ry="12" fill="#c98b1f"/>
    <text x="340" y="270" text-anchor="middle" font-size="14" font-weight="700">OneLake · ${tr(T("tablas Oro (Delta)", "Gold tables (Delta)"))}</text>
    ${[[30, "📥 Import", T("copia los datos", "copies the data"), "#fff"], [255, "🔁 DirectQuery", T("pregunta en cada clic", "asks on every click"), "#fff"], [480, "⚡ Direct Lake", T("lee Delta directo", "reads Delta directly"), "#fff8d6"]].map(([x, n, d, c], i) =>
      `${box(x, 100, 170, 64, c, n, tr(d))}
       ${i === 0 ? `<path d="M115 236 V172" stroke="#c46f35" stroke-width="3" stroke-dasharray="7 5" marker-end="url(#ah)"/><text x="125" y="214" font-size="12" fill="#c46f35">${tr(T("copia + refresh", "copy + refresh"))}</text>` : ""}
       ${i === 1 ? `<path d="M340 172 V236" stroke="#5d6372" stroke-width="2" marker-end="url(#ah)"/><path d="M352 236 V172" stroke="#5d6372" stroke-width="2" marker-end="url(#ah)"/><text x="362" y="214" font-size="12" fill="#5d6372">SQL</text>` : ""}
       ${i === 2 ? `<path d="M565 236 V172" stroke="#0e6b6b" stroke-width="4" marker-end="url(#ah)"/><text x="575" y="214" font-size="12" fill="#0e6b6b">${tr(T("sin copiar", "no copy"))}</text>` : ""}`).join("")}
    ${box(170, 14, 340, 50, "#e9f5f3", "🧩 " + tr(T("Modelo semántico", "Semantic model")), tr(T("relaciones · medidas · nombres · seguridad", "relationships · measures · names · security")))}
    ${arrow("M260 64 L140 96")}${arrow("M340 64 V96")}${arrow("M420 64 L540 96")}
  </svg>`,
  directLakeFlow: () => `<svg viewBox="0 0 680 270">${DEFS}
    ${box(20, 20, 190, 64, "#fff", "📊 " + tr(T("Visual del reporte", "Report visual")), tr(T("pide monto y region", "asks for monto and region")))}
    ${box(250, 20, 190, 64, "#fff8d6", "🧠 " + tr(T("Motor del modelo", "Model engine")), tr(T("¿ya están en memoria?", "already in memory?")))}
    ${box(480, 20, 180, 64, "#e3f4e9", "⚡ " + tr(T("Respuesta", "Answer")), tr(T("milisegundos", "milliseconds")))}
    ${arrow("M210 52 H244")}${arrow("M440 52 H474")}<text x="446" y="44" font-size="12" font-weight="700" fill="#2f8f5b">${tr(T("sí", "yes"))}</text>
    ${arrow("M345 84 V150")}<text x="353" y="124" font-size="12" font-weight="700" fill="#c46f35">${tr(T("no: carga solo esas columnas", "no: load just those columns"))}</text>
    <ellipse cx="345" cy="160" rx="200" ry="10" fill="#e3a234"/><rect x="145" y="160" width="400" height="32" fill="#e3a234"/><ellipse cx="345" cy="192" rx="200" ry="10" fill="#c98b1f"/>
    <text x="345" y="183" text-anchor="middle" font-size="13" font-weight="700">OneLake · fact_ventas ${tr(T("versión", "version"))} N</text>
    <text x="20" y="246" class="hw" font-size="19" fill="#0e6b6b">${tr(T("framing = mover el marco a la versión N+1 cuando llegan datos nuevos", "framing = moving the frame to version N+1 when new data lands"))}</text>
  </svg>`,
  whVsLh: () => `<svg viewBox="0 0 680 290">${DEFS}
    ${box(30, 20, 270, 150, "#e9f5f3", "", "")}
    <text x="165" y="48" text-anchor="middle" font-size="17" font-weight="700">🏭 Lakehouse</text>
    <text x="165" y="76" text-anchor="middle" font-size="13">📁 Files + 🗂 Tables</text>
    <text x="165" y="100" text-anchor="middle" font-size="13">${tr(T("escribes con Spark / pipelines", "write with Spark / pipelines"))}</text>
    <text x="165" y="124" text-anchor="middle" font-size="13">${tr(T("SQL endpoint: solo lectura", "SQL endpoint: read-only"))}</text>
    <text x="165" y="152" text-anchor="middle" class="hw" font-size="18" fill="#0e6b6b">${tr(T("el taller", "the workshop"))}</text>
    ${box(380, 20, 270, 150, "#f1ecff", "", "")}
    <text x="515" y="48" text-anchor="middle" font-size="17" font-weight="700">🏛️ Warehouse</text>
    <text x="515" y="76" text-anchor="middle" font-size="13">🗂 ${tr(T("solo tablas", "tables only"))}</text>
    <text x="515" y="100" text-anchor="middle" font-size="13">${tr(T("escribes con T-SQL completo", "write with full T-SQL"))}</text>
    <text x="515" y="124" text-anchor="middle" font-size="13">MERGE · ${tr(T("procedimientos · transacciones", "procedures · transactions"))}</text>
    <text x="515" y="152" text-anchor="middle" class="hw" font-size="18" fill="#6b4fbf">${tr(T("la biblioteca", "the library"))}</text>
    <path d="M300 95 H380" stroke="#c46f35" stroke-width="2.5" stroke-dasharray="6 4" marker-end="url(#ah)"/>
    <text x="340" y="86" text-anchor="middle" font-size="11" fill="#c46f35">${tr(T("lee con", "reads via"))}</text>
    <text x="340" y="116" text-anchor="middle" font-size="11" fill="#c46f35">lh.dbo.tabla</text>
    <ellipse cx="340" cy="222" rx="300" ry="14" fill="#e3a234"/><rect x="40" y="222" width="600" height="40" fill="#e3a234"/><ellipse cx="340" cy="262" rx="300" ry="14" fill="#c98b1f"/>
    <text x="340" y="250" text-anchor="middle" font-size="16" font-weight="700">OneLake · Delta Parquet</text>
    ${arrow("M165 170 V206")}${arrow("M515 170 V206")}
  </svg>`,
  starSchema: () => `<svg viewBox="0 0 680 352">
    <g stroke="#1d2330" stroke-width="2.5">
      <line x1="340" y1="165" x2="120" y2="60"/><line x1="340" y1="165" x2="560" y2="60"/>
      <line x1="340" y1="165" x2="120" y2="270"/><line x1="340" y1="165" x2="560" y2="270"/></g>
    ${box(250, 115, 180, 100, "#fff8d6", "", "")}
    <text x="340" y="140" text-anchor="middle" font-size="16" font-weight="700">⭐ fact_ventas</text>
    <text x="340" y="162" text-anchor="middle" font-size="12" font-family="JetBrains Mono, monospace">sk_fecha · sk_cliente</text>
    <text x="340" y="180" text-anchor="middle" font-size="12" font-family="JetBrains Mono, monospace">sk_producto</text>
    <text x="340" y="202" text-anchor="middle" font-size="13" font-weight="700" fill="#c46f35">monto 💲</text>
    ${[[30, 20, "📅 dim_fecha", T("¿cuándo?", "when?")], [470, 20, "👤 dim_cliente", T("¿quién? · región", "who? · region")], [30, 230, "📦 dim_producto", T("¿qué?", "what?")], [470, 230, "🏪 dim_tienda", T("¿dónde? (futuro)", "where? (future)")]].map(([x, y, n, d], i) =>
      `<rect x="${x}" y="${y}" width="180" height="80" rx="10" fill="${i === 3 ? "#fff" : "#e9f5f3"}" stroke="#1d2330" stroke-width="2" ${i === 3 ? 'stroke-dasharray="6 4"' : ""}/>
       <text x="${x + 90}" y="${y + 34}" text-anchor="middle" font-size="15" font-weight="700">${n}</text><text x="${x + 90}" y="${y + 58}" text-anchor="middle" font-size="13" fill="#5d6372">${tr(d)}</text>`).join("")}
    <text x="340" y="344" text-anchor="middle" class="hw" font-size="20" fill="#0e6b6b">${tr(T("hechos al centro (números), dimensiones alrededor (contexto)", "facts in the middle (numbers), dimensions around (context)"))}</text>
  </svg>`,
  sparkCluster: () => `<svg viewBox="0 0 680 290">${DEFS}
    ${box(250, 14, 180, 64, "#fff8d6", "👨‍🍳 Driver", tr(T("planea y reparte", "plans and hands out work")))}
    ${[0, 1, 2].map(i => { const x = 40 + i * 215; return `${arrow(`M340 78 C340 100 ${x + 85} 100 ${x + 85} 118`)}
      <rect x="${x}" y="120" width="170" height="120" rx="10" fill="#e9f5f3" stroke="#1d2330" stroke-width="2"/><text x="${x + 85}" y="150" text-anchor="middle" font-size="14" font-weight="700">🧑‍🍳 ${tr(T("Ejecutor", "Executor"))} ${i + 1}</text>
      ${[0, 1].map(j => `<rect x="${x + 16 + j * 74}" y="170" width="64" height="50" rx="8" fill="#fff" stroke="#c46f35" stroke-width="2"/><text x="${x + 48 + j * 74}" y="200" text-anchor="middle" font-size="12">P${i * 2 + j + 1}</text>`).join("")}`; }).join("")}
    <text x="20" y="278" class="hw" font-size="19" fill="#c46f35">${tr(T("P = partición: un pedazo de tus datos que un ejecutor procesa en paralelo", "P = partition: a slice of your data that an executor processes in parallel"))}</text>
  </svg>`,
  mergeFlow: () => `<svg viewBox="0 0 680 300">${DEFS}
    <text x="100" y="24" text-anchor="middle" font-size="14" font-weight="700">${tr(T("Fuente (cambios)", "Source (changes)"))}</text>
    ${[["2", "1050", "#fff8d6"], ["11", "520", "#e3f4e9"], ["12", "610", "#e3f4e9"]].map(([id, m, c], i) => box(30, 36 + i * 52, 140, 42, c, `id ${id} · ${m}`, "", 13)).join("")}
    ${box(250, 86, 160, 64, "#fff", "🔑 t.id = s.id", tr(T("¿existe la clave?", "does the key exist?")))}
    ${arrow("M170 108 H244")}
    <path d="M410 104 C450 104 450 60 486 60" stroke="#e3a234" stroke-width="3" fill="none" marker-end="url(#ah)"/>
    <path d="M410 132 C450 132 450 182 486 182" stroke="#2f8f5b" stroke-width="3" fill="none" marker-end="url(#ah)"/>
    ${box(490, 30, 170, 60, "#fff8d6", "✏️ UPDATE", tr(T("sí existe → id 2", "exists → id 2")))}
    ${box(490, 152, 170, 60, "#e3f4e9", "➕ INSERT", tr(T("no existe → ids 11, 12", "missing → ids 11, 12")))}
    <text x="340" y="268" text-anchor="middle" class="hw" font-size="21" fill="#0e6b6b">${tr(T("9 filas + 2 nuevas = 11 · ejecútalo 2 veces: siguen siendo 11", "9 rows + 2 new = 11 · run it twice: still 11"))}</text>
  </svg>`,
  deltaLog: () => `<svg viewBox="0 0 680 250">${DEFS}
    <line x1="40" y1="110" x2="650" y2="110" stroke="#1d2330" stroke-width="2"/>
    ${[["v0", "CREATE", T("9 filas", "9 rows")], ["v1", "MERGE", T("11 filas", "11 rows")], ["v2", "OPTIMIZE", T("mismos datos, menos archivos", "same data, fewer files")], ["v3", "…", T("tu próxima carga", "your next load")]].map(([v, op, d], i) => { const x = 60 + i * 150;
      return `<circle cx="${x + 50}" cy="110" r="22" fill="${i === 3 ? "#fff" : "#0e6b6b"}" stroke="#1d2330" stroke-width="2"/><text x="${x + 50}" y="115" text-anchor="middle" font-size="14" font-weight="700" fill="${i === 3 ? "#1d2330" : "#fff"}">${v}</text>
      <text x="${x + 50}" y="64" text-anchor="middle" font-size="14" font-weight="700">${op}</text><text x="${x + 50}" y="160" text-anchor="middle" font-size="12" fill="#5d6372">${tr(d)}</text>`; }).join("")}
    <path d="M410 200 C330 236 170 236 104 140" stroke="#c46f35" stroke-width="2.5" stroke-dasharray="6 4" fill="none" marker-end="url(#ah)"/>
    <text x="440" y="214" class="hw" font-size="20" fill="#c46f35">VERSION AS OF 0 ⟲</text>
    <text x="40" y="26" font-size="13" fill="#5d6372">_delta_log/</text>
  </svg>`,
  ingestMap: () => { const y = S.lang === "es" ? "Sí" : "Yes"; return `<svg viewBox="0 0 680 440">${DEFS}
    ${box(220, 10, 240, 52, "#fff8d6", tr(T("¿Necesitas MOVER los datos?", "Do you need to MOVE the data?")))}
    ${arrow("M220 36 H100 V78")}<text x="140" y="30" font-size="13" font-weight="700">No</text>
    ${box(14, 80, 164, 56, "#e9f5f3", "🔗 Shortcut", tr(T("leer sin copiar", "read without copying")))}
    ${arrow("M340 62 V96")}<text x="348" y="86" font-size="13" font-weight="700">${y}</text>
    ${box(190, 98, 300, 56, "#fff8d6", tr(T("¿Es una BD soportada y quieres", "Is it a supported DB and you want")), tr(T("réplica continua casi en tiempo real?", "continuous near-real-time replication?")))}
    ${arrow("M490 126 H560 V170")}<text x="510" y="118" font-size="13" font-weight="700">${y}</text>
    ${box(480, 172, 180, 56, "#e9f5f3", "🪞 Mirroring", tr(T("replica a Delta", "replicates to Delta")))}
    ${arrow("M340 154 V188")}<text x="348" y="178" font-size="13" font-weight="700">No</text>
    ${box(170, 190, 290, 56, "#fff8d6", tr(T("¿Quieres transformar con clics", "Want to transform with clicks")), tr(T("(Power Query, low-code)?", "(Power Query, low-code)?")))}
    ${arrow("M170 218 H110 V262")}<text x="120" y="210" font-size="13" font-weight="700">${y}</text>
    ${box(20, 264, 180, 56, "#e9f5f3", "🧹 Dataflow Gen2", tr(T("transformación visual", "visual transformation")))}
    ${arrow("M315 246 V280")}<text x="323" y="270" font-size="13" font-weight="700">No</text>
    ${box(215, 282, 250, 56, "#fff8d6", tr(T("¿Solo copiar (completo o", "Just copy (full or")), tr(T("incremental), sin orquestar pasos?", "incremental), no step orchestration?")))}
    ${arrow("M465 310 H560 V330")}<text x="485" y="302" font-size="13" font-weight="700">${y}</text>
    ${box(480, 332, 180, 56, "#e9f5f3", "📦 Copy job", tr(T("simple + incremental", "simple + incremental")))}
    ${arrow("M340 338 V362")}<text x="348" y="356" font-size="13" font-weight="700">No</text>
    ${box(250, 364, 180, 44, "#e9f5f3", "🧭 Pipeline", "", 14)}
    <text x="20" y="432" class="hw" font-size="17" fill="#c46f35">${tr(T("+ código → Notebook · streaming → Eventstream", "+ code → Notebook · streaming → Eventstream"))}</text>
  </svg>`; },
  pipelineFlow: () => `<svg viewBox="0 0 680 250">${DEFS}
    ${box(20, 90, 150, 64, "#fff", "🔎 Lookup", tr(T("lee parámetros", "reads parameters")))}
    ${box(230, 90, 150, 64, "#fff", "📋 Copy data", tr(T("fuente → Bronce", "source → Bronze")))}
    ${box(460, 20, 190, 64, "#e3f4e9", "📓 Notebook", tr(T("Bronce → Plata → Oro", "Bronze → Silver → Gold")))}
    ${box(460, 160, 190, 64, "#fbe6e3", "✉️ Teams / Outlook", tr(T("avisa del error", "reports the error")))}
    <path d="M170 122 H222" stroke="#2f8f5b" stroke-width="3" marker-end="url(#ah)"/>
    <path d="M380 112 C420 112 420 52 452 52" stroke="#2f8f5b" stroke-width="3" fill="none" marker-end="url(#ah)"/>
    <path d="M380 132 C420 132 420 192 452 192" stroke="#c2473b" stroke-width="3" fill="none" stroke-dasharray="6 4" marker-end="url(#ah)"/>
    <text x="374" y="46" font-size="13" font-weight="700" fill="#2f8f5b">${tr(T("al terminar bien", "on success"))}</text>
    <text x="374" y="222" font-size="13" font-weight="700" fill="#c2473b">${tr(T("si falla", "on failure"))}</text>
    <text x="20" y="236" class="hw" font-size="20" fill="#0e6b6b">${tr(T("un pipeline = actividades + dependencias", "a pipeline = activities + dependencies"))}</text>
  </svg>`,
  watermark: () => { const rows = [["1", "01-05"], ["2", "01-06"], ["3", "01-08"], ["4", "01-09"], ["5", "01-11"], ["6", "01-12"]];
    return `<svg viewBox="0 0 680 230">
    <line x1="30" y1="150" x2="650" y2="150" stroke="#1d2330" stroke-width="2"/>
    ${rows.map(([id, d], i) => { const x = 50 + i * 100, nw = i >= 3; return `<rect x="${x}" y="70" width="80" height="56" rx="10" fill="${nw ? "#e3f4e9" : "#efe7d4"}" stroke="${nw ? "#2f8f5b" : "#1d2330"}" stroke-width="2"/>
      <text x="${x + 40}" y="94" text-anchor="middle" font-size="13" font-weight="700">id ${id}</text><text x="${x + 40}" y="114" text-anchor="middle" font-size="12">${d}</text>
      <line x1="${x + 40}" y1="126" x2="${x + 40}" y2="150" stroke="#1d2330"/>`; }).join("")}
    <line x1="340" y1="40" x2="340" y2="180" stroke="#c46f35" stroke-width="4" stroke-dasharray="8 5"/>
    <text x="340" y="32" text-anchor="middle" font-size="14" font-weight="700" fill="#c46f35">watermark = 01-08</text>
    <text x="180" y="200" text-anchor="middle" class="hw" font-size="20" fill="#5d6372">${tr(T("ya copiado antes", "already copied"))}</text>
    <text x="500" y="200" text-anchor="middle" class="hw" font-size="20" fill="#2f8f5b">${tr(T("solo esto viaja hoy", "only this travels today"))}</text>
    <text x="30" y="222" font-size="12" fill="#5d6372">fecha_mod</text>
  </svg>`; },
  beforeAfter: () => `<svg viewBox="0 0 680 270">
    <text x="20" y="26" font-size="17" font-weight="700">${tr(T("ANTES: servicios separados", "BEFORE: separate services"))}</text>
    ${[["Data Factory", 30, 50], ["Synapse", 180, 50], ["Power BI", 30, 155], ["Machine Learning", 180, 155]].map(([n, x, y]) => `
      <rect x="${x}" y="${y}" width="125" height="80" rx="10" fill="#fff" stroke="#1d2330" stroke-width="2"/>
      <text x="${x + 62}" y="${y + 24}" text-anchor="middle" font-size="13" font-weight="700">${n}</text>
      <ellipse cx="${x + 62}" cy="${y + 45}" rx="22" ry="6" fill="#c46f35"/><rect x="${x + 40}" y="${y + 45}" width="44" height="18" fill="#c46f35"/><ellipse cx="${x + 62}" cy="${y + 63}" rx="22" ry="6" fill="#a95c2a"/>`).join("")}
    <g stroke="#c2473b" stroke-width="2" stroke-dasharray="5 4" fill="none"><path d="M155 90 H180"/><path d="M92 130 V155"/><path d="M242 130 V155"/><path d="M155 195 H180"/></g>
    <text x="167" y="250" text-anchor="middle" class="hw" font-size="20" fill="#c2473b">${tr(T("copias, silos, 4 facturas…", "copies, silos, 4 bills…"))}</text>
    <path d="M335 135 h40 m-12 -10 l12 10 l-12 10" stroke="#1d2330" stroke-width="3" fill="none"/>
    <text x="395" y="26" font-size="17" font-weight="700">${tr(T("CON FABRIC: una sola plataforma", "WITH FABRIC: one platform"))}</text>
    <rect x="395" y="42" width="270" height="200" rx="14" fill="#fffbe9" stroke="#1d2330" stroke-width="2"/>
    ${["Factory", "Engineering", "Warehouse", "Real-Time", "Science", "Power BI"].map((n, i) => `<rect x="${407 + (i % 3) * 86}" y="${56 + Math.floor(i / 3) * 40}" width="78" height="30" rx="7" fill="#0e6b6b"/><text x="${446 + (i % 3) * 86}" y="${76 + Math.floor(i / 3) * 40}" text-anchor="middle" font-size="12" fill="#fff" font-weight="700">${n}</text>`).join("")}
    <ellipse cx="530" cy="160" rx="110" ry="14" fill="#e3a234"/><rect x="420" y="160" width="220" height="50" fill="#e3a234"/><ellipse cx="530" cy="210" rx="110" ry="14" fill="#c98b1f"/>
    <text x="530" y="192" text-anchor="middle" font-size="18" font-weight="700">OneLake</text>
    <text x="530" y="262" text-anchor="middle" class="hw" font-size="16" fill="#0e6b6b">${tr(T("una copia, una seguridad, una capacidad", "one copy, one security model, one capacity"))}</text>
  </svg>`,
  hierarchy: () => `<svg viewBox="0 0 680 300">
    <rect x="10" y="10" width="660" height="280" rx="16" fill="#f4efe3" stroke="#1d2330" stroke-width="2"/>
    <text x="28" y="36" font-size="15" font-weight="700">Tenant · ${tr(T("tu organización", "your organization"))}</text>
    <rect x="28" y="48" width="624" height="226" rx="14" fill="#fff4d6" stroke="#1d2330" stroke-width="2"/>
    <text x="46" y="72" font-size="15" font-weight="700">OneLake · ${tr(T("uno solo por tenant", "exactly one per tenant"))}</text>
    <rect x="46" y="84" width="360" height="174" rx="12" fill="#fff" stroke="#0e6b6b" stroke-width="2.5"/>
    <text x="62" y="106" font-size="14" font-weight="700" fill="#0e6b6b">Workspace: ws_ventas</text>
    <rect x="62" y="118" width="190" height="124" rx="10" fill="#e9f5f3" stroke="#1d2330" stroke-width="2"/>
    <text x="76" y="140" font-size="14" font-weight="700">Lakehouse: lh_bronze</text>
    <rect x="76" y="152" width="74" height="34" rx="7" fill="#fff" stroke="#1d2330" stroke-width="1.5"/><text x="113" y="174" text-anchor="middle" font-size="13">📁 Files</text>
    <rect x="160" y="152" width="80" height="34" rx="7" fill="#fff" stroke="#1d2330" stroke-width="1.5"/><text x="200" y="174" text-anchor="middle" font-size="13">🗂 Tables</text>
    <text x="76" y="222" class="hw" font-size="18" fill="#c46f35">${tr(T("crudo · Delta", "raw · Delta"))}</text>
    <rect x="266" y="118" width="126" height="56" rx="10" fill="#f1ecff" stroke="#1d2330" stroke-width="2"/><text x="329" y="151" text-anchor="middle" font-size="13" font-weight="700">Warehouse</text>
    <rect x="266" y="186" width="126" height="56" rx="10" fill="#fdeee4" stroke="#1d2330" stroke-width="2"/><text x="329" y="219" text-anchor="middle" font-size="13" font-weight="700">Notebook</text>
    <rect x="422" y="84" width="214" height="174" rx="12" fill="#fff" stroke="#0e6b6b" stroke-width="2.5" stroke-dasharray="6 4"/>
    <text x="438" y="106" font-size="14" font-weight="700" fill="#0e6b6b">Workspace: ws_finanzas</text>
    <rect x="438" y="122" width="182" height="54" rx="10" fill="#e9f5f3" stroke="#1d2330" stroke-width="2"/><text x="529" y="154" text-anchor="middle" font-size="13" font-weight="700">Lakehouse: lh_gold</text>
    <path d="M529 186 v26" stroke="#c46f35" stroke-width="2.5"/><text x="529" y="236" text-anchor="middle" font-size="13">🔗 Shortcut → ADLS / S3</text>
  </svg>`,
  medallion: () => `<svg viewBox="0 0 680 230">
    ${[["#8a8f99", T("Fuentes", "Sources"), T("ERP, CRM, APIs, archivos", "ERP, CRM, APIs, files"), "🏭"], ["#c46f35", T("Bronce", "Bronze"), T("tal cual llegó + metadatos", "as it arrived + metadata"), "🥉"], ["#9aa3ad", T("Plata", "Silver"), T("limpio, tipado, sin duplicados", "clean, typed, deduplicated"), "🥈"], ["#e3a234", T("Oro", "Gold"), T("listo para el negocio (estrella)", "business-ready (star schema)"), "🥇"], ["#0e6b6b", T("Consumo", "Consumption"), T("Power BI, agentes de IA", "Power BI, AI agents"), "📊"]].map(([c, n, d, e], i) => {
      const x = 14 + i * 134; return `<rect x="${x}" y="40" width="114" height="100" rx="14" fill="#fff" stroke="#1d2330" stroke-width="2"/>
      <rect x="${x}" y="40" width="114" height="30" rx="14" fill="${c}"/><rect x="${x}" y="56" width="114" height="14" fill="${c}"/>
      <text x="${x + 57}" y="61" text-anchor="middle" font-size="15" font-weight="700" fill="#fff">${tr(n)}</text>
      <text x="${x + 57}" y="112" text-anchor="middle" font-size="30">${e}</text>
      <foreignObject x="${x - 6}" y="148" width="126" height="70"><div xmlns="http://www.w3.org/1999/xhtml" style="font:14px 'Atkinson Hyperlegible',sans-serif;text-align:center;color:#1d2330">${tr(d)}</div></foreignObject>
      ${i < 4 ? `<path d="M${x + 116} 90 h16 m-7 -7 l7 7 l-7 7" stroke="#1d2330" stroke-width="2.5" fill="none"/>` : ""}`;
    }).join("")}
    <text x="340" y="24" text-anchor="middle" class="hw" font-size="22" fill="#0e6b6b">${tr(T("cada capa sube el valor (y la confianza) del dato", "each layer raises the value (and trust) of the data"))}</text>
  </svg>`
};

/* =========================================================
   4) CONTENIDO: se carga desde /content (course.json + level-N.json)
   ========================================================= */
let COURSE = [], ALL = [], META = {};
async function getJSON(u) { const r = await fetch(u, { cache: "no-cache" }); if (!r.ok) throw new Error(u + " → " + r.status); return r.json(); }
async function loadCourse() {
  META = await getJSON("content/course.json");
  COURSE = await Promise.all(META.levels.map(async lv => lv.file && !lv.locked ? Object.assign({}, lv, await getJSON("content/" + lv.file), { id: lv.id }) : lv));
  ALL = COURSE.flatMap(l => (l.lessons || []).map(x => Object.assign(x, { level: l.id })));
}

/* =========================================================
   5) Render: encabezado, inicio, pie
   ========================================================= */
const app = document.getElementById("app");
function renderHeader() {
  document.documentElement.lang = S.lang;
  document.getElementById("hdr").innerHTML = `
    <a class="brand" href="#home"><span class="mini">${wizardSVG()}</span>Alquimio<small>· ${tr(UI.tagline)}</small></a>
    <span class="spacer"></span>
    <span class="pill" title="${tr(UI.rankLbl)}">⭐ <span id="xpv">${S.xp}</span> XP <span class="rank">· ${tr(rank())}</span></span>
    <span class="lang" role="group" aria-label="Idioma / Language"><button data-l="es" aria-pressed="${S.lang === "es"}">ES</button><button data-l="en" aria-pressed="${S.lang === "en"}">EN</button></span>`;
  document.querySelectorAll(".lang button").forEach(b => b.onclick = () => { S.lang = b.dataset.l; save(); renderAll(); });
}
function renderFooter() {
  const f = document.getElementById("ftr");
  f.innerHTML = `<span>🧙 Alquimio · &copy; Cristiam Espinoza — ${tr(UI.footer)}</span>
    <span><button class="linkbtn" id="wizToggle">${S.dock === "hidden" ? tr(UI.showWiz) : tr(UI.hideWiz)}</button> · <span id="resetZone"><button class="linkbtn" id="resetBtn">${tr(UI.reset)}</button></span></span>`;
  document.getElementById("wizToggle").onclick = () => { S.dock = S.dock === "hidden" ? "open" : "hidden"; save(); applyDock(); renderFooter(); };
  document.getElementById("resetBtn").onclick = () => {
    const z = document.getElementById("resetZone");
    z.innerHTML = `${tr(UI.sure)} <button class="linkbtn" id="rY">${tr(UI.yes)}</button> / <button class="linkbtn" id="rN">${tr(UI.no)}</button>`;
    document.getElementById("rY").onclick = () => { S.xp = 0; S.done = {}; S.awarded = {}; save(); renderAll(); };
    document.getElementById("rN").onclick = renderFooter;
  };
}
function applyDock() {
  const d = document.getElementById("dock");
  const onHome = !currentLesson;
  d.classList.toggle("hidden", S.dock === "hidden" || onHome);
}
function nextLesson() { return ALL.find(l => !S.done[l.id]); }
function renderHome() {
  currentLesson = null; applyDock();
  const doneN = ALL.filter(l => S.done[l.id]).length;
  const nl = nextLesson();
  app.innerHTML = `
  <section class="hero">
    <div>
      <h1>${tr(UI.heroTitle)}</h1>
      <p class="lead">${tr(UI.heroLead)}</p>
      <div class="actions">
        <a class="btn" href="#${(nl || ALL[0]).id}">${doneN ? tr(UI.cont) : tr(UI.start)} →</a>
        <span class="note">${tr(UI.handNote)}</span>
      </div>
    </div>
    <div class="hero-wiz">
      <div class="hero-bubble" id="heroBubble"><span id="heroText"></span></div>
      <button class="wizbtn" id="heroWiz" aria-label="Alquimio">${wizardSVG()}</button>
    </div>
  </section>
  <div class="stats">
    <div class="stat"><b>${S.xp}</b><span>${tr(UI.xp)}</span></div>
    <div class="stat"><b>${doneN}/${ALL.length}</b><span>${tr(UI.lessonsDone)}</span></div>
    <div class="stat"><b>${ALL.filter(l => S.done[l.id]).map(l => l.badge.e).join(" ") || "—"}</b><span>${tr(UI.badges)}</span></div>
    <div class="stat"><b style="font-family:var(--hand);font-size:30px">${tr(rank())}</b><span>${tr(UI.rankLbl)}</span></div>
  </div>
  <h2 class="section-title">${tr(UI.path)}</h2>
  <p style="margin:0;color:var(--muted)">${tr(UI.pathSub)}</p>
  ${COURSE.filter(l => !l.locked).map(lv => {
    const d = lv.lessons.filter(x => S.done[x.id]).length;
    return `<div class="level">
      <div class="level-head"><div class="lvl-num">${d === lv.lessons.length ? "🏆" : lv.id}</div><div style="flex:1"><h3>${tr(UI.level)} ${lv.id} · ${tr(lv.title)}</h3><p>${tr(lv.desc)}</p>
      <div class="progressbar"><i style="width:${Math.round(d / lv.lessons.length * 100)}%"></i></div></div></div>
      <div class="lessons">${lv.lessons.map((x, i) => `
        <a class="lesson-card ${S.done[x.id] ? "done" : ""}" href="#${x.id}" style="text-decoration:none;color:inherit">
          ${S.done[x.id] ? `<span class="tag">${tr(UI.done)} ${x.badge.e}</span>` : (nl && nl.id === x.id ? `<span class="tag">${tr(UI.next)}</span>` : "")}
          <div class="ico">${x.icon}</div><h4>${lv.id}.${i + 1} · ${tr(x.title)}</h4>
          <div class="meta">⏱ ${x.min} ${tr(UI.min)} · ${x.steps.length} ${S.lang === "es" ? "pasos" : "steps"}</div>
        </a>`).join("")}</div>
    </div>`;
  }).join("")}
  ${certCard()}
  <div class="locked-grid">${COURSE.filter(l => l.locked).map(l => `<div class="locked"><span class="soon">🔒 ${tr(UI.level)} ${l.id} · ${tr(UI.soon)}</span><h4>${tr(l.title)}</h4><div style="font-size:14px">${tr(l.desc)}</div></div>`).join("")}</div>
  <div style="height:30px"></div>`;
  bindMascot(document.getElementById("heroWiz"), document.getElementById("heroBubble"), document.getElementById("heroText"));
  const greet = doneN === ALL.length ? tr(UI.allDone) : tr(UI.heroSay);
  setTimeout(() => say(greet, doneN ? "happy" : null), 250);
  document.getElementById("heroWiz").onclick = () => say(tr(pick(TIPS)), "happy");
  window.scrollTo(0, 0);
}
const TIPS = [
  T("Tip: Fabric guarda <b>todas</b> las tablas en Delta. Aprende Delta y ya ganaste la mitad.", "Tip: Fabric stores <b>every</b> table in Delta. Learn Delta and you've won half the battle."),
  T("Tip: ponle prefijo a todo: <code>lh_</code>, <code>nb_</code>, <code>pl_</code>. Tu yo del futuro te lo agradecerá.", "Tip: prefix everything: <code>lh_</code>, <code>nb_</code>, <code>pl_</code>. Future you will thank you."),
  T("Tip: si algo se ve lento, primero revisa cuánto de tu capacidad estás usando.", "Tip: if something feels slow, first check how much of your capacity you're using."),
  T("Tip: nunca borres Bronce. Es tu máquina del tiempo.", "Tip: never delete Bronze. It's your time machine."),
  T("¿Sabías que el mejor momento para aprender es justo después de equivocarte? 🧠", "Did you know the best moment to learn is right after a mistake? 🧠")
];

/* =========================================================
   6) Reproductor de lecciones
   ========================================================= */
let currentLesson = null, idx = 0, stepOK = [];
function addXP(key, n, evt) {
  if (S.awarded[key] || !n) return;
  S.awarded[key] = n; S.xp += n; save();
  const x = document.getElementById("xpv"); if (x) x.textContent = S.xp;
  const r = document.querySelector(".pill .rank"); if (r) r.textContent = "· " + tr(rank());
  const f = document.createElement("div"); f.className = "xp-float"; f.textContent = `+${n} XP`;
  const ex = evt && evt.clientX ? evt.clientX : innerWidth / 2, ey = evt && evt.clientY ? evt.clientY : innerHeight / 2;
  f.style.left = (ex - 30) + "px"; f.style.top = (ey - 30) + "px"; document.body.appendChild(f); setTimeout(() => f.remove(), 1300);
}
function renderLesson(id) {
  currentLesson = ALL.find(l => l.id === id); idx = 0;
  stepOK = currentLesson.steps.map(s => ["story", "concept"].includes(s.type));
  applyDock();
  bindMascot(document.getElementById("dockWiz"), document.getElementById("bubble"), document.getElementById("bubbleText"));
  renderStep();
}
function shell(inner) {
  const L = currentLesson, n = L.steps.length;
  const lv = COURSE.find(c => c.id === L.level), num = lv.lessons.indexOf(L) + 1;
  return `<div class="lesson-top">
      <a class="btn ghost" href="#home" style="padding:6px 12px">← ${tr(UI.home)}</a>
      <h1>${L.icon} ${L.level}.${num} · ${tr(L.title)}</h1>
    </div>
    <div style="display:flex;align-items:center;gap:14px;flex-wrap:wrap">
      <span class="stepcount">${tr(UI.step)} ${idx + 1} ${tr(UI.of)} ${n}</span>
      <div class="dots">${L.steps.map((_, i) => `<span class="${i === idx ? "cur" : i < idx ? "done" : ""}"></span>`).join("")}</div>
    </div>
    ${inner}
    <div class="navbar">
      <button class="btn ghost" id="bk" ${idx === 0 ? "disabled" : ""}>${tr(UI.back)}</button>
      <button class="btn ${idx === n - 1 ? "gold" : ""}" id="nx" ${stepOK[idx] ? "" : "disabled"}>${idx === n - 1 ? tr(UI.finish) : tr(UI.fwd)}</button>
    </div>`;
}
function markOK(xp, evt) {
  stepOK[idx] = true;
  addXP(`${currentLesson.id}:${idx}`, xp, evt);
  const nx = document.getElementById("nx"); if (nx) nx.disabled = false;
  const d = document.querySelectorAll(".dots span")[idx]; if (d) d.classList.add("done");
}
function callout(c) {
  const lbl = { key: "🔑", brain: "🧠", watch: "⚠️", pencil: "✏️", nodumb: "❓" }[c.k] + " " + tr(UI.cl[c.k]);
  const inner = c.qa ? `<dl>${c.qa.map(x => `<dt>${tr(x.q)}</dt><dd>${tr(x.a)}</dd>`).join("")}</dl>` : `<div>${tr(c.b)}</div>`;
  return `<div class="callout ${c.k}"><span class="lbl">${lbl}</span>${inner}</div>`;
}
function codeBox(code, fill) {
  return `<div class="codebox"><pre>${fill ? code : esc(code).replace(/^(#.*)$/gm, '<span class="cm">$1</span>')}</pre>${fill ? "" : `<button class="copy" data-code="${esc(code)}">${tr(UI.copy)}</button>`}</div>`;
}
const shuffle = a => { const b = a.slice(); for (let i = b.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [b[i], b[j]] = [b[j], b[i]]; } return b; };

const R = {
  story: s => `${s.kicker ? `<span class="kicker">${tr(s.kicker)}</span>` : ""}<h2>${tr(s.title)}</h2><div class="prose">${tr(s.body)}</div>
               ${s.cards ? `<div class="grid-cards">${s.cards.map(c => `<div class="wl ${c.star ? "star" : ""}"><span class="e">${c.e || ""}</span><b>${tr(c.n)} ${c.star ? "⭐" : ""}</b><span>${tr(c.d)}</span></div>`).join("")}</div>` : ""}
               ${s.svg ? `<figure class="visual" style="margin-left:0;margin-right:0">${tr(s.svg)}</figure>` : ""}${s.visual ? `<figure class="visual" style="margin-left:0;margin-right:0">${VIS[s.visual]()}</figure>` : ""}${(s.callouts || []).map(callout).join("")}`,
  reveal: s => `<span class="kicker">${s.kind === "pencil" ? "✏️ " + tr(UI.cl.pencil) : "🧠 " + tr(UI.cl.brain)}</span>
               <div class="q">${tr(s.prompt)}</div><textarea class="think" placeholder="${tr(UI.thinkPh)}"></textarea>
               <div class="actions"><button class="btn gold" id="rv">${tr(UI.reveal)}</button></div><div class="answer" id="ans">${tr(s.answer)}</div>`,
  quiz: s => `<span class="kicker">✅ Quiz</span><p class="q">${tr(s.q)}</p><div class="opts">${s.opts.map((o, i) => `<button class="opt" data-i="${i}"><span class="l">${"ABCD"[i]}</span><span>${tr(o.t)}</span></button>`).join("")}</div><div class="why" id="why"></div>`,
  match: s => `<span class="kicker">🧩 ${S.lang === "es" ? "Relaciona" : "Match up"}</span><h2>${tr(s.title)}</h2><p style="color:var(--muted)">${tr(UI.matchHelp)}</p>
               <div class="match"><div class="col" id="mL">${s.pairs.map((p, i) => `<button class="chip" data-i="${i}">${tr(p[0])}</button>`).join("")}</div>
               <div class="col" id="mR">${shuffle(s.pairs.map((p, i) => [p, i])).map(([p, i]) => `<button class="chip" data-i="${i}">${tr(p[1])}</button>`).join("")}</div></div>`,
  order: s => `<span class="kicker">🔢 ${S.lang === "es" ? "Ordena" : "Put in order"}</span><h2>${tr(s.title)}</h2><p style="color:var(--muted)">${tr(UI.orderHelp)}</p><ol class="order-list" id="ol"></ol>
               <div class="actions"><button class="btn" id="ck">${tr(UI.check)}</button></div>`,
  fill: s => { let c = esc(s.code); s.blanks.forEach((b, i) => { c = c.replace(`{{${i}}}`, `<input data-i="${i}" aria-label="blank ${i + 1}" autocomplete="off" spellcheck="false">`); });
               return `<span class="kicker">⌨️ ${S.lang === "es" ? "Completa el código" : "Fill in the code"}</span><h2>${tr(s.title)}</h2><p style="color:var(--muted)">${tr(UI.fillHelp)}</p>
               <div class="fill">${codeBox(c, true)}</div><div class="hintline" id="hint"></div><div class="actions"><button class="btn" id="ck">${tr(UI.check)}</button></div>`; },
  lab: s => `<span class="kicker">🧪 ${S.lang === "es" ? "Laboratorio práctico" : "Hands-on lab"}</span><h2>${tr(s.title)}</h2><p>${tr(s.intro)}</p><p style="color:var(--muted);font-size:15px">${tr(UI.tasksLeft)}</p>
               <ul class="tasks">${s.tasks.map((t, i) => `<li><label><input type="checkbox" data-i="${i}"><span><span class="tn"></span> ${tr(t.t)}</span></label>${t.code ? codeBox(t.code) : ""}${t.solution ? `<details class="sol"><summary>${S.lang === "es" ? "🔑 Ver una solución (inténtalo primero)" : "🔑 Show a solution (try first)"}</summary>${codeBox(t.solution)}</details>` : ""}</li>`).join("")}</ul>
               ${s.expect ? callout({ k: "key", b: s.expect }) : ""}`
};
R.concept = R.story;

const MOUNT = {
  reveal: (s, el) => { el.querySelector("#rv").onclick = e => { el.querySelector("#ans").classList.add("show"); e.target.disabled = true; markOK(10, e); say(S.lang === "es" ? "¿Se parecía a lo que pensaste? Si sí, ¡excelente! Si no, ahora lo recordarás mejor." : "Was it close to what you thought? If yes, great! If not, now you'll remember it better.", "happy"); }; },
  quiz: (s, el) => {
    let tries = 0;
    el.querySelectorAll(".opt").forEach(b => b.onclick = e => {
      const o = s.opts[+b.dataset.i]; tries++;
      const w = el.querySelector("#why"); w.innerHTML = tr(o.why); w.classList.add("show");
      if (o.ok) { b.classList.add("ok"); el.querySelectorAll(".opt").forEach(x => x.disabled = true); markOK(tries === 1 ? 20 : tries === 2 ? 10 : 5, e); say(tr(pick(PRAISE)), "happy"); }
      else { b.classList.add("bad"); b.disabled = true; say(tr(pick(OOPS)), "think"); }
    });
  },
  match: (s, el) => {
    let sel = null, miss = 0, got = 0;
    el.querySelectorAll("#mL .chip").forEach(b => b.onclick = () => { if (b.classList.contains("ok")) return; el.querySelectorAll("#mL .chip").forEach(x => x.classList.remove("sel")); b.classList.add("sel"); sel = b; });
    el.querySelectorAll("#mR .chip").forEach(b => b.onclick = e => {
      if (!sel || b.classList.contains("ok")) { if (!sel) say(S.lang === "es" ? "Primero elige algo de la <b>izquierda</b>." : "Pick something on the <b>left</b> first.", "think"); return; }
      if (sel.dataset.i === b.dataset.i) { sel.classList.remove("sel"); sel.classList.add("ok"); b.classList.add("ok"); sel.disabled = b.disabled = true; sel = null; got++;
        if (got === s.pairs.length) { markOK(Math.max(10, 30 - miss * 5), e); say(tr(pick(PRAISE)), "happy"); } }
      else { miss++; b.classList.add("bad"); setTimeout(() => b.classList.remove("bad"), 400); say(tr(pick(OOPS)), "oops"); }
    });
  },
  order: (s, el) => {
    let cur = shuffle(s.items.map((t, i) => i)); if (cur.every((v, i) => v === i)) cur.reverse();
    let fails = 0;
    const draw = () => { el.querySelector("#ol").innerHTML = cur.map((v, p) => `<li data-p="${p}"><span class="n">${p + 1}</span><span class="t">${tr(s.items[v])}</span><button class="mv" data-d="-1" data-p="${p}" aria-label="up">↑</button><button class="mv" data-d="1" data-p="${p}" aria-label="down">↓</button></li>`).join("");
      el.querySelectorAll(".mv").forEach(b => b.onclick = () => { const p = +b.dataset.p, q = p + (+b.dataset.d); if (q < 0 || q >= cur.length) return; [cur[p], cur[q]] = [cur[q], cur[p]]; draw(); }); };
    draw();
    el.querySelector("#ck").onclick = e => {
      const lis = el.querySelectorAll("#ol li"); let ok = true;
      cur.forEach((v, p) => { lis[p].classList.toggle("ok", v === p); lis[p].classList.toggle("bad", v !== p); if (v !== p) ok = false; });
      if (ok) { markOK(Math.max(10, 30 - fails * 5), e); e.target.disabled = true; el.querySelectorAll(".mv").forEach(b => b.disabled = true); say(tr(pick(PRAISE)), "happy"); }
      else { fails++; say(S.lang === "es" ? "Los <b>verdes</b> ya están bien. Mueve los rojos." : "The <b>green</b> ones are right. Move the red ones.", "think"); }
    };
  },
  fill: (s, el) => {
    let fails = 0;
    el.querySelector("#ck").onclick = e => {
      let ok = true, firstBad = null;
      el.querySelectorAll(".fill input").forEach(inp => { const b = s.blanks[+inp.dataset.i]; const good = b.a.includes(inp.value.trim().replace(/["']/g, "").toLowerCase());
        inp.classList.toggle("ok", good); inp.classList.toggle("bad", !good); if (!good) { ok = false; if (!firstBad) firstBad = b; } });
      const h = el.querySelector("#hint");
      if (ok) { h.textContent = "✓ " + (S.lang === "es" ? "¡Código perfecto!" : "Perfect code!"); markOK(Math.max(10, 30 - fails * 5), e); e.target.disabled = true; say(tr(pick(PRAISE)), "happy"); }
      else { fails++; h.textContent = "💡 " + tr(firstBad.hint); say(S.lang === "es" ? "Mira la pista debajo del código." : "Check the hint below the code.", "think"); }
    };
  },
  lab: (s, el) => {
    const boxes = el.querySelectorAll(".tasks input");
    boxes.forEach(b => b.onchange = e => {
      b.closest("li").classList.toggle("checked", b.checked);
      const n = [...boxes].filter(x => x.checked).length;
      if (n === boxes.length && !stepOK[idx]) { markOK(40, e); say(S.lang === "es" ? "¡Laboratorio terminado! Eso ya es <b>experiencia real</b> en Fabric. 🎉" : "Lab complete! That's <b>real Fabric experience</b> now. 🎉", "happy"); }
      else if (b.checked) say(S.lang === "es" ? `Paso ${n} de ${boxes.length}. ¡Vas muy bien!` : `Step ${n} of ${boxes.length}. Going great!`);
    });
  }
};

function renderStep() {
  const s = currentLesson.steps[idx];
  app.innerHTML = shell(`<article class="card" id="stepCard">${R[s.type](s)}</article>`);
  const el = document.getElementById("stepCard");
  if (MOUNT[s.type]) MOUNT[s.type](s, el);
  el.querySelectorAll(".copy").forEach(b => b.onclick = () => {
    const txt = b.dataset.code.replace(/&quot;/g, '"').replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&amp;/g, "&");
    const done = () => { b.textContent = tr(UI.copied); setTimeout(() => b.textContent = tr(UI.copy), 1500); };
    try { navigator.clipboard.writeText(txt).then(done, () => selectPre(b)); } catch (e) { selectPre(b); }
  });
  document.getElementById("bk").onclick = () => { if (idx > 0) { idx--; renderStep(); } };
  document.getElementById("nx").onclick = e => { if (!stepOK[idx]) return; if (idx < currentLesson.steps.length - 1) { idx++; renderStep(); } else finishLesson(e); };
  if (s.say) setTimeout(() => say(tr(s.say)), 150);
  window.scrollTo({ top: 0, behavior: "smooth" });
}
function selectPre(b) { const pre = b.previousElementSibling; const r = document.createRange(); r.selectNodeContents(pre); const sel = getSelection(); sel.removeAllRanges(); sel.addRange(r); b.textContent = "Ctrl+C"; }

function confetti() {
  const cols = ["#0e6b6b", "#e3a234", "#c46f35", "#ffe680", "#2f8f5b", "#8fe0d2"];
  for (let i = 0; i < 90; i++) { const c = document.createElement("div"); c.className = "confetti";
    c.style.left = Math.random() * 100 + "vw"; c.style.background = pick(cols); c.style.animationDuration = 2 + Math.random() * 2 + "s"; c.style.animationDelay = Math.random() * .6 + "s";
    c.style.borderRadius = Math.random() > .5 ? "50%" : "2px"; document.body.appendChild(c); setTimeout(() => c.remove(), 5000); }
}
function badgeSVG(e) {
  return `<svg class="badge-big" viewBox="0 0 160 160"><g transform="translate(80 80)">
    ${Array.from({ length: 16 }, (_, i) => `<path d="M0 -76 L8 -58 L-8 -58 Z" fill="#e3a234" transform="rotate(${i * 22.5})"/>`).join("")}
    <circle r="58" fill="#e3a234" stroke="#1d2330" stroke-width="3"/><circle r="47" fill="#fff8d6" stroke="#c46f35" stroke-width="3" stroke-dasharray="4 4"/>
    <text y="16" text-anchor="middle" font-size="46">${e}</text></g></svg>`;
}
function finishLesson(evt) {
  const L = currentLesson, first = !S.done[L.id];
  const before = S.xp;
  S.done[L.id] = true; addXP(L.id + ":done", 50, evt); save();
  const gained = Object.keys(S.awarded).filter(k => k.startsWith(L.id + ":")).reduce((a, k) => a + S.awarded[k], 0);
  const nl = nextLesson(); const lvL = ALL.filter(l => l.level === L.level); const levelDone = lvL.every(l => S.done[l.id]);
  const lvMsg = ALL.every(l => S.done[l.id]) ? tr(UI.allDone) : tr(UI.levelDone).replace("{n}", L.level);
  app.innerHTML = `<article class="card finish" style="margin-top:30px">
    <span class="kicker">${tr(UI.lessonComplete)}</span>
    ${badgeSVG(L.badge.e)}
    <h2>${tr(UI.badgeGot)}: ${tr(L.badge.n)}</h2>
    <p style="font-size:19px">${tr(UI.earned)} <b>${gained} XP</b> ${S.lang === "es" ? "en esta lección" : "in this lesson"} · ${S.lang === "es" ? "Rango" : "Rank"}: <b class="hand" style="font-size:26px;color:var(--teal)">${tr(rank())}</b></p>
    ${levelDone ? `<p class="note" style="font-size:28px">${lvMsg}</p>` : ""}
    <div class="actions" style="justify-content:center">
      ${nl ? `<a class="btn" href="#${nl.id}">${tr(UI.nextLesson)}</a>` : `<a class="btn gold" href="#certificado">${tr(UI.certView)}</a>`}
      <a class="btn ghost" href="#home">${tr(UI.backPath)}</a>
    </div></article><div style="height:140px"></div>`;
  renderHeader();
  confetti();
  bindMascot(document.getElementById("dockWiz"), document.getElementById("bubble"), document.getElementById("bubbleText"));
  say(levelDone ? lvMsg : (S.lang === "es" ? `¡Lo lograste! Te ganaste la insignia <b>${tr(L.badge.n)}</b>. ${L.badge.e}` : `You did it! You earned the <b>${tr(L.badge.n)}</b> badge. ${L.badge.e}`), "happy");
  window.scrollTo(0, 0);
}

/* =========================================================
   6b) Certificado de finalización (#certificado)
   ========================================================= */
let view = "";
function certCard() {
  const doneN = ALL.filter(l => S.done[l.id]).length, all = doneN === ALL.length;
  return `<div class="level cert-card"><div class="level-head"><div class="lvl-num">🎓</div><div style="flex:1">
    <h3>${tr(UI.certTitle)}</h3><p>${tr(UI.certCard)}</p>
    <div class="progressbar"><i style="width:${Math.round(doneN / ALL.length * 100)}%"></i></div>
    <p style="margin-top:6px;font-size:14px">${tr(UI.certProgress)}: <b>${doneN}/${ALL.length}</b></p>
    <div class="actions"><a class="btn ${all ? "gold" : "ghost"}" href="#certificado">${all ? tr(UI.certView) : "🔒 " + tr(UI.certTitle)}</a></div></div></div></div>`;
}
function certCode(name) {
  let h = 2166136261; const str = `${name}|${S.certDate}|${ALL.length}`;
  for (let i = 0; i < str.length; i++) { h ^= str.charCodeAt(i); h = Math.imul(h, 16777619) >>> 0; }
  const a = h.toString(36).toUpperCase().padStart(7, "0");
  return `ALQ-${a.slice(0, 4)}-${a.slice(-3)}${(S.xp % 97).toString().padStart(2, "0")}`;
}
function certSVG(name) {
  const d = new Date(S.certDate || Date.now());
  const fecha = d.toLocaleDateString(S.lang === "es" ? "es-MX" : "en-US", { year: "numeric", month: "long", day: "numeric" });
  const serif = "Fraunces, Georgia, 'Times New Roman', serif", sans = "'Atkinson Hyperlegible', Arial, sans-serif";
  return `<svg id="certSvg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 700" style="width:100%;height:auto;display:block">
    <rect width="1000" height="700" fill="#fbf6e8"/>
    <rect x="22" y="22" width="956" height="656" rx="18" fill="none" stroke="#0e6b6b" stroke-width="10"/>
    <rect x="42" y="42" width="916" height="616" rx="12" fill="none" stroke="#e3a234" stroke-width="3" stroke-dasharray="2 7"/>
    <text x="500" y="122" text-anchor="middle" font-family="${sans}" font-size="20" letter-spacing="6" fill="#c46f35" font-weight="700">${esc(tr(T("CERTIFICADO DE FINALIZACIÓN", "CERTIFICATE OF COMPLETION")))}</text>
    <text x="500" y="182" text-anchor="middle" font-family="${sans}" font-size="20" fill="#5d6372">${esc(tr(T("Se otorga a", "Awarded to")))}</text>
    <text x="500" y="258" text-anchor="middle" font-family="${serif}" font-size="58" font-weight="800" fill="#1d2330">${esc(name || "—")}</text>
    <line x1="230" y1="282" x2="770" y2="282" stroke="#1d2330" stroke-width="1.5"/>
    <text x="500" y="330" text-anchor="middle" font-family="${sans}" font-size="20" fill="#1d2330">${esc(tr(T("por completar el programa", "for completing the program")))}</text>
    <text x="500" y="374" text-anchor="middle" font-family="${serif}" font-size="31" font-weight="800" fill="#0e6b6b">${esc(tr(T("Microsoft Fabric para Ingeniería de Datos", "Microsoft Fabric for Data Engineering")))}</text>
    <text x="500" y="410" text-anchor="middle" font-family="${sans}" font-size="19" fill="#5d6372">${esc(tr(T("de cero a experto, con Alquimio", "from zero to expert, with Alquimio")))}</text>
    <text x="500" y="458" text-anchor="middle" font-family="${sans}" font-size="17" fill="#1d2330">${esc(`${COURSE.filter(l => !l.locked).length} ${tr(T("niveles", "levels"))} · ${ALL.length} ${tr(T("lecciones", "lessons"))} · ${S.xp} XP · ${tr(T("Rango", "Rank"))}: ${tr(rank())}`)}</text>
    <g transform="translate(70 470) scale(.82)">${wizardSVG(true).replace('<svg class="wiz"', '<svg width="160" height="200"')}</g>
    <g transform="translate(850 560)"><circle r="62" fill="#e3a234" stroke="#1d2330" stroke-width="3"/><circle r="50" fill="#fff8d6" stroke="#c46f35" stroke-width="3" stroke-dasharray="4 4"/><text y="18" text-anchor="middle" font-size="48">🏆</text></g>
    <line x1="300" y1="590" x2="480" y2="590" stroke="#1d2330"/><line x1="520" y1="590" x2="700" y2="590" stroke="#1d2330"/>
    <text x="390" y="614" text-anchor="middle" font-family="${sans}" font-size="15" fill="#1d2330">Alquimio · ${esc(tr(T("Tutor de datos", "Data tutor")))}</text>
    <text x="610" y="614" text-anchor="middle" font-family="${sans}" font-size="15" fill="#1d2330">HexaMind Lab</text>
    <text x="390" y="578" text-anchor="middle" font-family="${sans}" font-size="15" fill="#5d6372">${esc(fecha)}</text>
    <text x="610" y="578" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="14" fill="#5d6372">${esc(certCode(name))}</text>
    <text x="500" y="650" text-anchor="middle" font-family="${sans}" font-size="12" fill="#8a8f99">${esc(tr(UI.certNote))}</text>
  </svg>`;
}
function renderCert() {
  currentLesson = null; applyDock();
  const pend = ALL.filter(l => !S.done[l.id]);
  if (pend.length) {
    app.innerHTML = `<div class="lesson-top"><a class="btn ghost" href="#home" style="padding:6px 12px">← ${tr(UI.home)}</a><h1>🎓 ${tr(UI.certTitle)}</h1></div>
      <article class="card"><p class="q">🔒 ${tr(UI.certLocked)}</p><ul class="pending">${pend.map(l => `<li><a href="#${l.id}">${l.level}.${COURSE.find(c => c.id === l.level).lessons.indexOf(l) + 1} · ${tr(l.title)}</a></li>`).join("")}</ul>
      <div class="progressbar"><i style="width:${Math.round((ALL.length - pend.length) / ALL.length * 100)}%"></i></div></article><div style="height:120px"></div>`;
    window.scrollTo(0, 0); return;
  }
  if (!S.certDate) { S.certDate = new Date().toISOString(); save(); }
  const standalone = (() => { try { return window.top === window.self; } catch (e) { return false; } })();
  app.innerHTML = `<div class="lesson-top"><a class="btn ghost" href="#home" style="padding:6px 12px">← ${tr(UI.home)}</a><h1>🎓 ${tr(UI.certTitle)}</h1></div>
    <article class="card">
      <label class="q" for="certName">${tr(UI.certName)}</label>
      <input id="certName" class="cert-input" maxlength="60" value="${esc(S.name || "")}" placeholder="${S.lang === "es" ? "Tu nombre completo" : "Your full name"}" autocomplete="name">
      <div class="cert-wrap" id="certWrap">${certSVG(S.name || "")}</div>
      <div class="actions">
        <button class="btn" id="certCopy">${tr(UI.certCopy)}</button>
        ${standalone ? `<button class="btn gold" id="certPng">${tr(UI.certPng)}</button>` : ""}
      </div>
      <p style="color:var(--muted);font-size:14px;margin-top:12px">${standalone ? "" : tr(UI.certShot) + " "}${tr(UI.certNote)}</p>
    </article><div style="height:140px"></div>`;
  const inp = document.getElementById("certName");
  inp.oninput = () => { S.name = inp.value.slice(0, 60); save(); document.getElementById("certWrap").innerHTML = certSVG(S.name); };
  document.getElementById("certCopy").onclick = e => {
    const txt = S.lang === "es"
      ? `🎓 Completé el programa gratuito "Microsoft Fabric para Ingeniería de Datos: de cero a experto" con Alquimio (HexaMind Lab): ${ALL.length} lecciones sobre Lakehouse, Spark, pipelines, Warehouse, Direct Lake, Real-Time Intelligence, gobierno y CI/CD. Código: ${certCode(S.name || "")}`
      : `🎓 I completed the free program "Microsoft Fabric for Data Engineering: from zero to expert" with Alquimio (HexaMind Lab): ${ALL.length} lessons on Lakehouse, Spark, pipelines, Warehouse, Direct Lake, Real-Time Intelligence, governance and CI/CD. Code: ${certCode(S.name || "")}`;
    const ok = () => { e.target.textContent = tr(UI.copied); setTimeout(() => e.target.textContent = tr(UI.certCopy), 1600); };
    try { navigator.clipboard.writeText(txt).then(ok, () => { inp.value = txt; inp.select(); }); } catch (err) { inp.value = txt; inp.select(); }
  };
  const png = document.getElementById("certPng");
  if (png) png.onclick = () => {
    const svg = document.getElementById("certSvg").outerHTML;
    const img = new Image();
    img.onload = () => {
      const c = document.createElement("canvas"); c.width = 2000; c.height = 1400;
      c.getContext("2d").drawImage(img, 0, 0, 2000, 1400);
      c.toBlob(b => { const a = document.createElement("a"); a.href = URL.createObjectURL(b); a.download = "certificado-alquimio-fabric.png"; document.body.appendChild(a); a.click(); a.remove(); });
    };
    img.src = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(svg);
  };
  bindMascot(document.getElementById("dockWiz"), document.getElementById("bubble"), document.getElementById("bubbleText"));
  document.getElementById("dock").classList.toggle("hidden", S.dock === "hidden");
  confetti();
  say(S.lang === "es" ? "¡Felicidades, colega! Ahora eres oficialmente un <b>alquimista de datos</b>. Escribe tu nombre y presume tu certificado. 🎓" : "Congratulations, colleague! You're now officially a <b>data alchemist</b>. Type your name and show off your certificate. 🎓", "happy");
  window.scrollTo(0, 0);
}

/* =========================================================
   7) Arranque y rutas (#home, #l1-1 …)
   ========================================================= */
document.getElementById("dockWiz").innerHTML = wizardSVG();
document.getElementById("dockWiz").onclick = () => {
  const d = document.getElementById("dock");
  if (d.classList.contains("min")) { d.classList.remove("min"); }
  const s = currentLesson && currentLesson.steps[idx];
  say(s && s.say && Math.random() > .5 ? tr(s.say) : tr(pick(TIPS)), "happy");
};
document.getElementById("bubbleX").onclick = () => document.getElementById("bubble").classList.remove("show");
function route() {
  const h = location.hash.slice(1);
  view = h === "certificado" ? "cert" : "";
  if (ALL.some(l => l.id === h)) renderLesson(h); else if (view === "cert") renderCert(); else renderHome();
}
function renderAll() { renderHeader(); renderFooter(); if (currentLesson) { const keep = idx; renderLesson(currentLesson.id); idx = Math.min(keep, currentLesson.steps.length - 1); stepOK = stepOK.map((v, i) => v || i < idx); renderStep(); } else if (view === "cert") renderCert(); else renderHome(); }
addEventListener("hashchange", () => { if (ALL.length) route(); });
renderHeader(); renderFooter();
app.innerHTML = `<div class="card" style="margin-top:40px;text-align:center"><span class="kicker">🪄 ${S.lang === "es" ? "Preparando el caldero…" : "Warming up the cauldron…"}</span></div>`;
loadCourse().then(route).catch(err => {
  console.error(err);
  app.innerHTML = `<div class="card" style="margin-top:40px"><h2>⚠️ ${tr(UI.loadErr)}</h2><p>${tr(UI.loadHelp)}</p><pre>${esc(err.message)}</pre></div>`;
});
