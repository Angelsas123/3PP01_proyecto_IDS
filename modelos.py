#Hecho por Karev: clase para los productos de la tienda
class Item:
    def __init__(self, nombre: str, id: int, descripcion: str, precio: float, lote: str, fecha_caducidad: str):
        self.nombre = nombre
        self.id = id
        self.desc = descripcion
        self.precio = precio
        self.lote = lote
        self.fechaCad = fecha_caducidad
        self.cantidad = 999
    
    def __str__(self):
        return f"({self.id}) - Producto: {self.nombre} | '{self.desc}'\
                \n | Precio: {self.precio} | Lote y fecha de caducidad: {self.lote}, {self.fechaCad}\
                \n | Stock disponible: {self.cantidad} |\n | "

# Lista de productos
productos = []