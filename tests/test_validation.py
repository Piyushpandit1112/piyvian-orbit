from orbit.career_intelligence.validation import validate_job , get_validation_errors


def test_valid_job_returns_true():
    job = {
        "title": "Python Developer",
        "company": "ABC Technologies",
        "job_url": "https://example.com/jobs/123"
    }

    assert validate_job(job) is True


def test_missing_company_returns_false():
    job = {
        "title": "Python Developer",
        "job_url": "https://example.com/jobs/123"
    }

    assert validate_job(job) is False

def test_empty_title_returns_false():
    job = {
        "title": "",
        "company": "ABC Technologies",
        "job_url": "https://example.com/jobs/123"
    }

    assert validate_job(job) is False

def test_company_only_spaces_returns_false():
    job = {
    "title": "Python Developer",
    "company": "   ",
    "job_url": "https://example.com/jobs/123"
    }
    assert validate_job(job) is False

def test_missing_location_returns_true():
    job = {
        "title": "Python Developer",
        "company": "ABC Technologies",
        "job_url": "https://example.com/jobs/123"
    }

    assert validate_job(job) is True


def test_valid_job_returns_no_errors():
    job = {
        "title": "Python Developer",
        "company": "ABC Technologies",
        "job_url": "https://example.com/jobs/123"
    }

    assert get_validation_errors(job) == []


def test_missing_company_returns_error():
    job = {
        "title": "Python Developer",
        "job_url": "https://example.com/jobs/123"
    }

    assert "company is missing or empty" in get_validation_errors(job)


def test_multiple_missing_fields_return_multiple_errors():
    job = {}

    errors = get_validation_errors(job)

    assert len(errors) == 3
