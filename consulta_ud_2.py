from pymongo import MongoClient

try:
    # Conexión a MongoDB
    client = MongoClient("localhost:27017")
    db = client["ubb"]  # Case-sensitive, should match database name
    collection = db["Neo"]

#Delete un elemento

    query = {"nombre": "Javier"}
    collection.delete_one(query)
    resultados = collection.find()
    for resultado in resultados:
        print(resultado)

#Delete todos los elementos antes de 2013

    #query={"Ingreso": {"$lte": 2013}}
    #collection.delete_many(query)
    #resultados = collection.find()
    #for resultado in resultados:
    #    print(resultado)

except Exception as e:  # Captura cualquier excepción
    print("Error al conectar a MongoDB:", e)

finally:
    client.close()  # Cerrar la conexión
