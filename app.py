import streamlit as st
from PIL import Image
import base64

# ==========================================
# KONFIGURASI
# ==========================================

st.set_page_config(
    page_title="Dashboard Prediksi Status Pinjaman Nasabah",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# LOAD LOGO
# ==========================================

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo = get_base64("logo.png")

# ==========================================
# CSS
# ==========================================

st.markdown("""
<style>

#MainMenu{visibility:hidden;}
header{visibility:hidden;}
footer{visibility:hidden;}

.stApp{
    background:linear-gradient(
        180deg,
        #EAF4FF 0%,
        #F5F9FF 50%,
        #FFFFFF 100%
    );
}

.block-container{
    max-width:1200px;
    margin:auto;
    padding-top:20px;
}

/* HERO */

.hero{
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    text-align:center;
    padding:30px 0;
}

.hero img{
    width:270px;
}

.hero h1{
    color:#0B3C78;
    font-size:60px;
    margin-top:20px;
    margin-bottom:5px;
    font-weight:800;
}

.hero h2{
    color:#17375E;
    font-size:34px;
    margin:0;
    font-weight:700;
}

.hero p{
    color:#666;
    font-size:22px;
    margin-top:10px;
}

</style>
""", unsafe_allow_html=True)
# ==================================================
# HERO SECTION
# ==================================================

st.markdown(f"""
<div class="hero">

<img src="data:image/png;base64,{logo}">

<h1>
SELAMAT DATANG
</h1>

<h2>
Dashboard Prediksi Status Pinjaman Nasabah
</h2>

<p>
Menggunakan Algoritma Random Forest
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<style>

...
</style>
/* ===============================
   DASHBOARD PENELITIAN
=============================== */

.dashboard-card{

display:flex;
align-items:center;
gap:25px;

background:white;

padding:30px;

margin-top:35px;

margin-bottom:40px;

border-radius:22px;

box-shadow:0px 8px 25px rgba(0,0,0,.12);

transition:0.35s;

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

font-size:42px;

color:white;

}

.dashboard-content h2{

margin:0;

color:#0B3C78;

font-size:34px;

}

.dashboard-content p{

font-size:18px;

line-height:1.8;

color:#444;

text-align:justify;

margin-top:12px;

}
""", unsafe_allow_html=True)
