from django.contrib import admin
from .models import Project, Tool, Material

# Register your models here.
admin.site.register(Project)
admin.site.register(Tool)
admin.site.register(Material)