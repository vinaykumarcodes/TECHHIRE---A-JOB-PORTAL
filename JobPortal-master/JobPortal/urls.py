"""JobPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jobapplication import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('ourprojects/', views.ourprojects, name='ourprojects'),
    path('careers/', views.careers, name='careers'),
    path('what_we_are/', views.what_we_are, name='what_we_are'),  # ✅ new route
    path('apply/', views.submit_application, name='submit_application'),
    path("login/", views.login_view, name="login_view"),
    path("signup/", views.signup_view, name="signup_view"),
    path("logout/", views.logout_view, name="logout_view"),
    path("loginandsignup/", views.login_signup, name="loginandsignup"),  # Combined login and signup
    path('accounts/', include('django.contrib.auth.urls')),  # Django auth routes
    path("apply/<int:job_id>/", views.apply, name="apply"),  # ✅ NEW
    path('submit_application/', views.submit_application, name='submit_application'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)