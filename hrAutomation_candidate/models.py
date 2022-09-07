from django.db import models

# Create your models here.

class hr_applicant_data_table(models.Model):
    applicantName = models.CharField(max_length=100, null='true')
    email = models.EmailField(max_length=100)
    cv = models.FileField(upload_to='cv',null='true',default=None,blank=True)
    ccat_score = models.IntegerField(null='true')
    testgorila_score = models.IntegerField(null='true')
    password=models.CharField(max_length=50, null='true')
    class Meta:
        db_table ='hr_applicant_data_table'
