'''
Aplicacion de login
'''
from os import system

import FinalUser
from FinalUser import UsuarioFinal

from FinalUser import ClaseAcciones #importo el paquete creado para realzar las acciones de login y singin
def menu():
#menú que al ingresar una opcion  limpia la pantalla automáticamente
    print('''
\t  MENÚ
*************************
1 - Iniciar Sesión      *
2 - Registrarse         *
3 - Ayuda (3 + enter)   *
4 - Salir               *
*************************
''')

    hacer = ClaseAcciones.Acciones()
    opc = input('Ingrese una opción: ')
    #Menú Recursivo papá
    if opc == '1' or opc == 'iniciar sesion' or opc == 'Iniciar Sesión' or opc == 'Iniciar sesión':
        system("cls")
        hacer.inicioSecion()

    elif opc == '2' or opc == 'registrarse' or opc == 'Registrarse':
        system("cls")
        usuario1 = UsuarioFinal.UsuarioFinal()
        #print(usuario1.usuario)
        usuario1.registro()

    elif opc == '3' or opc == 'Ayuda' or opc == 'ayuda' or opc == 'AYUDA':
            system("cls")
            hacer.ayuda()
            menu()
    elif opc == '4' or opc  == 'Salir' or opc == 'SALIR':
        system("cls")
        print("\t\t\t\tGRACIAS POR USAR NUESTROS SERVICIOS.")
        pass #es un comando que indica que no se ejecutará ninguna línea de código (similar al brak en los bucles)
    else:
        system("cls")
        print("\n")
        print("OPCION INCORRECTA, intente de nuevo...")
        menu()
menu()