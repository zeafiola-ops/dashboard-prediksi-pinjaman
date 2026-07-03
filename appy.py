import streamlit as st
import pandas as pd
from PIL import Image

# ======================================================
# KONFIGURASI
# ======================================================

st.set_page_config(
    page_title="Dashboard Prediksi Status Pinjaman Nasabah",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================================
# LOAD DATA
# ======================================================

df = pd.read_excel("hasil_prediksi_deployment_google_sheets(9).xlsx")

# ======================================================
# LOAD LOGO
# ======================================================

logo = Image.open("logo.png")

# ======================================================
# CSS
# ======================================================

st.markdown("""
<style>

#MainMenu{visibility:hidden;}
header{visibility:hidden;}
footer{visibility:hidden;}

.stApp{

background:linear-gradient(
180deg,
#edf5ff 0%,
#ffffff 45%,
#ffffff 100%
);

}

.block-container{

padding-top:2rem;
padding-left:3rem;
padding-right:3rem;
max-width:1300px;

}

[data-testid="stSidebar"]{

background:#0B3C78;

}

[data-testid="stSidebar"] *{

color:white;

}

</style>

""",unsafe_allow_html=True)
