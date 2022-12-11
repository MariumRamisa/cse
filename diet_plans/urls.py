from django.urls import path
from .views import user_list, user_info
from user_details.views import user_detail_list

urlpatterns = [
    path('user/', user_list),
    path('user_details/', user_detail_list),

]
