from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # homepage
    path('resources/', views.resource_list, name='resource_list'),
    path('export/', views.export_resources_csv, name='export_resources_csv'),  # ✅ Add this line
    path('import/', views.import_resources_csv, name='import_resources_csv'),
]
