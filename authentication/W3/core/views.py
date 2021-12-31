from django.shortcuts import render
from django.contrib.auth.views import  LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView
from django.views.generic import TemplateView
from core.forms import loginform
# Create your views here.
def dashbord(request):
    return render(request,'core/dashbord.html')

class mylogin(LoginView):
    authentication_form=loginform
    template_name='core/login.html'

class mylogout(LogoutView):
    template_name='core/logout.html'

class passchange(PasswordChangeView):
    template_name='core/PasswordChangeView.html'
    success_url='/passcdoen/'

class passcdoen(PasswordChangeView):
    template_name='core/PasswordChangeDoneView.html'

