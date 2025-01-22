# serializers.py

from rest_framework import serializers
from .models import Paciente, Atemed, Profesional, Entidad

class LoginSerializer(serializers.Serializer):
    Pcte_id = serializers.CharField(max_length=255)



class AtemedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atemed
        fields = '__all__'   

    def validate_Atemed_Prof_id(self, value):
        # Verificar si el Profesional existe
        if not Profesional.objects.filter(id_Pro=value).exists():
            raise serializers.ValidationError("El ID del Profesional no existe.")
        return value

    def validate_Atemed_Pcte_Id(self, value):
        # Verificar si el Paciente existe
        if not Paciente.objects.filter(Pcte_id=value).exists():
            raise serializers.ValidationError("El ID del Paciente no existe.")
        return value

    def validate_Atemed_Ent_id(self, value):
        # Verificar si la Entidad Medica existe
        if not Entidad.objects.filter(Ent_Id=value).exists():
            raise serializers.ValidationError("El ID de la Entidad Médica no existe.")
        return value

    def create(self, validated_data):
        # Crear el registro de Atemed
        atemed_instance = super().create(validated_data)
        
        # Retornar el 'Atemed_id' generado
        return atemed_instance
    
class AtemedSerializerConsulta(serializers.ModelSerializer):  
    class Meta:
        model = Atemed
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Convertir datetime a date para los campos Atemed_Fecha_Inicio y Atemed_Fecha_Fin
        if instance.Atemed_Fecha_Inicio:
            representation['Atemed_Fecha_Inicio'] = instance.Atemed_Fecha_Inicio.date()
        if instance.Atemed_Fecha_Fin:
            representation['Atemed_Fecha_Fin'] = instance.Atemed_Fecha_Fin.date()
        return representation
    
class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = [
            'Pcte_id', 
            'Pcte_nom', 
            'Pcte_sexo', 
            'Pcte_fecha_nac', 
            'Pcte_edad', 
            'Pcte_meses', 
            'Pcte_dias', 
            'Pcte_nacionalidad', 
            'Pcte_celular',
            'Pcte_edad_compuesta',
            'Pcte_nac_etnia',
            'Pcte_tipo_bono',
            'Pcte_seguro',
            'Pcte_provincia',
            'Pcte_canton',
            'Pcte_parroquia',
            'Pcte_peso',
            'Pcte_talla_cm',
            'Pcte_imc',
            'Permietro_cefalico',
            'Valor_hemoglobina',
            'Indice_anemia',
            'Imc_resultado',
            'Num_atencion_prenatal',
            'Pcte_disc',
            'Pcte_tipo_disc',
            'Pcte_porctj_disc'
        ]  

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__' 