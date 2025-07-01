import flet as ft

def Teclado_columna_1():
    
        return ft.Column(
            [
                ft.ElevatedButton(text="7", width=80, height=80, style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
                    )),
                ft.ElevatedButton(text="4", width=80, height=80, style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                    )),
                ft.ElevatedButton(text="1", width=80, height=80, style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                    )),
                ft.ElevatedButton(text="#", width=80, height=80, style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                    )),
            ]
        )       
def Teclado_columna_2():
        return ft.Column(
            [
                ft.ElevatedButton(text="8", width=80, height=80, style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
                    )),
                ft.ElevatedButton(text="5", width=80, height=80, style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                    )),
                ft.ElevatedButton(text="2", width=80, height=80, style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                    )),
                ft.ElevatedButton(text="0", width=80, height=80, style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                    )),
            ]
        )
def Teclado_columna_3():
        return ft.Column(
            [   
                ft.ElevatedButton(text="9", width=80, height=80, style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
                    )),
                ft.ElevatedButton(text="6", width=80, height=80, style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                    )),
                ft.ElevatedButton(text="3", width=80, height=80, style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                    )),
                ft.ElevatedButton(text=".", width=80, height=80, style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                    )),
            ]
        )
 
def full_keyboard():
        return ft.Column(
            [
                ft.Row([Teclado_columna_1(),
                        Teclado_columna_2(),
                        Teclado_columna_3()
                        ]
                       )  
            ]
        )