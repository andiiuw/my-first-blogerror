# -*- coding: utf-8 -*-
import MySQLdb
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'password'
DB_NAME = 'db1'


def run_query(query=''):

    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
    conn = MySQLdb.connect(*datos) # Conectar a la base de datos
    cursor = conn.cursor()         # Crear un cursor
    cursor.execute(query)          # Ejecutar una consulta

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()   # Traer los resultados de un select
    else:
        conn.commit()              # Hacer efectiva la escritura de datos
        data = None

    cursor.close()                 # Cerrar el cursor
    conn.close()                   # Cerrar la conexión

    return data

#query = "select * from tabla1"
#result = run_query(query)
#print (result)


def envia():
    texto = "<form action=\"http://python-web/recibe\" method=\"get\">\
            <p>Buscar <input type=\"text\" name=\"nombre\" value=\"\"/></p>\
            <p><input type=\"submit\" value=\"Enviar\"/></p>\
            </form>"
    return texto


def recibe(parametros):
    encontrar = parametros['QUERY_STRING']
    encontrar2 = encontrar[7:len(encontrar)]
    texto ="<p> Valor:" +encontrar2 + "</p>"

    query = "select tabla1col from db1.tabla1 where tabla1col2 like '%"+encontrar2+"%'"
    result = run_query(query)

    texto += "<table style=\"width:100%\"> "

    for x in result:
        texto += "<tr> \
                        <td>"+  str("Encontrado: ")   + "</td>\
                        <td><a href="+str(x)+">"+str(x)+"</a></td>\
                    </tr>"
    texto += " </table>"
    return texto
