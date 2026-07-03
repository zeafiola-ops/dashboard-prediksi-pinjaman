import streamlit as st
from PIL import Image
import base64

st.set_page_config(
    page_title="Dashboard Prediksi Status Pinjaman Nasabah",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)
import os

# ==========================
# Load CSS
# ==========================
def load_css():
    if os.path.exists("style.css"):
        with open("style.css", "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ==========================
# Sidebar
# ==========================

st.sidebar.title("Dashboard")

menu = st.sidebar.radio(
    "Menu",
    [
        "Home",
        "Dataset",
        "Visualisasi",
        "Prediksi",
        "Evaluasi Model",
        "Tentang"
    ]
)

# ==========================
# HOME
# ==========================

if menu=="Home":

    logo = Image.open("logo.png")

   col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image(logo, width=320)
    st.markdown("""
    <div class="judul">
    Dashboard Prediksi<br>
    Status Pinjaman Nasabah
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="subjudul">
    Menggunakan Metode Random Forest
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    #=========================
    # CARD DESKRIPSI
    #=========================

    st.markdown("""

    <div class="card">

    <h3>Dashboard Penelitian</h3>

    <p>

    Dashboard ini merupakan media visualisasi yang dikembangkan
    untuk menampilkan hasil prediksi status pinjaman nasabah
    menggunakan algoritma Random Forest.

    Dashboard menyajikan informasi penelitian secara interaktif,
    meliputi ringkasan data, visualisasi,
    hasil prediksi,
    serta evaluasi model sehingga mempermudah proses analisis
    dan interpretasi hasil penelitian.

    </p>

    </div>

    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <h2 class='judul2'>
    Informasi Penelitian
    </h2>
    """, unsafe_allow_html=True)

    col1,col2=st.columns(2)

    with col1:

        st.markdown("""

        <div class="info-card">

        <h4>Judul Penelitian</h4>

        <p>

        Prediksi Status Pinjaman Nasabah
        Menggunakan Algoritma Random Forest

        </p>

        </div>

        """,unsafe_allow_html=True)

        st.markdown("""

        <div class="info-card">

        <h4>Sumber Data</h4>

        <p>

        Dataset diperoleh dari Kaggle.

        </p>

        <a href="https://www.kaggle.com/datasets/ardava/dataset-klasifikasi-status-pinjaman"
        target="_blank">

        Dataset Klasifikasi Status Pinjaman

        </a>

        </div>

        """,unsafe_allow_html=True)

        st.markdown("""

        <div class="info-card">

        <h4>Fokus Penelitian</h4>

        <p>

        Mengklasifikasikan status pinjaman
        nasabah berdasarkan data historis
        menggunakan algoritma Random Forest.

        </p>

        </div>

        """,unsafe_allow_html=True)

    with col2:

        st.markdown("""

        <div class="info-card">

        <h4>Metode</h4>

        <p>

        Random Forest

        </p>

        </div>

        """,unsafe_allow_html=True)

        st.markdown("""

        <div class="info-card">

        <h4>Jumlah Data</h4>

        <p>

        49.700 Data

        </p>

        </div>

        """,unsafe_allow_html=True)

        st.markdown("""

        <div class="info-card">

        <h4>Tujuan Penelitian</h4>

        <p>

        Memprediksi status pinjaman nasabah
        (Lancar / Tidak Lancar)
        sehingga dapat membantu
        proses pengambilan keputusan
        pemberian pinjaman.

        </p>

        </div>

        """,unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.link_button(
        "Lihat Dataset Kaggle",
        "https://www.kaggle.com/datasets/ardava/dataset-klasifikasi-status-pinjaman"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <hr>

    <center>

    Program Studi Sistem Informasi<br>

    Peminatan Business Intelligence

    <br><br>

    2026
/* =========================================================
   IMPORT FONT
=========================================================*/

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

/* =========================================================
   BACKGROUND
=========================================================*/

.stApp{

background:linear-gradient(
135deg,
#edf5ff 0%,
#d9ebff 35%,
#c6e3ff 100%);

}


/* =========================================================
   SIDEBAR
=========================================================*/

section[data-testid="stSidebar"]{

background:#0F4C81;

}

section[data-testid="stSidebar"] *{

color:white;

}


/* =========================================================
   LOGO
=========================================================*/

img{

display:block;
margin-left:auto;
margin-right:auto;

}


/* =========================================================
   JUDUL
=========================================================*/

.judul{

text-align:center;

font-size:42px;

font-weight:700;

color:#0F4C81;

line-height:55px;

margin-top:10px;

}


.subjudul{

text-align:center;

font-size:20px;

color:#555;

margin-bottom:40px;

}


/* =========================================================
   SUB TITLE
=========================================================*/

.judul2{

text-align:center;

color:#0F4C81;

font-size:32px;

font-weight:700;

margin-bottom:25px;

}


/* =========================================================
   CARD BESAR
=========================================================*/

.card{

background:white;

padding:35px;

border-radius:25px;

box-shadow:
0px 10px 30px rgba(0,0,0,.10);

transition:.4s;

margin-bottom:30px;

}


.card:hover{

transform:translateY(-8px);

box-shadow:
0px 18px 45px rgba(0,0,0,.15);

}


.card h3{

text-align:center;

color:#0F4C81;

font-size:28px;

margin-bottom:20px;

}


.card p{

font-size:18px;

line-height:34px;

text-align:justify;

color:#444;

}


/* =========================================================
   INFO CARD
=========================================================*/

.info-card{

background:white;

padding:25px;

border-radius:20px;

margin-bottom:25px;

box-shadow:
0 10px 25px rgba(0,0,0,.08);

transition:.3s;

border-left:8px solid #0F4C81;

}


.info-card:hover{

transform:scale(1.02);

box-shadow:
0 15px 35px rgba(0,0,0,.15);

}


.info-card h4{

font-size:24px;

color:#0F4C81;

margin-bottom:12px;

}


.info-card p{

font-size:17px;

color:#555;

line-height:30px;

}


/* =========================================================
   LINK
=========================================================*/

.info-card a{

text-decoration:none;

font-size:17px;

font-weight:600;

color:#0077ff;

}


.info-card a:hover{

color:#003cff;

}


/* =========================================================
   BUTTON
=========================================================*/

.stButton>button{

background:#0F4C81;

color:white;

border:none;

padding:14px;

border-radius:12px;

font-size:17px;

font-weight:600;

transition:.3s;

width:100%;

}


.stButton>button:hover{

background:#2D74B2;

transform:scale(1.03);

}


/* =========================================================
   FOOTER
=========================================================*/

hr{

margin-top:40px;

margin-bottom:30px;

}


center{

font-size:17px;

color:#666;

line-height:30px;

}


/* =========================================================
   ANIMATION
=========================================================*/

.card{

animation:fade 1s;

}

.info-card{

animation:fade .8s;

}


@keyframes fade{

from{

opacity:0;

transform:translateY(40px);

}

to{

opacity:1;

transform:translateY(0px);

}

}


/* =========================================================
   RESPONSIVE
=========================================================*/

@media(max-width:768px){

.judul{

font-size:30px;

line-height:40px;

}

.subjudul{

font-size:17px;

}

.card p{

font-size:16px;

}

.info-card h4{

font-size:20px;

}

}
    </center>

    """,unsafe_allow_html=True)
