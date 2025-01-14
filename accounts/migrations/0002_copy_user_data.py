from django.db import migrations


def copy_user_data(apps, schema_editor):
   
    CustomUser = apps.get_model("accounts", "CustomUser")

    # Copia los datos de los usuarios existentes en el modelo CustomUser
    for user in CustomUser.objects.all():
        CustomUser.objects.create(
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=user.password,  # Si no deseas copiar la contraseña, no la incluyas
            is_active=user.is_active,
            is_staff=user.is_staff,
            is_superuser=user.is_superuser,
            date_joined=user.date_joined,
            last_login=user.last_login,
            middle_name=None,  # Aquí puedes dejarlo como None o asignar un valor predeterminado
            role="patient",  # Asigna un rol predeterminado o personaliza según tus necesidades
        )


class Migration(migrations.Migration):

    dependencies = [
        (
            "accounts",
            "0001_initial",
        ),  # Asegúrate de que esta migración dependa de la inicial
    ]

    operations = [
        migrations.RunPython(copy_user_data),
    ]
