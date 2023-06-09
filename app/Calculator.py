import numpy as np
from UserPrefrences.models import UserPref, Property_Info, Environmentals, Financing, Income, Operating_Expenses, Pests, Cash_requirements

def calculator(request, Fair_Market_Value=374000.00, Number_of_Units=6, Property_Taxes=5400.00, insurance_rate=0.003, First_Mtg_Interest_Rate=0.08, Average_rent_per_unit=800):
    # -------------------------
    # Property Info	
    # Address	91 Bellevue Rd

    
    prop=Property_Info.objects.get(user=request.user)
    env=Environmentals.objects.get(user=request.user)
    fin=Financing.objects.get(user=request.user)
    inc=Income.objects.get(user=request.user)
    op=Operating_Expenses.objects.get(user=request.user)
    pest=Pests.objects.get(user=request.user)
    cash=Cash_requirements.objects.get(user=request.user)

    Fair_Market_Value = float(Fair_Market_Value) #need to fetch from the api
    Vacancy_Rate = float(prop.Vacancy_Rate)#5.00/100 
    Management_Rate = float(prop.Management_Rate)#5.00/100
    Advertizing_Cost_per_Vacancy = float(prop.Advertizing_Cost_per_Vacancy)#100.00 
    if Number_of_Units==None:
        Number_of_Units=6
    Number_of_Units	= int(Number_of_Units) #need to fetch from the api
    Annual_Appreciation_Rate = 3.00/100
    if Average_rent_per_unit=="":
        Average_rent_per_unit=800.00
    Average_rent_per_unit = float(Average_rent_per_unit) #800.00 This is set at by intuition and taken reference from the given calculator. This must be somehow given to the user to feed the app.

    # --------------------------
    # Purchase Info	
    Offer_Price = Fair_Market_Value
    Repairs = (1.3/100)*Offer_Price
    Repairs_Contingency = 0.2*Repairs
    Lender_Fee = 0.01*Offer_Price
    Broker_Fee = (1.3/100)*Offer_Price
    # Environmentals 	=   
    Inspections_Engineer_Report	= float(env.Inspections_Engineer_Report) #700.00
    Appraisals = float(env.Appraisals) #700.00 
    Misc = float(env.Misc)#500.00 
    Transfer_Tax = (Offer_Price/500)*2.28
    Legal = float(env.Legal)#600.00 

    Real_Purchase_Price =  (Offer_Price + Repairs + Repairs_Contingency + Lender_Fee + Broker_Fee + Inspections_Engineer_Report + Appraisals + Misc + Transfer_Tax + Legal)

    # ----------------------------
    # Financing (Monthly)	
    First_Mtg_Principle_Borrowed = Offer_Price*0.95
    if First_Mtg_Interest_Rate=="":
        First_Mtg_Interest_Rate=0.08
    First_Mtg_Interest_Rate	= float(First_Mtg_Interest_Rate) #need to give an option to be user defined 0.08
    First_Mtg_Amortization_Period = float(fin.First_Mtg_Amortization_Period)#30 # in years
    First_Mtg_CMHC_Fee = float(fin.First_Mtg_CMHC_Fee)#0.00
    First_Mtg_Total_Principle_Incl_CMHC_Fees = First_Mtg_Principle_Borrowed + First_Mtg_CMHC_Fee

    # Calculating monthly payment with the formula Payment = pv* apr/12*(1+apr/12)^(nper*12)/((1+apr/12)^(nper*12)-1)
    # First_Mtg_Total_Monthly_Payment	= First_Mtg_Principle_Borrowed * First_Mtg_Interest_Rate/12 *(1+First_Mtg_Interest_Rate/12)**(First_Mtg_Amortization_Period*12)/((1+First_Mtg_Interest_Rate/12)**(First_Mtg_Amortization_Period*12)-1)
    First_Mtg_Total_Monthly_Payment = First_Mtg_Total_Principle_Incl_CMHC_Fees * ((((1+(First_Mtg_Interest_Rate/2))**(1/6))-1)/(1-(((1+(First_Mtg_Interest_Rate/2))**(1/6))**(First_Mtg_Amortization_Period*-12))))

    Second_Mtg_Principle_Amount	= float(fin.Second_Mtg_Principle_Amount)#0.00  
    Second_Mtg_Interest_Rate = 12/100.00
    Second_Mtg_Amortization_Period	= float(fin.Second_Mtg_Amortization_Period)#30 #in years...........

    # Second_Mtg_Total_Monthly_Payment = Second_Mtg_Principle_Amount * Second_Mtg_Interest_Rate/12 *(1+Second_Mtg_Interest_Rate/12)**(Second_Mtg_Amortization_Period*12)/((1+Second_Mtg_Interest_Rate/12)**(Second_Mtg_Amortization_Period*12)-1)
    Second_Mtg_Total_Monthly_Payment = Second_Mtg_Principle_Amount * ((((1+(Second_Mtg_Interest_Rate/2))**(1/6))-1)/(1-(((1+(Second_Mtg_Interest_Rate/2))**(1/6))**(Second_Mtg_Amortization_Period*-12))))
    # print("Second_Mtg_Total_Monthly_Payment ", Second_Mtg_Total_Monthly_Payment)

    Interest_Only_Principle_Amount	= float(fin.Interest_Only_Principle_Amount)#0.00   
    Interest_Only_Interest_Rate	= float(fin.Interest_Only_Interest_Rate)#0.00   
    Interest_Only_Total_Monthly_Payment	=float(fin.Interest_Only_Total_Monthly_Payment)# 0.00   
    Other_Monthly_Financing_Costs = float(fin.Other_Monthly_Financing_Costs)#300.00 

    Cash_Required_to_Close_after_financing = Real_Purchase_Price - (First_Mtg_Principle_Borrowed + First_Mtg_Total_Monthly_Payment + Second_Mtg_Principle_Amount + Second_Mtg_Total_Monthly_Payment + Interest_Only_Principle_Amount) 

    # -------------------------
    # Income(Annual)
    Gross_Rents = (Number_of_Units*Average_rent_per_unit*12)
    Parking	= float(inc.Parking)#0.00	
    Storage = float(inc.Storage)#0.00		
    Laundry_Vending	=float(inc.Laundry_Vending)#0.00	
    Other = float(inc.Other)#0.00  
    Total_Income = Gross_Rents +  Parking + Storage + Laundry_Vending + Other
    Vacancy_Loss = Total_Income * Vacancy_Rate #(% of Total Income)
    # print("Vacancy_Rate", Vacancy_Rate)
    # print("Total_Income ", Total_Income)
    # print("Vacancy_Loss ", Vacancy_Loss)

    Effective_Gross_Income	= Total_Income - Vacancy_Loss
    # print("Effective_Gross_Income ", Effective_Gross_Income)

    # -------------------------
    # Operating Expenses (Annual)	
    if Property_Taxes==None:	
        Property_Taxes=5400.00
    Property_Taxes = float(Property_Taxes) #must fetch from the api
    if insurance_rate==None:
        insurance_rate=0.003
    Insurance = float(insurance_rate)*Fair_Market_Value #must fetch from the api 
    Repairs	= (5.00/100)*Gross_Rents
    Electricity = float(op.Electricity)#0.00
    Gas = float(op.Gas)#0.00 
    Lawn_Snow_Maintenance = float(op.Lawn_Snow_Maintenance)#0.00	
    Water_Sewer = 100*12 
    Cable = 100*12
    Management	= Total_Income*Management_Rate
    Caretaking	= 200*12
    Advertizing	= Number_of_Units * 12 * Vacancy_Rate/2 * Advertizing_Cost_per_Vacancy
    Association_Fees = float(op.Association_Fees)#0.00  
    # Pest_Control
    if(Number_of_Units<2):
        Pest_Control = 140 * Number_of_Units
    else:
        Pest_Control = 70 * Number_of_Units
    Security = Number_of_Units * 12 * Vacancy_Rate/1.5 * 50 
    Trash_Removal = float(pest.Trash_Removal)#0.00	
    Miscellaneous = float(pest.Miscellaneous)#0.00	
    Common_Area_Maintenance	= float(pest.Common_Area_Maintenance)#0.00 
    Capital_Improvements = float(pest.Capital_Improvements)#0.00   
    Accounting = float(pest.Accounting)#0.00	
    Legal = float(pest.Legal)#0.00	
    Bad_Debts = float(pest.Bad_Debts)#0.00	
    Other = float(pest.Other)#0.00 # (licence, permits, bank charges, supplies, fees)		
    Evictions = Number_of_Units * 12 * Vacancy_Rate / 2 / 10 * 1000 

    Total_Expenses = (Property_Taxes + Insurance + Repairs + Electricity + Gas + Lawn_Snow_Maintenance + Water_Sewer + Cable + Management + Caretaking + Advertizing + Association_Fees + Pest_Control + Security + Trash_Removal + Miscellaneous + Common_Area_Maintenance + Capital_Improvements + Accounting + Legal + Bad_Debts + Other + Evictions)
    # print("Total_Expenses ", Total_Expenses)
    # -----------------------
    # Net Operating Income(Annual)
    Net_Operating_Income = Effective_Gross_Income - Total_Expenses

    # print("Effective_Gross_Income ", Effective_Gross_Income)
    # print("Net_Operating_Income ", Net_Operating_Income)
    

    # -----------------------
    # Cash requirements
    Deposit_made_with_Offer	= float(cash.Deposit_made_with_Offer)#0.00
    Less_ProRation_of_Rents	= float(cash.Less_ProRation_of_Rents)#0.00
    Cash_Required_to_Close = Cash_Required_to_Close_after_financing - Deposit_made_with_Offer
    Total_Cash_Required	= Cash_Required_to_Close + Deposit_made_with_Offer - Less_ProRation_of_Rents
    # print("Total_Cash_Required ", Total_Cash_Required)


    # -----------------------
    # Cashflow summary (Annual)

    EGI = Effective_Gross_Income
    OE = -1 * Total_Expenses
    NOI = Net_Operating_Income
    Debt_Servicing_costs = (-First_Mtg_Total_Monthly_Payment-Second_Mtg_Total_Monthly_Payment-Interest_Only_Total_Monthly_Payment-Other_Monthly_Financing_Costs) * 12
    Annual_Profit_or_Loss = NOI + Debt_Servicing_costs
    Total_Monthly_Profit_or_Loss = Annual_Profit_or_Loss/12
    Cashflow_per_unit_per_month = Total_Monthly_Profit_or_Loss/Number_of_Units 
    # print("Annual_Profit_or_Loss ", Annual_Profit_or_Loss)
    # print("Debt_Servicing_costs ", Debt_Servicing_costs)
    # print("NOI", NOI)

    # Quick Analysis
    First_Mtg_LTV = (First_Mtg_Principle_Borrowed / Fair_Market_Value) * 100
    First_Mtg_LTPP = (First_Mtg_Principle_Borrowed / Offer_Price) * 100
    Second_Mtg_LTV = (Second_Mtg_Principle_Amount / Fair_Market_Value) * 100
    Second_Mtg_LTPP = (Second_Mtg_Principle_Amount / Offer_Price) * 100
    CapRate_on_PP = (Net_Operating_Income/Fair_Market_Value) * 100
    CapRate_on_FMV = (Net_Operating_Income/Offer_Price) * 100
    Average_Rent = (Gross_Rents/Number_of_Units)/12
    GRM = Offer_Price/Gross_Rents
    # Calculating DCR
    if(-Debt_Servicing_costs<=0):
        print("No debt to cover")
    else:
        DCR = Net_Operating_Income/(-Debt_Servicing_costs)

    # Calculating Cash_On_Cash_ROI 
    if(Total_Cash_Required <= 0):
        print("Infinite")
    else:
        Cash_On_Cash_ROI = (Annual_Profit_or_Loss/Total_Cash_Required)*100


    # Calculating Equity_ROI 
    ending_balance_first_mtg = 0.993 * First_Mtg_Principle_Borrowed #Just for temporary purpose, assigning 90% of First_Mtg_Principle_Borrowed
    ending_balance_second_mtg = 0.993 * Second_Mtg_Principle_Amount #Just for temporary purpose, assigning 90% of Second_Mtg_Principle_Amount

    if(Total_Cash_Required <= 0):
        print("Infinite")
    else:
        Equity_ROI = ((First_Mtg_Principle_Borrowed-ending_balance_first_mtg + Second_Mtg_Principle_Amount - ending_balance_second_mtg) / Total_Cash_Required)*100

    # Calculating Appreciation_ROI
    if(Total_Cash_Required <= 0):
        print('Infite')
    else:
        Appreciation_ROI = ((Fair_Market_Value * (1 + Annual_Appreciation_Rate)-Fair_Market_Value) / abs(Total_Cash_Required)) * 100

    # Calculating Total_ROI
    if(Total_Cash_Required <= 0):
        print('Infite')
    else:
        Total_ROI = Cash_On_Cash_ROI + Equity_ROI + Appreciation_ROI

    # Calculating Forced_App_ROI
    if(Total_Cash_Required <= 0):
        print('Infite')
    else:
        Forced_App_ROI = ((Fair_Market_Value - Real_Purchase_Price) / abs(Total_Cash_Required)) * 100

    Expense_to_income_ratio = (Total_Expenses/Total_Income) * 100

    """print("First_Mtg_LTV " , First_Mtg_LTV , "\n" ,
    "First_Mtg_LTPP " , First_Mtg_LTPP , "\n" ,
    "Second_Mtg_LTV " , Second_Mtg_LTV , "\n" ,
    "Second_Mtg_LTPP " , Second_Mtg_LTPP , "\n" ,
    "CapRate_on_PP " , CapRate_on_PP , "\n" ,
    "CapRate_on_FMV " , CapRate_on_FMV , "\n" ,
    "Average_Rent " , Average_Rent , "\n" ,
    "GRM " , GRM , "\n" ,
    "DCR " , DCR , "\n" ,
    "Cash_On_Cash_ROI " , Cash_On_Cash_ROI , "\n" ,
    "Equity_ROI " , Equity_ROI , "\n" ,
    "Appreciation_ROI " , Appreciation_ROI , "\n" ,
    "Total_ROI " , Total_ROI , "\n" ,
    "Forced_App_ROI " , Forced_App_ROI , "\n" ,
    "Expense_to_income_ratio " , Expense_to_income_ratio, "\n")"""

    d=dict()
    d["Total_Monthly_Profit_or_Loss"]= "{:.2f}".format(Total_Monthly_Profit_or_Loss)
    d["Cashflow_per_unit_per_month"]= "{:.2f}".format(Cashflow_per_unit_per_month)
    d["First_Mtg_LTV"] ="{:.2f}".format(First_Mtg_LTV)
    d["First_Mtg_LTPP"] = "{:.2f}".format(First_Mtg_LTPP)
    d["Second_Mtg_LTV"] = "{:.2f}".format(Second_Mtg_LTV) 
    d["Second_Mtg_LTPP"] ="{:.2f}".format(Second_Mtg_LTPP)
    d["CapRate_on_PP"] = "{:.2f}".format(CapRate_on_PP)
    d["CapRate_on_FMV"] = "{:.2f}".format(CapRate_on_FMV)
    d["Average_Rent"] = "{:.2f}".format(Average_Rent )
    d["GRM"] = "{:.2f}".format(GRM )
    d["DCR"] = "{:.2f}".format(DCR )
    d["Cash_On_Cash_ROI"] = "{:.2f}".format(Cash_On_Cash_ROI)
    d["Equity_ROI"] = "{:.2f}".format(Equity_ROI)
    d["Appreciation_ROI"] = "{:.2f}".format(Appreciation_ROI)
    d["Total_ROI"] = "{:.2f}".format(Total_ROI )
    d["Forced_App_ROI"] = "{:.2f}".format(Forced_App_ROI)
    d["Expense_to_income_ratio"] = "{:.2f}".format(Expense_to_income_ratio)

    return d