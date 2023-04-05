from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class User_details(models.Model):
    user= models.OneToOneField(to=User, on_delete=models.CASCADE)
    Rent_type= models.IntegerChoices('Rent', '600 700 800 900 1000')
    Average_rent_per_unit = models.BigIntegerField(blank=True, choices=Rent_type.choices)
    First_Mtg_Interest_Rate = models.DecimalField(max_digits=5, decimal_places=2)

    
    
    def __str__(self):
        return str(user) + "s" + "details"




from django_google_maps import fields as map_fields

class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)