import streamlit as st
from PIL import Image

# ==================================================
# KONFIGURASI HALAMAN
# ==================================================

st.set_page_config(
    page_title="Dashboard Prediksi Status Pinjaman Nasabah",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# LOAD LOGO
# ==================================================

logo = Image.open("logo.png")

# ==================================================
# CSS
# ==================================================

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
135deg,
#dfefff 0%,
#eef6ff 35%,
#ffffff 100%
);

}

.block-container{

max-width:1200px;
padding-top:25px;

}

.hero{

background:white;
border-radius:25px;
padding:45px;
box-shadow:0 8px 30px rgba(0,0,0,.12);

}

.hero img{

display:block;
margin:auto;

}

.judul{

text-align:center;
font-size:60px;
font-weight:800;
color:#0B3C78;
margin-top:15px;

}

.subjudul{

text-align:center;
font-size:32px;
font-weight:700;
color:#17375E;
margin-top:5px;

}

.metode{

text-align:center;
font-size:22px;
color:#666;
margin-top:12px;

}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HERO
# ==================================================

st.markdown('<div class="hero">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image(logo, width=280)

st.markdown("""
<div class="judul">
SELAMAT DATANG
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subjudul">
Dashboard Prediksi Status Pinjaman Nasabah
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="metode">
Menggunakan Algoritma Random Forest
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
