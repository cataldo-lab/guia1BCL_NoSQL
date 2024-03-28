from pymongo import MongoClient

try:
    client = MongoClient("localhost:27017")
    db = client["ubb"]  # Case-sensitive, should match database name
    collection = db["Neo"]
    # Conexión a MongoDB


    document = [
        {"nombre": "Juan", "edad": 30, "Ingreso": 2019, "Ciudad": "Concepcion", "Region": "BioBio"},
        {"nombre": "Pedro", "edad": 25, "Ingreso": 2018, "Ciudad": "Concepcion", "Region": "BioBio"},
        {"nombre": "Maria", "edad": 28, "Ingreso": 2019, "Ciudad": "Lota", "Region": "BioBio"},
        {"nombre": "Jose", "edad": 22,"Ingreso": 2019, "Ciudad": "Coronel", "Region": "BioBio"},
        {"nombre": "Ana", "edad": 35,  "Ingreso": 2020, "Ciudad": "Coronel", "Region": "BioBio"},
        {"nombre": "Luis", "edad": 27,  "Ingreso": 2022, "Ciudad": "Talcahuano", "Region": "BioBio"},
        {"nombre": "Sofia", "edad": 23,  "Ingreso": 2021, "Ciudad": "Santiago Centro", "Region": "Metropolitana"},
        {"nombre": "Carlos", "edad": 29, "Ingreso": 2012, "Ciudad": "Maipu", "Region": "Metropolitana"},
        {"nombre": "Fernanda", "edad": 26, "Ingreso": 2013, "Ciudad": "Renca", "Region": "Metropolitana"},
        {"nombre": "Javier", "edad": 24, "Ingreso": 2009, "Ciudad": "Quilicura", "Region": "Metropolitana"}
    ]
    collection.insert_many(document)
    


except Exception as e:  # Captura cualquier excepción
    print("Error al conectar a MongoDB:", e)


