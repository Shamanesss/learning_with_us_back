import sqlite3

# para cerrar la conexion cuando acabe el bloque aunque tenga alguna excepcion seria
# with sqlite3.connect('academia.db')  as conexion:

conexion = sqlite3.connect('academia.db')
cursor = conexion.cursor()

# Para crear una tabla con SQLITE
cursor.execute('''CREATE TABLE IF NOT EXISTS lecciones  (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    curso_id INTEGER,
                    titulo TEXT,
                    lenguaje TEXT,
                    ejemplo_path TEXT,
                    contenido TEXT,
                    FOREIGN KEY ("curso_id") REFERENCES "cursos" ("id")
                )''')


cursor.execute('''CREATE TABLE IF NOT EXISTS cursos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT,
                    descripcion TEXT,
                    contenido TEXT,
                    nivel TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT,
                        apellido TEXT,
                        correo TEXT,
                        contraseña TEXT
                    )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS progreso (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        usuario_id INTEGER, 
                        curso_id INTEGER,
                        leccion_id INTEGER,
                        porcentaje_completo REAL,
                        FOREIGN KEY ("usuario_id") REFERENCES "usuarios" ("id"),
                        FOREIGN KEY ("curso_id") REFERENCES "cursos" ("id"),
                        FOREIGN KEY ("leccion_id") REFERENCES "lecciones" ("id")
                    )''')

conexion.commit()
conexion.close()
