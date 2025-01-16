# Usar una imagen base de Python
FROM python:3.9-slim

# Instalar las dependencias del sistema
RUN apt-get update && apt-get install -y \
    unixodbc-dev \
    msodbcsql17 \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Configuración de directorios de trabajo
WORKDIR /app

# Instalar dependencias de Python
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copiar el código de la aplicación
COPY . /app/

# Exponer el puerto (asegúrate de que el puerto coincida con el de tu app)
EXPOSE 8000

# Ejecutar el servidor de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
