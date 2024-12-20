from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer

from rest_framework_simplejwt.tokens import (
    RefreshToken,
)  # Importar para generar los tokens JWT
from .serializers import LoginSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # Validar los datos de entrada con el serializer
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")

            # Intentar autenticar al usuario
            user = authenticate(username=username, password=password)

            if user is not None:
                # Generar el refresh token y el access token
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                # Devolver los tokens en la respuesta
                return Response(
                    {
                        "message": "Login exitoso",
                        "user": user.username,
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
