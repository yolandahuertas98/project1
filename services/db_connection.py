import psycopg2

class PostgreSQL:

    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        try:
            self.conn = psycopg2.connect(dbname=self.dbname, user=self.user, password = self.password, 
                                    host=self.host, port=self.port)
            print("✅ Conexión exitosa a PostgreSQL")
        except Exception as e:
            print("❌ Error al conectar a PostgreSQL:", e)


    def insertar_dataframe(self):
        cursor = self.conn.cursor()

        


DB_CONFIG = {
    "dbname": "project1_db",  
    "user": "postgres",       
    "password": "postgres",  
    "host": "localhost",     
    "port": "5432"            
}

# Función para conectar a la base de datos
def connect():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("✅ Conexión exitosa a PostgreSQL")
        return conn
    except Exception as e:
        print("❌ Error al conectar a PostgreSQL:", e)
        return None
    

