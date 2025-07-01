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

