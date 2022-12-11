from django.db import models
from user.models import user
from food.models import foodCalories
# Create your models here.


class user_food_intake_detail(models.Model):
    user_id = models.ForeignKey(
        user, on_delete=models.CASCADE, primary_key=True)
    meal_type = models.CharField(max_length=50)
    date = models.DateField()
    food_name = models.ForeignKey(foodCalories, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return self.meal_type

    @property
    def total_cal(self):
        q = self.quantity
        c = self.food_name.calorie

        return q*c
