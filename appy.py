import streamlit as st
from PIL import Image

# ==========================================
# KONFIGURASI
# ==========================================

st.set_page_config(
    page_title="Dashboard Prediksi Status Pinjaman Nasabah",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# LOAD LOGO
# ==========================================

logo = Image.open("logo.png")

# ==========================================
# CSS
# ==========================================

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

header{
visibility:hidden;
}

footer{
visibility:hidden;
}

.stApp{

background:linear-gradient(
180deg,
#EAF4FF 0%,
#F5F9FF 40%,
#FFFFFF 100%
);

}

.block-container{

padding-top:30px;
max-width:1200px;

}

.hero{

text-align:center;

}

.hero img{

width:260px;

}

.hero h1{

font-size:60px;
color:#0B3C78;
margin-bottom:5px;

}

.hero h2{

font-size:32px;
font-weight:700;
color:#17375E;
margin-bottom:10px;

}

.hero p{

font-size:22px;
color:#666;

}

</style>

""", unsafe_allow_html=True)

# ==========================================
# HERO
# ==========================================

st.markdown('<div class="hero">', unsafe_allow_html=True)

st.image(logo, width=260)

st.markdown("""
<h1>SELAMAT DATANG</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h2>Dashboard Prediksi Status Pinjaman Nasabah</h2>
""", unsafe_allow_html=True)

st.markdown("""
<p>Menggunakan Algoritma Random Forest</p>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
