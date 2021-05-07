from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Create your views here.
def home(request):
  return HttpResponse('<h1>MyToolbox Home<h1>')

def landing(request):
  return render(request, 'landing.html')