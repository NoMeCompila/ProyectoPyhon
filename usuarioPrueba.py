class rol:
    def __init__(self, idRol, descripcion):
        self.__idRol = idRol
        self.__descripcion = descripcion

    @property
    def idRol(self):
        return self.__idRol


    @property
    def descripcion(self):
        return self.__descripcion


    @idRol.setter
    def idRol(self, p_idRol):
        self.__idRol = p_idRol

