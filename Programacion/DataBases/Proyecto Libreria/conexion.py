from pymongo import MongoClient
import bcrypt

# Configura la conexión a MongoDB
client = MongoClient('mongodb+srv://gersoncordero:gerson123456@clusterger.cytglrh.mongodb.net/?retryWrites=true&w=majority&appName=ClusterGer')
db = client.libreria

# Colecciones
libros = db.libros
autores = db.autores
clientes = db.clientes
pedidos = db.pedidos
usuarios = db.usuarios