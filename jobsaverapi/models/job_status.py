from django.db import models
from .job import Job
from .status import Status

class Job_Status(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)