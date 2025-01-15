from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import Atemed, Profesional, Paciente
from .serializers import LoginSerializer, AtemedSerializer
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
                    "Prof_FullNombre": profesional.Pro_FullNombre,
                    "Prof_Correo": profesional.Prof_Correo,
                    "Especialización": profesional.Especialización,                   
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error", "message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
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
                # Devuelve información básica del paciente
                response_data = {
                    "message": "Login exitoso",
                    "Pcte_id": paciente.Pcte_id,
                    "Pcte_nom": paciente.Pcte_nom,
                    "Pcte_sexo": paciente.Pcte_sexo,
                    "Pcte_fecha_nac": paciente.Pcte_fecha_nac,
                    "Pcte_edad": paciente.Pcte_edad,
                    "Pcte_celular": paciente.Pcte_celular,
                    "Pcte_provincia": paciente.Pcte_provincia,
                    "Pcte_canton": paciente.Pcte_canton,
                    "Pcte_parroquia": paciente.Pcte_parroquia
                }
                return Response(response_data, status=status.HTTP_200_OK)
            except Paciente.DoesNotExist:
                # Si no existe el paciente con ese Pcte_id, retornamos error 404
                return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Si los datos no son válidos, retornamos un error 400 con los detalles
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AtemedDetail(APIView):
    def get(self, request, Atemed_id):
        try:
            atemed = Atemed.objects.get(Atemed_id=Atemed_id)
            serializer = AtemedSerializer(atemed)
            return Response(serializer.data)
        except Atemed.DoesNotExist:
            return Response({"error": "Atemed not found"}, status=status.HTTP_404_NOT_FOUND)