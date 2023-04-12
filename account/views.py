from django.shortcuts import render, redirect
# from .forms import RegisterForm, PersonalDetailForm, ShippingAddresForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import User
# User = get_user_model()

def index(request):
    user = User.objects.filter().first()
    return render(request, 'index.html', {"user": user})

def register(request):
    return render(request, 'register.html', {})

def login_view(request):
    return render(request, 'login.html', {})

def logout_view(request):
    return redirect(reverse_lazy())
