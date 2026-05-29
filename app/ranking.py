import os

from app.resume_parser import parse_resume
from app.similarity import calculate_similarity

def rank_resumes(resume_folder, job_description_text):

    results = []

    for filename in os.listdir(resume_folder):
        
        file_path = os.path.join(resume_folder, filename)


        try:
            resume_text = parse_resume(file_path)

            similarity_score = calculate_similarity(
                resume_text,
                job_description_text
            )

            results.append({
                "resume": filename,
                "score": similarity_score
            })

        except Exception as e:

            print(f"Error processing {filename}: {e}")
    ranked_results = sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked_results