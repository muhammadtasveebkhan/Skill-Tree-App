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
    
         
