from django import forms
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm , UserChangeForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs) :
        super(UserLoginForm , self).__init__( *args, **kwargs)


    username = forms.CharField(label='Username' , widget=forms.TextInput())
    password = forms.CharField(label='Password' , widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username' , 'password']


class UserSingForm(UserCreationForm):

    first_name = forms.CharField(label='First name' , widget=forms.TextInput())
    last_name = forms.CharField(label='Last name' , widget=forms.TextInput())
    email = forms.EmailField(label='email' , widget=forms.TextInput())
    username = forms.CharField(label='Username' , widget=forms.TextInput())
    password1 = forms.CharField(label='Password' , widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password confirmation' , widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ['first_name' , 'last_name','email' , 'username','password1' , 'password2']



class ProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name' , 'last_name','email']