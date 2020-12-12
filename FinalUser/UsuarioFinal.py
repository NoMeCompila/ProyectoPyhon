from coneccionDB import cursor,conn

class UsuarioFinal:
    def __init__(self, idUsuario="", idPersona = 1, usuario="syndrasama", contraseña= "fernandito98",contra="fernandito98"):
        self.idUsuario = idUsuario
        self.idPersona = idPersona
        self.usuario = usuario
        self.contraseña = contraseña
        self.contra = contra

    #cursor.execute("INSERT INTO finalUser() VALUES ('Hector', 27, 'hector@ejemplo.com')")

    def registro(self):
        sql = "INSERT INTO finalUser(idPersona,usuario,contraseña,contra) values(?,?,?,?)"

        usuario = (self.idPersona,self.usuario,self.contraseña,self.contra)


        cursor.execute(sql,usuario)
        conn.commit()






    def identificar(self):
        pass

"""    @property
    def idUsuario(self):
        return self.__idUsuario
        
    @property
    def idPersona(self):
        return self.__idPersona
    @property
    def usuario"""


"""def registro():
    sql = "INSERT INTO finalUser(idPersona,usuario,contra) values(?,?,?)"
    usuario = (self.idPersona, self.usuario, self.contra)
    cursor.execute(sql, usuario)
    conn.commit()
    return None"""