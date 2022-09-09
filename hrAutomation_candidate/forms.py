from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import applicant_data_table


class ResumeForm(forms.ModelForm):
   class Meta:
     model = applicant_data_table
     fields = ['applicantName', 'email', 'cv','password']
     labels = {'applicantName': 'Name', 'email': 'Email ID', 'cv': 'Resume','password':'password'}
     widgets = {
         'name': forms.CharField(),
         'email': forms.EmailInput(),
     }
class Applicant_loginFrom(forms.Form):

   email=forms.CharField(max_length=100)
   password=forms.CharField(widget=forms.PasswordInput)