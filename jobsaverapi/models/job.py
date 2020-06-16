from django.db import models

class Job(models.Model):
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    notes = models.CharField(max_length=1500)
    interview_date = models.DateTimeField()
    # user_id = models.ForeignKey