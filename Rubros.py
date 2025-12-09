import os
from modelos import Item, productos
from datetime import datetime

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

# 2. Función para filtrar por ID (coincidencia exacta)
def filtrar_por_id():
    clear()
    print("|====================|")
    print("=== FILTRAR POR ID ===")

    # Validación de entrada
    try:
        id_buscar = int(input("Ingrese el ID del producto: "))
    except ValueError:
        print("\nERROR: Debes ingresar un valor numérico entero.")
        input("Presiona Enter para volver...")
        return
    
    print(f"\nBuscando producto con ID {id_buscar}...\n")

    # Validación: productos existente
    if not productos:
        print("No hay productos cargados para filtrar.")
        input("\nPresiona Enter para continuar...")
        return

    encontrado = None
    for p in productos:
        if p.id == id_buscar:
            encontrado = p
            break
    
    if encontrado:
        print("✓ Producto encontrado:\n")
        try:
            print(encontrado) 
        except:
            print(f"ID: {encontrado.id} - {encontrado.nombre} - ${encontrado.precio}")
    else:
        print(f"No se encontró ningún producto con ID {id_buscar}.")

    input("\nPresiona Enter para continuar...")

# 3. Función para filtrar por Fecha de Caducidad Omar
def filtrar_por_fecha():
    clear()
    print("|====================|")
    print("=== FILTRAR POR FECHA DE CADUCIDAD ===")

    print("Ingresa las fechas en formato DDMMAAAA")
    
    try:
        fecha_min_input = input("Fecha mínima (DDMMAAAA): ")
        fecha_max_input = input("Fecha máxima (DDMMAAAA): ")
        
        # Validar formato
        if not (fecha_min_input.isdigit() and len(fecha_min_input) == 8):
            raise ValueError("Formato de fecha mínima inválido")
        if not (fecha_max_input.isdigit() and len(fecha_max_input) == 8):
            raise ValueError("Formato de fecha máxima inválido")
        
        # Convertir a objetos datetime para comparación
        fecha_min = datetime.strptime(fecha_min_input, "%d%m%Y")
        fecha_max = datetime.strptime(fecha_max_input, "%d%m%Y")
        
    except ValueError as e:
        print(f"\nERROR: {e}")
        print("Asegúrate de ingresar fechas válidas en formato DDMMAAAA")
        input("Presiona Enter para volver...")
        return
    
    print(f"\nBuscando productos con caducidad entre {fecha_min.strftime('%d/%m/%Y')} y {fecha_max.strftime('%d/%m/%Y')}...\n")

    # Validación: productos existente
    if not productos:
        print("No hay productos cargados para filtrar.")
        input("\nPresiona Enter para continuar...")
        return

    encontrados = []
    for p in productos:
        try:
            # Convertir la fecha del producto (formato DD/MM/YYYY) a datetime
            fecha_prod = datetime.strptime(p.fechaCad, "%d/%m/%Y")
            if fecha_min <= fecha_prod <= fecha_max:
                encontrados.append(p)
        except ValueError:
            # Si hay error al convertir fecha, ignorar ese producto
            continue
    
    if encontrados:
        print(f"Se encontraron {len(encontrados)} coincidencias:\n")
        for item in encontrados:
            try:
                print(item) 
            except:
                print(f"{item.nombre} - Caducidad: {item.fechaCad}")
    else:
        print("No hay productos en ese rango de fechas.")

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


