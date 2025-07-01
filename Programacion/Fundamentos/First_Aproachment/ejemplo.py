class Automovil:
    motor = ""
    puertas = 0
    color = ""
    encendido = False
    velocidad = 0
    def frenar(self):
        self.velocidad = 0
    def encender(self):
        self.encendido = True
    def acelerar(self):
        if(self.encendido):
            self.velocidad += 10
        else:
            print("No se puede acelerar si el vehículo está apagado")
    def verEstado(self):
        if(self.encendido):
            print(chr(27)+"[2;32;102m")
        else:
            print(chr(27)+"[2;32;101m")
        print('*'*10)
        print("Encendido : ", self.encendido)
        print("Velocidad Actual : ", self.velocidad)
        print('*'*10)
        print(chr(27)+"[0m")
miautito = Automovil()
def menu():
    while(True):
        print(chr(27)+"[2J")
        print(chr(27)+"[1;32;104m")
        print('_'*20)
        print("|1. para encender \t |")
        print("|2. para apagar \t |")
        print("|3. para acelerar \t |")
        print("|0. para Salir \t\t |")
        print('_'*20)
        print(chr(27)+"[0m")
        miautito.verEstado()
        opc = int(input())
        if(opc == 0):
            exit()
        elif(opc == 1):
            miautito.encender()
        elif(opc == 3):
            miautito.acelerar()
menu()
