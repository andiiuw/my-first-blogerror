import MySQLdb
 
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

query = "SELECT * FROM tabla1" 
result = run_query(query) 
print(result)