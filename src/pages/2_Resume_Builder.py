import streamlit as st
import pandas as pd
import os

# --- PATH SETUP ---
# Because we are inside the 'pages' folder, we have to go UP one level to find 'data'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(BASE_DIR, "data", "skills.csv")