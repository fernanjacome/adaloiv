# serializers.py

from rest_framework import serializers
from .models import Paciente, Atemed

class LoginSerializer(serializers.Serializer):
    Pcte_id = serializers.CharField(max_length=255)
    
class AtemedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atemed
        fields = '__all__'