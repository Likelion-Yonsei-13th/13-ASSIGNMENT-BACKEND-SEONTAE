# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import CustomUser

class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ["username", "nickname", "email", "password1", "password2"]

