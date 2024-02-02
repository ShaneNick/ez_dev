from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobListingViewSet, JobCategoryViewSet, CompanyViewSet, LocationViewSet, apiOverview


router = DefaultRouter()
router.register(r'joblistings', JobListingViewSet)
router.register(r'jobcategories', JobCategoryViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('', apiOverview, name="api-overview"),
    path('', include(router.urls)),
]