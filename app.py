# ============================================================
# Dashboard Prediksi Status Pinjaman Nasabah
# Muhammad Rizki Maulidin
# Sistem Informasi
# Institut Informatika dan Bisnis Darmajaya
# ============================================================

# ===========================
# IMPORT LIBRARY
# ===========================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import joblib
from PIL import Image
from pathlib import Path
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    roc_curve,
    auc
)

# ===========================
# KONFIGURASI HALAMAN
# ===========================

st.set_page_config(
    page_title="Dashboard Prediksi Status Pinjaman Nasabah",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===========================
# PATH PROJECT
# ===========================

BASE_DIR = Path(__file__).parent

DATA_PATH = BASE_DIR / "data" / "hasil_prediksi_deployment_google_sheets.xlsx"

MODEL_PATH = BASE_DIR / "model" / "random_forest_model.pkl"

FEATURE_PATH = BASE_DIR / "data" / "feature_names.pkl"

LOGO_PATH = BASE_DIR / "assets" / "logo.png"

CSS_PATH = BASE_DIR / "style.css"

# ===========================
# LOAD CSS
# ===========================

if CSS_PATH.exists():
    with open(CSS_PATH) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ===========================
# LOAD DATA
# ===========================

@st.cache_data
def load_data():
    return pd.read_excel(DATA_PATH)

# ===========================
# LOAD MODEL
# ===========================

@st.cache_resource
def load_model():

    model = joblib.load(MODEL_PATH)

    feature_names = joblib.load(FEATURE_PATH)

    return model, feature_names

# ===========================
# MEMBACA DATA
# ===========================

df = load_data()

model, feature_names = load_model()

# ===========================
# LOAD LOGO
# ===========================

logo = None

if LOGO_PATH.exists():
    logo = Image.open(LOGO_PATH)
