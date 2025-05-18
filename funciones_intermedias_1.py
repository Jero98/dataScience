########### ejercicio 1. actualizar valores en diccionarios y listas ##########
matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

#actualizar valor 3 en matriz por 6
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 3:
            matriz[i][j] = 6
print(matriz) #imprime la matriz actualizada
#actualizar el nombre de Ricky Martin por el de Enrique Martin Morales
for i in range(len(cantantes)):
    if cantantes[i]["nombre"] == "Ricky Martin":
        cantantes[i]["nombre"] = "Enrique Martin Morales"

print(cantantes) #imprime la lista de cantantes actualizada

##cambiar el nombre de Cancún por Monterrey
for pais in ciudades:
    for ciudad in pais:
        if ciudad == "Cancún":
            ciudad = "Monterrey"

print(ciudades) #imprime la lista de ciudades actualizada

#cambiar el valor de latitud por 9.9355431
coordenadas[0]["latitud"] = 9.9355431
print(coordenadas) #imprime la lista de coordenadas actualizada

################# ejercicio 2. iterar a traves de una lista de diccionarios ##################
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
def iterarDiccionario(lista):
    for artista in lista:
        nombre, pais = artista.values()
        print(f"nombre - {nombre}, pais - {pais}")
iterarDiccionario(cantantes)

################ ejercicio 3. obtener valores de una lista de diccionarios ################
def iterarDiccionario2(llave, lista):
    for artista in lista:
        print(artista[llave])

iterarDiccionario2("nombre", cantantes) #imprime los nombres de los artistas
iterarDiccionario2("pais", cantantes) #imprime los paises de los artistas

################ ejercicio 4. iterar a traves de un diccionario con valores de lista ##############}
print("\n\n\n")
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(diccionario):
    for llave, valor in diccionario.items():
        print(f"llave {str(llave).upper()} con tamaño de lista {len(valor)}:")
        for i in valor:
            print(i)
imprimirInformacion(costa_rica) #imprime la lista de ciudades y comidas