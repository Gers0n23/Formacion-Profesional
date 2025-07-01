import Medios
import pygame

# Definimos una función que recibe como parámetro el objeto automóvil
def jugar(miobjeto):
    # Inicializamos pygame y creamos la ventana
    pygame.init()
    screen_width = 500
    screen_height = 400
    ventana = pygame.display.set_mode([screen_width,screen_height])
    # Cargamos las imágenes del fondo y del automóvil
    imagen = pygame.image.load(miobjeto.imagen)
    fondo = pygame.image.load('./background.png')
    # Ajustamos el tamaño de la imagen del automóvil
    imagen = pygame.transform.scale(imagen, (int(imagen.get_width() * (15/100)), int(imagen.get_height() * (15/100))))
    # Definimos la posición inicial del fondo
    fondo_x = -400.210
    # Definimos las fuentes para el texto
    font = pygame.font.Font(None, 36)
    little_font = pygame.font.Font(None, 20)
    # Definimos el texto inicial de la velocidad y el estado
    texto = f"Speed {int(miobjeto.velocidad)} Km/h"
    texto_estado= f"Estado: {miobjeto.estado}"
    
    # Creamos una variable para controlar el bucle principal
    running = True
    
    # Bucle principal del juego
    while running:
        # Actualizamos la posición del fondo según la velocidad del automóvil
        fondo_x -= miobjeto.velocidad / 100
        # Creamos los objetos de texto con el color correspondiente al estado
        texto_agregar = font.render(texto,True, (255,0,0))
        if miobjeto.estado=="Apagado":
            texto_agregar_estado = little_font.render(texto_estado,True, (255,0,0))
        else:
            texto_agregar_estado = little_font.render(texto_estado,True, (0,255,0))
        # Si el fondo se sale de la pantalla, lo reiniciamos
        if(fondo_x<-700):
            fondo_x = -400
        if(fondo_x > 0):
            fondo_x = -400
        # Rellenamos la ventana con color negro   
        ventana.fill((0,0,0))   
        # Dibujamos el fondo, el texto y el automóvil en la ventana
        ventana.blit(fondo,(fondo_x,0))
        ventana.blit(texto_agregar, (screen_width / 2, 0))
        ventana.blit(texto_agregar_estado, (10, 305))
        ventana.blit(imagen,(miobjeto.ubicacion["x"], miobjeto.ubicacion["y"]))
        
        # Procesamos los eventos de pygame
        for event in pygame.event.get():
            # Si el usuario cierra la ventana, salimos del bucle
            if event.type == pygame.QUIT:
                running = False
            # Si el usuario presiona una tecla, modificamos el estado o la velocidad del automóvil según corresponda
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    miobjeto.cambiarestado()
                    if miobjeto.velocidad!=0:
                        miobjeto.velocidad = 0
                if event.key == pygame.K_w:
                   if miobjeto.estado == "Encendido":
                       miobjeto.Subir()
                if event.key == pygame.K_a:
                    if miobjeto.estado == "Encendido":
                        miobjeto.Retroceder() 
                if event.key == pygame.K_s:
                   if miobjeto.estado == "Encendido":
                       miobjeto.Bajar() 
                if event.key == pygame.K_d:
                    if miobjeto.estado == "Encendido": # Solo avanza si el estado es encendido
                        if miobjeto.velocidad <= 250:
                            miobjeto.Avanzar() 
            # Si el automóvil supera la velocidad máxima, cambiamos el texto
            if(miobjeto.velocidad>250):
                texto = f"Max. Speed Reached"
            else:
                texto = f"Speed {int(miobjeto.velocidad)} Km/h"
            # Actualizamos el texto del estado
            texto_estado= f"Estado: {miobjeto.estado}"
            miobjeto.asignarimagen()
            imagen = pygame.image.load(miobjeto.imagen)
            imagen = pygame.transform.scale(imagen, (int(imagen.get_width() * (15/100)), int(imagen.get_height() * (15/100))))
        # Actualizamos la pantalla con los cambios realizados
        pygame.display.flip()
    
    # Salimos de pygame
    pygame.quit()

# Creamos el objeto automóvil
miobjeto = Medios.Automovil("CTBZ31", "CTBZ311", "CHEVROLET", "SPARK","2015","4","75000")
# Imprimimos la ubicación inicial en x
print(miobjeto.ubicacion["x"])
# Cambiamos la ubicación en y
miobjeto.ubicacion["y"] = 85
# Llamamos a la función jugar con el objeto automóvil como parámetro
jugar(miobjeto)