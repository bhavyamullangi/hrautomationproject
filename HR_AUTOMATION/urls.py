"""HR_AUTOMATION URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from hrAutomation_candidate import views
from hrAutomation_hradmin.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.applicant_login, name='applicant_login'),
    path('applicant_register',views.homeview.as_view(), name='applicant_register'),

    path('applicant_home',views.applicant_home, name='applicant_home'),
    path('register',register, name='register'),
    path('hr_register',hr_register,name='hr_register'),
    path('hr_login',hr_login,name='hr_login'),
    path('hr_search',hr_search ,name='hr_search'),
    path('<int:pk>',views.applicant_info.as_view(), name='applicant_info'),
    path('accounts/', include('allauth.urls')),


]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)