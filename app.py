import streamlit as st
import pandas as pd
import plotly.express as px
import base64

# ==========================
# KONFIGURASI HALAMAN
# ==========================

st.set_page_config(
    page_title="Dashboard Prediksi Random Forest",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# LOAD DATA
# ==========================

df = pd.read_excel("hasil_prediksi_deployment_google_sheets(9).xlsx")

# ==========================
# LOAD LOGO
# ==========================

def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo = get_base64("logo.png")

# ==========================
# CSS
# ==========================

st.markdown(f"""
<style>

#MainMenu{{visibility:hidden;}}
header{{visibility:hidden;}}
footer{{visibility:hidden;}}

.stApp{{
    background:linear-gradient(180deg,#eef5ff 0%,#ffffff 100%);
}}

.block-container{{
    padding-top:2rem;
    max-width:1200px;
}}

.hero{{
    text-align:center;
}}

.hero img{{
    width:300px;
}}

.hero h1{{
    color:#0B3C78;
    font-size:55px;
    margin-top:15px;
    margin-bottom:0px;
}}

.hero h3{{
    color:#666;
    font-size:25px;
    font-weight:400;
}}

.dashboard-box{{
    margin-top:40px;
    background:white;
    border-radius:22px;
    padding:35px;
    box-shadow:0 10px 30px rgba(0,0,0,.10);
}}

.dashboard-box:hover{{
    transform:translateY(-5px);
    transition:.3s;
}}

.dashboard-title{{
    color:#0B3C78;
    font-size:34px;
    font-weight:bold;
    margin-bottom:20px;
}}

.dashboard-text{{
    color:#444;
    font-size:18px;
    line-height:1.9;
    text-align:justify;
}}

</style>

<div class="hero">

<img src="data:image/png;base64,{logo}">

<h1>SELAMAT DATANG</h1>

<h3>
Dashboard Prediksi Status Pinjaman Nasabah
<br>
Menggunakan Algoritma Random Forest
</h3>

</div>

<div class="dashboard-box">

<div class="dashboard-title">
Dashboard Penelitian
</div>

<div class="dashboard-text">

Dashboard Prediksi Status Pinjaman Nasabah merupakan media visualisasi interaktif
yang dikembangkan untuk menyajikan hasil penelitian menggunakan algoritma
Random Forest.

Dashboard ini menampilkan ringkasan data, statistik penelitian,
visualisasi hasil prediksi, evaluasi model, serta informasi dataset
yang digunakan sehingga memudahkan proses analisis, interpretasi hasil,
dan mendukung pengambilan keputusan secara lebih efektif.

</div>

</div>

""", unsafe_allow_html=True)
