from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=30, blank=True, null=True)

    ROLE_CHOICES = [
        ("patient", "Patient"),
        ("doctor", "Doctor"),
        ("employee", "Employee"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="patient")
    identification_number = models.CharField(
        max_length=20, unique=True, null=True, blank=True
    )
    # Personaliza los campos groups y user_permissions para evitar conflictos
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups",  # related_name único
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",  # related_name único
        blank=True,
    )
