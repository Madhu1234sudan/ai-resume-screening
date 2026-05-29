from app.jd_parser import parse_job_description
from app.ranking import  rank_resumes

def run():
    
    resume_folder = "data/resumes" 

    jd_path = "data/job_descriptions/sample_jd.txt" 

    job_description_text = parse_job_description(jd_path)

    ranked_candidates = rank_resumes(
        resume_folder,
        job_description_text
    )

    print("\nCandidate Rankings:\n") 

    for index, candidate in enumerate(ranked_candidates, start=1):

        print(
            f"{index}.{candidate['resume']} "
            f"-> {candidate['score']}% Match"
        )
if __name__ == "__main__":
    run()