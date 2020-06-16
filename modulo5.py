import math #se usa para importar todo el modulo de operaciones matematicas
print(math.sin(math.pi/2)) #se usa el namespace math. para que pithon sepa que te refieres a la libreria de math

from math import sin,pi #se usa para importar solo lo que queremos sin usar namespaces (math.sin(math.pi)
print(sin(pi/2)) #te bota 1.0 ya que es seno de pi/2 usa la libreria de math

pi = 3.14 #redefines los valores de pi y sin, y a sin o hace una funcion
def sin(x): 
    if 2 * x == pi:
        return 0.99999999
    else:
        return None
print(sin(pi/2))

from math import sin,pi # si volvemos a importar vuelve a usar los valores del modulo math

#o pudes importar una libreria dando un alias
import math as mate
print(mate.sin(mate.pi/2))

from math import pi as PI, sin as sine #tambien se pude dar alias a cada nombre 
print(sine(PI/2))

#si usamos dir() se nos dara la bilioteca de funciones de que tiene el modulo ose los nombres
import math
for name in dir(math): ,#dis() puede ir solo, pero se ve feo, asi que lo recorremos con un for para verse mejor
    print(name, end="\t")

#MODULO DE RANDOM

#genera numeros aleatorio del 0 al 1
from random import random
for i in range(5):
    print(random())

#genera numero aleatorios enteros del 1 al 10, 10 veces por el for
from random import randint
for i in range(10):
    print(randint(1, 10), end=',') 

#ES COMO LA TINKA QUE ESCOGE NUMEROS DE LA LISTA
from random import choice, sample
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(choice(lst)) #elige un numero aleatorio
print(sample(lst, 5)) #elige 5 numero aleatorio
print(sample(lst, 10)) #elige 10 numero aleatorio

#TRY Y EXCEPT
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
#los except llevan el nombre de error que envia python
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero.")
except: #si se toca ctrl + c se enviara esta exepcion
    print("Oh cielos, algo salio mal...")

print("THE END.")

#MANEJO DE EXEPCIONES
def badFun(n):
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        raise
#inicia el try y al parcer un error imboca el RISE e inicio el exept del primer try
try:
    badFun(0)
except ArithmeticError:
    print("¡Ya veo!")

print("FIN.")

#PRACTICA EXEPCIONES
def readint(prompt, min, max):
	if prompt > min and prompt < max:
		return prompt
	else:
		print("El valor no se encuentra en el rango permitido ",min,max)
		readint(int(input("Ingresa un numero de -10 a 10: ")), -10, 10)

try:
	v = readint(int(input("Ingresa un numero de -10 a 10: ")), -10, 10)
except ValueError:
	print("Por favor, introduzca solo numeros")
	v = readint(int(input("Ingresa un numero de -10 a 10: ")), -10, 10)
print("El numero es:", v)

#ASCII sacara el ascii de una caracter y viseversa
print(ord('a'))
print(chr(945))

#METODOS CON CADENAS

#verifica si termina con lo que dice en el endswith
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")

# se puede usar como cadena
v="valhala"
print(v[1:3])

# en que index se ecuentra una palabra
txt = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""
fnd = txt.find('the') #para encontrar una palabra en una cadena y decir su posicion
while fnd != -1:
    print(fnd)
    fnd = txt.find('the', fnd + 1) # usar find con dos parametros uno para la palabra y otra desde donde empieza a buscar

# pasa todo a minusculas
print("SiGmA=60".lower())

#pasa todo a mayusculas
print("Yo sé que no sé nada. Parte 2.".upper())

#elimina los espacios en blanco del inicio
print(" tau ".lstrip())
print("www.cisco.com".lstrip("w.")) #tambien eimina lo que deceas del principio, pasandolo con parametro

#lo mismo pero al reves, borra desde la derecha
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

#reemplazar una parte de la cadena por otra
print("www.netacad.com".replace("netacad.com", "pythoninsti"))

#devuelve una lista con elementos de la cadena, entiende que debe separaralos por los espacios
print("phi       chi\npsi".split())

#borra los espacios de ambos lados
print("[" + "   aleph   ".strip() + "]")

#ordena listas
firstGreek = ['omega', 'alfa', 'pi', 'gama']
firstGreek2 = sorted(firstGreek)
print(firstGreek)
print(firstGreek2)
print()
#ordena listas
secondGreek = ['omega', 'alfa', 'pi', 'gama']
print(secondGreek)
secondGreek.sort()
print(secondGreek)

#convertir de numero a cadena
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

#convertir de cadena a numero
si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)
