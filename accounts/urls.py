
"""
from django.urls import path
from .views import RegisterAPIView, LoginAPIView
from user_details.views import (
    user_detail_list  # create_user_detail, user_detail
)
from food.views import food_detail_list
from nutrient_detail.views import nutrition_list
from user_food_intake_details.views import food_intake
from diet_plans.views import diet_list
from user_calorie_details.views import user_calorie_list
from exercise.views import exercise_detail_list
from burned_cal.views import burned_cal

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterAPIView.as_view()),
    path('api/login/', LoginAPIView.as_view()),



]
"""
