import sqlite3

# -------------------------POST--------------------------


def post_user(usuario):
    con = sqlite3.connect("academia.db")
    cur = con.cursor()
    res = "INSERT INTO usuario VALUES(?, ?, ?, ?)"
    valores = (usuario['id'], usuario['curso_id'],
               usuario['leccion_id'], usuario['porcentaje_completado'])
    cur.execute(res, valores)
    con.commit()
    con.close()
