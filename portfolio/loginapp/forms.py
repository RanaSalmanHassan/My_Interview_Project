from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = ('username','password1','password2','email',)
        # fields = "__all__"
