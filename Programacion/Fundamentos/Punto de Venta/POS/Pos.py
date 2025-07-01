import flet as ft

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

venta_actual = []
rows = []
cells = []

label_cod=ft.TextField(hint_text="Ingrese Codigo", width=300)
label_can=ft.TextField(hint_text="Ingrese Cantidad", width=300,keyboard_type=ft.KeyboardType.NUMBER)

def current_sale():
    
    # Define rows here
    return ft.Container(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("SKU",height=20)),
                ft.DataColumn(ft.Text("Producto",height=20)),
                ft.DataColumn(ft.Text("Cantidad",height=20), numeric=True),
                ft.DataColumn(ft.Text("Precio",height=20), numeric=True),
                ft.DataColumn(ft.Text("$ Total",height=20), numeric=True),
            ],
            rows=rows  # Use rows here 
        ),
        bgcolor=ft.colors.GREY_200,
        width=580,
        padding=5,
        height=280
        )
    
def agregar_venta_actual(e):
    global venta_actual
    codigo = int(label_cod.value)
    cantidad = int(label_can.value)
    # Buscar el producto en la lista maestra_productos
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
            label_cod.value = ""
            label_can.value = ""
            # Reiniciar la lista cells en cada iteración
            cells = [
                ft.DataCell(ft.Text(codigo)),
                ft.DataCell(ft.Text(nombre)),
                ft.DataCell(ft.Text(cantidad)),
                ft.DataCell(ft.Text(precio_un)),
                ft.DataCell(ft.Text(valor_total))
            ]
            rows.append(ft.DataRow(cells=cells))
            current_sale()
    
            page.update()
            print(venta_actual)
            subtotal_vta = sum(producto['valor_total'] for producto in venta_actual)
            subtotal_sale(1,2,3)
    print(subtotal_vta)


def main(page: ft.Page):
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
    
    label_cod=ft.TextField(hint_text="Ingrese Codigo", width=300)
    label_can=ft.TextField(hint_text="Ingrese Cantidad", width=300,keyboard_type=ft.KeyboardType.NUMBER)
    
    
    def item_capture():
        return ft.Column([
            
        ft.Row([label_cod,
                     label_can, 
            ft.ElevatedButton("Agregar",icon=ft.icons.TRANSIT_ENTEREXIT,width=230,height=58,on_click=agregar_venta_actual,style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
            ))])
    
        ]   
        )
    
    def full_sales_panel():
        return ft.Column(
                    [   
                        current_sale(),
                        subtotal_sale(),
                        button_1(),
                    ]
                    )


    def button_1():
        return ft.Container(
                            ft.ElevatedButton(text="Generar Venta",icon=ft.icons.TRANSIT_ENTEREXIT,style=ft.ButtonStyle(
                                                         shape=ft.RoundedRectangleBorder(radius=8))),
                            bgcolor=ft.colors.GREY_200,width=580,height=80
                            )
    
    def subtotal_sale():
        subtotal = sum(producto['valor_total'] for producto in venta_actual)
        iva = int(subtotal * 0.19)
        total = int(subtotal + iva)   
    # Calcular el subtotal sumando los valores totales de los productos en venta_actual
        print(subtotal)
        print(iva)
        print(total)
        page.update()
        return ft.Row([  
            ft.Text(f"Subtotal: $ {subtotal}", width=180, text_align=ft.TextAlign.CENTER),
            ft.Text(f"IVA: $ {iva}", width=200, text_align=ft.TextAlign.CENTER),
            ft.Text(f"Total: $ {total}", width=200, text_align=ft.TextAlign.CENTER)]
                      , alignment=ft.MainAxisAlignment.CENTER)
    

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

if __name__ == "__main__":   
    ft.app(target=main)