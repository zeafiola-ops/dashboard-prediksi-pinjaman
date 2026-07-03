import streamlit as st
from PIL import Image

# ==========================
# KONFIGURASI HALAMAN
# ==========================

st.set_page_config(
    page_title="DASHBOARD PREDIKSI PINJAMAN  METODE RANDOM FOREST",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# CSS
# ==========================

st.markdown("""
<style>

/* Hilangkan menu bawaan */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Background */
.stApp{

background:linear-gradient(180deg,#edf5ff,#ffffff);

}

/* Sidebar */

[data-testid="stSidebar"]{

background:#0b3c78;

}

[data-testid="stSidebar"] *{

color:white;

}

/* =======================
   LOGO
======================= */

.logo-container{

display:flex;

justify-content:center;

align-items:center;

width:100%;

margin-top:20px;

margin-bottom:20px;

}

.logo{

display:block;

width:320px;

height:auto;

margin:0 auto;

}

/* Judul */

.title{

font-size:58px;

font-weight:bold;

color:#0b3c78;

text-align:center;

line-height:70px;

margin-top:10px;

}

.subtitle{

font-size:28px;

color:#444;

text-align:center;

margin-bottom:40px;

}

/* Card */

.card{

background:white;

padding:35px;

border-radius:20px;

box-shadow:0 10px 25px rgba(0,0,0,.15);

margin-bottom:35px;

}

/* Judul Card */

.card h2{

color:#0b3c78;

}

/* Footer */

.footer{

background:#0b3c78;

padding:25px;

border-radius:15px;

color:white;

text-align:center;

margin-top:50px;

}

</style>
""", unsafe_allow_html=True)


# =====================================================
# HERO SECTION
# =====================================================

from PIL import Image
import base64

# ==============================
# LOGO TENGAH
# ==============================

logo = Image.open("logo.png")

def get_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo_base64 = get_base64("logo.png")

st.markdown(f"""
<div class="logo-container">

<img src="data:image/png;base64,{logo_base64}" class="logo">

</div>
""", unsafe_allow_html=True)
st.markdown("""
<h1 class="title">
 Selamat Datang<br>

</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p class="subtitle">
Dashboard ini menyajikan hasil prediksi status pinjaman nasabah <br>
   menggunakan algoritma Random Forest secara interaktif.
</p>

""", unsafe_allow_html=True)
st.markdown("""
<div class="dashboard-card">

<div class="dashboard-icon">
📊
</div>

<div class="dashboard-text">

<b>Dashboard ini merupakan media visualisasi yang dikembangkan untuk
menampilkan hasil prediksi status pinjaman nasabah menggunakan metode
Random Forest.</b>

<br><br>

Dashboard menyajikan informasi penelitian secara interaktif,
meliputi ringkasan data, hasil prediksi, visualisasi,
dan evaluasi model sehingga memudahkan proses analisis
serta interpretasi hasil penelitian.

</div>

</div>
""", unsafe_allow_html=True)
/* =========================
   CARD DASHBOARD
========================= */

.dashboard-card{
    background:white;
    border-radius:20px;
    padding:30px;
    box-shadow:0 8px 20px rgba(0,0,0,0.12);
    display:flex;
    align-items:center;
    gap:25px;
    margin-top:30px;
    margin-bottom:40px;
}

.dashboard-icon{
    width:90px;
    height:90px;
    background:#0B3C78;
    border-radius:15px;
    display:flex;
    align-items:center;
    justify-content:center;
    color:white;
    font-size:42px;
    flex-shrink:0;
}

.dashboard-text{
    color:#333;
    font-size:18px;
    line-height:1.8;
}
st.write("")
st.write("")
