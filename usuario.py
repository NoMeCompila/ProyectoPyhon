import pyodbc #libreria para conectar con SQL
#definbicion de una variable que sirve para traer la base de datos
#escribir todo sin espacios
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};' #driver que se descarga de la pagina oficial de microsoft
                      'SERVER=DESKTOP-S18EFJ4\SQLEXPRESS;' #nombre de mi server de SQL
                      'DATABASE=gimnasio;' #nombre de la base de datos
                      'Trusted_Connection=yes;'#Verificar que la coneccion sea verdadera
                      'UID=fernando;'#nombre de usuario
                      'PWD=fernandito98')#contraseña
cursor=conn.cursor() #definicion de una variable que sirve para recorrer las tablas

cursor.execute('select * from rol')#consulta de SQL
for row in cursor:#for para recorrer la tabla y traer los datos
    print(row)

#deficnicion de una clase del tipo rol
class rol:
    def __init__(self, idRol, descripcion=""):#constructor sobrecargado
        self.__idRol = idRol
        self.__descripcion = descripcion

    #getters
    @property
    def idRol(self):
        return self.__idRol


    @property
    def descripcion(self):
        return self.__descripcion

    #setters
    @idRol.setter
    def idRol(self, p_idRol):
        self.__idRol = p_idRol

    @descripcion.setter
    def descripcion(self,p_descripcion):
        self.__descripcion = p_descripcion

    #METODOS
    def insertarRol(self):
        sql = 'insert into rol() values'




'''
def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("select * from rol")
    for row in cursor:
        print(f'row = {row}')
    print()

def create(conn):
    print("Creado")
    cursor = conn.cursor()
    cursor.execute(
        'insert into rol(descripcion) values (?);',
        ('Entrenador')
    )
    conn.commit()
    read(conn)


def update(conn):
    print("Actualizando")
    cursor = conn.cursor()
    cursor.execute(
        'update rol set descripcion = ? where idRol = ? ',
        ('Dueño')
    )
    conn.commit()
    read(conn)


def delete(conn):
    print("Borrar")
    cursor = conn.cursor()
    cursor.execute(
        'delete from rol where idRol = ?',
    )
    conn.commit()
    read(conn)

conn = pyodbc.connect(
    'Driver = {ODBC Driver 17 for SQL Server};'
    'Server = DESKTOP-S18EFJ4\SQLEXPRESS;'
    'Database = gimnasio;'
    'Trusted_Connection = yes;'
)






read(conn)
create(conn)
update(conn)
delete(conn)

conn.close()
'''