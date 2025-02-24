from flask import Flask, request, jsonify
from job_scraper import fetch_jobs
from resume_parser import parse_resume
from job_matcher import calculate_fit_score
from resume_optimizer import optimize_resume

app = Flask(__name__)

@app.route("/upload_resume", methods=["POST"])
def upload_resume():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    resume_data = parse_resume(file)
    return jsonify(resume_data)

@app.route("/get_jobs", methods=["GET"])
def get_jobs():
    query = request.args.get("query", "Data Analyst")
    location = request.args.get("location", "Germany")
    jobs = fetch_jobs(query, location)
    return jsonify(jobs)

@app.route("/match_jobs", methods=["POST"])
def match_jobs():
    data = request.json
    resume_text = data.get("resume_text")
    job_description = data.get("job_description")
    
    score = calculate_fit_score(resume_text, job_description)
    return jsonify({"job_fit_score": score})

@app.route("/optimize_resume", methods=["POST"])
def optimize():
    data = request.json
    resume_text = data.get("resume_text")
    job_description = data.get("job_description")
    
    optimized_resume = optimize_resume(resume_text, job_description)
    return jsonify({"optimized_resume": optimized_resume})

if __name__ == "__main__":
    app.run(debug=True)