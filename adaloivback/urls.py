from django.contrib import admin
from django.urls import path, include

from api.views import AtemedDetailView, GetPacienteView, AddAtemedView, LoginProfesionalView, LoginPacienteView, RegistrarPacienteView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/login-profesional/', LoginProfesionalView.as_view(), name='loginProfesional'),
    path('api/login-paciente/', LoginPacienteView.as_view(), name='loginPaciente'),
    path('api/atemed/<int:atemed_id>/', AtemedDetailView.as_view(), name='atemed_detail'),
    path('api/add-atemed/', AddAtemedView.as_view(), name='add_atemed'),
    path('api/paciente/<str:pk>/', GetPacienteView.as_view(), name='get-paciente'),   
    path('api/registrar-paciente/', RegistrarPacienteView.as_view(), name='registrar-paciente'),

]
