from django import forms
from django.forms import ModelForm

from .models import hr_applicant_data_table

class ResumeForm(forms.ModelForm):
 class Meta:
  model = hr_applicant_data_table
  fields = ['applicantName', 'email', 'cv']
  labels = {'applicantName': 'Name', 'email': 'Email ID','cv':'Resume'}
  widgets = {
   'name': forms.CharField(),
   'email': forms.EmailInput(),
  }

class Applicant_loginFrom(forms.Form):

   '''fields=['email','password']
   labels = {'email': 'Email', 'password': 'Password'}
   widgets = {
                'password': forms.PasswordInput(),
   }'''
   email=forms.CharField(max_length=100)
   password=forms.CharField(widget=forms.PasswordInput)