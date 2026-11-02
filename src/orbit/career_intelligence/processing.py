
from .normalization import normalize_job
from .validation import get_validation_errors


def process_job_with_report(raw_job):
    # 1. Normalize the raw job
    normalized_job = normalize_job(raw_job)

    # 2. Get validation errors
    errors = get_validation_errors(normalized_job)

    # 3. Determine whether the job is valid
    is_valid = not errors

    # 4. Return a structured report
    return {
        "normalized_job": normalized_job,
        "is_valid": is_valid,
        "errors": errors
    }


def process_job(raw_job):
    # Get the processing report
    report = process_job_with_report(raw_job)

    # Return the job only if it is valid
    if report["is_valid"]:
        return report["normalized_job"]

    return None


def process_jobs(raw_jobs):
    valid_jobs = []

    for raw_job in raw_jobs:
        processed_job = process_job(raw_job)

        if processed_job is not None:
            valid_jobs.append(processed_job)

    return valid_jobs
