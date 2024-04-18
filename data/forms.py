from django import forms
from .models import Client

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ChangeStatusForm(forms.ModelForm):
    class Meta: 
        model = Client
        fields = ['status']
