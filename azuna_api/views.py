from django.shortcuts import render
from django.http import JsonResponse

#use api view decorator 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JobCategorySerializer, CompanySerializer, LocationSerializer, JobListingSerializer
from .models import JobListing, JobCategory, Company, Location
from rest_framework import viewsets

# Create your views here.
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


