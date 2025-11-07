from django.db import models

# Create your models here.

class Day(models.Model):
    date = models.DateField(unique=True)

class Meal(models.Model):
    date = models.ForeignKey(Day, on_delete=models.CASCADE, related_name="meals")
    meal_name = models.CharField(max_length=64)


class FoodData(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="item")
    food_name = models.CharField(max_length=64)
    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()
