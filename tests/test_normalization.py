
from orbit.career_intelligence.normalization import normalize_job


def test_normalize_job_maps_fields_and_removes_spaces():
    raw_job = {
        "job_title": " Python Developer ",
        "employer": " ABC Technologies ",
        "location": " Berlin ",
        "job_url": "https://example.com/jobs/123"
    }

    expected_job = {
        "title": "Python Developer",
        "company": "ABC Technologies",
        "location": "Berlin",
        "job_url": "https://example.com/jobs/123"
    }

    assert normalize_job(raw_job) == expected_job


def test_normalize_job_handles_missing_location():
    raw_job = {
        "job_title": "Python Developer",
        "employer": "ABC Technologies",
        "job_url": "https://example.com/jobs/123"
    }

    normalized_job = normalize_job(raw_job)

    assert normalized_job["location"] == ""


def test_normalize_job_preserves_original_capitalization():
    raw_job = {
        "job_title": "PYTHON Developer",
        "employer": "ABC Technologies",
        "location": "BERLIN",
        "job_url": "https://example.com/jobs/123"
    }

    normalized_job = normalize_job(raw_job)

    assert normalized_job["title"] == "PYTHON Developer"
    assert normalized_job["company"] == "ABC Technologies"
    assert normalized_job["location"] == "BERLIN"



def test_normalize_job_handles_none_values():
    raw_job = {
        "job_title": None,
        "employer": "ABC Technologies",
        "location": None,
        "job_url": "https://example.com/jobs/123"
    }

    normalized_job = normalize_job(raw_job)

    assert normalized_job["title"] == ""
    assert normalized_job["location"] == ""

def test_normalize_job_handles_non_string_values():
    raw_job = {
        "job_title": 123,
        "employer": "ABC Technologies",
        "location": None,
        "job_url": "https://example.com/jobs/123"
    }

    normalized_job = normalize_job(raw_job)

    assert normalized_job["title"] == ""
    assert normalized_job["company"] == "ABC Technologies"
    assert normalized_job["location"] == ""
