from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.contrib.auth.models import User
from django.views import generic


from django.contrib.auth import authenticate, login

class SignUpView(generic.edit.CreateView):
    form_class = UserCreationForm
    model = User
    template_name = 'auth/signup.html'
    success_url = '/'
    
    
class LoginView(generic.edit.FormView):
    
    form_class = AuthenticationForm
    template_name = 'auth/login.html'
    success_url = '/'
    
    def form_valid(self, form):
        
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)   
        
