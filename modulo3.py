#practica comparadores
numero = int(input("Introduza un numero para ser comparado: "))
print(numero >= 100) 

# prueba = 55>=100
# print(prueba)

#Practica el numero mas grande
numero1 = int(input("Ingresa el primer número:"))
numero2 = int(input("Ingresa el segundo número:"))
numero3 = int(input("Ingresa el tercer número:"))

nmasGrande = numero1 #asumimos temporalmente que el primer númeroes el más grandelo verificaremos pronto
if numero2 > nmasGrande: #comprobamos si el segundo número es más grande que el mayor número actual
    nmasGrande = numero2
if numero3 > nmasGrande: #comprobamos si el tercer número es más grande que el mayor número actual
    nmasGrande = numero3

#imprimir el resultado
print("El número más grande es:", nmasGrande)

#practica condicional
planta = input("INgresa una planta: ")
if planta=="Espatifilo" :
	print("¡Espatifilo es la mejor planta de todas")
else :
	print("Espatifilo! ¡No \""+planta+"\"!")

#PRactica cobro de impuestos
ingreso=float(input("Ingrese el ingreso anual:"))

if ingreso<0:
	impuesto=0
elif ingreso<85528:
	impuesto = ingreso*18/100 - 556.2
else :
	impuesto = 14839.2 + ((ingreso-85528)*32/100)

impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")

#Practica año bisiesto o comun
año = int(input("Introduzca un año:"))

if año < 1582 :
	print("El año ",año," no esta dentro del período del calendario gregoriano")
elif año%400 == 0 :
	print("El año ",año," es un año biciesto")
elif año%4 == 0 and año%100 != 0 :
	print("El año ",año," es un año biciesto")
else :
	print("El año ",año," es un año comun")

# Almacenaremos el número más grande y lo mostramos
numeroMayor = -999999999
numero = int(input ("Introduzca un número o escriba -1 para detener:"))

while numero != -1:
	if numero > numeroMayor:
		numeroMayor = numero

	numero = int (input("Introduce un número o escribe -1 para detener:")) # Ingresa el siguiente número
print("El número más grande es:", numeroMayor) # Imprimir el número más grande

#PRACTICA WHILE
numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
numero = int(input("\nIngresa el numero: "))
if numero != numeroSecreto:
	print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")

while numero!=numeroSecreto:
	numero = int(input("Ingresa el numero: "))
print("¡Bien hecho, muggle! Eres libre ahora")

#PRACTICA FOR
for i in range(10):
	print("¡Ja, ja! ¡Estás atrapado en mi FOR de 10! el valor de i es ",i)
for i in range(2,10): #Va del 2 al 9
	print("¡Ja, ja! ¡Estás atrapado en mi FOR de 2 a 10! el valor de i es ",i)
for i in "brother":
	print("FOR: pasame la ",i)
for i in [3,4,6,9]:
	print("FOR: [con arraay] el valor de i es ",i)
for i in range(2, 8, 3): #inicia con 2 y tiene que terminar en < a 8 pero incrementa en 3 cada recorrido
    print("El valor de i es actualmente", i)

import time
for i in range(1,6):
	print(i,"Mississippi")
	time.sleep(1)
print("listos o no, ahi voy")

# break - ejemplo
print("La instrucción de ruptura:")
for i in range(1,6):
    if i == 3:
        break
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")
# continua - ejemplo
print("\nLa instrucción continue:")
for i in range(1,6):
    if i == 3:
        continue
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

#PRACTICA CONTINUE Y BREAK
palabraSinVocal = ""
userWord = input("Ingresa la palabra para dejarla sin vocales: ")
userWord = userWord.upper() #Tranforma la palabra en mayuculas
for i in userWord:
	if i=="A" or i=="E" or i=="I" or i=="O" or i=="U" :
		continue
	palabraSinVocal+= i
print(palabraSinVocal)

#PRATICA WHILE
bloques = int(input("Ingrese el número de bloques:"))
altura = i = 1
if bloques > 0:
	num_bloques = (altura*(altura+1))/2
	while i <= bloques:
		if i > num_bloques:
			altura+= 1
			num_bloques = (altura*(altura+1))/2
		i+= 1
	if bloques < num_bloques:
		altura-=1
