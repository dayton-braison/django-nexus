# Generated by Django 4.1.5 on 2023-04-27 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus', '0010_alter_update_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]