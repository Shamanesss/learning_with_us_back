import src.database as db


database_path = ""

# function to connect to the database


def init_db(database):
    global database_path
    database_path = database


# def get_cursos():
#     try:
#         con = db.conexionBBDD()
#         cursor = con.cursor()
#         cursor.execute("SELECT * FROM cursos")
#         cursos = cursor.fetchall()
#         print(cursos)
#         con.commit()
#     except Exception as e:
#         print("Error:", str(e))
#     finally:
#         if con:
#             con.close()


def get_cursos():
    con = db.conexionBBDD()
    print("Conexión establecida")  # Mensaje de depuración

    cursor = con.cursor()
    print("Cursor creado")  # Mensaje de depuración

    cursor.execute("SELECT * FROM cursos")
    print("Consulta ejecutada")  # Mensaje de depuración

    cursos = cursor.fetchall()

    lista_cursos = []

    for curso in cursos:
        curso = {
            "id": curso[0],
            "created_at": curso[1],
            "titulo": curso[2],
            "descripcion": curso[3],
            "contenido": curso[4]
        }
        lista_cursos.append(curso)

    print(cursos)
    con.commit()
    con.close()
    print("Conexión cerrada")  # Mensaje de depuración
    return lista_cursos


def get_listado(id):
    con = db.conexionBBDD()
    print("Conexión establecida")  # Mensaje de depuración

    cursor = con.cursor()
    print("Cursor creado")  # Mensaje de depuración

    cursor.execute(
        "SELECT cursos.titulo as titulo, lecciones.titulo  as listado, cursos.idcursos as idcursos, lecciones.idlecciones as idlecciones FROM cursos INNER JOIN lecciones on cursos.idcursos = lecciones.idcursos WHERE lecciones.idlecciones= %s", (id))
    print("Consulta ejecutada")  # Mensaje de depuración

    indices = cursor.fetchall()

    listado = []
    for indice in indices:

        indice = {"titulo": indice[0],
                  "listado": indice[1],
                  "idcursos": indice[2],
                  "idlecciones": indice[3]}
        listado.append(indice)
    con.commit()
    con.close()
    print("Conexión cerrada")  # Mensaje de depuración
    return listado
