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
        user_notes = st.text_input("What did you learn today?")

    submit_button = st.form_submit_button("Save to My Skill-Tree")

# If the button is clicked, add the data to our CSV
if submit_button:
    new_data = pd.DataFrame([[user_date, user_skill, user_hours, user_notes]],
                            columns=['Date', 'Skill', 'Hours', 'Notes'])
    # 'mode=a' means append (add to the bottom)
    new_data.to_csv(DATA_PATH, mode='a', header=False, index=False)
    st.success(f"Nice work! Added {user_hours} hours to {user_skill}.")

# --- STEP 4: ANALYTICS & CHARTS ---
st.divider()
st.header("Progress Analytics")

# Read the current data
df = pd.read_csv(DATA_PATH)

if not df.empty:
    # 1. Group the data by Skill and sum the Hours
    summary_df = df.groupby('Skill')['Hours'].sum().reset_index()

    # 2. Create the Radar Chart (Complexity Requirement)
    radar_chart = px.line_polar(
        summary_df,
        r='Hours',
        theta='Skill', 
        line_close=True,
        markers=True
    )
    radar_chart.update_traces(fill='toself') # Fills in the center color

    # Show the chart
    st.plotly_chart(radar_chart)

    # 3. Show the raw table below
    st.subheader

