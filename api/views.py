from django.contrib.auth import authenticate
from rest_framework import status
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.http import JsonResponse
from .models import Atemed, Profesional, Paciente
from .serializers import LoginSerializer, AtemedSerializer, PacienteSerializer
import json
from django.views.decorators.csrf import csrf_exempt


class AtemedDetailView(APIView):
    def get(self, request, atemed_id):
        try:
            # Filtrar por Atemed_id y limitar los resultados a los primeros 1000
            atemed_records = Atemed.objects.filter(Atemed_id=atemed_id)[:1000]
            
            # Generar la respuesta con todos los campos solicitados
            data = [
                {
                    "Atemed_id": record.Atemed_id,
                    "Atemed_Prof_id": record.Atemed_Prof_id,
                    "Atemed_Pcte_Id": record.Atemed_Pcte_Id,
                    "Atemed_Ent_id": record.Atemed_Ent_id,
                    "Atemed_Fecha_Inicio": record.Atemed_Fecha_Inicio,
                    "Atemed_Hora_Inicio": record.Atemed_Hora_Inicio,
                    "Atemed_Fecha_Fin": record.Atemed_Fecha_Fin,
                    "Atemed_Hora_Fin": record.Atemed_Hora_Fin,
                    "Atemed_Diagnostico_CIE10": record.Atemed_Diagnostico_CIE10,
                    "Atemed_Not_Oblig": record.Atemed_Not_Oblig,
                    "Atemed_Tipo_Diag": record.Atemed_Tipo_Diag,
                    "Atemed_Cron_Diag": record.Atemed_Cron_Diag,
                    "Atemed_Con_Diagnostico": record.Atemed_Con_Diagnostico,
                    "Atemed_Tipo_Ate": record.Atemed_Tipo_Ate,
                    "Atemed_Receta": record.Atemed_Receta,
                    "F16": record.F16,
                    "F17": record.F17,
                }
                for record in atemed_records
            ]
            
            return Response(data, status=status.HTTP_200_OK)
        except Atemed.DoesNotExist:
            return Response({"error": "Atemed with the given ID does not exist."}, status=status.HTTP_404_NOT_FOUND)
class LoginProfesionalView(APIView):
    def post(self, request):
        try:
            data = request.data
            correo = data.get('email')
            id_Pro = data.get('id')

            if not correo or not id_Pro:
                return Response({"status": "error", "message": "Email and ID are required"}, status=status.HTTP_400_BAD_REQUEST)

            profesional = Profesional.objects.filter(Prof_Correo=correo, id_Pro=id_Pro).first()

            if profesional:
                # Devuelve información básica del profesional
                response_data = {
                    "status": "success",
                    "message": "Login successful",
                    "Prof_Id": profesional.id_Pro,
                    "Prof_FullNombre": profesional.Pro_FullNombre,
                    "Prof_Correo": profesional.Prof_Correo,
                    "Especialización": profesional.Especialización,                   
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error", "message": "Su correo o su contraseña son incorrectas."}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)



class LoginPacienteView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            pcte_id = serializer.validated_data['Pcte_id']  # Usa Pcte_id consistente
            
            try:
                # Intentamos encontrar al paciente en la base de datos usando Pcte_id
                paciente = Paciente.objects.get(Pcte_id=pcte_id)
                
                # Convierte el modelo Paciente completo a un diccionario
                paciente_data = model_to_dict(paciente)
                
                # Devuelve información completa del paciente
                response_data = {
                    "message": "Login exitoso",
                    "Data": paciente_data
                }
                return Response(response_data, status=status.HTTP_200_OK)
            except Paciente.DoesNotExist:
                # Si no existe el paciente con ese Pcte_id, retornamos error 404
                return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Si los datos no son válidos, retornamos un error 400 con los detalles
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
class AddAtemedView(generics.CreateAPIView):
    queryset = Atemed.objects.all()
    serializer_class = AtemedSerializer

    def create(self, request, *args, **kwargs):
        # Crear el objeto usando el serializador
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Guardar el objeto y obtener la instancia creada
        atemed_instance = serializer.save()

        # Retornar la respuesta con el 'Atemed_id' generado
        return Response({
            'Atemed_id': atemed_instance.Atemed_id,
            'message': 'Registro de Atemed creado correctamente'
        }, status=status.HTTP_201_CREATED)
        
class GetPacienteView(generics.RetrieveAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    def get(self, request, *args, **kwargs):
        try:
            paciente_id = kwargs.get('pk')

            paciente_instance = self.get_queryset().filter(Pcte_id=paciente_id).first()

            if not paciente_instance:
                return Response({
                    'message': f'No se encontró el paciente con ID: {paciente_id}'
                }, status=status.HTTP_404_NOT_FOUND)

            serializer = self.get_serializer(paciente_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'message': 'Ocurrió un error al obtener la información del paciente',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
class RegistrarPacienteView(APIView):
    def post(self, request):
        serializer = PacienteSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Paciente registrado exitosamente", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)