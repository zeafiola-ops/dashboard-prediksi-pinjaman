import streamlit as st
import pandas as pd

# ==========================
# KONFIGURASI HALAMAN
# ==========================
st.set_page_config(
    page_title="Dashboard Prediksi Status Pinjaman",
    page_icon="💳",
    layout="wide"
)

# ==========================
# MEMBACA DATA
# ==========================
df = pd.read_excel("hasil_prediksi_deployment_google_sheets.xlsx")

# ==========================
# CSS
# ==========================
st.markdown("""
<style>

.stApp{
    background-color:#F5F7FA;
}

.title{
    font-size:42px;
    font-weight:bold;
    color:#0B5394;
}

.sub{
    font-size:20px;
    color:#555555;
}

.card{
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.1);
}

</style>
""",unsafe_allow_html=True)

# ==========================
# SIDEBAR
# ==========================

st.sidebar.image(
"https://cdn-icons-png.flaticon.com/512/2830/2830284.png",
width=120
)

st.sidebar.title("MENU")

menu = st.sidebar.radio(
"",
[
"🏠 Home",
"📊 Dashboard",
"📈 Evaluasi Model",
"📋 Dataset",
"👨‍🎓 Tentang"
]
)

# ==========================
# HOME
# ==========================

if menu=="🏠 Home":

    col1,col2=st.columns([1,3])

    with col1:

        st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=180
        )

    with col2:

        st.markdown(
        "<p class='title'>Dashboard Prediksi Status Pinjaman Nasabah</p>",
        unsafe_allow_html=True
        )

        st.markdown(
        "<p class='sub'>Menggunakan Algoritma Random Forest</p>",
        unsafe_allow_html=True
        )

        st.write("""

Dashboard ini dibuat untuk membantu
menampilkan hasil prediksi status pinjaman
nasabah menggunakan algoritma Random Forest.

Dashboard menyajikan informasi berupa
ringkasan data, visualisasi hasil prediksi,
evaluasi model, serta dataset hasil prediksi.

        """)

    st.markdown("---")

    st.subheader("📖 Informasi Penelitian")

    st.info("""

**Judul Skripsi**

Prediksi Status Pinjaman Nasabah
Menggunakan Algoritma Random Forest

**Metode**

Random Forest

**Dataset**

Dataset Kredit Nasabah

**Tujuan**

Memprediksi status pinjaman nasabah
agar dapat membantu proses analisis
kelayakan pemberian kredit.

    """)

    st.markdown("---")

    st.subheader("🎯 Tujuan Dashboard")

    c1,c2,c3=st.columns(3)

    with c1:

        st.success("""
📊 Menampilkan
ringkasan hasil prediksi
""")

    with c2:

        st.success("""
📈 Menampilkan
visualisasi data
""")

    with c3:

        st.success("""
🤖 Menampilkan
evaluasi Random Forest
""")
