# Generated by Django 3.2.5 on 2021-07-01 12:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hotdeal_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='create_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]