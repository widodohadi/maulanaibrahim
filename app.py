import base64
from pathlib import Path

import streamlit as st

# ======================================================================
# ✏️  EDIT DATA DI SINI SAJA — sisanya otomatis
# ======================================================================
PROFILE = {
    "name": "Maulana Ibrahim",
    "role": "Developer • Creator • Explorer",
    "tagline": "Saya membangun hal-hal digital yang rapi, bermanfaat, dan enak dilihat — "
               "dan suka mencari inspirasi di puncak gunung.",
    "location": "Medan, Sumatera Utara",
    "email": "maulanaibrahim12@gmail.com",
    "photo": "assets/foto.jpg",
    "cv_url": "#",
}

ABOUT = (
    "Halo! Saya Maulana Ibrahim. Saya tertarik pada teknologi, desain, dan petualangan alam. "
    "Bagi saya, membuat sebuah produk itu seperti mendaki gunung: butuh persiapan, konsistensi, "
    "dan menikmati setiap langkahnya. Ganti teks ini dengan cerita singkat tentang dirimu."
)

STATS = [("10+", "Proyek"), ("3+", "Tahun Belajar"), ("5+", "Tools & Bahasa"), ("∞", "Rasa Ingin Tahu")]

SKILLS = {
    "Python": 85,
    "HTML & CSS": 80,
    "JavaScript": 70,
    "Data Analysis": 75,
    "UI / UX Design": 65,
}

TOOLS = ["Python", "Streamlit", "Pandas", "Git", "Figma", "SQL", "VS Code", "Canva"]

PROJECTS = [
    {"icon": "📊", "title": "Dashboard Analisis Data",
     "desc": "Dashboard interaktif untuk memvisualisasikan data dengan grafik yang mudah dipahami.",
     "tags": ["Python", "Pandas", "Streamlit"], "link": "#"},
    {"icon": "🛒", "title": "Website Toko Online",
     "desc": "Toko online responsif dengan katalog produk, keranjang, dan tampilan modern.",
     "tags": ["HTML", "CSS", "JavaScript"], "link": "#"},
    {"icon": "🤖", "title": "Chatbot Asisten",
     "desc": "Chatbot sederhana yang menjawab pertanyaan umum secara otomatis.",
     "tags": ["Python", "AI", "API"], "link": "#"},
]

TIMELINE = [
    ("2026", "Proyek Portofolio", "Membangun portofolio pribadi dengan Streamlit."),
    ("2025", "Pengembangan Skill", "Fokus pada Python, data, dan pengembangan web."),
    ("2024", "Mulai Perjalanan", "Mulai belajar pemrograman dan membuat proyek pertama."),
]

SOCIALS = [
    ("Instagram", "https://instagram.com/"),
    ("GitHub", "https://github.com/"),
    ("LinkedIn", "https://linkedin.com/"),
]

# ======================================================================
st.set_page_config(page_title=f"{PROFILE['name']} • Portfolio", page_icon="⛰️", layout="wide")


def img_b64(path: str) -> str:
    p = Path(__file__).parent / path
    if not p.exists():
        return ""
    return base64.b64encode(p.read_bytes()).decode()


photo = img_b64(PROFILE["photo"])
photo_src = f"data:image/jpeg;base64,{photo}" if photo else ""

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Inter:wght@300;400;500&display=swap');

:root{
  --bg:#0b0b1a; --card:rgba(255,255,255,.05); --line:rgba(255,255,255,.10);
  --txt:#e9e9f5; --mut:#a0a0c0; --a1:#8b5cf6; --a2:#22d3ee; --a3:#f472b6;
}
html{scroll-behavior:smooth}
.stApp{
  background:
    radial-gradient(900px 500px at 10% -10%, rgba(139,92,246,.28), transparent 60%),
    radial-gradient(800px 500px at 100% 10%, rgba(34,211,238,.18), transparent 60%),
    radial-gradient(700px 500px at 50% 110%, rgba(244,114,182,.15), transparent 60%),
    var(--bg);
  color:var(--txt); font-family:'Inter',sans-serif;
}
header[data-testid="stHeader"], footer, #MainMenu {display:none !important}
.block-container{max-width:1100px; padding-top:5.5rem; padding-bottom:3rem}
h1,h2,h3,h4{font-family:'Space Grotesk',sans-serif !important; color:var(--txt)}

