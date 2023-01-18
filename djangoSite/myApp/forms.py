from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Fweet


class NewUser(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]



class PostFweet(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, label='')

    class Meta:
        model = Fweet
        fields = ["content", ]
