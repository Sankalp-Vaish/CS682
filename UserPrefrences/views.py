from django.shortcuts import render
from django.contrib import messages

# Create your views here.
import json
from .models import UserPref, Property_Info, Environmentals, Financing, Income, Operating_Expenses, Pests, Cash_requirements
import decimal
def index(request):
    exists=UserPref.objects.filter(user=request.user).exists()
    exists2=Property_Info.objects.filter(user=request.user).exists()
    exists3=Income.objects.filter(user=request.user).exists()
    exists4=Pests.objects.filter(user=request.user).exists()
    prop=None
    pref=None
    env=None
    fin=None
    op=None
    inc=None
    pest=None
    cash=None
    if exists:
        pref=UserPref.objects.get(user=request.user)
    
    if exists2:
        prop=Property_Info.objects.get(user=request.user)
        print("1")
        print("gg", prop.Fair_Market_Value)

    else:
        Property_Info.objects.create(user=request.user)
    
    if exists3:
        env=Environmentals.objects.get(user=request.user)
        fin=Financing.objects.get(user=request.user)
        inc=Income.objects.get(user=request.user)
        op=Operating_Expenses.objects.get(user=request.user)
        # pest=Pests.objects.get(user=request.user)
        cash=Cash_requirements.objects.get(user=request.user)
        print("1")
        print("gg", prop.Fair_Market_Value)

    else:
        Environmentals.objects.create(user=request.user)
        Income.objects.create(user=request.user)
        Operating_Expenses.objects.create(user=request.user)
        Financing.objects.create(user=request.user)
        # Pests.objects.create(user=request.user)
        Cash_requirements.objects.create(user=request.user)

    if exists4:
        pest=Pests.objects.get(user=request.user)

    else:
        Pests.objects.create(user=request.user)
    
    if request.method== "POST":
        print(request.POST.get("Currency"))
        curr=request.POST.get("Currency")
        Fair_Market_Val=request.POST.get("Fair_Market_Value")
        print("in",Fair_Market_Val)
        if exists2:            
            #prop.Fair_Market_Value=Fair_Market_Val
            prop.Vacancy_Rate=request.POST.get("Vacancy_Rate")
            prop.Management_Rate=request.POST.get("Management_Rate")
            prop.Advertizing_Cost_per_Vacancy=request.POST.get("Advertizing_Cost_per_Vacancy")
            prop.Annual_Appreciation_Rate=request.POST.get("Annual_Appreciation_Rate")
            print("in2",prop.Fair_Market_Value)
            prop.save()
        else:
            # try:
            #     decimal_value=decimal.Decimal(Fair_Market_Value)
            #     if not decimal_value.is_finite():
            #         raise decimal.InvalidOperation("Decimal is not finite.")
            #     if decimal_value.is_nan() or decimal_value.is_infinite():
            #         raise decimal.InvalidOperation("Decimal contains NaN or Infinity values.")
            # except decimal.InvalidOperation:
            #     print("error", decimal_value)
            # my_value = decimal.Decimal(Fair_Market_Value)
            # my_integer = int(my_value)
            pass
            #Property_Info.objects.create(user=request.user, Fair_Market_Value=Fair_Market_Val, Vacancy_Rate=0.00)#, Management_Rate=0.0, Advertizing_Cost_per_Vacancy=0.0,Annual_Appreciation_Rate=0.0)
        if exists3:
            env.Inspections_Engineer_Report=request.POST.get("Inspections_Engineer_Report")
            env.Appraisals=request.POST.get("Appraisals")
            env.Misc=request.POST.get("Misc")
            env.Legal=request.POST.get("Legal")
            env.save()

            fin.First_Mtg_Amortization_Period=request.POST.get("First_Mtg_Amortization_Period")
            fin.First_Mtg_CMHC_Fee=request.POST.get("First_Mtg_CMHC_Fee")
            fin.Second_Mtg_Principle_Amount=request.POST.get("Second_Mtg_Principle_Amount")
            fin.Second_Mtg_Amortization_Period=request.POST.get("Second_Mtg_Amortization_Period")
            fin.Interest_Only_Principle_Amount=request.POST.get("Interest_Only_Principle_Amount")
            fin.Interest_Only_Interest_Rate=request.POST.get("Interest_Only_Interest_Rate")
            fin.Interest_Only_Total_Monthly_Payment=request.POST.get("Interest_Only_Total_Monthly_Payment")
            fin.Other_Monthly_Financing_Costs=request.POST.get("Other_Monthly_Financing_Costs")
            #fin.First_Mtg_Amortization_Period=request.POST.get("First_Mtg_Amortization_Period")
            fin.save()

            op.Electricity=request.POST.get("Electricity")
            op.Gas=request.POST.get("Gas")
            op.Lawn_Snow_Maintenance=request.POST.get("Lawn_Snow_Maintenance")
            op.Association_Fees=request.POST.get("Association_Fees")
            op.save()

            inc.Parking=request.POST.get("Parking")
            inc.Storage=request.POST.get("Storage")
            inc.Laundry_Vending=request.POST.get("Laundry_Vending")
            inc.Other=request.POST.get("Other")
            inc.save()

            pest.Trash_Removal=request.POST.get("Trash_Removal")
            pest.Miscellaneous=request.POST.get("Miscellaneous")
            pest.Common_Area_Maintenance=request.POST.get("Common_Area_Maintenance")
            pest.Capital_Improvements=request.POST.get("Capital_Improvements")
            pest.Accounting=request.POST.get("Accounting")
            pest.Legal=request.POST.get("Legal")
            pest.Bad_Debts=request.POST.get("Bad_Debts")
            pest.Other=request.POST.get("Other")
            pest.save()

            cash.Deposit_made_with_Offer=request.POST.get("Deposit_made_with_Offer")
            cash.Less_ProRation_of_Rents=request.POST.get("Less_ProRation_of_Rents")
            cash.save()
            
        if exists:            
            pref.currency=curr
            pref.save()
        else:
            UserPref.objects.create(user=request.user, currency=curr)
        messages.success(request, "Changes saved")
        
    d=json.load(open(r"UserPrefrences/currencies.json"))
    l=[]
    print(type(pref))
    for cur, value in d.items():
        l.append((cur, value))
    return render(request, "preferences/index.html", {"c": l, "user_pref":pref, "prop":prop, "env":env, "cash":cash, "op":op, "fin":fin, "inc":inc, "pest":pest})