import psycopg2
import cfg

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
        print('Hubo un error: ', error)
    print('Conexion exitosa')
    return conn