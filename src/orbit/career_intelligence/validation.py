
def get_validation_errors(job):
    errors = []

    required_fields = ["title", "company", "job_url"]

    for field in required_fields:
        value = job.get(field)

        if not isinstance(value, str) or not value.strip():
            errors.append(f"{field} is missing or empty")

    return errors


def validate_job(job):
    return not get_validation_errors(job)
