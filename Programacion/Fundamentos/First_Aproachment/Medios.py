from abc import ABC, abstractclassmethod
class MedioTransporte(ABC):
    def __init__(self):
        self.traccion = ""
        self.distancia = 0
        self.velocidad = 0
        self.capacidad = 0
        self.energia = ""
        self.ubicacion = {"x":0,"y":30,"z":0}
        self.estado = "Apagado"
        self.imagen = "test.png"
    @abstractclassmethod
    def Avanzar(self): # Aplico abstracción
        pass
class Terrestre(MedioTransporte): #Aplico Herencia
        def __init__(self):
            super().__init__()
            self.__propulsion = "Gasolina"

        def Avanzar(self):
            self.ubicacion["x"] += 10
            self.velocidad += 10
            return self.__propulsion
        def Retroceder(self):
            self.ubicacion["x"] -= 5
            self.velocidad -= 10
            return self.__propulsion
        def Subir(self):
            self.ubicacion["y"] -= 10
            return self.__propulsion
        def Bajar(self):
            self.ubicacion["y"] += 10
            return self.__propulsion
        def cambiarestado(self):
            if(self.estado == "Apagado"):
                self.estado = "Encendido"
            else:
                self.estado = "Apagado"
        def asignarimagen(self):
            if(self.estado == "Encendido"):
                self.imagen = "test2.png"
            else:
                self.imagen = "test.png"
        

           
class Automovil(Terrestre):
    
    def __init__(self,ptt,id,mc,md,año,cap,odo): #Override Polimorfismo
        super().__init__()
        self.patente=ptt
        self.id=id
        self.marca=mc
        self.modelo=md
        self.año=año
        self.capacidad_pasajeros=cap
        self.Odometro=odo
        
    def asignarimagen(self):
        super().asignarimagen()
        






