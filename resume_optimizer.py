import google.generativeai as genai

genai.configure(api_key="AIzaSyCL-Hi_5k1h6OCIMDfMf2eXhIW_-9TxSg4")

def optimize_resume(resume_text, job_description):
    prompt = f"Rewrite this resume to better match the job description: {job_description}\n\nResume:\n{resume_text}"
    response = genai.chat(prompt)
    return response.text