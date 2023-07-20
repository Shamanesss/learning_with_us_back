import src.database as db


database_path = ""

# function to connect to the database


def init_db(database):
    global database_path
    database_path = database


# ----- Metodo get de todo los cursos ---
def get_cursos():
    con = db.conexionBBDD()
    print("Conexión establecida")

    cursor = con.cursor()
    print("Cursor creado")

    cursor.execute("SELECT * FROM cursos")
    print("Consulta ejecutada")

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
    print("Conexión cerrada")
    return lista_cursos

# ---consulta a la BBDD que junte dos tablas y que nos de el titulo de la curso y id y el titulo de  lecciones y el id de lecciones-------------------------


def get_listado(id):
    con = db.conexionBBDD()
    print("Conexión establecida")

    cursor = con.cursor()
    print("Cursor creado")

    cursor.execute(
        "SELECT cursos.titulo as titulo, lecciones.titulo  as listado, cursos.idcursos as idcursos, lecciones.idlecciones as idlecciones FROM cursos INNER JOIN lecciones ON cursos.idcursos = lecciones.idcursos WHERE lecciones.idcursos = %s", (id,))
    print("Consulta ejecutada")

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
    print("Conexión cerrada")
    return listado

# --conseguir cada leccion


def get_leccion(idleccion):
    con = db.conexionBBDD()
    print("Conexión establecida")

    cursor = con.cursor()
    print("Cursor creado")

    cursor.execute(
        "SELECT * FROM lecciones WHERE idlecciones = %s", (idleccion,))
    print("Consulta ejecutada")

    leccion = cursor.fetchone()

    leccion_individual = {
        "idleccion": leccion[0],
        "created_at": leccion[1],
        "idcursos": leccion[2],
        "titulo": leccion[3],
        "contenido": leccion[4]
    }

    con.commit()
    con.close()
    print("Conexión cerrada")
    return leccion_individual
