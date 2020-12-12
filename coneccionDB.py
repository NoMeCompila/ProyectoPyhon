import pyodbc #libreria para conectar con SQL
#definbicion de una variable que sirve para traer la base de datos
#escribir todo sin espacios
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};' #driver que se descarga de la pagina oficial de microsoft
                      'SERVER=DESKTOP-S18EFJ4\SQLEXPRESS;' #nombre de mi server de SQL
                      'DATABASE=gimnasio;' #nombre de la base de datos
                      'Trusted_Connection=yes;'#Verificar que la coneccion sea verdadera
                      'UID=fernando;'#nombre de usuario
                      'PWD=fernandito98')#contraseña
#print("*-----------------------------------*")
print(conn)

cursor=conn.cursor() #definicion de una variable que sirve para recorrer las tablas

