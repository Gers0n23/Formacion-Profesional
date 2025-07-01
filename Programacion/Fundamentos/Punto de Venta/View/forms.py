from ast import main
from cProfile import label
from turtle import st, update
from typing import Self, Text
from unicodedata import numeric
import flet as ft
from _stock import Producto, maestra_productos

#label_cod=ft.TextField(hint_text="Ingrese Codigo", width=300)
#label_can=ft.TextField(hint_text="Ingrese Cantidad", width=300,keyboard_type=ft.KeyboardType.NUMBER)
venta_actual = []


#def item_capture():
#        return ft.Column([
#            
#        ft.Row([label_cod,
#                     label_can, 
#            ft.ElevatedButton("Agregar",icon=ft.icons.TRANSIT_ENTEREXIT,width=230,height=58,on_click=agregar_venta_actual,style=ft.ButtonStyle(
#                shape=ft.RoundedRectangleBorder(radius=8),
#            ))])
#    
#        ]   
#        )
        
#def agregar_producto(e):
#        lab_Q=int(label_can.value)
#        cod=Producto(1, 10, "Coca Cola", 1000)
#        cod.vender_stock(lab_Q)
#        print(Producto.consultar_stock)

def agregar_venta_actual(label_cod,label_can):
    codigo=int(label_cod)
    cantidad=int(label_can)
    
    venta_actual = []
    print(codigo, cantidad)
    print(maestra_productos)
    #Buscar el producto en la lista maestra_productos
    for producto in maestra_productos:
        if producto['codigo'] == codigo:
            nombre = producto['nombre']
            precio_un = producto['precio_un']

            # Calcular el valor total
            valor_total = precio_un * cantidad

            # Crear un diccionario con la información y agregarlo a venta_actual
            venta_actual.append({
                'nuevo_codigo': codigo,
                'cantidad': cantidad,
                'nombre': nombre,
                'precio_un': precio_un,
                'valor_total': valor_total
            })

            # Puedes detener la búsqueda si ya encontraste el producto
            break
    print(venta_actual)
    return venta_actual


