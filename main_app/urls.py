from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('landing/', views.landing, name='landing'),
  path('accounts/signup/', views.signup, name='signup'),
  path('projects/', views.ProjectList.as_view(), name='projects_index'),
  path('projects/<int:project_id>/', views.projects_detail, name='projects_detail'),
  path('projects/create/', views.ProjectCreate.as_view(), name='projects_create'),
  path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name='projects_update'),
  path('projects/<int:pk>/delete/', views.ProjectDelete.as_view(), name='projects_delete'),
  path('tools/<int:pk>/', views.ToolDetail.as_view(), name='tools_detail'),
  path('tools/create/', views.ToolCreate.as_view(), name='tools_create'),
  path('tools/<int:pk>/update/', views.ToolUpdate.as_view(), name='tools_update'),
  path('tools/<int:pk>/delete/', views.ToolDelete.as_view(), name='tools_delete'),
  path('tools/', views.ToolList.as_view(), name='tools_index'),
  path('projects/<int:project_id>/assoc_tool/<int:tool_id>/', views.assoc_tool, name='assoc_tool'),
  path('projects/<int:project_id>/unassoc_tool/<int:tool_id>/', views.unassoc_tool, name='unassoc_tool'),
  path('materials/<int:pk>/', views.MaterialDetail.as_view(), name='materials_detail'),
  path('materials/create/', views.MaterialCreate.as_view(), name='materials_create'),
  path('materials/<int:pk>/update/', views.MaterialUpdate.as_view(), name='materials_update'),
  path('materials/<int:pk>/delete/', views.MaterialDelete.as_view(), name='materials_delete'),
  path('materials/', views.MaterialList.as_view(), name='materials_index'),
  path('projects/<int:project_id>/assoc_material/<int:material_id>/', views.assoc_material, name='assoc_material'),
  path('projects/<int:project_id>/unassoc_material/<int:material_id>/', views.unassoc_material, name='unassoc_material'),
]