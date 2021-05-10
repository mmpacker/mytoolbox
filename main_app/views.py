from django.shortcuts import render, redirect
from .models import Project, Tool, Material
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def home(request):
  return render(request, 'home.html')

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
      return redirect('landing')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class ProjectList(LoginRequiredMixin, ListView):
  model = Project
  def get_queryset(self):
    self.user = self.request.user
    return Project.objects.filter(user=self.user)
  

# class ProjectDetail(LoginRequiredMixin, DetailView):
#   model = Project

#   def tools_project_doesnt_have(self, Tool.objects.exclude(id__in = project.tools.all().values_list('id'))

@login_required
def projects_detail(request, project_id):
  project = Project.objects.get(id=project_id)
  tools_project_doesnt_use = Tool.objects.exclude(id__in = project.tools.all().values_list('id'))
  materials_project_doesnt_use = Material.objects.exclude(id__in = project.materials.all().values_list('id'))
  return render(request, 'projects/detail.html', { 'project': project, 'tools': tools_project_doesnt_use, 'materials': materials_project_doesnt_use  })

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

class ToolList(LoginRequiredMixin, ListView):
  model = Tool

class ToolDetail(LoginRequiredMixin, DetailView):
  model = Tool

class ToolCreate(LoginRequiredMixin, CreateView):
  model = Tool
  fields = '__all__'

class ToolUpdate(LoginRequiredMixin, UpdateView):
  model = Tool
  fields = '__all__'

class ToolDelete(LoginRequiredMixin, DeleteView):
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

class MaterialList(LoginRequiredMixin, ListView):
  model = Material

class MaterialDetail(LoginRequiredMixin, DetailView):
  model = Material

class MaterialCreate(LoginRequiredMixin, CreateView):
  model = Material
  fields = '__all__'

class MaterialUpdate(LoginRequiredMixin, UpdateView):
  model = Material
  fields = '__all__'

class MaterialDelete(LoginRequiredMixin, DeleteView):
  model = Material
  success_url = '/materials/'

@login_required
def assoc_material(request, project_id, material_id):
  Project.objects.get(id=project_id).materials.add(material_id)
  return redirect('projects_detail', project_id=project_id)

@login_required
def unassoc_material(request, project_id, material_id):
  Project.objects.get(id=project_id).materials.remove(material_id)
  return redirect('projects_detail', project_id=project_id)