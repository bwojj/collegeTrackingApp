from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django import forms
from django.shortcuts import redirect
from foodData import get_foods, foodInfo
from django.db.models import Case, When, Value, IntegerField
from django.utils import timezone
from django.urls import reverse
import datetime 

from .models import Meal, FoodData, Day

class NewFoodAdd(forms.Form):
    food = forms.CharField(max_length=64, label="FoodName")
    quantity = forms.IntegerField(label="Weight")
    meal = forms.CharField(max_length=64, label="MealName")

class CustomFoodAdd(forms.Form):
    food = forms.CharField(max_length=64, label="FoodName")
    meal = forms.CharField(max_length=64, label="MealName")
    calories = forms.IntegerField()
    protein = forms.IntegerField()
    carbs = forms.IntegerField()
    fat = forms.IntegerField()

def ensure_meals_exist(day, user):
    default_meals = ["Breakfast", "Lunch", "Pre-Lift", "Dinner"]
    for name in default_meals:
        Meal.objects.get_or_create(date=day, meal_name=name, user=user)

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
                date = Day.objects.get(date=timezone.localdate(), user=request.user)
                ensure_meals_exist(date, request.user)
            except Day.DoesNotExist:
                date = Day(date=timezone.localdate(), user=request.user)
                date.save()

                ensure_meals_exist(date, request.user)

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
        selected_date = timezone.localdate().strftime("%Y-%m-%d")
    
    try:
        day = Day.objects.get(date=selected_date, user=request.user)
        ensure_meals_exist(day, request.user)
        meals = (
            day.meals.all()
            .prefetch_related("item")
            .annotate(
                order=Case(
                    When(meal_name="Breakfast", then=Value(1)),
                    When(meal_name="Lunch", then=Value(2)),
                    When(meal_name="Pre-Lift", then=Value(3)),
                    When(meal_name="Dinner", then=Value(4)),
                    default=Value(5),
                    output_field=IntegerField(),
                )
            )
            .order_by("order")
        )
    except Day.DoesNotExist:
        day = Day(date=selected_date, user=request.user)
        day.save()
        ensure_meals_exist(day, request.user)
        meals = (
            day.meals.all()
            .prefetch_related("item")
            .annotate(
                order=Case(
                    When(meal_name="Breakfast", then=Value(1)),
                    When(meal_name="Lunch", then=Value(2)),
                    When(meal_name="Pre-Lift", then=Value(3)),
                    When(meal_name="Dinner", then=Value(4)),
                    default=Value(5),
                    output_field=IntegerField(),
                )
            )
            .order_by("order")
        )
    included_dates = Day.objects.values_list('date', flat=True)
    print(included_dates)
    
    dates = sorted([d.strftime("%Y-%m-%d") for d in included_dates], reverse=True)
    dates.append((timezone.localdate() + datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
    dates = set(dates)
    print(dates)
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
        "todaysDate": timezone.localdate().strftime("%Y-%m-%d"),
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

def delete_data(request, id): 
    food = FoodData.objects.get(id=id)

    date = food.meal.date.date

    food.delete()
    
    
    return redirect(reverse('index'))

def custom(request):
    if request.method == "POST":
        form = CustomFoodAdd(request.POST)

        if form.is_valid():
            food_name = form.cleaned_data["food"]
            meal_name = form.cleaned_data["meal"]
            calories = form.cleaned_data["calories"]
            protein = form.cleaned_data["protein"]
            carbs = form.cleaned_data["carbs"]
            fat = form.cleaned_data["fat"]

            day, created = Day.objects.get_or_create(date=timezone.localdate().strftime("%Y-%m-%d"), user=request.user)
            meal, created = Meal.objects.get_or_create(date=day, meal_name=meal_name, user=request.user)
            food = FoodData(
                meal=meal,
                food_name=food_name,
                calories=calories,
                protein=protein,
                carbs=carbs,
                fat=fat,
            )
            food.save()

            return redirect(reverse('index'))
    
    return redirect(reverse('index'))