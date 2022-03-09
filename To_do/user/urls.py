from django.urls import path
from user import views

urlpatterns = [
    path('', views.user_register),
    path('login/', views.user_login, name="user_login"),
]
