from pymongo import MongoClient

try:
    # Conexión a MongoDB
    client = MongoClient("localhost:27017")
    db = client["ubb"]  # Case-sensitive, should match database name
    collection = db["Neo"]

#Update

    query = {"nombre": "Juan"}
    next_values = {"$set":{"edad":31}}
    collection.update_one(query, next_values)
    resultados = collection.find()
    for resultado in resultados:
        print(resultado)

except Exception as e:  # Captura cualquier excepción
    print("Error al conectar a MongoDB:", e)

finally:
    client.close()  # Cerrar la conexión
