from django.urls import path
from .views import *


urlpatterns = [
    path("", IndexView, name="home"),
    path("create/", CreateView, name="create"),
    path("edit/<int:pk>", EditView, name="edit"),
    path("delete/<int:pk>", DeleteView, name="delete"),
]
