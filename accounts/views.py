# views.py
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer
from .serializers import RegisterSerializer
from .serializers import IdentificationLoginSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # Validar los datos de entrada con el serializer
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")

            # Obtener el modelo de usuario configurado en settings.py (CustomUser)
            User = get_user_model()

            # Intentar autenticar al usuario
            user = authenticate(username=username, password=password)

            if user is not None:
                # Generar el refresh token y el access token
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                # Devolver los tokens en la respuesta junto con los detalles del usuario
                return Response(
                    {
                        "message": "Login exitoso",
                        "user": {
                            "last_login": user.last_login,
                            "is_superuser": user.is_superuser,
                            "username": user.username,
                            "first_name": user.first_name,
                            "last_name": user.last_name,
                            "email": user.email,
                            "is_staff": user.is_staff,
                            "is_active": user.is_active,
                            "date_joined": user.date_joined,
                            "middle_name": user.middle_name,  # Agregar middle_name
                            "role": user.role,  # Agregar role
                        },
                        "access_token": access_token,
                        "refresh_token": str(refresh),
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"error": "Credenciales incorrectas"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                {"error": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully!"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IdentificationLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = IdentificationLoginSerializer(data=request.data)
        if serializer.is_valid():
            identification_number = serializer.validated_data.get(
                "identification_number"
            )
            password = serializer.validated_data.get("password")
            User = get_user_model()
            user = User.objects.filter(
                identification_number=identification_number
            ).first()

            if user and user.check_password(password):
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                return Response(
                    {
                        "message": "Login exitoso",
                        "user": {
                            "username": user.username,
                            "first_name": user.first_name,
                            "last_name": user.last_name,
                            "email": user.email,
                            "is_staff": user.is_staff,
                            "is_active": user.is_active,
                            "date_joined": user.date_joined,
                            "middle_name": user.middle_name,
                            "role": user.role,
                        },
                        "access_token": access_token,
                        "refresh_token": str(refresh),
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"error": "Número de identificación o contraseña incorrectos"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                {"error": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
