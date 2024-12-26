from django.contrib import admin
from django.urls import path, include
from accounts.views import LoginView, RegisterView, IdentificationLoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/register/", RegisterView.as_view(), name="register"),
    path(
        "api/login/identification/",
        IdentificationLoginView.as_view(),
        name="identification_login",
    ),
]
