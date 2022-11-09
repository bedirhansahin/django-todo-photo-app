from django.urls import path
from django.contrib.auth.decorators import login_required

from core.views import (
    UserRegisterView,
    HomePageView,
    login_request,
    logout_request,
    UserDetailsView,
    TodoListView,
    PhotoListView,
    TodoDeleteView,
    TodoCreateView,
)


app_name = 'core'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('register', UserRegisterView.as_view(), name='register'),
    path('login/', login_request, name='login'),
    path('profile/<int:pk>/', login_required(UserDetailsView.as_view()), name='profile'),
    path('logout', logout_request, name='logout'),
    path('todo/create', TodoCreateView.as_view(), name='create-todo'),
    path('todos', TodoListView.as_view(), name='todos'),
    path('photos', PhotoListView.as_view(), name='photos'),
    path('delete/todo/<int:pk>/', TodoDeleteView.as_view(), name='delete-todo'),
]

