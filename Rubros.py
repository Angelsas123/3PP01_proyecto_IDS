import os
from modelos import Item, productos

def clear():
    os.system("cls" if os.name == "nt" else "clear")
# 1. Función para filtrar por Precio leonel
def filtrar_por_precio():
    clear()
    print("|====================|")
    print("=== FILTRAR POR PRECIO ===")

    # Validación de entrada
    try:
        min_precio = float(input("Ingrese el precio mínimo: "))
        max_precio = float(input("Ingrese el precio máximo: "))
    except ValueError:
        print("\nERROR: Debes ingresar valores numéricos.")
        input("Presiona Enter para volver...")
        return
    
    print(f"\nBuscando productos entre ${min_precio} y ${max_precio}...\n")

    # Validación: productos existente
    if not productos:
        print("No hay productos cargados para filtrar.")
        input("\nPresiona Enter para continuar...")
        return

    encontrados = [p for p in productos if min_precio <= p.precio <= max_precio]
    if encontrados:
        print(f"Se encontraron {len(encontrados)} coincidencias:\n")
        for item in encontrados:
            try:
                print(item) 
            except:
                print(f"{item.nombre} - ${item.precio}")
    else:
        print("No hay productos en ese rango de precios.")

    input("\nPresiona Enter para continuar...")

def filtrar_por_id():
    print("Función para filtrar por ID (Pendiente)")
    input("\nPresiona Enter para continuar...")

def filtrar_por_fecha():
    print("Función para filtrar por Fecha de Caducidad (Pendiente)")
    input("\nPresiona Enter para continuar...")

def filtrado():
    opc = 1
    clear()

    while opc != 0:
        print("|====================|")
        print("===== MENÚ FILTRADO =====")
        print("1. Por Precio")
        print("2. Por ID de Producto")
        print("3. Por Fecha de Caducidad")
        print("0. Volver al Menú Principal")

        try:
            opc = int(input("\n--> Selecciona una opción: "))
        except ValueError:
            clear()
            print("|====================|")
            print("ERROR: Debes ingresar un número.\n")
            continue

        clear()
        print("|====================|")
        print(f"-----> OPCIÓN {opc} <-----\n")

        match opc:
            case 1:
                filtrar_por_precio()
            case 2:
                filtrar_por_id()
            case 3:
                filtrar_por_fecha()
            case 0:
                print("-----> VOLVIENDO AL MENÚ PRINCIPAL <-----")
            case _:
                print("-----> OPCIÓN NO DISPONIBLE <-----")


def ordenar():
    print("Función ordenar en Rubros.py")


def borrar():
    print("Función borrar en Rubros.py")


def Rubros_menu():
    opc = 1
    clear()

    while opc != 0:
        print("|====================|")
        print("===== MENU =====")
        print("1. Filtrado")
        print("2. Ordenar")
        print("3. Borrar")
        print("0. Salir")

        try:
            opc = int(input("\n--> "))
        except ValueError:
            clear()
            print("|====================|")
            print("ERROR: Debes ingresar un número.\n")
            continue

        clear()
        print("|====================|")
        print(f"-----> OPCIÓN {opc} <-----\n")

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
                print("-----> OPCIÓN NO DISPONIBLE <-----")


