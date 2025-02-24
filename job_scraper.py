import requests

def fetch_jobs(query, location):
    api_key = "1b47da2be11ce366d18ca812991a0758a0ac9cfcac00783b2247b9a0f80c2dd8"
    url = f"https://serpapi.com/search.json?engine=google_jobs&q={query}&location={location}&api_key={api_key}"
    
    response = requests.get(url)
    data = response.json()
    
    job_listings = []
    for job in data.get("jobs_results", []):
        job_listings.append({
            "title": job.get("title"),
            "company": job.get("company_name"),
            "location": job.get("location"),
            "description": job.get("description"),
            "link": job.get("link")
        })
    return job_listings
