from django.db import models

# Create your models here.


class foodCalories(models.Model):

    food_name = models.CharField(max_length=50)
    quantity = models.FloatField()
    quantity_gm = models.FloatField()
    calorie = models.FloatField()

    def __str__(self):
        return self.food_name
