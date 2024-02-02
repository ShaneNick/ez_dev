import requests
from django.conf import settings

def fetch_adzuna_jobs(country, page, **kwargs):
    base_url = f'http://api.adzuna.com/v1/api/jobs/{country}/search/{page}'
    params = {
        'app_id': settings.ADZUNA_APP_ID,
        'app_key': settings.ADZUNA_APP_KEY,
    }
    # Add additional parameters based on kwargs
    params.update(kwargs)
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()  # Convert response to JSON
    else:
        return None
