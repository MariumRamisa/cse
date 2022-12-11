from django.db import models

# Create your models here.


class diet_plan(models.Model):
    goal_weight = models.DecimalField(max_digits=4, decimal_places=1)
    diet_plan = models.CharField(max_length=200)
