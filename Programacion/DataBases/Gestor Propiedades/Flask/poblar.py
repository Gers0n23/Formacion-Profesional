from pymongo import MongoClient
import bcrypt

# Configura la conexión a MongoDB
client = MongoClient('mongodb+srv://gersoncordero:gerson123456@clusterger.cytglrh.mongodb.net/?retryWrites=true&w=majority&appName=ClusterGer')
db = client.gestor_propiedades

# Colecciones
col_propiedades = db.propiedades


# Datos iniciales
col_propiedades.delete_many({})

propiedades_data = [
    {
        "nombrePropiedad": "Casa en La Reina",
        "tipo": "Casa",
        "comunaUbicacion": "La Reina",
        "precio": 5000,
        "metrosCuadrados": 200,
        "habitaciones": 3,
        "banos": 2,
        "estacionamientos": 2,
        "estado": "Disponible"
    },
    {
        "nombrePropiedad": "Departamento en Las Condes",
        "tipo": "Departamento",
        "comunaUbicacion": "Las Condes",
        "precio": 4500,
        "metrosCuadrados": 100,
        "habitaciones": 2,
        "banos": 2,
        "estacionamientos": 1,
        "estado": "Disponible"
    },
    {
        "nombrePropiedad": "Casa en La Florida",
        "tipo": "Casa",
        "comunaUbicacion": "La Florida",
        "precio": 6300,
        "metrosCuadrados": 150,
        "habitaciones": 4,
        "banos": 3,
        "estacionamientos": 1,
        "estado": "Disponible"
    },
    {
        "nombrePropiedad": "Increible Departamento Amoblado",
        "tipo": "Departamento",
        "comunaUbicacion": "Ñuñoa",
        "precio": 4800,
        "metrosCuadrados": 80,
        "habitaciones": 2,
        "banos": 2,
        "estacionamientos": 1,
        "estado": "Ocupado"
    },
    {
        "nombrePropiedad": "Amplia Casa en Barrio Universitario",
        "tipo": "Casa",
        "comunaUbicacion": "La Reina",
        "precio": 9000,
        "metrosCuadrados": 200,
        "habitaciones": 3,
        "banos": 2,
        "estacionamientos": 2,
        "estado": "Disponible"
    },
    {
        "nombrePropiedad": "Arriendo Departamento Amoblado",
        "tipo": "Departamento",
        "comunaUbicacion": "Conchali",
        "precio": 3500,
        "metrosCuadrados": 100,
        "habitaciones": 2,
        "banos": 2,
        "estacionamientos": 1,
        "estado": "Disponible"
    },
    {
        "nombrePropiedad": "Casona Patrimonial en Santiago Centro",
        "tipo": "Casa",
        "comunaUbicacion": "Santiago Centro",
        "precio": 6300,
        "metrosCuadrados": 150,
        "habitaciones": 4,
        "banos": 3,
        "estacionamientos": 1,
        "estado": "Disponible"
    },
    {
        "nombrePropiedad": "Departamento con Vista Panorámica",
        "tipo": "Departamento",
        "comunaUbicacion": "Ñuñoa",
        "precio": 4800,
        "metrosCuadrados": 80,
        "habitaciones": 2,
        "banos": 2,
        "estacionamientos": 1,
        "estado": "Ocupado"
    }
]

col_propiedades.insert_many(propiedades_data)

print("Datos insertados correctamente")