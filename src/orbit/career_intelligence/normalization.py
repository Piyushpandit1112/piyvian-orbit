

def normalize_job(raw_job):
    normalized_job = {
        "title":raw_job.get("job_title","").strip(),
        "company":raw_job.get("employer","").strip(),
        "location":raw_job.get("location","").strip(),
        "job_url":raw_job.get("job_url","").strip()
    }
    return normalized_job