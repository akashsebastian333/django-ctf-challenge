# Generated by Django 4.0.2 on 2023-02-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0011_alter_jobpost_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='job_type',
            field=models.CharField(choices=[('full time', 'Full Time'), ('part time', 'Part Time'), ('contract', 'Contract'), ('internship', 'Internship')], default='full_time', max_length=20),
        ),
    ]
