from calendar import c
from pickle import APPEND
from forms import venta_actual
from turtle import bgcolor
import flet as ft



def full_sales_panel():
    return ft.Column(
                [
                    ft.Container(ft.Text("Productos"),bgcolor=ft.colors.GREY_200,width=580,padding=5),
                    current_sale(),
                    total_sale(),
                    button_1()
    
                ]
                )

def button_1():
    return ft.Container(
                        ft.ElevatedButton(text="Generar Venta",icon=ft.icons.TRANSIT_ENTEREXIT,style=ft.ButtonStyle(
                                                     shape=ft.RoundedRectangleBorder(radius=8))),
                        bgcolor=ft.colors.GREY_200,width=580,height=80
                        )

def total_sale():
    
    subtotal = sum(producto['valor_total'] for producto in venta_actual)
    iva = subtotal * 0.19
    total = subtotal + iva
    
    return ft.Row([  
                      ft.Text(f"Subtotal: $ {subtotal}"),
                      ft.Text(f"IVA: $ {iva}"),
                      ft.Text(f"Total: $ {total}")
                    ],alignment=ft.MainAxisAlignment.CENTER
                  )

def current_sale():
    
    rows = []  # Define rows here
    
    for producto in venta_actual:
        cells = []

        cells.append(ft.DataCell(ft.Text(producto['nuevo_codigo'])))
        cells.append(ft.DataCell(ft.Text(producto['nombre'])))
        cells.append(ft.DataCell(ft.Text(producto['cantidad'])))
        cells.append(ft.DataCell(ft.Text(producto['precio_un'])))
        cells.append(ft.DataCell(ft.Text(producto['valor_total'])))

        rows.append(ft.DataRow(cells=cells))  # Remove comma here

    return ft.Container(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("SKU")),
                ft.DataColumn(ft.Text("Producto")),
                ft.DataColumn(ft.Text("Cantidad"), numeric=True),
                ft.DataColumn(ft.Text("Precio"), numeric=True),
                ft.DataColumn(ft.Text("$ Total"), numeric=True),
            ],
            rows=rows  # Use rows here
        ),
        bgcolor=ft.colors.GREY_200,
        width=580,
        padding=5,
        height=200
    )
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
