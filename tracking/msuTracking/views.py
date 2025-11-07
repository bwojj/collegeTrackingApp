from django.shortcuts import render
from django import forms
from django.shortcuts import redirect
from foodData import get_foods, foodInfo
import datetime 

from .models import Meal, FoodData, Day

class NewFoodAdd(forms.Form):
    food = forms.CharField(max_length=64, label="FoodName")
    quantity = forms.IntegerField(label="Weight")
    meal = forms.CharField(max_length=64, label="MealName")


# Create your views here.
def index(request):
    if request.method == "POST":
        form = NewFoodAdd(request.POST)

        if form.is_valid():
            food = form.cleaned_data["food"]
            quantity = form.cleaned_data["quantity"]
            meal_name = form.cleaned_data["meal"]

            food_nutrition = {key: int(value) * quantity for key, value in foodInfo(food).items()}
            
            date = Day.objects.get(date=datetime.date.today())
            try: 
                meal = Meal.objects.get(date=date, meal_name=meal_name)
            except Meal.DoesNotExist:
                meal = Meal(date=date, meal_name=meal_name)
            food_item = FoodData(
                meal=meal,
                food_name=food,
                calories=food_nutrition["calories"],
                protein=food_nutrition["protein"],
                carbs=food_nutrition["carbs"],
                fat=food_nutrition["fat"]
            )

            date.save()
            meal.save()
            food_item.save()

            return redirect('index')
    
    selected_date = request.GET.get("date", datetime.date.today())
    try:
        day = Day.objects.get(date=selected_date)
        meals = (
            day.meals.all()
            .prefetch_related("item")
            .order_by("meal_name")
        )
    except Day.DoesNotExist:
        day = Day(date=selected_date)
        day.save()
        meals = (
            day.meals.all()
            .prefetch_related("item")
            .order_by("meal_name")
        )

    return render(request, "msuTracking/index.html", {
        "foodInfo": get_foods().items(), 
        "meals": meals,
    }) 