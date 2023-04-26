from django.db import models

from django.contrib.auth.models import User
import decimal

# decimal.getcontext().prec = 50
# context = decimal.getcontext()
# context.traps[decimal.InvalidOperation] = 0
# Create your models here.

class UserPref(models.Model):
    user= models.OneToOneField(to=User, on_delete=models.CASCADE)
    currency= models.CharField(max_length=255, blank=True, null=True, default="USD")
    def __str__(self):
        return str(user) + "s" + "prefrences"
    # Property Info	
class Property_Info(models.Model):
    user= models.OneToOneField(to=User, on_delete=models.CASCADE)
    Fair_Market_Value = models.DecimalField(max_digits=10, decimal_places=2, default=374000.00)
    Vacancy_Rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.05)
    Management_Rate = models.DecimalField(max_digits=10, decimal_places=3, default=0.05)
    Advertizing_Cost_per_Vacancy = models.DecimalField(max_digits=8, decimal_places=3, default=100.00)
    Annual_Appreciation_Rate = models.DecimalField(max_digits=10, decimal_places=3, default=0.03)
    def __str__(self):
        return str(user) + "s" + "Property_Info"
    # Purchase Info	
    # Environmentals 
class Environmentals(models.Model):
    user= models.OneToOneField(to=User, on_delete=models.CASCADE)
    Inspections_Engineer_Report = models.DecimalField(max_digits=10, decimal_places=3, default=700.00)
    Appraisals = models.DecimalField(max_digits=10, decimal_places=3, default=700.00)
    Misc = models.DecimalField(max_digits=10, decimal_places=3, default=500.00)
    Legal = models.DecimalField(max_digits=10, decimal_places=3, default=600.00)
    # Financing (Monthly)
class Financing(models.Model):
    user= models.OneToOneField(to=User, on_delete=models.CASCADE)
    First_Mtg_Amortization_Period = models.DecimalField(max_digits=10, decimal_places=3, default=30.00)
    First_Mtg_CMHC_Fee = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Second_Mtg_Principle_Amount	 = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    #Second_Mtg_Interest_Rate = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Second_Mtg_Amortization_Period = models.DecimalField(max_digits=10, decimal_places=3, default=30.00)
    Interest_Only_Principle_Amount= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Interest_Only_Interest_Rate	= models.DecimalField(max_digits=10, decimal_places=3, default=0.00) 
    Interest_Only_Total_Monthly_Payment = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Other_Monthly_Financing_Costs= models.DecimalField(max_digits=10, decimal_places=3, default=300.00)
    # Income(Annual)
class Income(models.Model):
    user= models.OneToOneField(to=User, on_delete=models.CASCADE)
    Parking= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Storage= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Laundry_Vending= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Other= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # Operating Expenses (Annual)
class Operating_Expenses(models.Model):
    user= models.OneToOneField(to=User, on_delete=models.CASCADE)
    Electricity = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Gas= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Lawn_Snow_Maintenance= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Association_Fees= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)

    #Pest Control
class Pest_Control(models.Model):
    user= models.OneToOneField(to=User, on_delete=models.CASCADE)
    Trash_Removal = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Miscellaneous= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Common_Area_Maintenance= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Capital_Improvements= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Accounting= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Legal= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Bad_Debts= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Other= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)

class Pests(models.Model):
    user= models.OneToOneField(to=User, on_delete=models.CASCADE)
    Trash_Removal = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Miscellaneous= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Common_Area_Maintenance= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Capital_Improvements= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Accounting= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Legal= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Bad_Debts= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Other= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)

    # Cash requirements
class Cash_requirements(models.Model):
    user= models.OneToOneField(to=User, on_delete=models.CASCADE)
    Deposit_made_with_Offer= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    Less_ProRation_of_Rents= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)


    

    #     Fair_Market_Value = models.DecimalField(max_digits=10, decimal_places=3, default=374000.00)
    # Vacancy_Rate = models.DecimalField(max_digits=10, decimal_places=3, default=0.05)
    # Management_Rate = models.DecimalField(max_digits=10, decimal_places=3, default=0.05)
    # Advertizing_Cost_per_Vacancy = models.DecimalField(max_digits=10, decimal_places=3, default=100.00)
    # Annual_Appreciation_Rate = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # # Purchase Info	
    # # Environmentals 
    # Inspections_Engineer_Report = models.DecimalField(max_digits=10, decimal_places=3, default=700.00)
    # Appraisals = models.DecimalField(max_digits=10, decimal_places=3, default=700.00)
    # Misc = models.DecimalField(max_digits=10, decimal_places=3, default=500.00)
    # Legal = models.DecimalField(max_digits=10, decimal_places=3, default=600.00)
    # # Financing (Monthly)
    # First_Mtg_Amortization_Period = models.DecimalField(max_digits=10, decimal_places=3, default=30)
    # First_Mtg_CMHC_Fee = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # Second_Mtg_Principle_Amount	 = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # #Second_Mtg_Interest_Rate = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # Second_Mtg_Amortization_Period = models.DecimalField(max_digits=10, decimal_places=3, default=30)
    # Interest_Only_Principle_Amount= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # Interest_Only_Interest_Rate	= models.DecimalField(max_digits=10, decimal_places=3, default=0.00) 
    # Interest_Only_Total_Monthly_Payment = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # Other_Monthly_Financing_Costs= models.DecimalField(max_digits=10, decimal_places=3, default=300.00)
    # # Income(Annual)
    # Parking= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # Storage= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # Laundry_Vending= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # Other= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # # Operating Expenses (Annual)
    # Electricity = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # Gas= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # Lawn_Snow_Maintenance= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # Association_Fees= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # #Pest Control
    # Trash_Removal = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # Miscellaneous= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # Common_Area_Maintenance= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # Capital_Improvements= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # Accounting= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # Legal= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # Bad_Debts= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # Other= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # # Cash requirements
    # Deposit_made_with_Offer= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    # Less_ProRation_of_Rents= models.DecimalField(max_digits=10, decimal_places=3, default=0.00)