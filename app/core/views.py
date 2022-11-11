from audioop import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView, DetailView, ListView, DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth import login, logout, authenticate
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.urls import reverse_lazy

from . forms import UserRegisterForm, TodoForm, PhotoForm

from . models import Todo, Photo


class HomePageView(TemplateView):
    template_name = 'home.html'


class UserRegisterView(CreateView, SuccessMessageMixin):
    model = User
    template_name = 'registration/register.html'
    form_class = UserRegisterForm
    success_message = 'Your user was created successfully'
    success_url = reverse_lazy('core:login')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(
        request=request,
        template_name="registration/login.html",
        context={"form": form})


class UserDetailsView(DetailView, LoginRequiredMixin):
    model = User
    template_name = 'registration/profile.html'
    form_class = UserRegisterForm

    def get_success_url(self):
        return reverse_lazy('core:profile', kwargs={'pk': self.object.pk})

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserDetailsView, self).dispatch(*args, **kwargs)


def logout_request(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, "You have been logged out.")
        return redirect(reverse_lazy('core:home'))
    return render(request, "registration/logout.html", {})


class TodoCreateView(CreateView, LoginRequiredMixin):
    model = Todo
    template_name = 'todo-create.html'
    form_class = TodoForm
    success_url = reverse_lazy('core:todos')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TodoCreateView, self).dispatch(*args, **kwargs)


class TodoListView(ListView, LoginRequiredMixin):
    model = Todo
    template_name = 'todo.html'
    context_object_name = 'todos'
    paginate_by = 5

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        todos = Todo.objects.filter(todo__icontains=search, user=self.request.user).order_by(
            '-due_date'
        )
        return todos

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TodoListView, self).dispatch(*args, **kwargs)


class TodoPutItOffView(UpdateView, LoginRequiredMixin):
    model = Todo
    form_class = TodoForm
    template_name = 'todo-update.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('core:todos')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TodoPutItOffView, self).dispatch(*args, **kwargs)


class TodoDeleteView(DeleteView):
    model = Todo
    pk_url_kwarg = 'pk'
    template_name = 'delete-confirm.html'
    success_url = reverse_lazy('core:todos')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TodoDeleteView, self).dispatch(*args, **kwargs)


class PhotoListView(ListView):
    model = Photo
    template_name = 'photo.html'
    context_object_name = 'photos'
    paginate_by = 3

    def get_queryset(self):
        return Photo.objects.filter(
            user=self.request.user
        ).order_by('-publish_date')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PhotoListView, self).dispatch(*args, **kwargs)


class PhotoCreateView(CreateView, LoginRequiredMixin):
    model = Photo
    template_name = 'photo-create.html'
    form_class = PhotoForm
    success_url = reverse_lazy('core:photos')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PhotoCreateView, self).dispatch(*args, **kwargs)


class PhotoUpdateView(UpdateView, LoginRequiredMixin):
    model = Photo
    template_name = 'photo-update.html'
    fields = ['photo', 'name', 'description']
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('core:photos')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PhotoUpdateView, self).dispatch(*args, **kwargs)


class PhotoDeleteView(DeleteView):
    model = Photo
    pk_url_kwarg = 'pk'
    template_name = 'delete-confirm-photo.html'
    success_url = reverse_lazy('core:photos')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PhotoDeleteView, self).dispatch(*args, **kwargs)


class SinglePhotoView(DetailView, LoginRequiredMixin):
    model = Photo
    template_name = 'single-photo.html'
    context_object_name = 'single_photo'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SinglePhotoView, self).dispatch(*args, **kwargs)

