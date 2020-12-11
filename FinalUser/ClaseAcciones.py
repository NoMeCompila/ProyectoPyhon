class Acciones:

    #Metodo que permite ingresar datos para guardar en el sistema
    def registrarse(self):
        print('Registrando...')
        usuario = input('Ingrese su nombre de usuario: ')
        contra  = input('Ingrese su contraseña: ')

    #Método que permite ingresar al sistema con datos ya guardados
    def inicioSecion(self):
        print('\t\t\t\tINICIO DE SESIÓN')
        usuario = input('Ingrese su nombre de usuario: ')
        contra = input('Ingrese su contraseña: ')

    #ayuda permite visualizar en pantalla las instrucciones para el uso del sistema
    def ayuda(self):
        print("\n")
        print('Para iniciar sesión presione "1" o escriba "iniciar sesion" luego presione enter')
        print('Para Registrarse presione "2" o escriba "registrarse" seguido de la tecla enter')
        print('Si desea salir del sistema debe presionar la opción "4" o escribir "salir",  \nacto seguido presionar enter')


