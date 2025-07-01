'''import tkinter as tk
from tkinter import messagebox


# Crear la ventana principal
root = tk.Tk()

# Crear la lista de vehículos
vehiculos = []

# Definir la función que se llama al presionar el botón
def configurar_vehiculo():
    # Crear una ventana secundaria
    win = tk.Toplevel()
    # Crear un diccionario para almacenar los datos del vehículo
    auto = {}
    # Crear las etiquetas y los campos de entrada para cada dato
    tk.Label(win, text="Patente vehículo:").grid(row=0, column=0)
    patente = tk.Entry(win)
    patente.grid(row=0, column=1)
    tk.Label(win, text="Marca vehículo:").grid(row=1, column=0)
    marca = tk.Entry(win)
    marca.grid(row=1, column=1)
    tk.Label(win, text="Modelo vehículo:").grid(row=2, column=0)
    modelo = tk.Entry(win)
    modelo.grid(row=2, column=1)
    tk.Label(win, text="Año vehículo:").grid(row=3, column=0)
    año = tk.Entry(win)
    año.grid(row=3, column=1)
    tk.Label(win, text="Capacidad pasajeros:").grid(row=4, column=0)
    capacidad = tk.Entry(win)
    capacidad.grid(row=4, column=1)

    # Definir la función que se llama al presionar el botón "Guardar"
    def guardar():
        # Asignar los valores de los campos de entrada al diccionario
        auto['patente'] = patente.get()
        auto['id'] = auto['patente'] + '1'
        auto['marca'] = marca.get()
        auto['modelo'] = modelo.get()
        auto['año'] = año.get()
        auto['capacidad pasajeros'] = capacidad.get()
        # Agregar el diccionario a la lista de vehículos
        vehiculos.append(auto)
        # Mostrar un mensaje de confirmación
        tk.messagebox.showinfo("Información", "Vehículo agregado")
        # Cerrar la ventana secundaria
        win.destroy()

    # Crear el botón "Guardar" y asignarle la función anterior
    tk.Button(win, text="Guardar", command=guardar).grid(row=5, column=0, columnspan=2)

# Crear el menú principal
menubar = tk.Menu(root)

# Crear el menú "Acción" y asignarle la función configurar_vehiculo
menu_accion = tk.Menu(menubar, tearoff=0)
menu_accion.add_command(label="Configurar vehículo", command=configurar_vehiculo)

# Agregar el menú "Acción" al menú principal
menubar.add_cascade(label="Acción", menu=menu_accion)

# Configurar la ventana principal para usar el menú principal
root.config(menu=menubar)

# Iniciar el bucle principal de la ventana
root.mainloop()'''

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()

# Crear la lista de vehículos
vehiculos = [
    {'patente': 'ABC123', 'id': 'ABC1231', 'marca': 'Toyota', 'modelo': 'Corolla', 'año': '2010', 'capacidad pasajeros': '5'},
    {'patente': 'DEF456', 'id': 'DEF4561', 'marca': 'Nissan', 'modelo': 'Versa', 'año': '2015', 'capacidad pasajeros': '4'},
    {'patente': 'GHI789', 'id': 'GHI7891', 'marca': 'Ford', 'modelo': 'Fiesta', 'año': '2020', 'capacidad pasajeros': '5'}
]

# Definir las columnas del Treeview
columns = ('Patente', 'Marca', 'Modelo', 'Año', 'Capacidad')

# Crear el Treeview y asignarle las columnas
tree = ttk.Treeview(root, columns=columns, show='headings')

# Configurar los encabezados de las columnas
for col in columns:
    tree.heading(col, text=col)

# Insertar los datos de la lista de vehículos en el Treeview
for i, auto in enumerate(vehiculos):
    tree.insert('', i, values=(auto['patente'], auto['marca'], auto['modelo'], auto['año'], auto['capacidad pasajeros']))

# Empaquetar el Treeview
tree.pack()

