from django.shortcuts import render, redirect
from .models import Project
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
  return redirect('login')

@login_required
def landing(request):
  return render(request, 'landing.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class ProjectList(ListView):
  model = Project

class ProjectDetail(DetailView):
  model = Project

class ProjectCreate(CreateView):
  model = Project
  fields = ['title', 'location', 'budget']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ProjectUpdate(UpdateView):
  model = Project
  fields = ['title', 'location', 'budget']