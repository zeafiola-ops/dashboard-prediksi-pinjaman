import streamlit as st
from PIL import Image
import base64

# ==========================================================
# KONFIGURASI
# ==========================================================

st.set_page_config(
    page_title="Dashboard Prediksi Random Forest",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# LOAD LOGO
# ==========================================================

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo = get_base64("logo.png")
st.markdown(f"""
<div class="hero">

<img src="data:image/png;base64,{logo}">

<h1>
SELAMAT DATANG
</h1>

<p> <b>
Visualisasi Prediksi Status Pinjaman Nasabah 
Random Forest
</p>

</div>

""",unsafe_allow_html=True)
# ==========================================================
# CSS
# ==========================================================

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

<style>

html,body,[class*="css"]{
font-family:'Poppins',sans-serif;
}

/* Hilangkan menu bawaan */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* Background */

.stApp{

background:linear-gradient(
180deg,
#eef6ff 0%,
#ffffff 100%
);

}

/* Sidebar */

[data-testid="stSidebar"]{

background:#0B3C78;

}

[data-testid="stSidebar"] *{

color:white;

}

/* Hero */

.hero{

text-align:center;

padding-top:20px;

padding-bottom:30px;

}

.hero img{

width:320px;

}

.hero h1{

font-size:58px;

font-weight:800;

color:#0B3C78;

margin-top:20px;

margin-bottom:10px;

line-height:65px;

}

.hero p{

font-size:24px;

color:#666;

}

</style>

""",unsafe_allow_html=True)
/* =========================
CARD DASHBOARD
========================= */

.dashboard-card{

width:92%;

margin:auto;

background:white;

border-radius:22px;

padding:30px;

box-shadow:0px 10px 30px rgba(0,0,0,.12);

display:flex;

align-items:center;

gap:30px;

margin-top:20px;

margin-bottom:45px;

transition:.3s;

}

.dashboard-card:hover{

transform:translateY(-6px);

box-shadow:0px 18px 40px rgba(0,0,0,.18);

}

.dashboard-icon{

width:90px;

height:90px;

background:#0B3C78;

border-radius:18px;

display:flex;

justify-content:center;

align-items:center;

flex-shrink:0;

}

.dashboard-icon img{

width:48px;

}

.dashboard-text{

font-size:18px;

line-height:1.8;

color:#333;

text-align:justify;

}
