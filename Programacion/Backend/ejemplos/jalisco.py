from os import system

while True:

    #Entrada

    try:
        number=int(input("ingrese un numero: "))

    except ValueError:
        print("ingrese un numero valido")
        number=int(input("ingrese un numero: "))

    #Procesamiento

    if number>=1 and number<=100:
        respuesta=number+1
        print(f"ja ja ja te gane con el {respuesta}")
    else:
        print("eres un tramposo, te dije entre 1 y 100  ")
    
    reintentar=input("¿Quieres jugar de nuevo? (s/n): ")

    if reintentar.lower()!="s":
        break
        cls.clear()
    else:
        cls.clear()
        continue

    #Salida

    print("¡Gracias por jugar!")