from django.contrib import admin
from django.urls import path, include

from api.views import AtemedDetailView
from api.views import LoginProfesionalView
from api.views import LoginPacienteView
from api.views import AtemedDetail

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/login-profesional/', LoginProfesionalView.as_view(), name='loginProfesional'),
    path('api/login-paciente/', LoginPacienteView.as_view(), name='loginPaciente'),
    path('atemed/<int:Atemed_id>/', AtemedDetail.as_view(), name='atemed-detail'),
    path('api/atemed/<int:atemed_id>/', AtemedDetailView.as_view(), name='atemed_detail'),
]
