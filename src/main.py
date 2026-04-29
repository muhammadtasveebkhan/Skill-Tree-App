import streamlit as st
import pandas as pd
import os
import plotly.express as px
from datetime import datetime

# --- STEP 1: SETUP FILE PATHS ---
# This part makes sure the app finds the 'data' folder correctly
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "skills.csv")

# Create the folder and file if they are missing so the app doesn't crash
if not os.path.exists(os.path.dirname(DATA_PATH)):
    os.makedirs(os.path.dirname(DATA_PATH))

if not os.path.exists(DATA_PATH):
    # Create the CSV with headers
    df_start = pd.DataFrame(columns=['Date', 'Skill', 'Hours', 'Notes'])
    df_start.to_csv(DATA_PATH, index=False)

# --- STEP 2: APP UI SETUP ---
st.set_page_config(page_title="My Skill Tracker")
st.title("My Personal Skill-Tree") 
st.write("Welcome! Use this tool to track your coding progress and build your resume.")     

# --- STEP 3: THE DATA ENTRY FORM ---
st.header("Log a New Session")

# We use a form so the app doesn't refresh until we hit 'Save'
with st.form("entry_form", clear_on_submit=True):
    # Split the form into two side-by-side columns
    left, right = st.columns(2)

    with left:
        user_skill = st.selectbox("Select a Skill:", ["Python", "Data Science", "SQL", "Streamlit"])
        user_hours = st.number_input("How many hours?", min_value=0.5, step=0.5)

    with right:
        user_date = st.date_input("When did you do this?", datetime.now())
        user_notes = st.text_input    
