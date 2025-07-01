from bson import json_util
from conectar import *

class Buscar():

    def __init__(self, id):
        self.id = id

    def buscar(self):

        db = conexion() # sample_restaurants
        coleccion = db.restaurants.find_one({"restaurant_id": self.id})
        documento = coleccion

        return documento