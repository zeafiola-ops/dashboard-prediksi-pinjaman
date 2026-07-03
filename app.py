import streamlit as st
from PIL import Image

# =====================================
# KONFIGURASI
# =====================================

st.set_page_config(
    page_title="Dashboard Prediksi Status Pinjaman Nasabah",
    page_icon="📊",
    layout="wide"
)

# =====================================
# LOAD LOGO
# =====================================

logo = Image.open("logo.png")

# =====================================
# CSS
# =====================================

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
#E9F4FF 0%,
#F8FBFF 45%,
white 100%
);

}

.block-container{

max-width:1300px;
padding-top:20px;

}

/* HERO */

.hero{

display:flex;
flex-direction:column;
align-items:center;
justify-content:center;
padding-top:20px;
padding-bottom:40px;

}

.hero img{

width:270px;
display:block;
margin:auto;

}

.hero-title{

font-size:62px;
font-weight:800;
color:#083D77;
margin-top:15px;

}

.hero-sub{

font-size:38px;
font-weight:700;
color:#163D66;

}

.hero-text{

font-size:24px;
color:#666;

}

</style>

""",unsafe_allow_html=True)
# =====================================
# HERO
# =====================================

st.markdown('<div class="hero">',unsafe_allow_html=True)

st.image(logo,width=270)

st.markdown("""
<div class="hero-title">

SELAMAT DATANG

</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="hero-sub">

Dashboard Prediksi Status Pinjaman Nasabah

</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="hero-text">

Menggunakan Algoritma Random Forest

</div>
""",unsafe_allow_html=True)

st.markdown("</div>",unsafe_allow_html=True)
