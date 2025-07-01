from conectar import * 

#db.restaurants.updateOne({"restaurant_id": "19042024231"},{$set:{"cuisine": "PorotosConRiendas","cuisine": "Tipico - Chileno"}})

id = input("Ingrese el ID del restaurante para modificar: ")
tipoCocina = input("Ingrese el tipo de cocina: ")
db = conexion()
coleccion = db.restaurants
filtro = {"restaurant_id":id}
update = {"$set":{"cuisine":tipoCocina}}

try:
    modificando = coleccion.update_one(filtro,update)
    print("Dato modificado, OK")
except Exception as e:
    print (e)