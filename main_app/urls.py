from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('landing/', views.landing, name='landing'),
  path('accounts/signup/', views.signup, name='signup'),
  path('projects/', views.ProjectList.as_view(), name='projects_index'),
  path('project/<int:pk>/', views.ProjectDetail.as_view(), name='projects_detail'),
]