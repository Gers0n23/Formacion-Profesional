import flet as ft
from header import buttons_
from keyboard_ import full_keyboard
from table import full_sales_panel
from forms import agregar_venta_actual,venta_actual


def main(page: ft.Page):
    page.update()
    page.window_height=650
    page.window_width=890

    page.appbar = ft.AppBar(
        leading_width=0,
        title=ft.Text("Sistema de Ventas"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
           ]
        
    )
    
    label_cod=ft.TextField(hint_text="Ingrese Codigo", width=300)
    label_can=ft.TextField(hint_text="Ingrese Cantidad", width=300,keyboard_type=ft.KeyboardType.NUMBER)
    
    def item_capture():
        return ft.Column([
            
        ft.Row([label_cod,
                     label_can, 
            ft.ElevatedButton("Agregar",icon=ft.icons.TRANSIT_ENTEREXIT,width=230,height=58,on_click=agregar_venta_actual(1,2),style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
            ))])
    
        ]   
        )
    page.update()
       
    page.add(
        #aqui se agregan todos los elementos de la pagina
        
        buttons_(), #Botones de cabecera
        item_capture(), #Formulario de captura de productos
        
        ft.Row(
            [
                full_keyboard(), #Teclado numerico
                full_sales_panel(), #Resumen de la venta
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.START,
        )
    )

    
ft.app(target=main)