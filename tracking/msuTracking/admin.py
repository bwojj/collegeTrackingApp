from django.contrib import admin

# Register your models here.
from .models import Meal, FoodData

admin.site.register(Meal)
admin.site.register(FoodData)