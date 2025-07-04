personas=[] 
auto5=[]
costo_mt = 602
rendimiento_vehiculo=14.3
valor_combustible=1250
vacio= "pendiente"
Estanque_Combustible=70

import math
from math import sqrt

def mostrar_menu(nombre, opciones):  
    print(f'# {nombre}. Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')
def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(nombre, opciones, opcion_salida):  
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(nombre, opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def menu_inicio():
    opciones = {
        '1': ('Iniciar Dia >', iniciar)
    }

    generar_menu('Menú inicio', opciones, '1') 
def menu_principal():
    opciones = {
        '1': ('Vehiculos', menu_vehiculo),
        '2': ('Viajes', menu_viajes),
        '3': ('Resumen', menu_resumen),
        '4': ('Finalizar Dia', salir)
    }

    generar_menu('Menu Principal', opciones, '4') 

def menu_vehiculo():
    opciones = {
        '1': ('Agregar Vehículo', configurar_vehiculo),
        '2': ('Mostrar vehiculos', mostrar_vehiculos),
        '3': ('Modificar vehiculos', modifica_vehiculo1),
        '4': ('Eliminar Vehículo', elimina_auto),
        '5': ('Agregar Combustible', comprar_combustible),
        '6': ('Volver al menú principal', menu_principal)
    }

    generar_menu('Configuración Vehiculo', opciones, '6') 

def menu_viajes():
    opciones = {
        '1': ('Agregar nuevo viaje', nuevo_viaje),
        '2': ('Mostrar viajes', mostrar_viajes),
        '3': ('Buscar un viaje',busca_viaje1),
        '4': ('Modificar un Viaje', modifica_viaje1),
        '5': ('Eliminar un viaje', elimina_viaje1),
        '6': ('Ultimo Viaje', obtener_ultimo_destino),
        '7': ('Volver al menú principal', menu_principal)
    }

    generar_menu('Configuración Viajes', opciones, '7')

def menu_resumen():
    opciones = {
        '1': ('Detalle viajes', mostrar_viajes),
        '2': ('Resumen diario', resumen_viajes),
        '3': ('Volver al menú principal', menu_principal)
    }

    generar_menu('Resumen Diario', opciones, '3') 
    
# A partir de aquí estan todas las funciones de las opciones de los menu

def funcion1():
    print('Falta Construir')

def agregar_punto_inicio(tipo): 
    georeferencia_i = {} 
    georeferencia_i['latitud'] = float(input(f"Ingrese latitud {tipo}:")) 
    georeferencia_i['longitud'] = float(input(f"Ingrese longitud {tipo}:")) 
    return georeferencia_i

def agregar_georeferencia(tipo):
    latitud = float(input(f"Ingrese latitud {tipo}:"))
    longitud = float(input(f"Ingrese longitud {tipo}:"))
    return (latitud, longitud)

def agregar_combustible(tipo):
    global Estanque_Combustible
    Estanque_Combustible = float(input(f"Agregar combustible {tipo}:"))
    return (Estanque_Combustible)

def iniciar():
    persona = {} 
    Estanque_Combustible=agregar_combustible('(% de estanque)')/100*70
    print("Combustible disponible ",Estanque_Combustible," lts")
    persona['nombre'] = "Viaje Inicio"
    persona['origen'] = agregar_georeferencia('origen')
    persona['destino'] = persona['origen']
    x1, y1 = persona['origen']
    x2, y2 = persona['destino']
    distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)*111
    costo_viaje = distancia * costo_mt
    gasto_combustible = distancia / rendimiento_vehiculo*valor_combustible 
    persona['distancia'] = distancia
    persona['costo_viaje'] = f"${int(0):,}" 
    persona['gasto_combustible'] = f"${int(gasto_combustible):,}" 
    personas.append(persona) 
    auto = {"patente":"BKN1234","marca":"Hyundai","modelo":"Accent","año":2020,"capacidad pasajeros":4,"rendimiento":rendimiento_vehiculo}
    auto5.append(auto)
    for auto in auto5:
        print("auto elegido =",auto)
    menu_principal()
    
def obtener_ultimo_destino():
    if personas:
        ultimo_registro = personas[-1]
        print(ultimo_registro)
        return ultimo_registro['destino']
    else:
        return None

def nuevo_viaje():
    persona = {} 
    persona['nombre'] = input("Ingrese el nombre de la persona: ") 
    persona['origen'] = agregar_georeferencia('origen') 
    persona['destino'] = agregar_georeferencia('destino') 
    x1, y1 = persona['origen']
    x2, y2 = persona['destino']
    distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)*111
    costo_viaje = distancia * costo_mt 
    gasto_combustible = distancia / rendimiento_vehiculo*valor_combustible 
    persona['distancia'] = distancia
    persona['costo_viaje'] = f"${int(costo_viaje):,}" 
    
    persona['gasto_combustible'] = f"${int(gasto_combustible):,}" 
    personas.append(persona) 

    traslado_entre_viajes()

def traslado_entre_viajes():
    if len(personas) >= 2: 
        penultimo = personas[-2] 
        ultimo = personas[-1] 
        x1, y1 = penultimo['destino'] 
        x2, y2 = ultimo['origen'] 
        distancia_last = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)*111 
        
        persona = {} 
        persona['nombre'] = "Traslado entre viajes"
        persona['origen'] = penultimo['destino']
        persona['destino'] = ultimo['origen']
        costo_viaje = distancia_last * costo_mt 
        gasto_combustible_last = distancia_last / rendimiento_vehiculo*valor_combustible 
        persona['distancia'] = distancia_last
        persona['costo_viaje'] = f"${int(0):,}" 
    
        persona['gasto_combustible'] = f"${int(gasto_combustible_last):,}" 
        personas.append(persona)
        
        return distancia_last 
        
    else:
        return None 

