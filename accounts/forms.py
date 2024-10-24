from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs) :
        super(UserLoginForm , self).__init__( *args, **kwargs)


    username = forms.CharField(label='Username' , widget=forms.TextInput())
    password = forms.CharField(label='Password' , widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username' , 'password']