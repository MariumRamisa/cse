from django.db import models

# Create your models here.


class exercisecal(models.Model):

    exercise_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    calorie = models.FloatField()

    def __str__(self):
        return self.exercise_name
