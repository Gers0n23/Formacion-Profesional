import flet as ft

but_width=133

def buttons_():
        return ft.Column([
            
            ft.Row([ft.ElevatedButton(text="Archivo",width=but_width, style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
            )),
            ft.ElevatedButton(text="Diario",width=but_width, style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
            )),
            ft.ElevatedButton(text="Mes",width=but_width, style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
            )),
            ft.ElevatedButton(text="Compras", width=but_width,style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
            )),
            ft.ElevatedButton(text="Ventas", width=but_width,style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
            )),
            ft.ElevatedButton(text="Inventario", width=but_width,style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
            )),])
        ]   )