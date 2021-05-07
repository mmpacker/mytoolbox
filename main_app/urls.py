from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('landing/', views.landing, name='landing'),
  path('accounts/signup/', views.signup, name='signup'),
  path('projects/', views.ProjectList.as_view(), name='projects_index'),
  path('project/<int:pk>/', views.ProjectDetail.as_view(), name='projects_detail'),
  path('projects/create/', views.ProjectCreate.as_view(), name='projects_create'),
  path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name='projects_update'),
  path('projects/<int:pk>/delete/', views.ProjectDelete.as_view(), name='projects_delete'),
]