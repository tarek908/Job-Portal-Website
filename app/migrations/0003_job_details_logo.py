# Generated by Django 5.1.2 on 2024-11-06 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_job_details_company_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_details',
            name='logo',
            field=models.ImageField(default='', upload_to='app/img/JobPost'),
        ),
    ]
