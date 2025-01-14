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

class Atemed(models.Model):
    Atemed_id = models.AutoField(primary_key=True)
    Atemed_Prof_id = models.IntegerField()
    Atemed_Pcte_Id = models.IntegerField()
    Atemed_Ent_id = models.IntegerField()
    Atemed_Fecha_Inicio = models.DateField()
    Atemed_Hora_Inicio = models.TimeField()
    Atemed_Fecha_Fin = models.DateField()
    Atemed_Hora_Fin = models.TimeField()
    Atemed_Diagnostico_CIE10 = models.CharField(max_length=255)
    Atemed_Not_Oblig = models.TextField()
    Atemed_Tipo_Diag = models.CharField(max_length=50)
    Atemed_Cron_Diag = models.CharField(max_length=50)
    Atemed_Con_Diagnostico = models.CharField(max_length=50)
    Atemed_Tipo_Ate = models.CharField(max_length=50)
    Atemed_Receta = models.TextField()
    F16 = models.CharField(max_length=255, blank=True, null=True)
    F17 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'Atemed$'