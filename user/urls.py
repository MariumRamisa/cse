from django.urls import path
from .views import user_list
from user_details.views import user_detail_list
from food.views import food_detail_list
from nutrient_detail.views import nutrition_list
from user_food_intake_details.views import food_intake
from diet_plans.views import diet_list
from user_calorie_details.views import user_calorie_list
from exercise.views import exercise_detail_list
from burned_cal.views import burned_cal


urlpatterns = [
    # user
    path('user/', user_list.as_view()),
    path('single_user/<int:id>/', user_list.as_view()),
    # user details
    path('user_detail/', user_detail_list.as_view()),
    path('single_user_detail/<int:user_id>/', user_detail_list.as_view()),
    # food
    path('food_detail/', food_detail_list.as_view()),
    path('single_food_detail/<int:id>/', food_detail_list.as_view()),
    # nutrition detail
    path('nutrition_list/', nutrition_list.as_view()),
    path('single_food_nutrition/<str:food_name>/', nutrition_list.as_view()),
    # user food intake
    path('food_intake/', food_intake.as_view()),
    path('single_food_intake/<int:user_id>', food_intake.as_view()),
    # diet list
    path('diet_list/', diet_list.as_view()),
    path('single_diet_list/<int:id>/', diet_list.as_view()),
    # user calorie detail
    path('user_calorie/', user_calorie_list.as_view()),
    path('single_user_calorie/<int:user_id>/',
         user_calorie_list.as_view()),
    # exercise
    path('exercise/', exercise_detail_list.as_view()),
    path('single_exercise/<str:exercise_name>/',
         exercise_detail_list.as_view()),
    # burned cal
    path('burned_calorie/', burned_cal.as_view()),
    path('single_user_burned/<int:user_id>/',
         burned_cal.as_view()),




]
