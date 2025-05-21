from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Resource, Category
import csv

# Home page view
def home(request):
    return render(request, 'inventory/home.html')

# Resource list view
def resource_list(request):
    resources = Resource.objects.select_related('category').all()
    return render(request, 'inventory/resource_list.html', {'resources': resources})

# Export resources to CSV
def export_resources_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="resources.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Category', 'Quantity'])

    for resource in Resource.objects.select_related('category').all():
        writer.writerow([resource.name, resource.category.name, resource.quantity])

    return response

# Optional: Import resources from CSV (only works with POST and uploaded CSV)
def import_resources_csv(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.reader(decoded_file)
        next(reader)  # Skip header row

        for row in reader:
            name, category_name, quantity = row
            category, _ = Category.objects.get_or_create(name=category_name)
            Resource.objects.create(name=name, category=category, quantity=int(quantity))

        return redirect('resource_list')

    return HttpResponse("Upload failed or invalid request method.", status=400)
