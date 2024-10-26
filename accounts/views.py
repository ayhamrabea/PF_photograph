from django.shortcuts import render , redirect
from django.urls import reverse_lazy 
from .forms import UserSingForm , ProfileForm
from django.views.generic.edit import CreateView 
from django.contrib.auth import login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.


class RegisterView(CreateView):

    form_class = UserSingForm
    # success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def get_success_url(self) :
        login(self.request , self.object)
        return reverse_lazy('home')


def logout_app(request):
    logout(request)
    return redirect('login')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST , instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=request.user)
        return render(request,'profile.html',{'form':form})