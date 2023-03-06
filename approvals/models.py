from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Program(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("approvals:program_detail", args=[str(self.id)])



class Request(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="requests_created"
    )
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(
        User, related_name="requests_assigned_to", blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return self.title


