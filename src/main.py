import streamlit as st
import pandas as pd
import os
import plotly.express as px
from datetime import datetime

# --- STEP 1: SETUP FILE PATHS ---
# This part makes sure the app finds the 'data' folder correctly
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "skills.csv")

