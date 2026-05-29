import pdfplumber
import docx
import re


def extract_text_from_pdf(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

    return text


def extract_text_from_docx(docx_path):

    document = docx.Document(docx_path)

    text = []

    for paragraph in document.paragraphs:
        text.append(paragraph.text)

    return "\n".join(text)


def clean_resume_text(text):

    text = text.lower()

    text = re.sub(r"http\S+", "", text)

    text = re.sub(r"[^a-zA-Z\s]", "", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def parse_resume(file_path):

    if file_path.endswith(".pdf"):

        raw_text = extract_text_from_pdf(file_path)

    elif file_path.endswith(".docx"):

        raw_text = extract_text_from_docx(file_path)

    else:
        raise ValueError("Unsupported file format")

    cleaned_text = clean_resume_text(raw_text)

    return cleaned_text