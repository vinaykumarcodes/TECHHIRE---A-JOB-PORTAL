from django.contrib import admin

from .models import Contact, Career
from .models import Job, JobApplication
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'email', 'message', 'time', 'mobno']
    list_filter = ['time']

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'req_skills', 'contact_no', 'updated_time', 'job_location']
    list_filter = ['job_title', 'updated_time', 'job_location']

from django.contrib import admin
from .models import Job, JobApplication

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'created_at')
    search_fields = ('title', 'location')

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'job', 'email', 'applied_at')
    search_fields = ('name', 'email', 'job__title')
