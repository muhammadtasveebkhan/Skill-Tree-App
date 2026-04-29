import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import os

# -----------------------------
# 1. FILE PATH SETUP
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create data folder path
DATA_DIR = os.path.join(BASE_DIR, "data")

# Create folder automatically if it doesn't exist
os.makedirs(DATA_DIR, exist_ok=True)

# CSV file path
FILE_PATH = os.path.join(DATA_DIR, "skills.csv")

# -----------------------------
# 2. CREATE CSV IF NOT EXISTS
# -----------------------------
if not os.path.exists(FILE_PATH):
    empty_df = pd.DataFrame(columns=["Date", "Skill", "Hours", "Notes"])
    empty_df.to_csv(FILE_PATH, index=False)

# -----------------------------
# 3. PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Skill Tracker", layout="wide")

st.title("🛡️ My Personal Skill-Tree")

# -----------------------------
# 4. INPUT FORM
# -----------------------------
st.header("Log a New Session")

with st.form("entry_form", clear_on_submit=True):

    col1, col2 = st.columns(2)

    with col1:
        skill = st.selectbox(
            "Skill",
            ["Python", "SQL", "Streamlit", "Business Analytics"]
        )

        hours = st.number_input(
            "Hours",
            min_value=0.5,
            step=0.5
        )

    with col2:
        date = st.date_input("Date", datetime.now())

        note = st.text_input("Notes")

    submitted = st.form_submit_button("Save")

    if submitted:
        try:
            new_row = pd.DataFrame(
                [[date, skill, hours, note]],
                columns=["Date", "Skill", "Hours", "Notes"]
            )

            new_row.to_csv(
                FILE_PATH,
                mode="a",
                header=False,
                index=False
            )

            st.success("✅ Saved successfully!")

        except Exception as e:
            st.error(f"Error saving data: {e}")

# -----------------------------
# 5. ANALYTICS
# -----------------------------
st.divider()

try:
    df = pd.read_csv(FILE_PATH)

    # Convert Hours column safely
    df["Hours"] = pd.to_numeric(df["Hours"], errors="coerce")

    if not df.empty:

        st.subheader("Skill Analytics")

        chart_data = (
            df.groupby("Skill")["Hours"]
            .sum()
            .reset_index()
        )

        fig = px.line_polar(
            chart_data,
            r="Hours",
            theta="Skill",
            line_close=True
        )

        fig.update_traces(fill="toself")

        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Recent Entries")

        st.dataframe(df, use_container_width=True)

    else:
        st.info("Log your first skill above!")

except Exception as e:
    st.error(f"Error loading file: {e}")

# -----------------------------
# 6. DEBUG INFO
# -----------------------------
st.sidebar.header("Debug Info")

st.sidebar.write("BASE_DIR:")
st.sidebar.code(BASE_DIR)

st.sidebar.write("FILE_PATH:")
st.sidebar.code(FILE_PATH)

st.sidebar.write("File Exists:")
st.sidebar.write(os.path.exists(FILE_PATH))