from django.shortcuts import render, redirect
from .models import Project, Tool
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def home(request):
  return redirect('landing')

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

class ProjectList(LoginRequiredMixin, ListView):
  model = Project

# class ProjectDetail(LoginRequiredMixin, DetailView):
#   model = Project

#   def tools_project_doesnt_have(self, Tool.objects.exclude(id__in = project.tools.all().values_list('id'))

@login_required
def projects_detail(request, project_id):
  project = Project.objects.get(id=project_id)
  tools_project_doesnt_use = Tool.objects.exclude(id__in = project.tools.all().values_list('id'))
  return render(request, 'projects/detail.html', { 'project': project, 'tools': tools_project_doesnt_use })

class ProjectCreate(LoginRequiredMixin, CreateView):
  model = Project
  fields = ['title', 'location', 'budget']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ProjectUpdate(LoginRequiredMixin, UpdateView):
  model = Project
  fields = ['title', 'location', 'budget']

class ProjectDelete(LoginRequiredMixin, DeleteView):
  model = Project
  success_url = '/projects/'

class ToolList(ListView):
  model = Tool

class ToolDetail(DetailView):
  model = Tool

class ToolCreate(CreateView):
  model = Tool
  fields = '__all__'

class ToolUpdate(UpdateView):
  model = Tool
  fields = '__all__'

class ToolDelete(DeleteView):
  model = Tool
  success_url = '/tools/'

@login_required
def assoc_tool(request, project_id, tool_id):
  Project.objects.get(id=project_id).tools.add(tool_id)
  return redirect('projects_detail', project_id=project_id)

@login_required
def unassoc_tool(request, project_id, tool_id):
  Project.objects.get(id=project_id).tools.remove(tool_id)
  return redirect('projects_detail', project_id=project_id)