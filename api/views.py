from django.contrib.auth import authenticate
from rest_framework import status
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.http import JsonResponse
from .models import Atemed, Profesional, Paciente
from .serializers import LoginSerializer, AtemedSerializer, PacienteSerializer, AtemedSerializerConsulta
import json
from django.views.decorators.csrf import csrf_exempt



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
        
        
class ConsultarAtemedPorPcteIdView(APIView):
   def get(self, request, pcte_id):
        # Filtrar los registros por el campo Atemed_Pcte_Id
        registros = Atemed.objects.filter(Atemed_Pcte_Id=pcte_id)
        if registros.exists():
            serializer = AtemedSerializer(registros, many=True)
            return Response(
                {"message": "Registros encontrados", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": "No se encontraron registros para el Pcte_Id proporcionado"},
                status=status.HTTP_404_NOT_FOUND
            )

class ConsultarAtemedPorIdView(APIView):
    def get(self, request, atemed_id):
        # Filtrar el registro por el campo Atemed_id
        try:
            registro = Atemed.objects.get(Atemed_id=atemed_id)
            serializer = AtemedSerializerConsulta(registro)
            return Response(
                {"message": "Registro encontrado", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        except Atemed.DoesNotExist:
            return Response(
                {"message": "No se encontró un registro con el Atemed_id proporcionado"},
                status=status.HTTP_404_NOT_FOUND
            )


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
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
        
class EditarPacienteView(APIView):
    def put(self, request, pcte_id):
        try:
            paciente = Paciente.objects.get(Pcte_id=pcte_id)  # Obtener paciente por ID
        except Paciente.DoesNotExist:
            return Response(
                {"message": "Paciente no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # No permitir que el ID sea modificado
        data = request.data # Eliminar el campo 'Pcte_id' de los datos entrantes
        
        # Crear el serializer con los datos actualizados, sin modificar el ID
        serializer = PacienteSerializer(paciente, data=data)
        
        if serializer.is_valid():
            serializer.save()  # Guardar los datos actualizados del paciente
            return Response(
                {"message": "Paciente actualizado exitosamente", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )