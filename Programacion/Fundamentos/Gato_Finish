#Función para imprimir el juego 
def imprimir_gato(valores):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(valores[0], valores[1], valores[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(valores[3], valores[4], valores[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(valores[6], valores[7], valores[8]))
    print("\t     |     |")
    print("\n")
 
 
#Función para imprimir el marcador
def imprimir_marcador(marcador):
    print("\t--------------------------------")
    print("\t            MARCADOR          ")
    print("\t--------------------------------")
 
    jugadores = list(marcador.keys())
    print("\t   ", jugadores[0], "\t    ", marcador[jugadores[0]])
    print("\t   ", jugadores[1], "\t    ", marcador[jugadores[1]])
 
    print("\t--------------------------------\n")
 
#Función para saber si algún jugador ha ganado
def ganador(pos_jug, act_jug):
 
    #Combinaciones para ganar
    comb_ganar = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
    #Loop para checar si alguna combinacion ganadora ya salió
    for x in comb_ganar:
        if all(y in pos_jug[act_jug] for y in x):
 
            #True si ya se cumplió
            return True
    #False si no se ha cumplido       
    return False       
 
#Función para saber si el juego está empatado
def empate(pos_jug):
    if len(pos_jug['X']) + len(pos_jug['O']) == 9:
        return True
    return False       
 
#Función para un solo juego
def solo_uno(act_jug):
 
    #Representar gato
    valores = [' ' for x in range(9)]
     
    #Almacenar las posiciones ocupadas por X y 0
    pos_jug = {'X':[], 'O':[]}
     
    #Loop para un solo juego
    while True:
        imprimir_gato(valores)
         
        #Turno para mover
        try:
            print("Turno de:",act_jug,". ¿En que espacio?: ", end="")
            mover = int(input()) 
        except ValueError:
            print("Error, vuelva a intentarlo")
            continue
 
        #Válidez del movimiento
        if mover < 1 or mover > 9:
            print("Ingrese un numero mayor a 1 y menor que 9")
            continue
 
        #Checar que el espacio no esté ocupado
        if valores[mover-1] != ' ':
            print("¡No puede colocar aquí, está ocupado! Vuelva a intentarlo")
            continue
 
        #Actualizar la información del juego
 
        #Actualizar el tablero 
        valores[mover-1] = act_jug
 
        #Actualizar las posiciones de los jugadores
        pos_jug[act_jug].append(mover)
 
        #Verificar victoria
        if ganador(pos_jug, act_jug):
            imprimir_gato(valores)
            print("¡El jugador", act_jug,"ha ganado!")     
            print("\n")
            return act_jug
 
        #Verificar empate
        if empate(pos_jug):
            imprimir_gato(valores)
            print("Empate")
            print("\n")
            return 'D'
 
        #Cambiar los movimientos del jugador
        if act_jug == 'X':
            act_jug = 'O'
        else:
            act_jug = 'X'
 
if __name__ == "__main__":
 
    print("Jugador 1")
    jugador1 = input("Ingrese el nombre: ")
    print("\n")
 
    print("Jugador 2")
    jugador2 = input("Ingrese el nombre: ")
    print("\n")
     
    #Guarda al jugador
    act_jug = jugador1
 
    #Guarda si eligieron X o O
    eleccion_jugador = {'X' : "", 'O' : ""}
 
    #Guarda las opciones
    opciones = ['X', 'O']
 
    #Guarda el marcador
    marcador = {jugador1: 0, jugador2: 0}
    imprimir_marcador(marcador)
 
    #Loop para varios juegos, el loop continua hasta que el jugador decide salir
    while True:
 
        #Menú
        print("Elige", act_jug)
        print("Ingrese 1 para X")
        print("Ingrese 2 para O")
        print("Ingrese 3 para salir")
 
        #Opcion invalida
        try:
            eleccion = int(input())   
        except ValueError:
            print("Ingrese una opción válida\n")
            continue
 
        #Condiciones del menú  
        if eleccion == 1:
            eleccion_jugador['X'] = act_jug
            if act_jug == jugador1:
                eleccion_jugador['O'] = jugador2
            else:
                eleccion_jugador['O'] = jugador1
 
        elif eleccion == 2:
            eleccion_jugador['O'] = act_jug
            if act_jug == jugador1:
                eleccion_jugador['X'] = jugador2
            else:
                eleccion_jugador['X'] = jugador1
         
        elif eleccion == 3:
            print("Marcador final")
            imprimir_marcador(marcador) 
            break  
 
        else:
            print("Ingrese una opción válida\n")
 
        #Guarda al ganador de una sola partida
        gan = solo_uno(opciones[eleccion-1])
         
        #Modifica el marcador de acuerdo al ganador
        if gan != 'D' :
            jugador_gano = eleccion_jugador[gan]
            marcador[jugador_gano] = marcador[jugador_gano] + 1
 
        imprimir_marcador(marcador)
        
        #Cambia al jugador que eligió X o O
        if act_jug == jugador1:
            act_jug = jugador2
        else:
            act_jug = jugador1 
