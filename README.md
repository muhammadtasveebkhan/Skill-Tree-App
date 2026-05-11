# Personal Skill-Tree & Resume Tracker 

### **App Description**
This application is a professional development dashboard designed to help students and professionals track their learning journey. It goes beyond a simple static resume by quantifying "Mastery" through logged hours and visualizing skill growth using interactive data visualizations (Plotly radar charts).

---

## How to Run the App
To run this application locally, ensure you have Python installed, then install the required libraries:
'pip install streamlit pandas plotly'

To launch the app, execute the following command in your terminal:
`streamlit run dist/main.py`

*(Note: The 'dist/' folder contains the final production code. You can also run the development version using 'streamlit run src/main.py').*

---

## User Instructions (Help)
1. **Log a Session:** On the main page, select a skill from the dropdown, enter the hours spent learning, add a brief note, and click "Save".
2. **View Progress:** Scroll down to the "Skill Analytics" section to view your dynamically updated Radar Chart. The shape will stretch toward your most mastered skills.
3. **Review History:** Your recent entries are displayed in the dataframe at the bottom of the page.

---

## File Structure
* 'dist/': **Production Environment (Graded Version)**
   * 'main.py': The main entry point for the app.
   * 'data/': Contains 'skills.csv', the local database for all logged sessions.
   * 'pages/': 
    * '1_Data_Export.py': Allows users to download their raw data.
    * '2_Resume_Builder.py': Auto-generates resume bullet points based on logged hours. 
* 'src/': **Development Environment** (Contains the working development drafts of the files above).
'demo.mp4': A brief video walkthrough demonstrating the app's functionality.   
* 'README.md': Project documentation and setup instructions.
'requirements.txt' : Lists the Python libraries needed to deploy the app to the cloud.  

---

## AI and Open-Source Usage Disclosure
* **AI Assistance:** AI was used as a learning tool to help troubleshoot Windows file pathing errors ('os.path.join') and to generate boilerplate structures for the multi-page layout. All logic was reviewed, manually implemented, and understood by the author.
* **Open Source:** This project utilizes Streamlit for the frontend web framework, Pandas for data manipulation and calculations, and Plotly for interactive data visualization.






