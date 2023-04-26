# Generated by Django 4.0.7 on 2023-04-26 00:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserPrefrences', '0007_pest_control_operating_expenses_income_financing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property_info',
            name='Annual_Appreciation_Rate',
            field=models.DecimalField(decimal_places=3, default=0.03, max_digits=10),
        ),
        migrations.CreateModel(
            name='Pests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trash_Removal', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('Miscellaneous', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('Common_Area_Maintenance', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('Capital_Improvements', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('Accounting', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('Legal', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('Bad_Debts', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('Other', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
