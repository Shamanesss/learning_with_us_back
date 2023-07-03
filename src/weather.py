

""" Este archivo es el principal de nuestro respositorio  -- sería el dominio de nuestra carpeta (negocio) porque calcula las temperaturas 

La estructura funcionaría así: webserver.py (hablar con HTTP) -> weather.py (funcionamiento de la aplicación) -> weather_repository.py (se guardaría la BBDD y las funciones del CRUD)



# Para crear una función: function para a ser def
# No se utiliza camelCase, se separan las palabras con un barra baja
# Los bloques de la función no se pone entre llaves, sino que se pone dos puntos
# Importante la tabulación para que se sepa que el return esta incluido en la función


# def get_weather():
#     return {
#     "id": "BIO",
#     "name": "Bilbao",
#     "temperature": 11,
#     "rain_probability": 0.9
#     }


# Data de todas las ciudades
def list_weather_all():
    return read_all()


def get_weather_by(city_id):
    return read(city_id)


def add_city(weather):
    # vamos a suponer que cuando creamos una ciudad el sistema clacula la probabilidad de lluvia "rain_probability" dependiendo de la temperatura.
    # Eliminamos en el postman "rain_probability" porque es lo que va a crear el sistema
    # Antes de llamar a la función create vamos a decirle que rain_probability queremos
    # rain_probability = 0.7
    # Ahora tendremos que incluirlo en el diccionario, incluimos en el weather rain_probability para que cuando se cree nos los muestre.

    # 1) Queremos obtener el temperatura previa de la ciudad, como no sabemos como acceder ponermos unos valores estáticos
    temperatura_ciudad_previa = 22

    # #2) Calcular la diferencia de antes y la nueva
    diff_temperatura = int(weather["temperature"]) - temperatura_ciudad_previa

    if diff_temperatura < 0:
        rain_probability = 0.5
    else:
        rain_probability = 0.2

    # #rain_probability = 0.7 if diff_temperatura < 0 else rain_probability = 0.2 ---> Esto es para simplificar la función if else en una sola línea

    # rain_probability = 0.7
    weather["rain_probability"] = rain_probability
    # Comporbar que todos los campos están incluidos

    create(weather)


def update_city_data(city_id, data):
    new_name = data["name"]
    new_temperature = data["temperature"]
    new_rain_probability = data["rain_probability"]

    update(city_id, new_name, new_temperature, new_rain_probability)


def remove_city(id):
    delete(id)
    """
