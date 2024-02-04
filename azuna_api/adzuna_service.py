import requests
from django.conf import settings

def fetch_adzuna_jobs(country, page, **kwargs):
    base_url = f'http://api.adzuna.com/v1/api/jobs/{country}/search/{page}'
    params = {
        'app_id': settings.ADZUNA_APP_ID,
        'app_key': settings.ADZUNA_APP_KEY,
    }
    params.update(kwargs)
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def parse_adzuna_response(json_response):
    job_listings = []
    for job in json_response.get('results', []):
        job_data = {
            'title': job.get('title'),
            'description': job.get('description'),
            'company': job.get('company', {}).get('display_name', 'Not Specified'),
            'location': job.get('location', {}).get('display_name', 'Not Specified'),
            'salary_min': job.get('salary_min'),
            'salary_max': job.get('salary_max'),
            'redirect_url': job.get('redirect_url'),
            'created_at': job.get('created'),
        }
        job_listings.append(job_data)
    return job_listings
