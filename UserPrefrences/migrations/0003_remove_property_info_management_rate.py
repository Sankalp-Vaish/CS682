# Generated by Django 4.0.7 on 2023-04-25 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserPrefrences', '0002_property_info_management_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property_info',
            name='Management_Rate',
        ),
    ]