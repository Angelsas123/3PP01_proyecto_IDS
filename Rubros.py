import os
from modelos import Item, productos

def filtrado():
    print("Función filtrado en Rubros.py")

def ordenar():
    print("Función ordenar en Rubros.py")

def borrar():
    print("Función borrar en Rubros.py")

def clear():
    return os.system("cls" if os.name == "nt" else "clear")

def Rubros_menu():
    opc = 1 # variable de control de opciones

    clear()
    while opc!=0: #menú copiado de orion y adaptado a rubros por simmel
        print("|====================|")
        print("===== MENU =====\
              \n1. Filtrado\
              \n2. Ordenar\
              \n3. borrar\
              \n0. Salir")
        
        try:
            opc = int(input(" \n    --> "))

        except ValueError:
            clear()
            print("|====================|\n")
            print("ERROR! Tipo de dato incorrecto. Inténtalo de nuevo.\n")

        else:
            print("|====================|")
            print(f"-----> OPCIÓN {opc} <-----")

            match opc:
                case 1:
                    filtrado()

                case 2:
                    ordenar()

                case 3:
                    borrar()

                case 0:
                    print("-----> SALIENDO <-----")

                case _:
                    print("-----> OPCION NO DISPONIBLE <-----")