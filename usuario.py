import pyodbc

def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("select * from rol")
conn = pyodbc.connect(
    "Driver = {SQL Server Native Client  11.0};"
    "Server = DESKTOP-S18EFJ4\SQLEXPRESS;"
    "Database = gimnasio;"
    "Trusted_Connection = yes;"
)

read(conn)
create(conn)
update(conn)
delete(conn)

conn.close()