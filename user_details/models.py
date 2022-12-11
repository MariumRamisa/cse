from django.db import models
from user.models import user

# Create your models here.


class user_details(models.Model):

    user_id = models.OneToOneField(
        user, on_delete=models.CASCADE, primary_key=True)
    goal_weight = models.IntegerField()
    activity_level = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    location = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.IntegerField()
    age = models.IntegerField()
    net_goal = 1200
    weekly_goal = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return self.user_id.name

    @property
    def bmi(self):
        return self.weight/(self.height*self.height)
