from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Program(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    members = models.ManyToManyField(User, related_name='programs')
    default_approvers = models.ManyToManyField(User, related_name='default_approvers')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("approvals:program_detail", args=[str(self.id)])

class ApproverType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Approver(models.Model):
    TYPE_CHOICES = [
        ("client", "Client"),
        ("integrator", "Systems Integrator"),
        ("authority", "Authority"),
        ("vendor", "Vendor"),
    ]

    SUB_TYPE_CHOICES = [
        ("none", "N/A"),
        ("procure", "Procurement"),
        ("project", "Project Manager"),
        ("assurance", "Information Assurance"),
        ("developer", "Developer"),
        ("sustain", "Sustainment"),
        ("operator", "Operator"),
        ("lead", "Lead"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    sub_type = models.CharField(max_length=20, choices=SUB_TYPE_CHOICES, default="none")
    approver_type = models.ForeignKey(ApproverType, on_delete=models.CASCADE, null=True)


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
