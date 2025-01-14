# serializers.py

from rest_framework import serializers
from .models import CustomUser


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        user = CustomUser.objects.filter(username=username).first()
        if user and user.check_password(password):
            return {"username": username, "password": password}
        raise serializers.ValidationError("Credenciales incorrectas")

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser  # Usa la clase del modelo, no una instancia
        fields = (
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "middle_name",
            "role",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            email=validated_data.get("email", ""),
            middle_name=validated_data.get("middle_name", ""),
            role=validated_data.get("role", "patient"),
        )
        return user

class IdentificationLoginSerializer(serializers.Serializer):
    identification_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        identification_number = data.get("identification_number")
        password = data.get("password")

        user = CustomUser.objects.filter(
            identification_number=identification_number
        ).first()
        if user and user.check_password(password):
            return {
                "identification_number": identification_number,
                "password": password,
            }
        raise serializers.ValidationError(
            "Número de identificación o contraseña incorrectos"
        )
