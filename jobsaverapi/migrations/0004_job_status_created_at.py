# Generated by Django 3.0.7 on 2020-06-22 18:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobsaverapi', '0003_job_status_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_status',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
