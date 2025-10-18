
from django.db import models
from django.utils import timezone


class Career(models.Model):
    job_title = models.CharField(max_length=30, editable=True)
    experience_required = models.IntegerField(default=0, editable=True)
    req_skills = models.CharField(max_length=100, default='skills required', null=False, editable=True)
    job_description = models.TextField(max_length=5000, null=True, editable=True)
    contact_no = models.CharField(max_length=10, editable=True, default='0000000')
    updated_time = models.DateTimeField(auto_now=True)
    job_id = models.CharField(max_length=8, default='0')
    job_location = models.CharField(max_length=15, default='location')

    def __str__(self):
        return f"{self.job_title} ({self.job_location})"

class Contact(models.Model):
    firstname = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=1000)
    mobno = models.CharField(max_length=13, default='')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} ({self.email})"

# jobapplication/models.py

# -----------------------------
#  Job Model
# -----------------------------

class Job(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.job.title}"
