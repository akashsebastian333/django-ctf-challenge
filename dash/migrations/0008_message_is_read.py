# Generated by Django 4.0.2 on 2023-02-19 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0007_message_read_at_message_unread'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]