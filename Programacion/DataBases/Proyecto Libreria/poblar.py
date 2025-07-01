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
categorias = db.categorias

# Datos iniciales

autores.delete_many({})
libros.delete_many({})
clientes.delete_many({})
pedidos.delete_many({})
usuarios.delete_many({})
categorias.delete_many({})


autores_data = [
    {"_id": 1, "nombre": "J.R.R. Tolkien", "nacionalidad": "Británico"},
    {"_id": 2, "nombre": "George Orwell", "nacionalidad": "Británico"},
    {"_id": 3, "nombre": "Gabriel García Márquez", "nacionalidad": "Colombiano"},
    {"_id": 4, "nombre": "Jane Austen", "nacionalidad": "Británica"},
    {"_id": 5, "nombre": "Mark Twain", "nacionalidad": "Estadounidense"},
    {"_id": 6, "nombre": "J.K. Rowling", "nacionalidad": "Británica"},
    {"_id": 7, "nombre": "Stephen King", "nacionalidad": "Estadounidense"},
    {"_id": 8, "nombre": "Agatha Christie", "nacionalidad": "Británica"},
    {"_id": 9, "nombre": "Isaac Asimov", "nacionalidad": "Estadounidense"},
    {"_id": 10, "nombre": "Harper Lee", "nacionalidad": "Estadounidense"},
    {"_id": 11, "nombre": "Jorge Luis Borges", "nacionalidad": "Argentino"},
    {"_id": 12, "nombre": "Ernest Hemingway", "nacionalidad": "Estadounidense"},
    {"_id": 13, "nombre": "F. Scott Fitzgerald", "nacionalidad": "Estadounidense"},
    {"_id": 14, "nombre": "Virginia Woolf", "nacionalidad": "Británica"},
    {"_id": 15, "nombre": "Arthur Conan Doyle", "nacionalidad": "Británico"}
]

