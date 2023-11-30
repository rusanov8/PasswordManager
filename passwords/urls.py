from django.urls import path
from .apps import PasswordsConfig
from .views import PasswordRetrieveCreateView, PasswordListView

app_name = PasswordsConfig.name


urlpatterns = [
    path('password/<str:service_name>', PasswordRetrieveCreateView.as_view({'get': 'retrieve', 'post': 'create'}), name='password_detail'),
    path('password/', PasswordListView.as_view(), name='password-list')
]
