from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobListingViewSet, JobCategoryViewSet, CompanyViewSet, LocationViewSet, apiOverview, fetch_us_jobs


router = DefaultRouter()
router.register(r'joblistings', JobListingViewSet)
router.register(r'jobcategories', JobCategoryViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('', apiOverview, name="api-overview"),
    path('fetch-us-jobs/', fetch_us_jobs, name='fetch_us_jobs'),
    path('', include(router.urls)),
    path('listings/', fetch_us_jobs, name = 'listings')
]