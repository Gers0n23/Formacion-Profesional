
from Medios import Automovil

def menu_ventana():
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.title("Menu con Botones")

    frame = tk.Frame(root)
    frame.pack()

    boton1 = tk.Button(frame, text="Agregar Vehículo", command=configurar_vehiculo, bd=5, bg="blue", fg="white", font=("Arial", 12))
    boton2 = tk.Button(frame, text="Mostrar vehiculos", command=visualizar, bd=5, bg="green", fg="white", font=("Arial", 12))
    boton3 = tk.Button(frame, text="Modificar vehiculos", command=visualizar, bd=5, bg="yellow", fg="black", font=("Arial", 12))
    boton4 = tk.Button(frame, text="Eliminar Vehículo", command=visualizar, bd=5, bg="red", fg="white", font=("Arial", 12))
    boton5 = tk.Button(frame, text="Jugar", command=jugar, bd=5, bg="orange", fg="white", font=("Arial", 12))

    boton1.grid(row=0, column=0, padx=10, pady=10)
    boton2.grid(row=0, column=1, padx=10, pady=10)
    boton3.grid(row=1, column=0, padx=10, pady=10)
    boton4.grid(row=1, column=1, padx=10, pady=10)
    boton5.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

vehiculos=[]

auto1 = Automovil("CTBZ31", "CTBZ311", "CHEVROLET", "SPARK","2015","4","75000")
auto2 = Automovil("HHZI32", "HHZI321", "NISSAN", "SENTRA","2018","4","100000")
auto3 = Automovil("JJVP05", "JJVP051", "HYUNDAY", "ACCENT","2013","4","60000")

vehiculos.append(auto1)
vehiculos.append(auto2) 
vehiculos.append(auto3)

# A partir de aquí estan todas las funciones de las opciones de los menu

def configurar_vehiculo():
    import tkinter as tk
    
    
    win = tk.Toplevel()
    auto = {}
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

    def guardar():
        auto['patente'] = patente.get()
        auto['id'] = auto['patente'] + '1'
        auto['marca'] = marca.get()
        auto['modelo'] = modelo.get()
        auto['año'] = año.get()
        auto['capacidad pasajeros'] = capacidad.get()
        vehiculos.append(auto)
        tk.messagebox.showinfo("Información", "Vehículo agregado")
        win.destroy()

    tk.Button(win, text="Guardar", command=guardar).grid(row=5, column=0, columnspan=2)

def visualizar():
    columns = ('Patente', 'Marca', 'Modelo', 'Año', 'Capacidad')

    import tkinter as tk
    from tkinter import ttk
    from tkinter import messagebox
    root = tk.Tk()

    # Crear el Treeview y asignarle las columnas
    tree = ttk.Treeview(root, columns=columns, show='headings')

    # Configurar los encabezados de las columnas
    for col in columns:
        tree.heading(col, text=col)

    # Insertar los datos de la lista de vehículos en el Treeview
    for i, auto in enumerate(vehiculos):
        tree.insert('', i, values=(auto.patente, auto.marca, auto.modelo, auto.año, auto.capacidad_pasajeros))

    # Empaquetar el Treeview
    tree.pack()

    # Definir la función que se llama al presionar el botón "Modificar"
    def modificar():
        import tkinter as tk

        # Obtener el ítem seleccionado en el Treeview
        item = tree.selection()[0]
        # Obtener los valores del ítem seleccionado
        values = tree.item(item, 'values')
        # Obtener la patente del ítem seleccionado
        patauto = values[0]
        # Recorrer la lista de vehículos
        for auto in vehiculos:
            # Si se encuentra el vehículo con la patente seleccionada
            if auto.patente == patauto:
                # Crear una ventana secundaria
                win = tk.Toplevel()
                # Crear las etiquetas y los campos de entrada para cada dato
                tk.Label(win, text="Patente vehículo:").grid(row=0, column=0)
                patente = tk.Entry(win)
                patente.grid(row=0, column=1)
                patente.insert(0, auto.patente) # Insertar el valor actual
                patente.config(state='disabled') # Deshabilitar el campo de entrada
                tk.Label(win, text="Marca vehículo:").grid(row=1, column=0)
                marca = tk.Entry(win)
                marca.grid(row=1, column=1)
                marca.insert(0, auto.marca) # Insertar el valor actual
                tk.Label(win, text="Modelo vehículo:").grid(row=2, column=0)
                modelo = tk.Entry(win)
                modelo.grid(row=2, column=1)
                modelo.insert(0, auto.modelo) # Insertar el valor actual
                tk.Label(win, text="Año vehículo:").grid(row=3, column=0)
                año = tk.Entry(win)
                año.grid(row=3, column=1)
                año.insert(0, auto.año) # Insertar el valor actual
                tk.Label(win, text="Capacidad pasajeros:").grid(row=4, column=0)
                capacidad = tk.Entry(win)
                capacidad.grid(row=4, column=1)
                capacidad.insert(0, auto.capacidad_pasajeros) # Insertar el valor actual

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

        import tkinter as tk
        
        # Obtener el ítem seleccionado en el Treeview
        item = tree.selection()[0]
        # Obtener los valores del ítem seleccionado
        values = tree.item(item, 'values')
        # Obtener la patente del ítem seleccionado
        patauto = values[0]
        # Recorrer la lista de vehículos
        for auto in vehiculos:
            # Si se encuentra el vehículo con la patente seleccionada
            if auto.patente == patauto:
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

def jugar():
    from Game import jugar
    jugar()
    