from django.db import models
from user.models import user
from exercise.models import exercisecal
# Create your models here.

# declation of fields


class burned_cal_detail(models.Model):
    user_id = models.ForeignKey(
        user, on_delete=models.CASCADE, primary_key=True)
    date = models.DateField()
    exercise_name = models.ForeignKey(exercisecal, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return self.exercise_name.exercise_name
# caltulate the burned calorie

    @property
    def burned_cal(self):
        q = self.quantity
        c = self.exercise_name.calorie
        return q*c
