# Generated by Django 3.2.5 on 2021-08-06 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='url',
        ),
    ]
