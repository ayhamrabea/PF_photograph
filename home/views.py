from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')



def about(request):
    return render(request,'about.html')

def portfolio(request):
    return render(request,'portfolio.html')


def contact(request):
    return render(request,'contact.html')

def add_comment(request):
    return render(request,'add_comment.html')