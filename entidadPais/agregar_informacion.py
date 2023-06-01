"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.dataAE4
coleccion = db.pais

# conjunto de datos a guardar en la colección
# importante, aquí se usa la estructura de Python denominada diccionario
# proceso que agrega un solo documento
data_01 = {"nombre_pais": "Ecuador", "ciudad_capital": "Quito",
"continente":"America del Sur", "poblacion": 17000000}

coleccion.insert_one(data_01)

# proceso que agrega una lista de documentos
lista = [
{"nombre_pais": "Peru", "ciudad_capital": "Lima",
"continente":"America del Sur", "poblacion": 20000000},
{"nombre_pais": "Holanda", "ciudad_capital": "Amsterdam",
"continente":"Europa", "poblacion": 3000000}
]

coleccion.insert_many(lista)
