import psycopg2


def conexionBBDD():
    host = "db.xzojqmxyrvvgxzoiwfcl.supabase.co"
    user = "postgres"
    password = "JUGWM0S6HBjFK1md"
    database = "postgres"
    port = 5432

    try:
        con = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            dbname=database,
            port=port)
        print("Base de datos conectada")

        return con

    except psycopg2.Error as error:
        print(f"No hay conexicon con la base de datos: {error}")

        return None
