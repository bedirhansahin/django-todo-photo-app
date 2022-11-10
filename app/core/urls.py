from django.urls import path
from django.contrib.auth.decorators import login_required

from . views import (
    UserRegisterView,
    HomePageView,
    login_request,
    logout_request,
    UserDetailsView,
    TodoListView,
    PhotoListView,
    TodoDeleteView,
    TodoCreateView,
    PhotoCreateView,
    PhotoUpdateView, SinglePhotoView,
)


app_name = 'core'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('register', UserRegisterView.as_view(), name='register'),
    path('login/', login_request, name='login'),
    path('profile/<int:pk>/', login_required(UserDetailsView.as_view()), name='profile'),
    path('logout', logout_request, name='logout'),
    path('create/todo', TodoCreateView.as_view(), name='create-todo'),
    path('todos', TodoListView.as_view(), name='todos'),
    path('upload/photo', PhotoCreateView.as_view(), name='upload-photo'),
    path('photos', PhotoListView.as_view(), name='photos'),
    path('photo/<int:pk>/', SinglePhotoView.as_view(), name='single-photo'),
    path('update/photo/<int:pk>/', PhotoUpdateView.as_view(), name='update-photo'),
    path('delete/todo/<int:pk>/', TodoDeleteView.as_view(), name='delete-todo'),
]

