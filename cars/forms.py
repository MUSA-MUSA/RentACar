__author__ = 'mu'
from cars.models import UserProfile, Car, Question
from django.contrib.auth.models import User
from django import forms
from .models import *


class QuestinForm(forms.ModelForm):
    Username = forms.CharField(max_length=100)
    Email = forms.EmailField(max_length=255)
    Question =forms.CharField(max_length=255)

    class Meta:
        model=Question