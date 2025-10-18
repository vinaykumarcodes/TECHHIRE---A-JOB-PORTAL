# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import requests
import random

from django.conf import settings
from django.utils import timezone
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

from .forms import ContactForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Contact, Career, JobApplication, Job


from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .models import Job




from .models import Contact, Career, JobApplication, Job
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Job, JobApplication
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            email = form.cleaned_data['email']
            mobn = form.cleaned_data['mobno']
            message = form.cleaned_data['message']

            # Save to DB
            Contact.objects.get_or_create(
                firstname=firstname,
                email=email,
                message=message,
                mobno=mobn
            )

            subject = 'Thank you for contacting us'
            email_message = 'We will get back to you in a few moments.'
            from_mail = settings.EMAIL_HOST_USER  # Make sure this is set in settings.py
            to_list = [email]

            try:
                send_mail(subject, email_message, from_mail, to_list, fail_silently=False)
                # ✅ Success message
                messages.success(request, "✅ Thank you! Your message has been sent successfully.")
            except BadHeaderError:
                # ❌ Error message
                messages.error(request, "❌ Invalid header found. Please try again.")
            except Exception as e:
                # ❌ General error message
                messages.error(request, "❌ Something went wrong. Please try again later.")

            return redirect("home")  # change to your index page route

    return render(request, "index.html")
def what_we_are(request):
    return render(request, 'what_we_are.html')



def ourprojects(request):
    return render(request, 'ourprojects.html')


def careers(request):
    jobs = Job.objects.all().order_by("-created_at")
    return render(request, "careers.html", {"jobs": jobs})


def apply(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        resume = request.FILES.get('resume')
        JobApplication.objects.create(job=job, name=name, email=email, resume=resume)
        messages.success(request, 'Application submitted successfully!')
        return redirect('careers')


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def submit_application(request):
    if request.method == "POST":
        job_id = request.POST.get("job_id")
        name = request.POST.get("name")
        email = request.POST.get("email")
        resume = request.FILES.get("resume")
        message = request.POST.get("message", "")

        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            messages.error(request, "❌ Job not found.")
            return redirect("careers")

        # Save the application
        JobApplication.objects.create(
            job=job,
            name=name,
            email=email,
            resume=resume,
            
        )

        # Success message
        messages.success(request, f"✅ Your application for '{job.title}' was submitted successfully!")
        return redirect("careers")

    messages.error(request, "❌ Invalid request method.")
    return redirect("careers")

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if user exists
        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            username = email   # fallback if login with username

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in successfully!")
            return redirect("home")  # change 'home' to where you want to go
        else:
            messages.error(request, "Invalid credentials, please try again.")

    return render(request, "loginandsignup.html")
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            messages.success(request, "Signup successful! Please log in.")
            return redirect("login_view")

    return render(request, "loginandsignup.html")
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect("login_view")  # Redirect back to login page

def login_signup(request):
    return render(request, "loginandsignup.html")  # Template will contain both login + signup
