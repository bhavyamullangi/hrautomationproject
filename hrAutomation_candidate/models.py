from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class applicant_data_table(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    applicantName = models.CharField(max_length=100, null='true')
    email = models.EmailField(max_length=100)
    cv = models.FileField(upload_to='cv',null='true',default=None,blank=True)
    ccat_score = models.IntegerField(null='true')
    testgorila_score = models.IntegerField(null='true')
    password=models.CharField(max_length=50, null='true')
    class Meta:
        db_table ='applicant_data_table'

