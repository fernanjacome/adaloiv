from django.contrib import admin
from django.urls import path, include

from api.views import  GetPacienteView, AddAtemedView, LoginProfesionalView, LoginPacienteView, RegistrarPacienteView, EditarPacienteView, ConsultarAtemedPorPcteIdView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/login-profesional/', LoginProfesionalView.as_view(), name='loginProfesional'),
    path('api/login-paciente/', LoginPacienteView.as_view(), name='loginPaciente'),
    path('api/add-atemed/', AddAtemedView.as_view(), name='add_atemed'),
    path('api/atemed/<int:pcte_id>/', ConsultarAtemedPorPcteIdView.as_view(), name='consultar_atemed_por_pcte_id'),

    path('api/paciente/<str:pk>/', GetPacienteView.as_view(), name='get-paciente'),   
    path('api/registrar-paciente/', RegistrarPacienteView.as_view(), name='registrar-paciente'),
    path('api/paciente/editar/<str:pcte_id>/', EditarPacienteView.as_view(), name='editar_paciente'),

]
