from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('contact',views.contact,name='contact'),
    path('add_comment',views.add_comment,name='add_comment'),
]