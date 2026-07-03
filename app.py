import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# KONFIGURASI
# =========================
st.set_page_config(
    page_title="Dashboard Prediksi Status Pinjaman",
    page_icon="💳",
    layout="wide"
)

# =========================
# CSS
# =========================
st.markdown("""
<style>

.main{
    background-color:#f5f7fb;
}

.block-container{
    padding-top:1rem;
}

.metric-card{
    background:white;
    padding:15px;
    border-radius:15px;
    box-shadow:0px 4px 10px rgba(0,0,0,0.1);
}

</style>
""",unsafe_allow_html=True)

# =========================
# LOAD DATA
# =========================

df = pd.read_excel("hasil_prediksi_deployment_google_sheets.xlsx")

# =========================
# SIDEBAR
# =========================

st.sidebar.image(
"https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
width=120
)

menu = st.sidebar.radio(
"Menu",
[
"🏠 Home",
"📊 Dashboard",
"📋 Dataset"
]
)

# =========================
# HOME
# =========================

if menu=="🏠 Home":

    st.title("💳 Dashboard Prediksi Status Pinjaman Nasabah")

    st.write("""
Dashboard ini digunakan untuk menampilkan hasil prediksi status pinjaman
menggunakan algoritma **Random Forest**.
""")

    st.markdown("---")

    c1,c2,c3,c4=st.columns(4)

    c1.metric(
        "Jumlah Data",
        len(df)
    )

    lancar=len(df[df["status_prediksi"]==1])

    tidak=len(df[df["status_prediksi"]==0])

    c2.metric(
        "Prediksi Lancar",
        lancar
    )

    c3.metric(
        "Prediksi Tidak Lancar",
        tidak
    )

    akurasi=(
        (df["status_aktual"]==df["status_prediksi"]).mean()*100
    )

    c4.metric(
        "Akurasi",
        f"{akurasi:.2f}%"
    )

    st.success("Model Random Forest berhasil digunakan untuk melakukan prediksi.")

# =========================
# DASHBOARD
# =========================

if menu=="📊 Dashboard":

    st.title("📊 Dashboard Visualisasi")

    col1,col2=st.columns(2)

    with col1:

        pie=df["status_prediksi"].value_counts()

        fig=px.pie(
            values=pie.values,
            names=["Tidak Lancar","Lancar"],
            title="Distribusi Status Prediksi",
            hole=0.45
        )

        st.plotly_chart(fig,use_container_width=True)

    with col2:

        fig2=px.histogram(
            df,
            x="usia",
            title="Distribusi Usia Nasabah"
        )

        st.plotly_chart(fig2,use_container_width=True)

    st.markdown("---")

    col3,col4=st.columns(2)

    with col3:

        fig3=px.scatter(
            df,
            x="pendapatan_tahunan",
            y="jumlah_pinjaman",
            color="status_prediksi",
            title="Pendapatan vs Jumlah Pinjaman"
        )

        st.plotly_chart(fig3,use_container_width=True)

    with col4:

        fig4=px.box(
            df,
            y="suku_bunga",
            title="Distribusi Suku Bunga"
        )

        st.plotly_chart(fig4,use_container_width=True)

# =========================
# DATASET
# =========================

if menu=="📋 Dataset":

    st.title("📋 Dataset")

    status=st.selectbox(
        "Filter Status Prediksi",
        ["Semua","Lancar","Tidak Lancar"]
    )

    if status=="Lancar":
        tampil=df[df["status_prediksi"]==1]

    elif status=="Tidak Lancar":
        tampil=df[df["status_prediksi"]==0]

    else:
        tampil=df

    st.dataframe(
        tampil,
        use_container_width=True
    )

    st.download_button(
        "📥 Download Dataset",
        data=tampil.to_csv(index=False),
        file_name="hasil_prediksi.csv",
        mime="text/csv"
    )
