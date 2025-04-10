# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import CustomUser  # 커스텀 유저 모델이라 가정

class RegisterForm(UserCreationForm):
    nickname = forms.CharField(max_length=50, required=True, label="닉네임")

    class Meta:
        model = CustomUser
        fields = ["username", "nickname", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        # nickname 필드를 실제 DB에도 저장
        user.nickname = self.cleaned_data["nickname"]
        if commit:
            user.save()
        return user
