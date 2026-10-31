job = {
    "title": "Python Developer",
    "company": "ABC Technologies",
    "location": "Berlin",
    "job_url": "https://example.com/jobs/123"
}

def validate_job(job):
    required_fields = ["title", "company", "job_url"]
    for field in required_fields:
        if field not in job or not job[field].strip():
            return False
    return True