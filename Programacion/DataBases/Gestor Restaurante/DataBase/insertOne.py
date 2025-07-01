from conectar import *
import json

db = conexion()
coleccion = db.restaurants

#datos a insertar son

building = input("Ingrese el numero del edificio: ")
street = input("Ingrese el nombre de la calle: ")
zipcode = input("Ingrese el codigo postal: ")
coord_lon = float(input("ingrese la longitud: "))
coord_lat = float(input("ingrese la latitud: "))
borough = input("Ingrese la comuna del restaurante: ")
cuisine = input("Ingrese el tipo de cocina: ")
name = input("Ingrese el nombre del restaurante: ")
restaurant_id = input("Ingresa el ID del restaurante: ")

nuevoDocumento =  {
        
        "address": {
            "building": building,
            "coord": [coord_lon, coord_lat],
            "street": street,
            "zipcode": zipcode
        },
        "borough": borough,
        "cuisine": cuisine,
        "grades": [
            {
                "date": {
                    "$date": "2014-05-29T00:00:00Z"
                },
                "grade": "A",
                "score": 10
            },
            {
                "date": {
                    "$date": "2014-01-14T00:00:00Z"
                },
                "grade": "A",
                "score": 10
            },
            {
                "date": {
                    "$date": "2013-08-03T00:00:00Z"
                },
                "grade": "A",
                "score": 8
            },
            {
                "date": {
                    "$date": "2012-07-18T00:00:00Z"
                },
                "grade": "A",
                "score": 10
            },
            {
                "date": {
                    "$date": "2012-03-09T00:00:00Z"
                },
                "grade": "A",
                "score": 13
            },
            {
                "date": {
                    "$date": "2011-10-14T00:00:00Z"
                },
                "grade": "A",
                "score": 9
            }
        ],
        "name": name,
        "restaurant_id": restaurant_id
    }

resultado = coleccion.insert_one(nuevoDocumento)

print("El Id del nuevo documento es: ", resultado.inserted_id)