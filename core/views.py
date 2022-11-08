from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin


class RegisterView(CreateView, SuccessMessageMixin):
    model = User
    template_name = 'register.html'
