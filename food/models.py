from django.db import models
from rest_framework import serializers

# Create your models here.


def func(value):
    if (value > 0):
        return value
    else:
        raise serializers.ValidationError("Invalid number")


class foodCalories(models.Model):

    food_name = models.CharField(max_length=50)
    quantity = models.FloatField(validators=[func])
    quantity_gm = models.FloatField(validators=[func])
    calorie = models.FloatField(validators=[func])

    def __str__(self):
        return self.food_name
