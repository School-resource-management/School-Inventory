# admin.py

from django.contrib import admin
from .models import Category, Resource, ResourceItem, AssignedResource

class ResourceItemAdmin(admin.ModelAdmin):
    list_display = ('resource', 'serial', 'description')

class AssignedResourceAdmin(admin.ModelAdmin):
    list_display = ('user', 'resource_item', 'assigned_at')
admin.site.site_header = "Tigray School-Resource-Management System"
admin.site.site_title = "Tigray School-Resource-Management"
admin.site.index_title = "Welcome to the Admin Panel"
admin.site.register(Category)
admin.site.register(Resource)
admin.site.register(ResourceItem, ResourceItemAdmin)
admin.site.register(AssignedResource, AssignedResourceAdmin)
