maestra_productos = [
    {'codigo': 1, 'cantidad': 100, 'nombre': 'Manzana', 'precio_un': 800},
    {'codigo': 2, 'cantidad': 50, 'nombre': 'Plátano', 'precio_un': 1500},
    {'codigo': 3, 'cantidad': 30, 'nombre': 'Naranja', 'precio_un': 750},
    {'codigo': 4, 'cantidad': 20, 'nombre': 'Zanahoria', 'precio_un': 1000},
    {'codigo': 5, 'cantidad': 40, 'nombre': 'Lechuga', 'precio_un': 1300},
    {'codigo': 6, 'cantidad': 25, 'nombre': 'Uva', 'precio_un': 670},
    {'codigo': 7, 'cantidad': 10, 'nombre': 'Pera', 'precio_un': 900},
    {'codigo': 8, 'cantidad': 15, 'nombre': 'Papaya', 'precio_un': 2000},
    {'codigo': 9, 'cantidad': 5, 'nombre': 'Piña', 'precio_un': 3000},
    {'codigo': 10, 'cantidad': 10, 'nombre': 'Sandía', 'precio_un': 2500},
    {'codigo': 11, 'cantidad': 10, 'nombre': 'Cebolla', 'precio_un': 1400}]



class Producto:
    def __init__(self, codigo, cantidad, nombre, precio_un):
        self.codigo = codigo
        self.cantidad = cantidad
        self.nombre = nombre
        self.precio_un = precio_un

    def agregar_stock(self, cantidad):
        self.cantidad += cantidad

    def vender_stock(self, cantidad):
        if cantidad > self.cantidad:
            print("No hay suficiente stock disponible.")
        else:
            self.cantidad -= cantidad

    def consultar_stock(self):
        return self.cantidad

    def modificar_precio_un(self, nuevo_precio):
        self.precio_un = nuevo_precio


#producto1 = Producto(1, 10, "Coca Cola", 1000)
#producto1.vender_stock(12)
#stock_disponible= producto1.consultar_stock()

#print(stock_disponible)