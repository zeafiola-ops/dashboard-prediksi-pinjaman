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
</style>
""", unsafe_allow_html=True)
/* ===========================
   INFO PENELITIAN
=========================== */

.info-title{

    text-align:center;

    font-size:42px;

    font-weight:700;

    color:#0B3C78;

    margin-top:60px;

    margin-bottom:30px;

}

.info-grid{

    display:grid;

    grid-template-columns:repeat(2,1fr);

    gap:25px;

    width:90%;

    margin:auto;

}

.info-card{

    background:white;

    border-radius:18px;

    padding:25px;

    box-shadow:0 8px 20px rgba(0,0,0,.12);

    transition:all .3s ease;

    border-top:5px solid #0B3C78;

}

.info-card:hover{

    transform:scale(1.05);

    box-shadow:0 15px 35px rgba(0,0,0,.18);

}

.info-card h3{

    color:#0B3C78;

    margin-bottom:12px;

}

.info-card p{

    color:#444;

    line-height:1.8;

}



