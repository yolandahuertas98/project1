from db_connection import connect

# Probar conexión
conn = connect()
if conn:
    conn.close()