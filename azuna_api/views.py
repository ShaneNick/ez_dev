from django.shortcuts import render
from django.http import JsonResponse

#use api view decorator 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JobCategorySerializer, CompanySerializer, LocationSerializer, JobListingSerializer
from .models import JobListing, JobCategory, Company, Location
from rest_framework import viewsets
from .adzuna_service import fetch_adzuna_jobs, parse_adzuna_response #store_adzuna_job_listings
@api_view(['GET'])

def apiOverview(request):
    api_urls = {
        'List': '/job-listing/',
        'Detail View': '/job-listing/<str:pk>/',
        'Create': '/job-listing/create/',
        'Update': '/job-listing/update/<str:pk>/',
        'Delete': '/job-listing/delete/<str:pk>/',
    }
    return Response(api_urls)

# @api_view(['GET'])
# def fetch_and_store_jobs(request):
#     # Example of fetching job listings for 'gb' and page 1
#     response_json = fetch_adzuna_jobs('gb', 1)
#     if response_json:
#         parsed_listings = parse_adzuna_response(response_json)
#         store_adzuna_job_listings(parsed_listings)
#         return Response({'message': 'Job listings fetched and stored successfully.'})
#     else:
#         return Response({'error': 'Failed to fetch data from Adzuna.'}, status=400)
    
@api_view(['GET'])
def fetch_us_jobs(request):
    # Define search parameters correctly in a dictionary
    search_params = {
        'results_per_page': 10,  # Limit to 10 jobs
        'where': "New York City",  # Specify the location as New York City
        'what_or': "Junior JR jr",  # Keywords that may be found
        'title_only': "software developer",  # Keywords found only in the title
    }

    # Fetch job listings for the US with specified parameters
    response_json = fetch_adzuna_jobs('us', 1, **search_params)

    if response_json:
        job_listings = parse_adzuna_response(response_json)
    else:
        job_listings = []

    # Render the listings in the template
    return render(request, 'azuna_api/listings.html', {'jobs': job_listings})
    

class JobListingViewSet(viewsets.ModelViewSet):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer

class JobCategoryViewSet(viewsets.ModelViewSet):
    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


