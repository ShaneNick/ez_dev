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
    # Fetch job listings for the US, limiting the results to 10
    country_code = 'us'  # ISO country code for the United States
    results_per_page = 10  # Limit to 10 jobs
    response_json = fetch_adzuna_jobs(country_code, 1, results_per_page=results_per_page)  # Page 1
    
    if response_json:
        # Directly parse and return the job listings without storing them
        job_listings = parse_adzuna_response(response_json)
        return Response({'jobs': job_listings})
    else:
        return Response({'error': 'Failed to fetch data from Adzuna.'}, status=400)
    

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


