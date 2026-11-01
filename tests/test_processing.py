
from orbit.career_intelligence.processing import process_job,  process_jobs


def test_process_job_returns_normalized_valid_job():
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

    assert process_job(raw_job) == expected_job


def test_process_job_returns_none_for_invalid_job():
    raw_job = {
        "job_title": "Python Developer",
        "job_url": "https://example.com/jobs/123"
    }

    assert process_job(raw_job) is None




def test_process_multiple_jobs():
    raw_jobs = [
        {
            "job_title": "Python Developer",
            "employer": "ABC Technologies",
            "job_url": "https://example.com/jobs/1"
        },
        {
            "job_title": "Backend Developer",
            "job_url": "https://example.com/jobs/2"
        },
        {
            "job_title": "AI Engineer",
            "employer": "XYZ Technologies",
            "job_url": "https://example.com/jobs/3"
        }
    ]

    result = process_jobs(raw_jobs)

    assert len(result) == 2
    assert result[0]["company"] == "ABC Technologies"
    assert result[1]["company"] == "XYZ Technologies"


def test_process_empty_job_list():
    assert process_jobs([]) == []


def test_process_all_invalid_jobs():
    raw_jobs = [
        {
            "job_title": "Python Developer",
            "job_url": "https://example.com/jobs/1"
        },
        {
            "job_title": "Backend Developer",
            "job_url": "https://example.com/jobs/2"
        }
    ]

    assert process_jobs(raw_jobs) == []

