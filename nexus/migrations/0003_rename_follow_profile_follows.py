# Generated by Django 4.1.5 on 2023-04-22 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nexus', '0002_rename_profie_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='follow',
            new_name='follows',
        ),
    ]
