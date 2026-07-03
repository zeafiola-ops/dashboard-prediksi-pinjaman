import streamlit as st

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Dashboard Prediksi Status Pinjaman Nasabah",
    page_icon="📊",
    layout="wide"
)

# =========================
# CSS
# =========================
st.markdown("""
<style>

html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
}

/* Background */
.stApp{
    background: linear-gradient(to bottom,#f4f8ff,#ffffff);
}

/* Hero */
.hero{
    background: linear-gradient(135deg,#0B3C91,#1565C0);
    padding:45px;
    border-radius:25px;
    text-align:center;
    color:white;
    box-shadow:0px 10px 25px rgba(0,0,0,0.20);
    animation: fadeIn 1.2s;
}

.hero img{
    width:220px;
}

.hero h1{
    font-size:45px;
    margin-top:20px;
    margin-bottom:5px;
}

.hero h3{
    color:#d8e8ff;
    margin-top:0px;
    font-weight:400;
}

.hero p{
    font-size:18px;
    line-height:1.8;
    margin-top:25px;
}

/* Card */
.card{
    background:white;
    padding:30px;
    border-radius:20px;
    box-shadow:0px 8px 18px rgba(0,0,0,0.08);
    transition:0.4s;
    height:100%;
}

.card:hover{
    transform:translateY(-8px);
    box-shadow:0px 15px 25px rgba(0,0,0,.15);
}

/* Judul */
.section-title{
    font-size:32px;
    font-weight:bold;
    color:#0B3C91;
    text-align:center;
    margin-top:50px;
    margin-bottom:30px;
}

/* Animasi */
@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(30px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO
# =========================
st.markdown("""
<div class="hero">

<img src="https://raw.githubusercontent.com/zeafiola-ops/dashboard-prediksi-pinjaman/main/assets/logo.png" width="220">

<h1>Dashboard Prediksi Status Pinjaman Nasabah</h1>

<h3>Metode Random Forest</h3>

<p>

Dashboard ini merupakan media visualisasi yang dikembangkan untuk
menampilkan hasil prediksi status pinjaman nasabah menggunakan
algoritma Random Forest. Dashboard menyajikan informasi penelitian
secara interaktif, meliputi ringkasan data, hasil prediksi,
visualisasi, dan evaluasi model sehingga memudahkan proses analisis
serta interpretasi hasil penelitian.

</p>

</div>

""", unsafe_allow_html=True)
