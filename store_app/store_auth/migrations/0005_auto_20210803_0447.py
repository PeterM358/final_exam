# Generated by Django 3.2.5 on 2021-08-03 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_auth', '0004_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storeuser',
            name='username',
        ),
        migrations.AlterField(
            model_name='storeuser',
            name='email',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
