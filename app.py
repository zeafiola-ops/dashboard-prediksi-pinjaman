import streamlit as st
import pandas as pd
import plotly.express as px
import base64

# ==========================================
# KONFIGURASI
# ==========================================

st.set_page_config(
    page_title="Dashboard Prediksi Random Forest",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# LOAD LOGO
# ==========================================

def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo = get_base64("logo.png")

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_excel("hasil_prediksi.xlsx")
