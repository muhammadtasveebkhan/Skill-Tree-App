import streamlit as st
import pandas as pd
import os

# Pathing
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(BASE_DIR, "data", "skills.csv")
st.title("Export Your Data")
st.write("Download your skill-tree data for your resume or portfolio.")