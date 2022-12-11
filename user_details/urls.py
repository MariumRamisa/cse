from django.urls import path
from user.views import user_list
from .views import user_detail_list
from food.views import food_detail_list
from nutrient_detail.views import nutrition_list
from user_food_intake_details.views import food_intake
from diet_plans.views import diet_list
from user_calorie_details.views import user_calorie_list
urlpatterns = [
    path('user/', user_list.as_view()),
    path('single_user/<int:id>/', user_detail_list.as_view()),
    path('user_details/', user_detail_list.as_view()),
    path('single_user_detail/<int:user_id>/', user_detail_list.as_view()),
    path('food_detail/', food_detail_list.as_view()),
    path('single_food_detail/<int:id>/', food_detail_list.as_view()),
    path('nutrition_list/', nutrition_list.as_view()),
    path('single_food_nutrition_detail/<int:id>/', nutrition_list.as_view()),
    path('food_intake/', food_intake.as_view()),
    path('single_food_intake/<int:id>', food_intake.as_view()),
    path('diet_list/', diet_list.as_view()),
    path('single_diet_list/<int:id>', diet_list.as_view()),
    path('user_calorie/', user_calorie_list.as_view()),
    path('single_user_calorie_detail/<int:user_id>/',
         user_calorie_list.as_view()),

]