libros_data = [
    {"_id": 1, "titulo": "El señor de los anillos", "autor_id": 1, "precio": 20990, "stock": 50, "categoria_id": 1,"idioma": "Español", "año": 1954, "paginas": 1200, "isbn": "978-84-450-7370-6","formato": "Tapa dura", "editorial": "Minotauro"},
    {"_id": 2, "titulo": "1984", "autor_id": 2, "precio": 15990, "stock": 30, "categoria_id": 4,"idioma": "Español", "año": 1949, "paginas": 328, "isbn": "978-84-450-7370-6","formato": "Tapa blanda", "editorial": "Debolsillo"},
    {"_id": 3, "titulo": "Cien años de soledad", "autor_id": 3, "precio": 18990, "stock": 20, "categoria_id": 4,"idioma": "Español", "año": 1967, "paginas": 432, "isbn": "978-84-450-7370-6","formato": "Tapa blanda", "editorial": "Debolsillo"},
    {"_id": 4, "titulo": "Orgullo y prejuicio", "autor_id": 4, "precio": 10990, "stock": 40, "categoria_id": 4,"idioma": "Español", "año": 1813, "paginas": 424, "isbn": "978-84-450-7370-6","formato": "Tapa blanda", "editorial": "Debolsillo"},
    {"_id": 5, "titulo": "Las aventuras de Tom Sawyer", "autor_id": 5, "precio": 12990, "stock": 60, "categoria_id": 5,"idioma": "Español", "año": 1876, "paginas": 288, "isbn": "978-84-450-7370-6","formato": "Tapa blanda", "editorial": "Debolsillo"},
    {"_id": 6, "titulo": "Harry Potter y la piedra filosofal", "autor_id": 6, "precio": 20990, "stock": 70, "categoria_id": 1,"idioma": "Español", "año": 1997, "paginas": 256, "isbn": "978-84-450-7370-6","formato": "Tapa dura", "editorial": "Salamandra"},
    {"_id": 7, "titulo": "It", "autor_id": 7, "precio": 15990, "stock": 40, "categoria_id": 3,"idioma": "Español", "año": 1986, "paginas": 1536, "isbn": "978-84-450-7370-6","formato": "Tapa blanda", "editorial": "Debolsillo"},
    {"_id": 8, "titulo": "Asesinato en el Orient Express", "autor_id": 8, "precio": 18990, "stock": 30, "categoria_id": 10,"idioma": "Español", "año": 1934, "paginas": 288, "isbn": "978-84-450-7370-6","formato": "Tapa blanda", "editorial": "Debolsillo"},
    {"_id": 9, "titulo": "Fundación", "autor_id": 9, "precio": 10990, "stock": 50, "categoria_id": 2,"idioma": "Español", "año": 1951, "paginas": 256, "isbn": "978-84-450-7370-6","formato": "Tapa blanda", "editorial": "Debolsillo"},
    {"_id": 10, "titulo": "Matar a un ruiseñor", "autor_id": 10, "precio": 12990, "stock": 40, "categoria_id": 4,"idioma": "Español", "año": 1960, "paginas": 424, "isbn": "978-84-450-7370-6","formato": "Tapa blanda", "editorial": "Debolsillo"},
    {"_id": 11, "titulo": "Ficciones", "autor_id": 11, "precio": 20990, "stock": 30, "categoria_id": 4,"idioma": "Español", "año": 1944, "paginas": 224, "isbn": "978-84-450-7370-6","formato": "Tapa blanda", "editorial": "Debolsillo"},
    {"_id": 12, "titulo": "Adiós a las armas", "autor_id": 12, "precio": 15990, "stock": 40, "categoria_id": 4,"idioma": "Español", "año": 1929, "paginas": 352, "isbn": "978-84-450-7370-6","formato": "Tapa blanda", "editorial": "Debolsillo"},
    {"_id": 13, "titulo": "El gran Gatsby", "autor_id": 13, "precio": 18990, "stock": 20, "categoria_id": 4,"idioma": "Español", "año": 1925, "paginas": 256, "isbn": "978-84-450-7370-6","formato": "Tapa blanda", "editorial": "Debolsillo"},
    {"_id": 14, "titulo": "La señora Dalloway", "autor_id": 14, "precio": 10990, "stock": 50, "categoria_id": 4,"idioma": "Español", "año": 1925, "paginas": 224, "isbn": "978-84-450-7370-6","formato": "Tapa blanda", "editorial": "Debolsillo"},
    {"_id": 15, "titulo": "El perro de los Baskerville", "autor_id": 15, "precio": 12990, "stock": 40, "categoria_id": 10,"idioma": "Español", "año": 1902, "paginas": 256, "isbn": "978-84-450-7370-6","formato": "Tapa blanda", "editorial": "Debolsillo"}
]

categorias_data = [
    {"_id": 1, "nombre": "Fantasía"},
    {"_id": 2, "nombre": "Ciencia Ficción"},
    {"_id": 3, "nombre": "Terror"},
    {"_id": 4, "nombre": "Novela"},
    {"_id": 5, "nombre": "Cuento"},
    {"_id": 6, "nombre": "Ensayo"},
    {"_id": 7, "nombre": "Poesía"},
    {"_id": 8, "nombre": "Biografía"},
    {"_id": 9, "nombre": "Historia"},
    {"_id": 10, "nombre": "Policial"}
]


