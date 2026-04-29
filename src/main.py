import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import os

# --- 1. DIRECT PATH (No folder creation logic) ---
# We point directly to the file you just made manually
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "data", "skills.csv")

# --- 2. UI LAYOUT ---
st.set_page_config(page_title="Skill Tracker", layout="wide")
st.title("🛡️ My Personal Skill-Tree")

# --- 3. INPUT FORM ---
st.header("Log a New Session")
with st.form("entry_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        skill = st.selectbox("Skill", ["Python", "SQL", "Streamlit", "Business Analytics"])
        hours = st.number_input("Hours", min_value=0.5, step=0.5)
    with col2:
        date = st.date_input("Date", datetime.now())
        note = st.text_input("Notes")
    
    if st.form_submit_button("Save"):
        new_row = pd.DataFrame([[date, skill, hours, note]], columns=['Date', 'Skill', 'Hours', 'Notes'])
        new_row.to_csv(FILE_PATH, mode='a', header=False, index=False)
        st.success("✅ Saved successfully!")

# --- 4. ANALYTICS ---
st.divider()
try:
    df = pd.read_csv(FILE_PATH)
    if not df.empty:
        chart_data = df.groupby('Skill')['Hours'].sum().reset_index()
        fig = px.line_polar(chart_data, r='Hours', theta='Skill', line_close=True)
        fig.update_traces(fill='toself')
        st.plotly_chart(fig)
        
        st.subheader("Recent Entries")
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Log your first skill above!")
except FileNotFoundError:
    st.error("Could not find skills.csv. Please ensure it is inside the src/data/ folder!")