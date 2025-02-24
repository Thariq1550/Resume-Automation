import PyPDF2
import re

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text

def extract_skills(text):
    skills_keywords = ["Python", "SQL", "Machine Learning", "Flask", "Data Analysis", "Product Management"]
    found_skills = [skill for skill in skills_keywords if skill.lower() in text.lower()]
    return found_skills

def extract_experience(text):
    experience_pattern = re.findall(r"(\d+ years?|[a-zA-Z]+ experience)", text, re.IGNORECASE)
    return experience_pattern

def parse_resume(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    skills = extract_skills(text)
    experience = extract_experience(text)
    return {"skills": skills, "experience": experience, "raw_text": text}
