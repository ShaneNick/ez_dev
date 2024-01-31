from django.db import models

# Create your models here.
class JobCategory(models.Model):
    tag = models.CharField(max_length = 100)
    label = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.label
    
class Company(models.Model):
    display_name = models.CharField(max_length = 255)

    def __str__(self):
        return self.display_name
    
class Location(models.Model):
    display_name = models.CharField(max_length = 255)
    area = models.JSONField()# Stores area as a list 

    def __str__(self):
        return self.display_name

class JobListing(models.Model):
    job_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary_min = models.FloatField(null=True, blank=True)
    salary_max = models.FloatField(null=True, blank=True)
    salary_is_predicted = models.CharField(max_length=5)
    created = models.DateTimeField()
    redirect_url = models.URLField(max_length=500)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    adref = models.TextField()
    contract_type = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title