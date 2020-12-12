import coneccionDB

cursor = coneccionDB.cursor

#cursor.execute('select * from rol')#consulta de SQL
#for row in cursor:#for para recorrer la tabla y traer los datos
#    print(row)

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
