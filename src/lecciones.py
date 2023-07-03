import sqlite3

# -------------------------POST--------------------------


def post_lesson(leccion):
    con = sqlite3.connect("academia.db")
    cur = con.cursor()
    res = "INSERT INTO lecciones VALUES (NUll, ?, ?, ?,?,?)"
    valores = (leccion['curso_id'],
               leccion['titulo'], leccion['lenguaje'], leccion['ejemplo_path'], leccion['contenido'])
    cur.execute(res, valores)

    con.commit()
    con.close()


"""
# create({"id": "ALI", "nombre": "Alicante","temperature": 30, "rain_probability": 0.0})

#     WEATHER_DATA[weather["id"]] = weather

# para crear una consulta de un campo por medio de un id en la barra del navegador

# --------------------------Get un ID--------------------
def read(city_id):
    con = sqlite3.connect("weather.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM cities WHERE id=?", [city_id])
    row = res.fetchone()
    con.close()

    city = {"id": row[0],
            "name": row[1],
            "temperature": row[2],
            "rain_probability": row[3]
            }

    return city


# ----------------------Get TODAS las CIUDADES


def read_all():
    con = sqlite3.connect("weather.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM cities")
    rows = res.fetchall()

    city_list = []

    for row in rows:
        row = {"id": row[0],
               "name": row[1],
               "temperature": row[2],
               "rain_probability": row[3]
               }
        city_list.append(row)
        print("***que es esto ***", row)

    return city_list

# -----------------------DELETE


def delete(city_id):
    con = sqlite3.connect("weather.db")
    cur = con.cursor()
    res = "DELETE FROM cities WHERE id = ?"
    cur.execute(res, (city_id))
    con.commit()
    con.close()

# ------------------------UPDATE


def update(city_id, new_name, new_temperature, new_rain_probability):
    con = sqlite3.connect("weather.db")
    cur = con.cursor()
    res = "UPDATE cities SET name = ?, temperature = ?, rain_probability = ? WHERE id = ?"
    values = (new_name, new_temperature, new_rain_probability, city_id)
    cur.execute(res, values)
    con.commit()
    con.close()


update("ALI", "Alicate", 28.5, 0.2)


def delete(id):
    con = sqlite3.connect("weather.db")
    cur = con.cursor()
    cur.execute("DELETE FROM cities WHERE id=?", [id])
    con.commit()
    con.close()


conexion.commit
cerrar_conexion.close()
"""
