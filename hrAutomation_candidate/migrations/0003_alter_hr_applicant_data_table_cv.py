# Generated by Django 4.1 on 2022-08-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrAutomation_candidate', '0002_alter_hr_applicant_data_table_ccat_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hr_applicant_data_table',
            name='cv',
            field=models.FileField(blank=True, default=None, null='true', upload_to='cv'),
        ),
    ]