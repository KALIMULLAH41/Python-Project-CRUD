
from FoodApp import views
from django.urls import path
app_name='FoodApp'
urlpatterns = [
    path('',views.home,name='home'),
    path('<int:item_id>/',views.details,name='details'),
    path('add/',views.add_item,name='additem'),
]

