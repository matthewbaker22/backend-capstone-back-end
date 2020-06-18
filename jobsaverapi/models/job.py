from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    notes = models.CharField(max_length=1500)
    interview_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)