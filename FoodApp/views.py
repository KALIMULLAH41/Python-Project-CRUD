from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Items
from FoodApp.forms import ItemForm


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

def add_item(request):
    form=ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('FoodApp:home')
        
    return render(request,'FoodApp/item-form.html',{'form':form})