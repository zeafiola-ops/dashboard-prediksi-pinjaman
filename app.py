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
# BOOTSTRAP ICON
# ==========================================

st.markdown("""
<link rel="stylesheet"
href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
""", unsafe_allow_html=True)
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
# ==========================================
# DASHBOARD PENELITIAN
# ==========================================
st.markdown("""
<div class="dashboard-card">

    <div class="dashboard-icon">
        <i class="bi bi-diagram-3-fill"></i>
    </div>

    <div class="dashboard-content">

        <h2>Dashboard Penelitian</h2>

        <p>
        Dashboard Prediksi Status Pinjaman Nasabah merupakan media visualisasi
        interaktif yang dikembangkan sebagai implementasi penelitian mengenai
        prediksi status pinjaman nasabah menggunakan algoritma
        <b>Random Forest</b>. Dashboard ini dirancang untuk menyajikan hasil
        analisis secara informatif sehingga memudahkan pengguna dalam memahami
        pola data, hasil prediksi, serta performa model yang telah dibangun.
        </p>

        <p>
        Informasi yang disajikan meliputi ringkasan jumlah data nasabah,
        distribusi status pinjaman, visualisasi hasil prediksi dalam bentuk
        diagram lingkaran (Pie Chart), diagram batang (Bar Chart),
        histogram distribusi jumlah pinjaman, serta tabel hasil prediksi.
        Selain itu, dashboard juga menampilkan hasil evaluasi model sebagai
        bahan analisis terhadap tingkat kinerja algoritma Random Forest
        dalam mengklasifikasikan status pinjaman nasabah.
        </p>

        <p>
        Dengan adanya dashboard ini, pengguna dapat melakukan analisis data
        secara lebih cepat, interaktif, dan mudah dipahami sehingga dapat
        mendukung proses pengambilan keputusan berdasarkan hasil prediksi
        yang dihasilkan oleh model machine learning.
        </p>

    </div>
</div>
""", unsafe_allow_html=True)


