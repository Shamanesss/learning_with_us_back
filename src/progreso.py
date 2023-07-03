import sqlite3


def post_progress(progreso):
    con = sqlite3.connect("academia.db")
    cur = con.cursor()
    res = "INSERT INTO progreso VALUES(?, ?, ?, ?, ?)"
    valores = (progreso['id'], progreso['usuario_id'],
               progreso['curso_id'], progreso['leccion_id'], progreso['porcentaje_completado'])
    cur.execute(res, valores)
    con.commit()
    con.close()
