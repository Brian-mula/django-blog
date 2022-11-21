from django.shortcuts import render

from accounts.models import IceCream


# Create your views here.
def home(request):
    all_blogs=IceCream.objects.all()
    return render(request,'accounts/dashboard.html',{'blogs':all_blogs})

def products(request):
    return render(request,'accounts/products.html')

def contact(request):
    return render(request,'accounts/contacts.html')