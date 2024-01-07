from django.shortcuts import render,redirect
from . import forms
from car_model import models
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
def sing_up(request):
    if request.method == 'POST':
        sing_up_form = forms.SingForm(request.POST)
        if sing_up_form.is_valid():
            sing_up_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('Loginview')
    
    else:
        sing_up_form = forms.SingForm()
    return render(request, 'register.html', {'form' : sing_up_form, 'type' : 'sing_up'})

class Loginview(LoginView):
    template_name = 'register.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

class LogoutView(LogoutView):
    next_page = reverse_lazy('Loginview')

@login_required
def profile(request):
    data = models.Phurses.objects.all()
    return render(request,'profile.html',{'dataa':data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'update_profile.html', {'form' : profile_form})

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html', {'form' : form})

