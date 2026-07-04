import plotly.express as px
import streamlit as st

st.markdown("## 📊 Visualisasi Data")

# ==========================
# KPI
# ==========================

col1, col2, col3, col4 = st.columns(4)

total = len(df)
lancar = len(df[df["Status Pinjaman"]=="Lancar"])
tidak = len(df[df["Status Pinjaman"]=="Tidak Lancar"])
akurasi = 98.40

col1.metric("📁 Total Data", total)
col2.metric("✅ Lancar", lancar)
col3.metric("❌ Tidak Lancar", tidak)
col4.metric("🎯 Akurasi", f"{akurasi}%")
