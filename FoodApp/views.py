from django.shortcuts import render
from django.http import HttpResponse
from .models import Items
# Create your views here.
def home(request):
    item_list=Items.objects.all()
    context={
        'item_list':item_list
    }
    return render(request,'FoodApp/home.html',context)
def details(request,item_id):
    item_list=Items.objects.get(pk=item_id)
    context={
        'item_list':item_list
    }
    return render(request,'FoodApp/details.html',context)