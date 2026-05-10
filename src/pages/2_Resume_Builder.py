import streamlit as st
import pandas as pd
import os

# --- PATH SETUP ---
# Because we are inside the 'pages' folder, we have to go UP one level to find 'data'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(BASE_DIR, "data", "skills.csv")

# --- UI LAYOUT ---
st.title("Auto-Resume Builder")
st.write("Turn your hard work into professional bullet points for your portfolio or applications.")

# --- LOGIC ---
try:
    df = pd.read_csv(FILE_PATH)
    
    # Check if the dataframe actually has data
    if not df.empty:
        st.subheader("Your Career Highlights")

        # 1. Complex Data Calculations
        total_hours = df['Hours'].sum()
        top_skill = df.groupby('Skill')['Hours'].sum().idxmax()
        top_skill_hours = df.groupby('Skill')['Hours'].sum().max()
        unique_skills = df['Skill'].nunique()
        
        # 2. Dynamic Display Badges
        st.success(f"**Subject Matter Expert:** Dedicated **{top_skill_hours} hours** to mastering **{top_skill}**.")
        st.info(f"🚀 **Continuous Learner:** Accumulated **{total_hours} total hours** of development across **{unique_skills}** technical domains.")

        st.divider()
        
        # 3. The "Copy-Paste" Generator
        st.subheader("Copy-Paste Resume Bullets")

        # We use an f-string to automatically inject your data into professional sentences
        resume_text= (
            f"Dedicated {top_skill_hours} hours to advanced {top_skill} development and application.\n"
            f"Maintained a continuous learning streak, totaling {total_hours} hours of independent study.\n"
            f"Developed proficiencies in {unique_skills} key technical areas including: {', '.join(df['Skill'].unique())}."
        )

        st.text_area("Copy these into your Word Doc:", resume_text, height=150)
    else:
        st.warning("Your skill-tree is empty. Go log some hours on the main page first!")

except FileNotFoundError:
    st.error("Data file not found. Please log a skill on the main page first.")


