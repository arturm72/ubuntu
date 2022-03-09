from django import forms
from django.forms import ModelForm
from task.models import Task


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
