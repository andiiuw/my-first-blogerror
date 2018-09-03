

    




def envia():
    texto = "<form action=\"http://python-web/recibe\" method=\"get\">\
            <p>Tu nombre: <input type=\"text\" name=\"nombre\" value=\"\"/></p>\
            <p><input type=\"submit\" value=\"Enviar\"/></p>\
            </form>"
    return texto



def recibe(parametros):
import MySQLdb


DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'andiiuw1'
DB_NAME = 'bd1'

    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

    conn = MySQLdb.connect(*datos)
    cursor = conn.cursor()
    cursor.execute(query)

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()
    else:
        conn.commit()
        data = None

    cursor.close()
    conn.close()
    query = "SELECT * from links"
    run_query(query)
    texto = run_query(query)
    return texto
