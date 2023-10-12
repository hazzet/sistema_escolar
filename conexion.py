import mysql.connector

def conectar_bd():
    
    bd = mysql.connector.connect(
        host = "localhost",
        user = "root",
        paswd = "",
        database = "control_escolar",
        port = 3306
        
    )
    cursor.execute("CREATE DATABASE IF NOT EXISTS control_escolar")
    
    cursor = bd.cursor(buffered= True)
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
        id
        nombre
        apellidos
        correo
        contraseña
        rol
        
        )""")