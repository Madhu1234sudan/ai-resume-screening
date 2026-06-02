import os
import shutil

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
uploaded_resumes = st.file_uploader(
    "Upload Resume Files",
    type=["pdf", "docx"],
    accept_multiple_files=True
)
jd_file = st.file_uploader(
    "Upload Job Description File (.txt)",
    type=["txt"]
)

job_description = st.text_area(
    "Paste Job Description Here (Optional)",
    height=250
)

if st.button("Rank Candidates"):
    if jd_file is not None:

        job_description = jd_file.read().decode("utf-8")
    if not uploaded_resumes:
        st.warning("Please upload at least one resume.")

    elif not job_description.strip():
        st.warning("Please enter a Job Description.")

    else:

        os.makedirs("uploads", exist_ok=True)

        for file in uploaded_resumes:

            file_path = os.path.join(
                "uploads",
                file.name
            )

            with open(file_path, "wb") as f:
                f.write(file.getbuffer())
                
        cleaned_jd = clean_job_description(
            job_description
        )

        results = rank_resumes(
            "uploads",
            cleaned_jd
        )

        df = pd.DataFrame(results)
        csv = df.to_csv(index=False)

        st.download_button(
            label="📥 Download Results CSV",
            data=csv,
            file_name="candidate_rankings.csv",
            mime="text/csv"
        )

        if not df.empty:

            df.index = range(1, len(df) + 1)

            st.subheader("Candidate Rankings")

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.error("No resumes processed.")
