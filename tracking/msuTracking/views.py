from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
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
@login_required
def index(request):
    if request.method == "POST":
        form = NewFoodAdd(request.POST)

        if form.is_valid():
            food = form.cleaned_data["food"]
            quantity = form.cleaned_data["quantity"]
            meal_name = form.cleaned_data["meal"]
            user = request.user 

            food_nutrition = {key: int(value) * quantity for key, value in foodInfo(food).items()}
            try: 
                date = Day.objects.get(date=datetime.date.today(), user=request.user)
            except Day.DoesNotExist:
                date = Day(date=datetime.date.today(), user=request.user)
                date.save()

            meal, created = Meal.objects.get_or_create(date=date, meal_name=meal_name, user=request.user)
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
    
    if request.GET.get("date"):
        selected_date = request.GET.get("date")
    else:
        selected_date = datetime.date.today().strftime("%Y-%m-%d")
    
    try:
        day = Day.objects.get(date=selected_date, user=request.user)
        meals = (
            day.meals.all()
            .prefetch_related("item")
            .order_by("meal_name")
        )
    except Day.DoesNotExist:
        day = Day(date=selected_date, user=request.user)
        day.save()
        meals = (
            day.meals.all()
            .prefetch_related("item")
            .order_by("meal_name")
        )
    included_dates = Day.objects.values_list('date', flat=True)
    print(included_dates)
    
    dates = set([d.strftime("%Y-%m-%d") for d in included_dates])

    meal_totals = dict()
    for meal in meals:
        total_calories, total_protein, total_carbs, total_fat = 0, 0, 0, 0
        for item in meal.item.all():
            total_calories += item.calories
            total_protein += item.protein 
            total_carbs += item.carbs 
            total_fat += item.fat

        meal_totals[meal.meal_name] = [total_calories, total_protein, total_carbs, total_fat]
    
    total_calories, total_protein, total_carbs, total_fat = 0, 0, 0, 0 

    if meal_totals:
        for meal, totals in meal_totals.items():
            total_calories += totals[0]
            total_protein += totals[1]
            total_carbs += totals[2]
            total_fat += totals[3]
    

    return render(request, "msuTracking/index.html", {
        "foodInfo": get_foods().items(), 
        "meals": meals,
        "dates": dates, 
        "todaysDate": datetime.date.today().strftime("%Y-%m-%d"),
        "day": selected_date,
        "totals": meal_totals,
        "total_calories": total_calories,
        "total_protein": total_protein, 
        "total_carbs": total_carbs, 
        "total_fat": total_fat, 
    }) 

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'msuTracking/signup.html')

def login(request):
    return render(request, 'msuTracking/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def delete_data(request): 
    pass 