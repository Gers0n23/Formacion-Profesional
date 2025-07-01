import flet as ft

class Boleta(ft.UserControl):
    
    def build(self):
        but_width = 133  # Define the button width
        
        return ft.Container(
              ft.Column([
                  ft.Row([ft.Text("Boleta", width=200, text_align=ft.TextAlign.CENTER)]),]),
        )
    
    
def main(page: ft.Page):
    
    page.window_height=500
    page.window_width=400
    page.title="Boleta"
    
    boleta=Boleta()
    page.add(boleta)
    
ft.app(target=main)