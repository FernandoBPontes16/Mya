from database import connection

def salvarDB(role,message):
    connection.cursor.execute(
        'INSERT INTO memory (role,message) VALUES (%s, %s)',
        (role,message)
    )
    connection.meudb.commit()