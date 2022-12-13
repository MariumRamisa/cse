from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (RegistrationView, LoginView, AccountViewSet)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)
app_name = "accounts"

router = SimpleRouter()
router.register(r'account', AccountViewSet, basename='account')
urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='login_view'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegistrationView.as_view(), name="api-register"),
    path('api/login/', LoginView.as_view(), name="api-login"),
    path('api/', include((router.urls, 'accounts')))

]
