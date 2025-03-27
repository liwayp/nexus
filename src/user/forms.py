from django import  forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Username"}))
    password = forms.CharField(max_length=20,
                               widget=forms.PasswordInput(attrs={'class': "form-control", "placeholder": "Password"}))

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()

    def save(self, commit=True):
        user = super().save(commit=False)
        if user:
            Profile.objects.create(
                user=user
            )