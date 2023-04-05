from django.shortcuts import render
from django.contrib import messages

# Create your views here.
import json
from .models import UserPref

def index(request):
    exists=UserPref.objects.filter(user=request.user).exists()
    pref=None
    if exists:
        pref=UserPref.objects.get(user=request.user)
    
    if request.method== "POST":
        print(request.POST.get("Currency"))
        curr=request.POST.get("Currency")
        if exists:            
            pref.currency=curr
            pref.save()
        else:
            UserPref.objects.create(user=request.user, currency=curr)
        messages.success(request, "Changes saved")
        
    d=json.load(open(r"UserPrefrences/currencies.json"))
    l=[]
    for cur, value in d.items():
        l.append((cur, value))
    return render(request, "preferences/index.html", {"c": l, "user_pref":pref})