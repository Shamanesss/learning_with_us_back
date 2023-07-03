import sqlite3
# conexion = sqlite3.connect('academia.db')
# cursor = conexion.cursor()

# # Crear tabla de cursos


# # Confirmar los cambios y cerrar la conexión
# conexion.commit()
# conexion.close()

# -------------------------POST--------------------------


def post_course(cursos):
    con = sqlite3.connect("academia.db")
    cur = con.cursor()
    res = "INSERT INTO cursos VALUES(?, ?, ?, ?,?)"
    valores = (cursos['id'], cursos['titulo'],
               cursos['descripcion'], cursos['contenidos'], cursos['nivel'])
    cur.execute(res, valores)
    con.commit()
    con.close()
