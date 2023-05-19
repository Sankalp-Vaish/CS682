from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from .models import Property_Info, Environmentals, Financing, Income, Operating_Expenses, Pests, Cash_requirements

# For the USer Prefrence page
def index(request):
    exists=Property_Info.objects.filter(user=request.user).exists()
    prop=None
    env=None
    fin=None
    op=None
    inc=None
    pest=None
    cash=None
    if exists:
        prop=Property_Info.objects.get(user=request.user)
        env=Environmentals.objects.get(user=request.user)
        fin=Financing.objects.get(user=request.user)
        inc=Income.objects.get(user=request.user)
        op=Operating_Expenses.objects.get(user=request.user)
        pest=Pests.objects.get(user=request.user)
        cash=Cash_requirements.objects.get(user=request.user)

    else:
        Property_Info.objects.create(user=request.user)
        prop=Property_Info.objects.get(user=request.user)
        Environmentals.objects.create(user=request.user)
        Income.objects.create(user=request.user)
        Operating_Expenses.objects.create(user=request.user)
        Financing.objects.create(user=request.user)
        Cash_requirements.objects.create(user=request.user)
        env=Environmentals.objects.get(user=request.user)
        fin=Financing.objects.get(user=request.user)
        inc=Income.objects.get(user=request.user)
        op=Operating_Expenses.objects.get(user=request.user)
        cash=Cash_requirements.objects.get(user=request.user)

        Pests.objects.create(user=request.user)
        pest=Pests.objects.get(user=request.user)
    
    if request.method== "POST":

        if exists:            
            #prop.Fair_Market_Value=Fair_Market_Val
            prop.Vacancy_Rate=request.POST.get("Vacancy_Rate")
            prop.Management_Rate=request.POST.get("Management_Rate")
            prop.Advertizing_Cost_per_Vacancy=request.POST.get("Advertizing_Cost_per_Vacancy")
            prop.Annual_Appreciation_Rate=request.POST.get("Annual_Appreciation_Rate")
            print("in2",prop.Fair_Market_Value)
            prop.save()

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

        else:
            pass
        messages.success(request, "Changes saved")
        

    return render(request, "preferences/index.html", { "prop":prop, "env":env, "cash":cash, "op":op, "fin":fin, "inc":inc, "pest":pest})