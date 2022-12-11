from django.db import models
from user.models import user
from user_food_intake_details.models import user_food_intake_detail
from user_details.models import user_details
from burned_cal.models import burned_cal_detail
# Create your models here.


class user_calorie_detail(models.Model):

    user_id = models.OneToOneField(
        user, on_delete=models.CASCADE, primary_key=True)
    calorie_intake = models.ForeignKey(
        user_food_intake_detail, on_delete=models.CASCADE)
    goal_calorie = models.ForeignKey(user_details, on_delete=models.CASCADE)
    burned_calorie = models.ForeignKey(
        burned_cal_detail, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.name
