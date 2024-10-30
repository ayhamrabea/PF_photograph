from django.urls import path 
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('contact',login_required(views.contact.as_view()),name='contact'),
    path('add_comment',login_required(views.add_comment.as_view()),name='add_comment'),
    # path('add_comment',views.add_comment,name='add_comment'),
]