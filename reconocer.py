numero1 = 70  # variable tipo entero. valor 70
numero2 = 3.14 #variable tipo flotante. valor 3.14
booleano = False #Variable tipo booleano. valor False
cadena = 'Hola Mundo' #variable tipo string. valor Hola Mundo
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate'] #Variable tipo lista. 5 datos registrados
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False} #variable tipo diccionario. 4 datos registrados. 2 strings, 1 entero y 1 booleano
frutas = ('guayaba', 'fresa', 'papaya') #variable tipo tupla. 3 datos registrados. 3 strings
print(type(frutas)) #función print para mostrar el argumento en consola. el argumento es la función type que muestra el tipo de dato de la variable frutas
print(ingredientes_pastel[2]) #función print que muestra el tercer elemento de la lista ingredientes_pastel
ingredientes_pastel.append('Mantequilla') #añade un nuevo elemento a la lista ingredientes_pastel
print(persona['nombre']) #función print que muestra el valor del elemento nombre del diccionario persona
persona['nombre'] = 'Kevin' #modifica el valor del elemento nombre del diccionario persona. agrega el valor kevin
persona['color_ojos'] = 'cafe' #añade el valor del elemento color_ojos al diccionario persona. el valor es cafe
print(frutas[2]) #función print que muestra el tercer elemento d la tupla frutas

if numero1 > 45: #condicional if que evalua si el valor de la variable numero1 es mayor a 45
    print("Numero mayor") #si la condición se cumple, imprime "Numero mayor"
else:   #condicional else que se ejecuta si la condición del if no se cumple
    print("Numero menor") #si la condición no se cumple, imprime "Numero menor"

if len(cadena) < 5: #condicional if que evalua si la longitud de la string cadena es menor a 5
    print("Cadena corta") #si la condición se cumple, imprime "Cadena corta"
elif len(cadena) > 15: 
    print("Cadena larga")
else:
    print("Cadena perfecta")

for x in range(8):
    print(x)
for x in range(2,8):
    print(x)
for x in range(2,8,2):
    print(x)
x
while(x < 8):
    print(x)
    x += 1

ingredientes_pastel.pop()
ingredientes_pastel.pop(1)

print(persona)
persona.pop('color_ojos')
print(persona)

for ingrediente in ingredientes_pastel:
    if ingrediente == 'Harina':
        continue
    print('Después de la primera sentencia')
    if ingrediente == 'Chocolate':
        break

def imprime_hola_10_veces():
    for numero in range(10):
        print('Hola')

imprime_hola_10_veces()

def imprime_hola_n_veces(n):
    for numero in range(n):
        print('Hola')

imprime_hola_n_veces(5)

def imprime_hola_n_o_diez_veces(n = 10):
    for numero in range(n):
        print('Hola')

imprime_hola_n_o_diez_veces()
imprime_hola_n_o_diez_veces(5)


"""
Sección BONUS
"""

# print(numero3) # ERROR: La variable numero3 no ha sido definida. (NameError: name 'numero3' is not defined)
# numero3 = 86 #definición de la variable numero3. valor 86
# frutas[0] = 'naranja' #ERROR: Las tuplas no pueden ser modificadas. (TypeError: 'tuple' object does not support item assignment)
# print(persona['hobbies']) #Error: La clave hobbies no existe en el diccionario persona. (KeyError: 'hobbies')
# print(ingredientes_pastel[11]) #Error: El índice 11 no existe en la lista ingredientes_pastel. (IndexError: list index out of range)
#   print(booleano) #Error: IndentationError: unexpected indent
# frutas.append('manzana') #ERROR: Las tuplas no pueden ser modificadas. AttributeError: 'tuple' object has no attribute 'append'
# frutas.pop(1) #ERROR: Las tuplas no pueden ser modificadas. (AttributeError: 'tuple' object has no attribute 'pop')