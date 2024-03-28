from pymongo import MongoClient
#READ
try:
    # Conexión a MongoDB
    client = MongoClient("localhost:27017")
    db = client["ubb"]  # Case-sensitive, should match database name
    collection = db["Neo"]

    ############## Consultas Solo Nombre ################
    # Consulta mayor a 25 años
    print("Documentos de mayores de 25 años")
    resultados = collection.find({"edad": {"$gt": 25}})

    for resultado in resultados:
        print(resultado)
        
 ############ Consulta menor a 25 años ##########|
    print("----------------------------------------------------------------")
    print("Documentos de menores de 25 años")
    resultados = collection.find({"edad": {"$lt": 25}},())

    for resultado in resultados:
        print(resultado)

    print("----------------------------------------------------------------")
    
    # Consulta de personas que ingresaron desde 2019
    print("Nombre de personas que ingresaron desde 2019, con su año")
    resultados = collection.find({"Ingreso": {"$gte": 2019}},{"nombre":1,"Ingreso":1})
    for resultado in resultados:
        print(resultado)
    print("----------------------------------------------------------------")
    #Solo nombres de personas que ingresaron en 2019 en adelante
    print("Solo Nombre de personas que ingresaron en 2019 en adelante")
    print("Solucion")
    #Solucion 1
    resultados = collection.find({"Ingreso": {"$gte": 2019}},{"nombre":1})
    for resultado in resultados:
        print(resultado)
    print("----------------------------------------------------------------")


except Exception as e:  # Captura cualquier excepción
    print("Error al conectar a MongoDB:", e)

finally:
    client.close()  # Cerrar la conexión

