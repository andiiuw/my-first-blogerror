import MySQLdb
from urllib.request import urlopen
import re

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'andiiuw1'
DB_NAME = 'bd1'

def run_query(query=''):
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

    return data




url = ("http://www.marca.com")
html = urlopen(url).read()
enlaces = re.findall('href="(http://.*?)"', html.decode('utf-8','ignore'))
enlaces2 = re.findall('title="(.*?)"', html.decode('utf-8','ignore'))


for  enlace,enl in zip(enlaces2, enlaces):
    print ( enl +" // " + enlace)


    query = "INSERT INTO links (link, palabra) VALUES ('%s','%s')" % (enl, enlace)
    run_query(query)







