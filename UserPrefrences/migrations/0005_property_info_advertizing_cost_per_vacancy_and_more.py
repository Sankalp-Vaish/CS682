# Generated by Django 4.0.7 on 2023-04-25 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserPrefrences', '0004_property_info_management_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='property_info',
            name='Advertizing_Cost_per_Vacancy',
            field=models.DecimalField(decimal_places=3, default=100.0, max_digits=8),
        ),
        migrations.AddField(
            model_name='property_info',
            name='Annual_Appreciation_Rate',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=5),
        ),
    ]
