# Generated by Django 4.1.5 on 2023-05-01 23:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nexus', '0011_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='update_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
