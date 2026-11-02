def clean_text(value):
    # Check whether value is a string
    if isinstance(value, str):
        return value.strip()
    else:
        return ""
    

def normalize_job(raw_job):
    normalized_job = {
        "title":clean_text(raw_job.get("job_title")),
        "company":clean_text(raw_job.get("employer")),
        "location":clean_text(raw_job.get("location")),
        "job_url":clean_text(raw_job.get("job_url"))
    }
    return normalized_job