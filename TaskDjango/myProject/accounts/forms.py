from django.contrib.auth.forms import  UserCreationForm, UsernameField
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

from .models import Item

class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='password',widget=forms.
    PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='confirm password',widget=forms.
    PasswordInput(attrs={'class':'form-control'}))
    username = forms.CharField(required=True,widget=forms.
    TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','password1', 'password2']

class LoginForm(forms.ModelForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,
      'class': 'form-control'}))
    password = forms.CharField(label=_("password"),strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
     'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username','password']

