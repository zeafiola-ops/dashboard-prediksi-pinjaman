import streamlit as st
from PIL import Image

# ==========================
# KONFIGURASI HALAMAN
# ==========================

st.set_page_config(
    page_title="Dashboard Prediksi Status Pinjaman Nasabah",
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

/* Logo */

.logo{

text-align:center;

margin-top:20px;

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
Dashboard Prediksi<br>
Status Pinjaman Nasabah
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p class="subtitle">
Menggunakan Metode Random Forest
</p>
""", unsafe_allow_html=True)

st.write("")
st.write("")
