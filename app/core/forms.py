from django.forms import ModelForm, TextInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . models import Todo, Photo


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Username'}),
            'email': TextInput(attrs={'placeholder': 'Email'}),
        }


class TodoForm(ModelForm):

    class Meta:
        model = Todo
        exclude = ('is_active', 'user')
        widgets = {
            'due_date': DateInput(),
            'due_time': TimeInput(),
        }
        labels = {
            'due_time': "Due time (it's not compulsory)",
        }


class PhotoForm(ModelForm):

    class Meta:
        model = Photo
        exclude = ('user', 'publish_date')

