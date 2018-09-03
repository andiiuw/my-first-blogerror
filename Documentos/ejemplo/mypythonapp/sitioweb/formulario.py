
def envia():
    texto = "<form action=\"http://python-web/recibe\" method=\"get\">\
            <p>Buscar links: <input type=\"text\" name=\"nombre\" value=\"\"/></p>\
            <p><input type=\"submit\" value=\"Enviar\"/></p>\
            </form>"
    return texto


    
def recibe(parametros):
	import MySQLdb
	from urllib.request import urlopen
	import re
    texto ="<p>Valor2:" +parametros['QUERY_STRING'] + "</p>"




    return texto

