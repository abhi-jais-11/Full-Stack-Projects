from django.urls import path
from .views import *


urlpatterns = [
    path("register/", SignUp, name="register"),
    path("login/", SignIn, name="login"),
    path("logout/", SignOut, name="logout"),
]
