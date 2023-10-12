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
        id int(2000) AUTO_INCREMENT NOT NULL,
        nombre VARCHAR NOT NULL,
        apellidos VARCHAR NOT NULL,
        correo VARCHAR NOT NULL,
        contraseña VARCHAR NOT NULL,
        rol VARCHAR NOT NULL,
        fecha DATE NOT NULL,
        CONSTRAINT  PK_usuarios PRIMARY KEY(id),
        CONSTRAINT uq_email UNIQUE(correo)
        
        ENGINE = INNODB;
        )""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS materias(
        id int(2000) AUTO_INCREMENT NOT NULL,
        nombre_materia VARCHAR NOT NULL,
        maestro varchar NOT NULL,
        fecha DATE NOT NULL,
        CONSTRAINT  PK_materias PRIMARY KEY(id)
        
        ENINE = INNODB;
        
        )""")
    
    cursor.execute("""CREATE TABLE IF NOT datos_generales_alumnos(
        id int(2000) AUTO_INCREMENT NOT NULL,
        nombre_materia VARCHAR NOT NULL,
        maestro varchar NOT NULL
        fecha DATE NOT NULL,
        CONSTRAINT PK_materias PRIMARY KEY(id)
        CONSTRAINT fk_usuarios_materias FOREING KEY
        )""")
    
    
    
     