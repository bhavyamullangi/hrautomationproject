# Generated by Django 4.1 on 2022-08-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrAutomation_candidate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hr_applicant_data_table',
            name='ccat_score',
            field=models.IntegerField(null='true'),
        ),
        migrations.AlterField(
            model_name='hr_applicant_data_table',
            name='cv',
            field=models.FileField(default=None, null='true', upload_to='cv/'),
        ),
        migrations.AlterField(
            model_name='hr_applicant_data_table',
            name='testgorila_score',
            field=models.IntegerField(null='true'),
        ),
    ]
