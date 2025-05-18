# ejercicio 1. Básico
for i in range(101): #imprime los numeros del 0 al 100
        print(i)

#ejercicio 2. Múltiples de 2
for i in range(2,501,2):
        print(i) #imprime todos los numeros pares entre 2 y 500

#ejercicio 3. Contando Vanilla Ice
for i in range(1,101):
        if i % 5 == 0:
                print("ice ice") #imprimir ice ice si el numero es un multiplo de 5
        elif i % 10 == 0:
                print("baby") #imprime baby si el numero es un multiplo de 10

#ejercicio 4. Wow. Número gigante a la vista
suma_total = 0
for i in range(0,500000,2):
        suma_total += i #suma todos los numeros pares entre 0 y 500000
print(suma_total) #imprime la suma total

#ejercicio 5. Regrésame al 3
for i in range(2024,1, -3):
        print(i) #imprime todos los positivos menores a 2024 de 3 en 3

#ejercicio 6. Contador dinámico
numInicial= 3
numFinal = 12
multiplo = 2
for i in range(numInicial, numFinal+1):
        if i %multiplo == 0:
            print(i) #imprime todos los numeros entre numInicial y NumFinal de multiplo en multiplo