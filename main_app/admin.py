from django.contrib import admin
from .models import Project, Tool, Material, ToolPhoto, MaterialPhoto

# Register your models here.
admin.site.register(Project)
admin.site.register(Tool)
admin.site.register(Material)
admin.site.register(ToolPhoto)
admin.site.register(MaterialPhoto)