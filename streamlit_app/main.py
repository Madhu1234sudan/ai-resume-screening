import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

import streamlit as st 
import pandas as pd 

from app.jd_parser import clean_job_description
from app.ranking import rank_resumes

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Screening System")

st.write(
    "Enter a Job Description and rank resumes automatically."
)

job_description = st.text_area(
    "Paste Job Description Here",
    height=250
)

if st.button("Rank Candidates"):
    if not job_description.strip():
        st.warning("Please enter a Job Description.")
    else:
        cleaned_jd = clean_job_description(
            job_description
        )
        
        results = rank_resumes(
            "data/resumes",
            cleaned_jd
        )

        df = pd.DataFrame(results)

        if not df.empty:
            df.index = range(1, len(df) + 1)

            st.subheader("Candidate Rankings")

            st.dataframe(
                df,
                use_container_width=True
            )
        else:

            st.error(
                "No resumes found in data/resumes"
            )
