from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("register/", views.register, name='register'),
    path("login/", views.login_view, name='login'),
    path("logout/", views.logout_view, name='logout'),
]