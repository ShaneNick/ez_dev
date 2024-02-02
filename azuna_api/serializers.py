from rest_framework import serializers
from .models import JobListing, JobCategory, Company, Location

class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class JobListingSerializer(serializers.ModelSerializer):
    category = JobCategorySerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    location = LocationSerializer(read_only=True)
    salary_range = serializers.SerializerMethodField()
    days_since_created = serializers.SerializerMethodField()


    class Meta:
        model = JobListing
        fields = '__all__'

    def get_salary_range(self, obj):
        """Constructs a string representation of the salary range."""
        if obj.salary_min and obj.salary_max:
            return f"${obj.salary_min} - ${obj.salary_max}"
        elif obj.salary_min:
            return f"From ${obj.salary_min}"
        elif obj.salary_max:
            return f"Up to ${obj.salary_max}"
        return "Salary not specified"

    def get_days_since_created(self, obj):
        """Calculates how many days ago the job was posted."""
        from django.utils.timezone import now
        return (now() - obj.created).days