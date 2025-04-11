from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import *

# Create your views here.


def SignUp(request):
    if request.user.is_authenticated:
        return redirect("/auth/login/")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/auth/login/")
        else:
            form = UserCreationForm()
            return render(
                request,
                "user/register.html",
                {"form": form, "mssg": "Somthing Went Worng !"},
            )
    form = UserCreationForm()
    return render(request, "user/register.html", {"form": form})


def SignIn(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        user_name = request.POST.get("username")
        pass_word = request.POST.get("password")
        user = authenticate(request, username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            form = AuthenticationForm()
            return render(
                request,
                "user/login.html",
                {"form": form, "mssg": "Somthing Went Wrong !"},
            )

    form = AuthenticationForm()
    return render(request, "user/login.html", {"form": form})


def SignOut(request):
    logout(request)
    return redirect("/")
