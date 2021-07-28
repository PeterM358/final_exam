# Generated by Django 3.2.5 on 2021-07-28 18:22

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('store_auth', '0002_storeuser_email'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='storeuser',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='storeuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
