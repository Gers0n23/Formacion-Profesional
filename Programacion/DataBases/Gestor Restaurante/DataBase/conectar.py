from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

url = "mongodb+srv://paulo:plto4956@inacap2023.guvc7ax.mongodb.net/?retryWrites=true&w=majority&appName=Inacap2023"

def conexion():
    cliente = MongoClient(url, server_api = ServerApi('1'))

    try:
        cliente.admin.command('ping')
        db = cliente.sample_restaurants
        print("Conectado a MongoDB")
        return (db)
    except Exception as e:
        print(e)