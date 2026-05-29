import re


def clean_job_description(text):

    text = text.lower()

    text = re.sub(r"http\S+", "", text)

    text = re.sub(r"[^a-zA-Z\s]", "", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def parse_job_description(file_path):

    with open(file_path, "r", encoding="utf-8") as file:

        raw_text = file.read()

    cleaned_text = clean_job_description(raw_text)

    return cleaned_text