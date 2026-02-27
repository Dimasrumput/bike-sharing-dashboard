import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os as os

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    layout="wide"
)

st.title("🚲 Bike Sharing Data Dashboard")
st.markdown("Dashboard interaktif untuk eksplorasi data penyewaan sepeda.")

# ==============================
# LOAD DATA
# ==============================
@st.cache_data
def load_data():
    base_path = os.path.dirname(__file__)  # folder dashboard/
    file_path = os.path.join(base_path, "main_data.csv")
    df = pd.read_csv(file_path)
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

df = load_data()

# ==============================
# SIDEBAR - INTERACTIVE FILTER
# ==============================
st.sidebar.header("🔎 Filter Data")

# Date range filter (FITUR INTERAKTIF UTAMA)
min_date = df['dteday'].min()
max_date = df['dteday'].max()

date_range = st.sidebar.date_input(
    "Pilih Rentang Tanggal",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Season filter
season_options = df['season_label'].unique()
selected_season = st.sidebar.multiselect(
    "Pilih Musim",
    options=season_options,
    default=season_options
)

# Working day filter
workingday_options = df['workingday_label'].unique()
selected_workingday = st.sidebar.multiselect(
    "Pilih Tipe Hari",
    options=workingday_options,
    default=workingday_options
)

# ==============================
# APPLY FILTER
# ==============================
filtered_df = df[
    (df['dteday'] >= pd.to_datetime(date_range[0])) &
    (df['dteday'] <= pd.to_datetime(date_range[1])) &
    (df['season_label'].isin(selected_season)) &
    (df['workingday_label'].isin(selected_workingday))
]

# ==============================
# KPI SECTION
# ==============================
st.subheader("📊 Ringkasan Data")

col1, col2, col3 = st.columns(3)

col1.metric("Total Penyewaan", f"{int(filtered_df['cnt'].sum()):,}")
col2.metric("Rata-rata Harian", f"{round(filtered_df['cnt'].mean(), 2):,}")
col3.metric("Maksimum Harian", f"{int(filtered_df['cnt'].max()):,}")

# ==============================
# TREND OVER TIME
# ==============================
st.subheader("📈 Tren Penyewaan Sepeda")

daily_trend = filtered_df.groupby('dteday')['cnt'].sum()

fig1, ax1 = plt.subplots(figsize=(12, 5))
ax1.plot(daily_trend.index, daily_trend.values)
ax1.set_xlabel("Tanggal")
ax1.set_ylabel("Jumlah Penyewaan")
ax1.set_title("Tren Penyewaan Sepeda Berdasarkan Tanggal")
st.pyplot(fig1)

# ==============================
# SEASON ANALYSIS
# ==============================
st.subheader("🌤️ Rata-rata Penyewaan Berdasarkan Musim")

season_avg = filtered_df.groupby('season_label')['cnt'].mean().sort_values()

fig2, ax2 = plt.subplots()
sns.barplot(x=season_avg.index, y=season_avg.values, ax=ax2)
ax2.set_xlabel("Musim")
ax2.set_ylabel("Rata-rata Penyewaan")
st.pyplot(fig2)

# ==============================
# WORKING DAY ANALYSIS
# ==============================
st.subheader("🏢 Perbandingan Working Day vs Non-Working Day")

workingday_avg = filtered_df.groupby('workingday_label')['cnt'].mean()

fig3, ax3 = plt.subplots()
sns.barplot(x=workingday_avg.index, y=workingday_avg.values, ax=ax3)
ax3.set_xlabel("Tipe Hari")
ax3.set_ylabel("Rata-rata Penyewaan")
st.pyplot(fig3)

# ==============================
# RAW DATA (Optional)
# ==============================
with st.expander("Lihat Data Mentah"):
    st.dataframe(filtered_df)