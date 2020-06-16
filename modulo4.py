#PRACTICA FUNCIONES
def mensaje(numero, nombre): #declaracion de variables
    print("Ingresa un número:", numero)

numero = 1234 #se puede usar una variable con el mismo nombre del parametro de una funcion
mensaje(1,"Renato") # el numero de argumentos debe ser el mismo numero de parametros que tiene la funcion
mensaje(numero=1, nombre="Renato") # puedes decirle al argumento a donde ir si le asignas al nonbre del parametro de la funcion 
print(numero) 

#RETURN en funciones
def funcion_aburrida():
	print("'Modo aburrimiento' ON.")
	return 123	
# retur solo hace que la funcion finalice pero con una exprecion, 
# develve el valor del return a la variable con la que fue invocada
print("¡Esta lección es interesante!")
valor=funcion_aburrida()
print("Esta lección es aburrida ...") 

#PRATICA FUNCIONES con año biciesto y numero de meses
#calculasi el año es bisiesto
def isYearLeap(year):
	if year < 1582 :
		return False
	elif year%400 == 0:
		return True
	elif year%4 == 0 and year%100 != 0 :
		return True
	else :
		return False

def daysInMonth(year, month):
	bisiesto= isYearLeap(year)
	if month == 2:
		if bisiesto == True:
			return 29
		else:
			return 28
	else:
		if month==4 or month==6 or month==9 or month==11:
			return 30
		else:
			return 31

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")

# PRACTIA FUNCIONES NUMERO PRIMO
def isPrime(num):
	c=0
	for i in range(2,num):
		if num%i == 0:
			c+= 1
	if c == 0:
		return True
	else:
		return False

for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()

#PRACTICA FUNCIONES CONVERTIR CONSUMO DE GASOLINA 
def l100kmtompg(liters):
	galon=liters/3.785411784
	return 62.1371192237/galon

def mpgtol100km(miles):
	kl=miles*1.609344
	return 3.785411784/kl*100

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))

#PRACTICA DE DICCIONARIOS
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"} #un diccionario, puede llevar cualquier variable
words = ['gato', 'leon', 'caballo']

for word in words:
    if word in dict: #Pregunta si el elemto del array esta en el dicionario
        print(word, "->", dict[word])
    else:
        print(word, "no está en el diccionario")

# FORMAS DE RECORER DICIONARIOS Y ORDEREDDIC
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

# con KEY
for key in dict.keys():
    print(key, "->", dict[key])
#con ITEMS
for spanish, french in dict.items():
    print(spanish, "->", french)
#con VALUES
for french in dict.values():
    print(french) #solo muestra el valor de cada key

#PARA JUNTAR DOS TUPLAS ARREGLOS O DICCIONARIOS
d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}

for elemento in (d1, d2):
    d3.update(elemento)

print(d3)
