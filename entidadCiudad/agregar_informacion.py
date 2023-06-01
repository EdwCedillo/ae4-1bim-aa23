"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.dataAE4
coleccion = db.ciudad

# conjunto de datos a guardar en la colección
# importante, aquí se usa la estructura de Python denominada diccionario
# proceso que agrega un solo documento
data_01 = {"nombre_ciudad": "Machala", "localidad_provincia": "El Oro",
"num_habitantes":"250k", "area_km": 400}

coleccion.insert_one(data_01)

# proceso que agrega una lista de documentos
lista = [
{"nombre_ciudad": "Guayaquil", "localidad_provincia": "Guayas",
"num_habitantes":"3 Millones", "area_km": 800},
{"nombre_ciudad": "Cuenca", "localidad_provincia": "Azuay",
"num_habitantes":"600k", "area_km": 500}
]

coleccion.insert_many(lista)