clientes_data = [
    {"_id": 1, "nombre": "Ana Maria Godoy Suazo", "email": "ana@example.com", "telefono": "+56912345678", "direccion": "Calle Falsa 123"},
    {"_id": 2, "nombre": "Luis Caballero Pino", "email": "luis@example.com", "telefono": "+56987654321", "direccion": "Avenida Siempreviva 742"},
    {"_id": 3, "nombre": "María Pia Herrera Diaz", "email": "maria@example.com", "telefono": "+56911223344", "direccion": "Calle de la Amargura 666"},
    {"_id": 4, "nombre": "Pedro Sanchez Mariqueo", "email": "pedro@example.com", "telefono": "+56944332211", "direccion": "Calle de la Alegría 777"},
    {"_id": 5, "nombre": "Sofía Cordero Gammara", "email": "sofia@example.com", "telefono": "+56999887766", "direccion": "Calle de la Felicidad 888"},
    {"_id": 6, "nombre": "Juan Perez", "email": "juan@example.com", "telefono": "+56911223344", "direccion": "Calle de la Amargura 666"},
    {"_id": 7, "nombre": "Carla González", "email": "carla@example.com", "telefono": "+56944332211", "direccion": "Calle de la Alegría 777"},
    {"_id": 8, "nombre": "Miguel Soto", "email": "miguel@example.com", "telefono": "+56999887766", "direccion": "Calle de la Felicidad 888"},
    {"_id": 9, "nombre": "Andrea Rojas", "email": "andrea@example.com", "telefono": "+56911223344", "direccion": "Calle de la Amargura 666"},
    {"_id": 10, "nombre": "Felipe Torres", "email": "felipe@example.com", "telefono": "+56944332211", "direccion": "Calle de la Alegría 777"}
]

pedidos_data = [
    {"_id": 1, "cliente_id": 1, "libro_id": 1, "cantidad": 2, "total": 41980},
    {"_id": 2, "cliente_id": 2, "libro_id": 2, "cantidad": 1, "total": 15990},
    {"_id": 3, "cliente_id": 3, "libro_id": 3, "cantidad": 3, "total": 56970},
    {"_id": 4, "cliente_id": 4, "libro_id": 4, "cantidad": 1, "total": 10990},
    {"_id": 5, "cliente_id": 5, "libro_id": 5, "cantidad": 2, "total": 25980},
    {"_id": 6, "cliente_id": 6, "libro_id": 6, "cantidad": 1, "total": 20990},
    {"_id": 7, "cliente_id": 7, "libro_id": 7, "cantidad": 1, "total": 15990},
    {"_id": 8, "cliente_id": 8, "libro_id": 8, "cantidad": 1, "total": 18990},
    {"_id": 9, "cliente_id": 9, "libro_id": 9, "cantidad": 1, "total": 10990},
    {"_id": 10, "cliente_id": 10, "libro_id": 10, "cantidad": 1, "total": 12990}
]

# Función para generar el hash de una contraseña
def generar_hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

usuarios_data = [
    {"username": "gerson.cordero@inacapmail.cl", "password": generar_hash_password("123456"), "rol": "admin"},
    {"username": "luis.canales21@inacapmail.cl", "password": generar_hash_password("123456"), "rol": "admin"},
    {"username": "ana@example.com", "password": generar_hash_password("123456"), "rol": "user"},
    {"username": "luis@example.com", "password": generar_hash_password("123456"), "rol": "user"},
    {"username": "maria@example.com", "password": generar_hash_password("123456"), "rol": "user"},
    {"username": "pedro@example.com", "password": generar_hash_password("123456"), "rol": "user"},
    {"username": "sofia@example.com", "password": generar_hash_password("123456"), "rol": "user"},
    {"username": "juan@example.com", "password": generar_hash_password("123456"), "rol": "user"},
    {"username": "carla@example.com", "password": generar_hash_password("123456"), "rol": "user"},
    {"username": "miguel@example.com", "password": generar_hash_password("123456"), "rol": "user"},
    {"username": "andrea@example.com", "password": generar_hash_password("123456"), "rol": "user"},
    {"username": "felipe@example.com", "password": generar_hash_password("123456"), "rol": "user"}
]

# Insertar datos en las colecciones
autores.insert_many(autores_data)
libros.insert_many(libros_data)
clientes.insert_many(clientes_data)
pedidos.insert_many(pedidos_data)
usuarios.insert_many(usuarios_data)
categorias.insert_many(categorias_data)

print("Datos insertados correctamente")