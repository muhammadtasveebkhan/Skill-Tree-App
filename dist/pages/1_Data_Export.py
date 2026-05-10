import streamlit as st
import pandas as pd
import os

# Pathing
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(BASE_DIR, "data", "skills.csv")

st.title("Export Your Data")
st.write("Download your skill-tree data for your resume or portfolio.")

try:
    df = pd.read_csv(FILE_PATH)
    st.dataframe(df) 

    # Create a download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download as CSV",
        data=csv,
        file_name='my_resume_skills.csv',
        mime='text/csv',
        )
except Exception:
    st.info("No data available to export yet.")
    

