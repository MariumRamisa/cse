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

    # user
    #path('userlist/', user.as_view()),
    # path('single_user/<int:id>/', user.as_view()),
    # path('single_user/<str:name>/', user.as_view()),
    #path('login/', LoginView.as_view()),
    #path('login/', views.login_api),
    #path('register/', views.register_api),

    # user details
    path('api/user_detail_list/', user_detail_list.as_view()),
    path('api/user_detail_list/<int:user_id>/', user_detail_list.as_view()),
    #path('api/user_detail/create/', create_user_detail.as_view()),
    #path('api/user_detail/<int:id>/', user_detail.as_view()),
    # food
    path('api/food_detail/', food_detail_list.as_view()),
    path('api/single_food_detail/<int:id>/', food_detail_list.as_view()),
    # nutrition detail
    path('api/nutrition_list/', nutrition_list.as_view()),
    path('api/single_food_nutrition/<str:food_name>/', nutrition_list.as_view()),
    # user food intake
    path('api/food_intake/', food_intake.as_view()),
    path('api/single_food_intake/<int:user_id>', food_intake.as_view()),
    # diet list
    path('api/diet_list/', diet_list.as_view()),
    path('api/single_diet_list/<int:id>/', diet_list.as_view()),
    # user calorie detail
    path('api/user_calorie/', user_calorie_list.as_view()),
    path('api/single_user_calorie/<int:user_id>/',
         user_calorie_list.as_view()),
    # exercise
    path('api/exercise/', exercise_detail_list.as_view()),
    path('api/single_exercise/<str:exercise_name>/',
         exercise_detail_list.as_view()),
    # burned cal
    path('api/burned_calorie/', burned_cal.as_view()),
    path('api/single_user_burned/<int:user_id>/',
         burned_cal.as_view()),


]

"""
