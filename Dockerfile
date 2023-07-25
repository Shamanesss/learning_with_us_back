# Usa la imagen oficial de Python como base
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el contenido actual al directorio /app en el contenedor
COPY . /app

# Instala las dependencias, incluyendo Gunicorn
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Expone el puerto 80, que es el puerto por defecto para HTTP
EXPOSE 80

# Comando para ejecutar la aplicación con Gunicorn
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:80"]

