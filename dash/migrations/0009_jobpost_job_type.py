# Generated by Django 4.0.2 on 2023-02-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0008_message_is_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='job_type',
            field=models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('contract', 'Contract'), ('internship', 'Internship')], default='full_time', max_length=20),
        ),
    ]
