import psycopg2
import spotifyETL.cfg as cfg

hostname = cfg.database_hostname
database = cfg.database
username = cfg.database_username
pwd = cfg.database_pwd
port_id = cfg.database_port_id

# Connect to the database
def connectToDatabase():
    try:
        conn = psycopg2.connect(
            dbname = database,
            user = username,
            password = pwd,
            host = hostname,
            port = port_id)
        
    except Exception as error:
        print('Hubo un error al conectarse a la BD: ', error)
    print('Conexion a la BD exitosa')
    return conn

def dissconectFromDatabase(conn):
    try:
        conn.close()
    except Exception as error:
        print('Hubo un error al desconectarse de la BD: ', error)
    print('Desconexion de la BD exitosa')