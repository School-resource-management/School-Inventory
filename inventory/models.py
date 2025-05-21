# models.py

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class ResourceItem(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    serial = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.resource.name} - {self.serial}"

class AssignedResource(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource_item = models.ForeignKey(ResourceItem, on_delete=models.CASCADE)
    assigned_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.resource_item} to {self.user.username}"
