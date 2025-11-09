from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Day(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='days', default=1)
    date = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'date'], name='unique_day_per_user')
        ]

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals', default=1)
    date = models.ForeignKey(Day, on_delete=models.CASCADE, related_name="meals")
    meal_name = models.CharField(max_length=64)


class FoodData(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="item", default=1)
    food_name = models.CharField(max_length=64)
    calories = models.IntegerField()
    protein = models.IntegerField()
    carbs = models.IntegerField()
    fat = models.IntegerField()
