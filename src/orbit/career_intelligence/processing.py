from .normalization import normalize_job
from .validation import validate_job

def process_job(raw_job):
    # 1. Normalize the raw job
    normalized_job = normalize_job(raw_job)

    # 2. Validate the normalized job
    is_valid = validate_job(normalized_job)

    # 3. If valid, return normalized job
    if is_valid:
        return normalized_job

    # 4. If invalid, return None
    return None



def process_jobs(raw_jobs):
    valid_jobs=[]
    for raw_job in raw_jobs:
        processed_job = process_job(raw_job)
        if processed_job is not None:
            valid_jobs.append(processed_job)
    return valid_jobs
