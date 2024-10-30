from django.shortcuts import render , redirect
from .models import Comments , Messsages 
from .forms import Add_Comment_Form , Contact_Us_form
from django.views.generic.edit import CreateView 
from django.urls import reverse_lazy 
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):

    context = {
        'comments' : Comments.objects.all(),
    }
    return render(request,'index.html', context)



def about(request):
    return render(request,'about.html')



def portfolio(request):

    return render(request,'portfolio.html')



class contact(CreateView):

    model = Messsages
    form_class = Contact_Us_form
    success_url = reverse_lazy('home')
    template_name = 'contact.html'
    extra_context={'comments': Messsages.objects.all()}

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class add_comment(CreateView):

    model = Comments
    form_class = Add_Comment_Form
    success_url = reverse_lazy('home')
    template_name = 'add_comment.html'
    extra_context={'comments': Comments.objects.all()}

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

    # def get_success_url(self) :
    #     login(self.request , self.object)
    #     return reverse_lazy('home')