else:
	print("Introduzca un numero mayor a 0")
print(altura)

#PRATICA WHILE NUMERO LOTHAR
c0= int(input("Introduzca un numero para tenderlo a 1:"))
c=0
while c0 != 1:
	if c0%2==0:
		c0//= 2
		print(c0)
		c+= 1
	else:
		c0 = 3*c0+1
		print(c0)
		c+= 1
print("total de pasos",c)

#PRACTICA ARRAYS
numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprimiendo contenido de la lista original

numeros[0] = 111
print("\nPrevio contenido de la lista:", numeros) # imprimiendo contenido de la lista anterior

numeros[1] = numeros[4] # copiando el valor del quinto elemento al segundo
print("Contenido de la lista anterior:", numeros) # imprimiendo contenido de la lista anterior

print ("\nLongitud de la lista:", len(numeros)) # imprimiendo la longitud de la lista anterior

del numeros[1] # eliminando el segundo elemento de la lista
print("Longitud de la nueva lista:", len(numeros)) # imprimiendo nueva longitud de la lista
print("\nNuevo contenido de la lista:", numeros) # imprimiendo el contenido de la lista actual

#ARRAY Y METODOS
numeros = [111, 7, 2, 1]
print(len(numeros))
print(numeros)
numeros.insert(0,222)# insertas un valor (222) al una posicion de la lista (0)
print(len(numeros))
print(numeros)

miLista = [] # creando una lista vacía
for i in range (5):
    miLista.append (i + 1) #append() agrega un valor (i) al final de la lista
print(miLista)

#RACTICA ARRAYS
miLista = [10, 1, 8, 3, 5]
suma = 0
for i in miLista:
    suma += i
print(suma) 

#Revertir los elemtos de una lista
miLista = [10, 1, 8, 3, 5]
longitud = len(miLista)
for i in range (longitud // 2): #i inicia en 0
	miLista[i], miLista[longitud-i-1] = miLista[longitud-i-1], miLista[i]
print(miLista) 

#METODO ORDENAMINTO BURBUJA
# miLista.sort()  tambien se puede usar ese metodo resumiento el metodo busrbuja
# miLista.sort()  tambien se puede usar ese metodo para ordenaro al revez
miLista = [8, 10, 6, 2, 4] # lista para ordenar
swapped = True # lo necesitamos verdadero (True) para ingresar al bucle while
while swapped:
	swapped = False # no hay swaps hasta ahora
	for i in range(len(miLista) - 1):
		if miLista[i] > miLista[i + 1]:
			swapped= True # ocurrió el intercambio!
			miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i] 
print(miLista)

# Copiando toda la lista
lista1 = [1]
lista2 = lista1[:] # [:] crea una copia exta en otra seccion de memoria, sin eso la lisa2 tomaria cambios de la lista1
lista1[0] = 2
print(lista2)

# Copiando parte de la lista
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[1:3] # [inicio:fin] o [inicio:] o [:fin] Copia el elemento 1 hasta el fin-1 osease 2
print(nuevaLista)

#elementos in y not in para verificar elementos en una ista
miLista = [0, 3, 12, 8, 2]
print(5 in miLista)
print(5 not in miLista)
print(12 in miLista)

#PRACTICA ARRAYS BORRAR DUPLICADOS
miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# myList = list(set(myList)) es un metodo para borrar duplicados en listas 
miLista2 = miLista[:]
del miLista[:]
for i in miLista2:
	if i not in miLista:
		miLista.append(i)
print("La lista solo con elementos únicos:")
print(miLista)

#MATRICES
#Forma facil de crear matriz. La parte interna crea una fila, y la parte externa crea una lista de filas. 
EMPTY="-"
tablero = [[EMPTY for i in range(8)] for j in range(8)]
print(tablero)
#forma normal
EMPTY = "-"
tablero = []
for i in range(8):
    fila = [EMPTY for i in range(8)]
    tablero.append (fila)
print(tablero)

