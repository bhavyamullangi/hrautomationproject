from django.db import models

# Create your models here.
class hr_hradmin_data_table(models.Model):
    hrName = models.TextField(max_length=100, null='true')
    company_name = models.TextField(max_length=100, null='true')
    email = models.EmailField(max_length=100,unique='True')
    password = models.TextField(max_length=100, null='true')
    confirm_password = models.TextField(max_length=100, null='true')
    class Meta:
        db_table ='hr_hradmin_db_table'