# Definir la función que se llama al presionar el botón "Modificar"
def modificar():
    # Obtener el ítem seleccionado en el Treeview
    item = tree.selection()[0]
    # Obtener los valores del ítem seleccionado
    values = tree.item(item, 'values')
    # Obtener la patente del ítem seleccionado
    patauto = values[0]
    # Recorrer la lista de vehículos
    for auto in vehiculos:
        # Si se encuentra el vehículo con la patente seleccionada
        if auto['patente'] == patauto:
            # Crear una ventana secundaria
            win = tk.Toplevel()
            # Crear las etiquetas y los campos de entrada para cada dato
            tk.Label(win, text="Patente vehículo:").grid(row=0, column=0)
            patente = tk.Entry(win)
            patente.grid(row=0, column=1)
            patente.insert(0, auto['patente']) # Insertar el valor actual
            patente.config(state='disabled') # Deshabilitar el campo de entrada
            tk.Label(win, text="Marca vehículo:").grid(row=1, column=0)
            marca = tk.Entry(win)
            marca.grid(row=1, column=1)
            marca.insert(0, auto['marca']) # Insertar el valor actual
            tk.Label(win, text="Modelo vehículo:").grid(row=2, column=0)
            modelo = tk.Entry(win)
            modelo.grid(row=2, column=1)
            modelo.insert(0, auto['modelo']) # Insertar el valor actual
            tk.Label(win, text="Año vehículo:").grid(row=3, column=0)
            año = tk.Entry(win)
            año.grid(row=3, column=1)
            año.insert(0, auto['año']) # Insertar el valor actual
            tk.Label(win, text="Capacidad pasajeros:").grid(row=4, column=0)
            capacidad = tk.Entry(win)
            capacidad.grid(row=4, column=1)
            capacidad.insert(0, auto['capacidad pasajeros']) # Insertar el valor actual

            # Definir la función que se llama al presionar el botón "Actualizar"
            def actualizar():
                # Asignar los valores de los campos de entrada al diccionario
                auto['marca'] = marca.get()
                auto['modelo'] = modelo.get()
                auto['año'] = año.get()
                auto['capacidad pasajeros'] = capacidad.get()
                # Actualizar los valores del ítem seleccionado en el Treeview
                tree.item(item, values=(auto['patente'], auto['marca'], auto['modelo'], auto['año'], auto['capacidad pasajeros']))
                # Mostrar un mensaje de confirmación
                tk.messagebox.showinfo("Información", "Vehículo modificado")
                # Cerrar la ventana secundaria
                win.destroy()

            # Crear el botón "Actualizar" y asignarle la función anterior
            tk.Button(win, text="Actualizar", command=actualizar).grid(row=5, column=0, columnspan=2)
            return
    # Si no se encuentra el vehículo con la patente seleccionada
    tk.messagebox.showerror("Error", "No se encontró el registro")

# Definir la función que se llama al presionar el botón "Eliminar"
def eliminar():
    # Obtener el ítem seleccionado en el Treeview
    item = tree.selection()[0]
    # Obtener los valores del ítem seleccionado
    values = tree.item(item, 'values')
    # Obtener la patente del ítem seleccionado
    patauto = values[0]
    # Recorrer la lista de vehículos
    for auto in vehiculos:
        # Si se encuentra el vehículo con la patente seleccionada
        if auto['patente'] == patauto:
            # Mostrar un mensaje de confirmación
            answer = tk.messagebox.askyesno("Confirmación", "¿Está seguro de eliminar el vehículo?")
            # Si el usuario confirma la eliminación
            if answer:
                # Eliminar el diccionario de la lista de vehículos
                vehiculos.remove(auto)
                # Eliminar el ítem del Treeview
                tree.delete(item)
                # Mostrar un mensaje de confirmación
                tk.messagebox.showinfo("Información", "Vehículo eliminado")
            return
    # Si no se encuentra el vehículo con la patente seleccionada
    tk.messagebox.showerror("Error", "No se encontró el registro")

# Crear el botón "Modificar" y asignarle la función anterior
tk.Button(root, text="Modificar", command=modificar).pack()

# Crear el botón "Eliminar" y asignarle la función anterior
tk.Button(root, text="Eliminar", command=eliminar).pack()

# Iniciar el bucle principal de la ventana
root.mainloop()