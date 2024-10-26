from django.urls import path , include
from django.contrib.auth.views import LoginView, LogoutView
from accounts.forms import UserLoginForm
from . import views



urlpatterns = [
    path('login',LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('logout1',views.logout_app, name='logout1'),
    path('profile',views.edit_profile, name='profile'),
    path('register',views.RegisterView.as_view(), name='register'),
    path('',include('django.contrib.auth.urls')),
]