from django.contrib.auth.models import AbstractUser
from django.db import models
import time


from django.db import models

class Atemed(models.Model):
    Atemed_id = models.FloatField(primary_key=True, editable=False)  # Cambiado a Float
    Atemed_Prof_id = models.FloatField(null=True, blank=True)
    Atemed_Pcte_Id = models.FloatField(null=True, blank=True)
    Atemed_Ent_id = models.FloatField(null=True, blank=True)
    Atemed_Fecha_Inicio = models.DateField(null=True, blank=True)
    Atemed_Hora_Inicio = models.TimeField(null=True, blank=True)
    Atemed_Fecha_Fin = models.DateField(null=True, blank=True)
    Atemed_Hora_Fin = models.TimeField(null=True, blank=True)
    Atemed_Diagnostico_CIE10 = models.CharField(max_length=255, null=True, blank=True)
    Atemed_Not_Oblig = models.FloatField(null=True, blank=True)
    Atemed_Tipo_Diag = models.CharField(max_length=255, null=True, blank=True)
    Atemed_Cron_Diag = models.CharField(max_length=255, null=True, blank=True)
    Atemed_Con_Diagnostico = models.CharField(max_length=255, null=True, blank=True)
    Atemed_Tipo_Ate = models.CharField(max_length=255, null=True, blank=True)
    Atemed_Receta = models.CharField(max_length=255, null=True, blank=True)
    F16 = models.CharField(max_length=255, null=True, blank=True)
    F17 = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'Atemed'

    def save(self, *args, **kwargs):
        if not self.Atemed_id: 
            # Obtener el tiempo en segundos desde la época y convertirlo en un entero
            current_time = int(time.time())  # Convertir a entero para evitar decimales
            self.Atemed_id = current_time  
        super(Atemed, self).save(*args, **kwargs)
        
class Profesional(models.Model):
    id_Pro = models.IntegerField(primary_key=True)
    Pro_FullNombre = models.CharField(max_length=255)
    Prof_Fecha_Nac = models.DateField(null=True, blank=True)
    Especialización = models.CharField(max_length=255, null=True, blank=True)
    Prof_Correo = models.EmailField(unique=True)
    F6 = models.CharField(max_length=255, null=True, blank=True)
    F7 = models.CharField(max_length=255, null=True, blank=True)
    F8 = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "Profesional"


class Paciente(models.Model):
    Pcte_id = models.CharField(max_length=255, unique=True, primary_key=True)
    Pcte_nom = models.CharField(max_length=255, null=True)
    Pcte_sexo = models.CharField(max_length=255, null=True)
    Pcte_fecha_nac = models.DateTimeField(null=True)
    Pcte_edad = models.FloatField(null=True)
    Pcte_meses = models.FloatField(null=True)
    Pcte_dias = models.FloatField(null=True)
    Pcte_edad_compuesta = models.CharField(max_length=255, null=True)
    Pcte_nacionalidad = models.CharField(max_length=255, null=True)
    Pcte_nac_etnia = models.CharField(max_length=255, null=True)
    Pcte_celular = models.CharField(max_length=255, null=True)
    Pcte_tipo_bono = models.CharField(max_length=255, null=True)
    Pcte_seguro = models.CharField(max_length=255, null=True)
    Pcte_provincia = models.CharField(max_length=255, null=True)
    Pcte_canton = models.CharField(max_length=255, null=True)
    Pcte_parroquia = models.CharField(max_length=255, null=True)
    Pcte_peso = models.CharField(max_length=255, null=True)
    Pcte_talla_cm = models.FloatField(null=True)
    Pcte_imc = models.CharField(max_length=255, null=True)
    Permietro_cefalico = models.FloatField(null=True)
    Valor_hemoglobina = models.CharField(max_length=255, null=True)
    Indice_anemia = models.CharField(max_length=255, null=True)
    Imc_resultado = models.CharField(max_length=255, null=True)
    Num_atencion_prenatal = models.CharField(max_length=255, null=True)
    Pcte_disc = models.CharField(max_length=255, null=True)
    Pcte_tipo_disc = models.CharField(max_length=255, null=True)
    Pcte_porctj_disc = models.CharField(max_length=255, null=True)
    F28 = models.CharField(max_length=255, null=True)
    F29 = models.CharField(max_length=255, null=True)
    F30 = models.CharField(max_length=255, null=True)
    F31 = models.CharField(max_length=255, null=True)
    F32 = models.CharField(max_length=255, null=True)
    F33 = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'Paciente'

    def __str__(self):
        return self.Pcte_nom
    
    from django.db import models

class Entidad(models.Model):
    Ent_Id = models.FloatField(null=False)
    Ent_Nom = models.CharField(max_length=255, null=True)
    Ent_Tipo = models.CharField(max_length=255, null=True)
    Ent_Prov = models.CharField(max_length=255, null=True)
    Ent_Cant = models.CharField(max_length=255, null=True)
    Ent_Parr = models.CharField(max_length=255, null=True)
    Ent_Tipo_Parr = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'EntidadMedica'

    def __str__(self):
        return self.Ent_Nom

