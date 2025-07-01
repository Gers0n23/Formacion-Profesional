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
historico_ventas = []
rows = []
cells = []
trow = []


label_cod=ft.TextField(hint_text="Ingrese Codigo", width=300)
label_can=ft.TextField(hint_text="Ingrese Cantidad", width=300,keyboard_type=ft.KeyboardType.NUMBER)
subtotal=ft.Text(f"Subtotal: $ {int(0)}", width=180, text_align=ft.TextAlign.CENTER)
iva=ft.Text(f"Iva: $ {int(0)}", width=180, text_align=ft.TextAlign.CENTER)
total=ft.Text(f"Total: $ {int(0)}", width=180, text_align=ft.TextAlign.CENTER)


class App(ft.UserControl):
    def build(self):
        self.reset()
        self.result = ft.Text(value="0", color=ft.colors.WHITE, size=20)
        but_width = 133  # Define the button width
        
        global label_cod
        global label_can
        global rows
        global cells
        global subtotal
        global iva
        global total
          
        # application's root control (i.e. "view") containing all other controls
        return ft.Container(
            ft.Column([
                ft.Row(
                    [
                        ft.Column([
                            ft.Row([
                                ft.ElevatedButton(text="Archivo", width=but_width, style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                )),
                                ft.ElevatedButton(text="Diario", width=but_width, style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                )),
                                ft.ElevatedButton(text="Mes", width=but_width, style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                )),
                                ft.ElevatedButton(text="Compras", width=but_width, style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                )),
                                ft.ElevatedButton(text="Ventas", width=but_width, style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                )),
                                ft.ElevatedButton(text="Inventario", width=but_width, style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                )),
                            ])
                        ])
                    ]
                ),
                
                ft.Column([
                            ft.Row([label_cod,label_can, 
                            ft.ElevatedButton("Agregar",icon=ft.icons.TRANSIT_ENTEREXIT,width=230,height=58,on_click=self.agregar_venta_actual,style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=8),
                            ))])]),
                
                ft.Row(
                    [
                        ft.Column([
                            ft.ElevatedButton(text="7", width=80, height=80, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),)),
                            ft.ElevatedButton(text="4", width=80, height=80, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),)),
                            ft.ElevatedButton(text="1", width=80, height=80, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),)),
                            ft.ElevatedButton(text="#", width=80, height=80, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),)),
                        ]),
                        
                        ft.Column([
                            ft.ElevatedButton(text="8", width=80, height=80, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),)),
                            ft.ElevatedButton(text="5", width=80, height=80, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),)),
                            ft.ElevatedButton(text="2", width=80, height=80, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),)),
                            ft.ElevatedButton(text="0", width=80, height=80, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),)),
                        ]),
                        
                        ft.Column([
                            ft.ElevatedButton(text="9", width=80, height=80, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),)),
                            ft.ElevatedButton(text="6", width=80, height=80, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),)),
                            ft.ElevatedButton(text="3", width=80, height=80, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),)),
                            ft.ElevatedButton(text=".", width=80, height=80, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),)),
                        ]),
                        
                        ft.Column([
                            ft.DataTable(
                                columns=[
                                ft.DataColumn(ft.Text("SKU",height=20)),
                                ft.DataColumn(ft.Text("Producto",height=20)),
                                ft.DataColumn(ft.Text("Cantidad",height=20), numeric=True),
                                ft.DataColumn(ft.Text("Precio",height=20), numeric=True),
                                ft.DataColumn(ft.Text("$ Total",height=20), numeric=True),
                                ],
                                rows=rows
                                ),
                            ft.Row([
                                    subtotal,
                                    iva,
                                    total
                            ]),
                            
                            ft.Row([
                                ft.ElevatedButton(text="Generar Venta",on_click=self.generar_venta,icon=ft.icons.TRANSIT_ENTEREXIT,style=ft.ButtonStyle(
                                                         shape=ft.RoundedRectangleBorder(radius=8)),width=580,height=80),
                                #bgcolor=ft.colors.GREY_200,width=580,height=80
                            ])
                                #bgcolor=ft.colors.AMBER_100,
                                #width=580,
                                #padding=5,
                                #height=280
                        ])
                        ]
                    )
            ])
        )

    def agregar_venta_actual(self, e):
        global subtotal,iva,total
        
        codigo = int(label_cod.value)
        cantidad = int(label_can.value)

        for producto in maestra_productos:
            if producto['codigo'] == codigo:
                nombre = producto['nombre']
                precio_un = producto['precio_un']
                
                valor_total = precio_un * cantidad

        # Create a dictionary with the information and add it to venta_actual
        venta_actual.append({
            'nuevo_codigo': codigo,
            'cantidad': cantidad,
            'nombre': nombre,
            'precio_un': precio_un,
            'valor_total': valor_total
        })

        label_cod.value = ""
        label_can.value = ""
        current_subtotal=0
        current_subtotal += valor_total
        current_iva=current_subtotal*0.19
        current_total=current_subtotal+current_iva
    
        
        subtotal.value=f"Subtotal: $ {int(current_subtotal)}"
        iva.value= f"Iva: $ {int(current_iva)}"  
        total.value=f"Iva: $ {int(current_total)}"
        
        # Reiniciar la lista cells en cada iteración
        cells = [
            ft.DataCell(ft.Text(codigo)),
            ft.DataCell(ft.Text(nombre)),
            ft.DataCell(ft.Text(cantidad)),
            ft.DataCell(ft.Text(precio_un)),
            ft.DataCell(ft.Text(valor_total))
        ]
        rows.append(ft.DataRow(cells=cells))
        print(rows)
        print(cells)
        self.update()
        
    def generar_venta(self,e):
        global venta_actual
        
        for producto in venta_actual:
            codigo = producto['nuevo_codigo']
            nombre = producto['nombre']
            precio_un = producto['precio_un']
            valor_total = producto['valor_total']
            cantidad = producto['cantidad']
            
            historico_ventas.append({
                'nuevo_codigo': codigo,
                'cantidad': cantidad,
                'nombre': nombre,
                'precio_un': precio_un,
                'valor_total': valor_total
            })
            #print(historico_ventas)
        
        rows.clear()
        cells.clear()
        venta_actual.clear()
        
        subtotal.value=f"Subtotal: $ {int(0)}"
        iva.value= f"Iva: $ {int(0)}"  
        total.value=f"Iva: $ {int(0)}"
    
        print(rows)
        print(cells)
        print(venta_actual)
        print(historico_ventas)
        self.update()

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True


def main(page: ft.Page):
    page.window_height=650
    page.window_width=890
    page.title="Sistema de Ventas"
    
    page.appbar = ft.AppBar(
            leading_width=0,
            title=ft.Text("Sistema de Ventas"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
               ])

    app = App()
    
    page.add(app)
    

ft.app(target=main)