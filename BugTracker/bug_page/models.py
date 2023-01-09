from django.contrib.auth.models import User
from django.db import models
import uuid

# Create your models here.


class TrackerUser(models.Model):
    ROLE_CHOICES = [
        ("customer", "Customer"),
        ("developer", "Developer"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    role = models.CharField(choices=ROLE_CHOICES, default="customer", max_length=20)

    def __str__(self):
        return self.user.username


class BugDetail(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("open", "Open"),
        ("closed", "Closed"),
    ]
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, default="new", max_length=20)
    priority = models.CharField(
        choices=PRIORITY_CHOICES, default="medium", max_length=20
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
