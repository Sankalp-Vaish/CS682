from django.db import models

# Create your models here.


class User_details(models.Model):
    Rent_type= models.TextChoices('Rent', '600 700 800 900 1000')
    Average_rent_per_unit = models.BigIntegerField(blank=True, choices=Rent_type.choices)
    First_Mtg_Interest_Rate = models.DecimalField(max_digits=5, decimal_places=2)