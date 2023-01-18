from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import NewUser, PostFweet
from .models import Fweet


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect("viewer/")
    else:
        return redirect("login")


def register(request):
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = NewUser()
    return render(request, "register/register.html", {"form": form})


def viewer(request):
    if request.user.is_authenticated:
        context = {}
        form = PostFweet(request.POST, instance=Fweet(user=request.user))
        fweet_list = Fweet.objects.all().order_by('-date')
        if form.is_valid():
            form.save()
        context['form'] = form
        return render(request, "myApp/viewer.html", {"form": form, 'fweet_list': fweet_list})
    else:
        return redirect("login")


def yourprofile(request):
    if request.user.is_authenticated:
        fweet_list = Fweet.objects.all().order_by('-date')
        return render(request, "myApp/profile.html", {'fweet_list': fweet_list})
    else:
        return redirect("login")


def profiles(request):
    if request.user.is_authenticated:
        fweet_list = Fweet.objects.all().order_by('-date')
        return render(request, "myApp/profiles.html", {'fweet_list': fweet_list})
    else:
        return redirect("login")
