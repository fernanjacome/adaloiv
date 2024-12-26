# serializers.py
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import CustomUser

User = get_user_model()  # Obtiene el modelo de usuario configurado en settings.py


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            return {"username": username, "password": password}
        raise serializers.ValidationError("Credenciales incorrectas")


User = get_user_model()  # Obtiene el modelo de usuario configurado en settings.py


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
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
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
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
