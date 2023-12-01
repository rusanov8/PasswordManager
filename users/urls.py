from django.urls import path
from .apps import UsersConfig
from .views import UserCreateApiView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = UsersConfig.name


urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token-create'),
    path('token/refresh', TokenRefreshView.as_view(), name='token-refresh'),

    path('users/create', UserCreateApiView.as_view(), name='user-create'),
]