/* NAVBAR */
.nav{position:fixed; top:14px; left:50%; transform:translateX(-50%); z-index:999;
  display:flex; gap:6px; padding:8px 12px; border-radius:999px;
  background:rgba(20,20,40,.65); backdrop-filter:blur(14px); border:1px solid var(--line)}
.nav a{color:var(--mut); text-decoration:none; font-size:.88rem; padding:6px 14px; border-radius:999px; transition:.25s}
.nav a:hover{color:#fff; background:linear-gradient(90deg,var(--a1),var(--a2))}

/* HERO */
.hero{display:grid; grid-template-columns:1.25fr .75fr; gap:40px; align-items:center; min-height:76vh}
.badge{display:inline-block; padding:6px 14px; border:1px solid var(--line); border-radius:999px;
  background:var(--card); color:var(--a2); font-size:.82rem; margin-bottom:18px}
.hero h1{font-size:4.2rem; line-height:1.02; margin:0 0 14px; font-weight:700}
.grad{background:linear-gradient(90deg,var(--a1),var(--a2),var(--a3)); -webkit-background-clip:text;
  -webkit-text-fill-color:transparent; background-size:200% auto; animation:shine 6s linear infinite}
@keyframes shine{to{background-position:200% center}}
.role{font-family:'Space Grotesk'; font-size:1.25rem; color:var(--a2); letter-spacing:.5px; margin-bottom:14px}
.tag{color:var(--mut); font-size:1.05rem; line-height:1.7; max-width:520px}
.btns{display:flex; gap:12px; margin-top:28px; flex-wrap:wrap}
.btn{padding:12px 26px; border-radius:12px; text-decoration:none; font-weight:500; transition:.25s}
.btn.p{background:linear-gradient(90deg,var(--a1),var(--a2)); color:#fff; box-shadow:0 8px 30px rgba(139,92,246,.35)}
.btn.p:hover{transform:translateY(-3px); box-shadow:0 12px 36px rgba(34,211,238,.35)}
.btn.s{border:1px solid var(--line); color:var(--txt); background:var(--card)}
.btn.s:hover{border-color:var(--a2); transform:translateY(-3px)}

.photo-wrap{position:relative; width:min(340px,100%); margin:auto; animation:float 6s ease-in-out infinite}
.photo-wrap::before{content:""; position:absolute; inset:-14px; border-radius:36px;
  background:linear-gradient(135deg,var(--a1),var(--a2),var(--a3)); filter:blur(26px); opacity:.55}
.photo-wrap img{position:relative; width:100%; aspect-ratio:4/5; object-fit:cover; object-position:top;
  border-radius:32px; border:1px solid var(--line); display:block}
.chip{position:absolute; padding:8px 14px; border-radius:14px; font-size:.8rem;
  background:rgba(20,20,40,.75); backdrop-filter:blur(10px); border:1px solid var(--line)}
.chip.c1{left:-22px; bottom:70px} .chip.c2{right:-18px; top:40px}
@keyframes float{50%{transform:translateY(-12px)}}

/* SECTIONS */
.sec{padding-top:70px}
.eyebrow{color:var(--a2); font-size:.85rem; letter-spacing:3px; text-transform:uppercase}
.title{font-size:2.5rem; font-weight:700; margin:6px 0 26px}
.glass{background:var(--card); border:1px solid var(--line); border-radius:20px; padding:26px;
  backdrop-filter:blur(10px); transition:.3s}
.glass:hover{transform:translateY(-6px); border-color:rgba(139,92,246,.6); box-shadow:0 18px 40px rgba(0,0,0,.35)}
.about-txt{color:var(--mut); font-size:1.08rem; line-height:1.85}
.stats{display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin-top:24px}
.stat{text-align:center; padding:18px 8px; border-radius:16px; background:var(--card); border:1px solid var(--line)}
.stat b{display:block; font-family:'Space Grotesk'; font-size:1.8rem}
.stat span{color:var(--mut); font-size:.82rem}

.skill{margin-bottom:18px}
.skill .row{display:flex; justify-content:space-between; font-size:.95rem; margin-bottom:7px}
.bar{height:8px; border-radius:99px; background:rgba(255,255,255,.08); overflow:hidden}
.fill{height:100%; border-radius:99px; background:linear-gradient(90deg,var(--a1),var(--a2));
  animation:grow 1.4s ease-out both}
@keyframes grow{from{width:0}}
.pill{display:inline-block; margin:4px 6px 4px 0; padding:7px 14px; border-radius:999px; font-size:.85rem;
  border:1px solid var(--line); background:rgba(255,255,255,.04); color:var(--txt); transition:.25s}
.pill:hover{background:linear-gradient(90deg,var(--a1),var(--a2)); border-color:transparent}

.pj-ico{font-size:2.2rem; margin-bottom:10px}
.pj h3{font-size:1.25rem; margin:0 0 8px}
.pj p{color:var(--mut); font-size:.95rem; line-height:1.65}
.pj a{color:var(--a2); text-decoration:none; font-size:.9rem}
.tg{font-size:.75rem; color:var(--a3); margin-right:10px}

.tl{border-left:2px solid var(--line); margin-left:8px; padding-left:28px}
.tl-i{position:relative; margin-bottom:28px}
.tl-i::before{content:""; position:absolute; left:-37px; top:6px; width:16px; height:16px; border-radius:50%;
  background:linear-gradient(135deg,var(--a1),var(--a2)); box-shadow:0 0 14px var(--a1)}
.tl-i .y{font-family:'Space Grotesk'; color:var(--a2); font-size:.9rem}
.tl-i h4{margin:2px 0 4px; font-size:1.15rem}
.tl-i p{color:var(--mut); margin:0}

.contact{text-align:center; padding:50px 24px}
.contact h2{font-size:2.4rem; margin:0 0 10px}
.contact p{color:var(--mut)}
.soc{display:flex; gap:12px; justify-content:center; margin-top:22px; flex-wrap:wrap}
.foot{text-align:center; color:var(--mut); font-size:.85rem; margin-top:50px}

@media(max-width:820px){
  .hero{grid-template-columns:1fr; text-align:center; min-height:auto}
  .hero h1{font-size:2.8rem} .tag{margin:auto}
  .btns{justify-content:center} .stats{grid-template-columns:repeat(2,1fr)}
  .nav{width:92%; justify-content:center; overflow-x:auto}
  .chip{display:none} .photo-wrap{margin-top:20px}
}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# NAVBAR
st.markdown(
    """<div class="nav">
    <a href="#home">Home</a><a href="#about">Tentang</a><a href="#skills">Skill</a>
    <a href="#projects">Proyek</a><a href="#journey">Perjalanan</a><a href="#contact">Kontak</a></div>""",
    unsafe_allow_html=True,
)

# HERO
first, last = PROFILE["name"].split(" ", 1)
photo_html = (
    f"""<div class="photo-wrap"><img src="{photo_src}" alt="{PROFILE['name']}">
        <div class="chip c1">⛰️ Pecinta Alam</div><div class="chip c2">💻 Tech Enthusiast</div></div>"""
    if photo_src else ""
)
st.markdown(
    f"""<div id="home" class="hero">
      <div>
        <div class="badge">👋 Halo, selamat datang di portofolio saya</div>
        <h1>Saya <span class="grad">{first}<br>{last}</span></h1>
        <div class="role">{PROFILE['role']}</div>
        <div class="tag">{PROFILE['tagline']}</div>
        <div class="btns">
          <a class="btn p" href="#projects">Lihat Proyek</a>
          <a class="btn s" href="#contact">Hubungi Saya</a>
          <a class="btn s" href="{PROFILE['cv_url']}">Unduh CV</a>
        </div>
      </div>
      {photo_html}
    </div>""",
    unsafe_allow_html=True,
)

# ABOUT
stats_html = "".join(f"<div class='stat'><b class='grad'>{n}</b><span>{l}</span></div>" for n, l in STATS)
st.markdown(
    f"""<div id="about" class="sec">
      <div class="eyebrow">Tentang</div><div class="title">Sedikit tentang saya</div>
      <div class="glass"><div class="about-txt">{ABOUT}</div>
      <div class="about-txt" style="margin-top:12px">📍 {PROFILE['location']}</div>
      <div class="stats">{stats_html}</div></div></div>""",
    unsafe_allow_html=True,
)

# SKILLS
bars = "".join(
    f"<div class='skill'><div class='row'><span>{k}</span><span>{v}%</span></div>"
    f"<div class='bar'><div class='fill' style='width:{v}%'></div></div></div>"
    for k, v in SKILLS.items()
)
pills = "".join(f"<span class='pill'>{t}</span>" for t in TOOLS)
st.markdown(
    f"""<div id="skills" class="sec"><div class="eyebrow">Keahlian</div>
    <div class="title">Skill &amp; Tools</div></div>""",
    unsafe_allow_html=True,
)
c1, c2 = st.columns([1.2, 1], gap="large")
with c1:
    st.markdown(f"<div class='glass'>{bars}</div>", unsafe_allow_html=True)
with c2:
    st.markdown(
        f"<div class='glass'><h4 style='margin-top:0'>Tools favorit</h4>{pills}</div>",
        unsafe_allow_html=True,
    )

# PROJECTS
st.markdown(
    """<div id="projects" class="sec"><div class="eyebrow">Karya</div>
    <div class="title">Proyek pilihan</div></div>""",
    unsafe_allow_html=True,
)
cols = st.columns(len(PROJECTS), gap="medium")
for col, p in zip(cols, PROJECTS):
    tags = "".join(f"<span class='tg'>#{t}</span>" for t in p["tags"])
    with col:
        st.markdown(
            f"""<div class="glass pj"><div class="pj-ico">{p['icon']}</div>
            <h3>{p['title']}</h3><p>{p['desc']}</p><div>{tags}</div>
            <p style="margin-top:14px"><a href="{p['link']}">Lihat proyek →</a></p></div>""",
            unsafe_allow_html=True,
        )

# JOURNEY
items = "".join(
    f"<div class='tl-i'><div class='y'>{y}</div><h4>{t}</h4><p>{d}</p></div>" for y, t, d in TIMELINE
)
st.markdown(
    f"""<div id="journey" class="sec"><div class="eyebrow">Perjalanan</div>
    <div class="title">Langkah demi langkah</div><div class="tl">{items}</div></div>""",
    unsafe_allow_html=True,
)

# CONTACT
socs = "".join(f"<a class='btn s' href='{u}' target='_blank'>{n}</a>" for n, u in SOCIALS)
st.markdown(
    f"""<div id="contact" class="sec"><div class="glass contact">
      <div class="eyebrow">Kontak</div>
      <h2>Mari <span class="grad">berkolaborasi</span> ✨</h2>
      <p>Punya ide, proyek, atau sekadar ingin menyapa? Kirim pesan kapan saja.</p>
      <div class="btns" style="justify-content:center">
        <a class="btn p" href="mailto:{PROFILE['email']}">✉️ {PROFILE['email']}</a></div>
      <div class="soc">{socs}</div></div>
      <div class="foot">© 2026 {PROFILE['name']} • Dibuat dengan Streamlit &amp; ☕</div></div>""",
    unsafe_allow_html=True,
)
