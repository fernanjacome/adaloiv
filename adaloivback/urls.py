from django.contrib import admin
from django.urls import (
    path,
    include,
)  # Importa 'include' para incluir URLs de otras aplicaciones
from users.views import (
    LoginView,
)  # Asegúrate de que la vista LoginView está importada correctamente

from users.views import RegisterView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/register/", RegisterView.as_view(), name="register"),
]
