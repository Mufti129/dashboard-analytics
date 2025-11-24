import streamlit as st
from app.data_loader import load_data
from app.analyzer import run_analysis
from app.visualizer import render_charts
from app.config import SHEET_URL

st.set_page_config(page_title="Analytics Dashboard", layout="wide")

st.title("📊 Analytics Dashboard")

# Load data
df = load_data(SHEET_URL)
if df is None:
    st.error("Gagal memuat data")
    st.stop()

# Sidebar menu
menu = st.sidebar.selectbox(
    "Pilih Analisis",
    ["Overview", "Sales Analysis", "Cancel Rate", "Product Insights", "QTY Rank"]
)

# Perform analysis
results = run_analysis(df, menu)

# Render output
render_charts(results, menu)
