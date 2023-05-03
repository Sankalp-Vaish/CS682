from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class User_details(models.Model):
    user= models.OneToOneField(to=User, on_delete=models.CASCADE)
    Rent_type= models.IntegerChoices('Rent', '600 700 800 900 1000')
    Average_rent_per_unit = models.BigIntegerField(blank=True, choices=Rent_type.choices)
    First_Mtg_Interest_Rate = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return str(self.user) + "s" + "details"


class favourites(models.Model):
    user= models.ForeignKey(to=User, on_delete=models.CASCADE)
    city= models.CharField(max_length=30)
    status= models.CharField(max_length=30, null=True)
    year_built= models.CharField(max_length=30, null=True)
    baths= models.CharField(max_length=30, null=True)
    beds= models.CharField(max_length=30, null=True)
    stories= models.CharField(max_length=30, null=True)
    list_price= models.CharField(max_length=30, null=True)
    unit= models.CharField(max_length=30, null=True)
    postal_code= models.CharField(max_length=30, null=True)
    street_name= models.CharField(max_length=30, null=True)
    lat= models.CharField(max_length=30, null=True)
    lon= models.CharField(max_length=30, null=True)
    link= models.TextField(null=True)
    property_id= models.CharField(max_length=30, null=False)
    tax= models.CharField(max_length=30, null=True)
    insurance_rate= models.CharField(max_length=30, null=True)
    fav_toggle= models.BooleanField(default=False)
    Cash_On_Cash_ROI=models.CharField(max_length=30, null=True)
    Cashflow_per_unit_per_month=models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.user) + "s" + "favourites"



from django_google_maps import fields as map_fields

class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)