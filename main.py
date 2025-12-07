# Lista de productos
productos = []
# Función por Pedro
def ingresar():
    print("===== INGRESAR PRODUCTO =====")
    id_producto = input("ID del producto: ")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    descripcion = input("Descripción: ")
    lote = input("Lote: ")
    fecha_caducidad = input("Fecha de Caducidad (DD/MM/AAAA): ")

    producto = {
        'id': id_producto,
        'nombre': nombre,
        'precio': precio,
        'descripcion': descripcion,
        'lote': lote,
        'fecha_caducidad': fecha_caducidad
    }
    
    productos.append(producto)
    
    print("\n✓ Producto ingresado exitosamente!")

# Función por Pedro
def mostrar():
    print("===== LISTA DE PRODUCTOS =====")
    if len(productos) == 0:
        print("No hay productos registrados.")
        print("|====================|\n")
        return
    
    for i, prod in enumerate(productos, 1):
        print(f"\n--- Producto {i} ---")
        print(f"ID: {prod['id']}")
        print(f"Nombre: {prod['nombre']}")
        print(f"Precio: ${prod['precio']:.2f}")
        print(f"Descripción: {prod['descripcion']}")
        print(f"Lote: {prod['lote']}")
        print(f"Fecha de Caducidad: {prod['fecha_caducidad']}")
    
    print(f"\nTotal de productos: {len(productos)}")

# funcion por Danny
def borrar():
    print("borrar")
    print("borrar producto")

    if len(productos) == 0:
        print("No hay productos para borrar.")
        return
    
    id_borrar = input("Ingrese el ID del producto a borrar: ")
    
    # Borrar producto por ID
    for i, prod in enumerate(productos):
        if prod['id'] == id_borrar:
            del productos[i]
            print(f"✓ Producto con ID {id_borrar} borrado exitosamente.")
            return
        else:
            print("✗ Producto no encontrado.")
  
# Función por Pavel
def modificar():
    print("MODIFICAR")
    if len(productos) == 0:
        print("No hay productos registrados.")
        return
    
    id_buscar = input("Ingrese el ID del producto a modificar: ")
    
    for prod in productos:
        if prod['id'] == id_buscar:
            print("\nProducto encontrado. Deje vacío cualquier campo para NO modificarlo.\n")
            
            nuevo_nombre = input(f"Nombre ({prod['nombre']}): ")
            nuevo_precio = input(f"Precio ({prod['precio']}): ")
            nueva_desc = input(f"Descripción ({prod['descripcion']}): ")
            nuevo_lote = input(f"Lote ({prod['lote']}): ")
            nueva_fecha = input(f"Fecha de Caducidad ({prod['fecha_caducidad']}): ")
            
            if nuevo_nombre != "":
                prod['nombre'] = nuevo_nombre
            if nuevo_precio != "":
                try:
                    prod['precio'] = float(nuevo_precio)
                except:
                    print("Precio inválido. Se mantiene el valor anterior.")
            if nueva_desc != "":
                prod['descripcion'] = nueva_desc
            if nuevo_lote != "":
                prod['lote'] = nuevo_lote
            if nueva_fecha != "":
                prod['fecha_caducidad'] = nueva_fecha
            
            print("\nProducto modificado exitosamente!")
            return

    print("No se encontró un producto con ese ID.")

def ordenar():
    print("ORDENAR")
    print("ordenar productos por ID")

    if len(productos) == 0:
        print("No hay productos para ordenar.")
        return
    
    # usamos metodo burbuja
    for i in range(len(productos)-1):
        for j in range(len(productos)-1-i):
            if productos[j]['id'] > productos[j+1]['id']:
                # intercambiar productos
                productos[j],productos[j+1] = productos[j+1],productos[j]
    print("✓ Productos ordenados por ID exitosamente.")

opc = 1 # variable de control de opciones

while opc!=0: #menú por Orión
    print("|====================|")
    print("===== MENU =====")
    print("0. Salir")
    print("1. Ingresar Producto")
    print("2. Mostrar")
    print("3. Modificar lo ingresado")
    print("4. Ordenar")
    print("5. Borrar")
    opc = int(input("----> "))
    print("|====================|")
    print("-----> OPCION: ", opc," <-----")

    match opc:
        case 0:
            print("-----> SALIENDO <-----")
        case 1:
            ingresar()
        case 2:
            mostrar()
        case 3:
            modificar()
        case 4:
            ordenar()
        case 5:
            borrar()
        case _:
            print("-----> OPCION NO DISPONIBLE <-----")