def mostrar_viajes(): 
    for persona in personas:
        print(persona)

def busca_viaje1():
    nombre=nombre = input("Ingrese el nombre a buscar: ")
    buscar_viaje(nombre)
def buscar_viaje(nombre):
    for persona in personas:
        if persona['nombre'] == nombre:
            print(persona)

def modifica_viaje1():
    nombre=nombre = input("Ingrese el nombre a buscar: ")
    modificar_viaje(nombre)
def modificar_viaje(nombre):
    for persona in personas:
        if persona['nombre'] == nombre:
            nuevo_origen = agregar_georeferencia('origen')
            nuevo_destino = agregar_georeferencia('destino')
            persona['origen'] = nuevo_origen
            persona['destino'] = nuevo_destino
            print("Registro actualizado.")
            return
    print("No se encontró el registro.")

def elimina_viaje1():
    nombre=nombre = input("Ingrese el nombre que quiere eliminar (esto no se puede deshacer): ")
    eliminar_registro(nombre)
def eliminar_registro(nombre):
    for i, persona in enumerate(personas):
        if persona['nombre'] == nombre:
            del personas[i]
            print("Registro eliminado.")
            return
    print("No se encontró el registro.")

def resumen_viajes():
    global Estanque_Combustible
    global rendimiento_vehiculo
    
    suma_distancias = sum(p['distancia'] for p in personas if p['nombre'] == 'Traslado entre viajes')

    viajes_sin_pago = sum (1 for p in personas if p['nombre'] == 'Traslado entre viajes')
    
    total_km = sum([int(persona['distancia']) for persona in personas]) 
    total_costo = sum([int(persona['costo_viaje'].replace('$','').replace(',','')) for persona in personas]) # Suma de los costos de todos los viajes
    gasto_combustible_total = sum(round(float(persona['gasto_combustible'].replace('$','').replace(',','')), 0) for persona in personas)
    impuestos= total_costo*0.19
    
    print("# Metricas")
    print(f"Número de viajes realizados: {len(personas)-int(viajes_sin_pago)-1}") # Conteo del número total de viajes
    print(f"Traslados sin ganancias: {int(suma_distancias)} KM")
    print(f"Distancia total recorrida: {total_km} KM")
    print(f"Combustible restante: {int((Estanque_Combustible/100*70)-(total_km/rendimiento_vehiculo))} lts")
    print("")
    print("# Ganancias")
    print(f"Monto total recaudado: ${total_costo:,}")
    print(f"Gasto en combustible: ${int(gasto_combustible_total):,}")
    print(f"Impuestos: ${int(impuestos):,}")
    print(f"Ganancia final del Conductor: ${int(total_costo -gasto_combustible_total-impuestos):,} Neto") 
     
    return total_costo
def resumen_gasto_combustible():
    gasto_combustible_total = sum(round(float(persona['gasto_combustible'].replace('$','').replace(',','')), 0) for persona in personas)
    
    print(gasto_combustible_total)
    return gasto_combustible_total

def configurar_vehiculo():
    auto = {} 
    auto['patente'] = input("patente vehiculo :")
    auto['marca'] = input("marca vehiculo :")
    auto['modelo'] = input("modelo vehiculo :")
    auto['año'] = input("Año vehiculo :")
    auto['capacidad pasajeros'] = input("capacidad pasajeros :")
    rendimiento_vehiculo=input("rendimiento vehiculo (km/l):")
    auto['rendimiento'] = rendimiento_vehiculo
    auto5.append(auto)
    print("vehiculo Agregado")

def mostrar_vehiculos():
    for auto in auto5:
        print(auto)

def modifica_vehiculo1():
    patauto=patauto = input("Ingrese patente: ")
    modificar_vehiculo(patauto)
def modificar_vehiculo(patauto):
    for auto in auto5:
        if auto['patente'] == patauto:
            print("por favor ingrese los nuevos datos")
            nueva_marca = input("marca vehiculo :")
            nuevo_modelo = input("modelo vehiculo :")
            nuevo_año = input("año :")
            nuevo_cap = input("capacidad pasajeros :")
            rendimiento_vehiculo=input("rendimiento vehiculo (km/l):")
            
            auto['marca'] = nueva_marca
            auto['modelo'] = nuevo_modelo
            auto['año'] = nuevo_año
            auto['capacidad pasajeros'] = nuevo_cap
            auto['rendimiento'] = rendimiento_vehiculo
            
            print("Registro actualizado.")
            return
    print("No se encontró el registro.")

def elimina_auto():
    patauto=patauto = input("Ingrese patente que quiere eliminar, esto no se puede deshacer: ")
    eliminar_registroauto(patauto)
def eliminar_registroauto(patauto):
    for i, auto in enumerate(auto5):
        if auto['patente'] == patauto:
            del auto5[i]
            print("Registro eliminado.")
            return
    print("No se encontró el registro.")

def comprar_combustible():
    global Estanque_Combustible
    global rendimiento_vehiculo
    global valor_combustible
    com_restante=Estanque_Combustible
    nuevo_combustible=int(agregar_combustible('(lts comprados)'))*100/70
    valor_combustible= int(input("ingrese valor total pagado: $"))/(nuevo_combustible/100*70)
    Estanque_Combustible = com_restante + nuevo_combustible
    print("Combustible total disponible ",Estanque_Combustible/100*70," lts, suficiente para recorrer ",int(Estanque_Combustible/rendimiento_vehiculo), " Kms, a un costo de $",int(valor_combustible), " pesos el lt")
    
def salir():
    print('Finalizando Sesion, Hasta Pronto')
    
if __name__ == '__main__':
    menu_inicio()