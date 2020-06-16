#PILAS EN PROCEDIMENTAL
pila = [1]

def push(val):
    pila.append(val)

def pop():
	try:
		if len(pila) > 1:
			val = pila[-1]
			del pila[-1]
			return val
		else:
			val = pila[0]
			del pila[0]
			return val
	except IndexError:
		print("no hay elementos en a lista")

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop()) 

#PILAS CON PROGRAMACION PRIENTADA A OBJETOS (POO)
#el parametro self tambien se usa para imbocar otros metodos self.otroMetodo()
class Pila:
	def __init__(self): #esto es un constructor,  (__init__ inicia siempre al instanciar la clase)
		self.__listaPila = [] #Esto es un atributo o propiedad osea las caracteriticas del objeto, que se hereda a los otros metodos

	def push(self, val): #esto es un metodo,ose las acciones que va a realizar el objeto
		self.__listaPila.append(val) #Esto es un atributo o propiedad

	def pop(self): #esto es un metodo
		try:
			if len(self.__listaPila) > 1:
				val = self.__listaPila[-1]
				del self.__listaPila[-1]
				return val
			else:
				val = self.__listaPila[0]
				del self.__listaPila[0]
				return val
		except IndexError:
			print("no hay elementos en a lista")

#esto es una subclase si le pasas como atributo la otra clase se heredan todos los metodos
class SumarPila(Pila): # se puede llamar a mas de una clase (clase1, clase2) y se hereda de izquierda a derecha
	def __init__(self):
		Pila.__init__(self) # para crear una subclase se inicia primero el contructor de la clase primaria
		self.__sum = 0

	def getSuma(self):
		return self.__sum # se guarada el atributo o propiedad en el objeto

	def push(self, val):
		self.__sum += val
		Pila.push(self, val)

	def pop(self):
		val = Pila.pop(self)
		self.__sum -= val
		return val

objetoPila = Pila() #esto es un objeto que instancia la clase
objetoPila2 = Pila() #creo un segundo objeto, para eso sierve el POO

pequeñaPila = Pila()
otraPila = Pila()
graciosaPila = Pila()

pequeñaPila.push(1)
otraPila.push(pequeñaPila.pop() + 1)
graciosaPila.push(otraPila.pop() - 2)

print(graciosaPila.pop())

objetoPila = SumarPila()
for i in range(5):
    objetoPila.push(i)
print(objetoPila.getSuma())
# el __dic__ devuelve un diccionario de del objeto
print(objetoPila.__dict__)
#verifica si existe un atributo en un objeto 
#hasattr(objetoEjemplo, 'b')

for i in range(5):
    print(objetoPila.pop())

#PRACTICA CLASES
class MiClase:
    # def __str__(self): este metodo devuelve un string, de auerdo a los atributos heredados
    # 	print ("algo")

obj = MiClase()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.entero = 4
obj.z = 5
obj2 = obj

def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'): #si empieza con i
            val = getattr(obj, name) # de acuerda un objeto devuelve su atributo
            if isinstance(val, int): # compueba si es un numero, tabien para saber si un objeto pertenece a una clase isinstance(obj, clase)
                setattr(obj, name, val + 1) # de acuerdo al objeto reemplaza su atributo por el ultimo parametro

print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)
print(obj.__dir__) #no tengo muy en claro para que sirve, pero vas a saber laclase en la que esta instanciada
print(obj2 is obj) #se usa oara verificar si son el mismo objeto

# EXCEPCIONES
def reciproco(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        n = None
    else: # se ejecutara igual, si y solo si no se ejecuto el exept
        print("Todo salió bien")
    finally: # se ejecutara no importa o que se haya heho antes
        print("Es el momento de decir adiós")
        return n

print(reciproco(2))
print(reciproco(0))

# PARA CONOCER TODAS LAS EXCEPCIONES DE PYTHON
def printExcTree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        printExcTree(subclass, nest + 1)

printExcTree(BaseException)

#ANATOMIA DE LAS EXCEPCIONES DE PYTHON
def printargs(args):
	lng = len(args)
	if lng == 0:
		print("")
	elif lng == 1:
		print(args[0])
	else:
		print(str(args))

try:
	raise Exception
except Exception as e:
	print(e, e.__str__(), sep=' : ' ,end=' : ')
	printargs(e.args)

try:
	raise Exception("mi excepción")
except Exception as e:
	print(e, e.__str__(), sep=' : ', end=' : ')
	printargs(e.args)

try:
	raise Exception("mi", "excepción")
except Exception as e:
	print(e, e.__str__(), sep=' : ', end=' : ')
	printargs(e.args)

# CREA TU PROPIA EXCEPCION en base a otra
class MyZeroDivisionError(ZeroDivisionError):	
	pass

def doTheDivision(mine):
	if mine:
		raise MyZeroDivisionError("peores noticias")
	else:		
		raise ZeroDivisionError("malas noticias")

for mode in [False, True]:
	try:
		doTheDivision(mode)
	except ZeroDivisionError:
		print('División entre cero')


for mode in [False, True]:
	try:
		doTheDivision(mode)
	except MyZeroDivisionError:
		print('Mi división entre cero')
	except ZeroDivisionError:
		print('División entre cero original')



# CREA TU PROPIA EXEPCION
class PizzaError(Exception): #inicias heredando la clase EXCEPT
    def __init__(self, pizza, mensaje):
        Exception.__init__(mensaje) #inicias el constructor de la clase primaria EXCEPT
        self.pizza = pizza	


class DemasiadoQuesoError(PizzaError): #puedes crear sub clases como un sub error
    def __init__(self, pizza, queso, mensaje):
        PizzaError._init__(self, pizza, mensaje)
        self.queso = queso

def makePizza(pizza, queso): # y le das las condiciones para que verifique las exepciones, creando una funcion
	if pizza not in ['margherita', 'capricciosa', 'calzone']:
		raise PizzaError(pizza, "no hay tal pizza en el menú")
	if queso > 100:
		raise DemasiadoQuesoError(pizza, queso, "demasiado queso")
	print("¡Pizza lista!")

# O PUEDES PASAR LAS CODICIONALES PARA QUE SEAN ESTATICAS EN EL MISMO EXCEPT
# class PizzaError(Exception):
#     def __init__(self, pizza='desconocida', mensaje=''):
#         Exception.__init__(self, mensaje)
#         self.pizza = pizza


# class DemasiadoQuesoError(PizzaError):
#     def __init__(self, pizza='desconocida', queso='>100', mensaje=''):
#         PizzaError.__init__(self, pizza, mensaje)
#         self.queso = queso


# def makePizza(pizza, queso):
# 	if pizza not in ['margherita', 'capricciosa', 'calzone']:
# 		raise PizzaError
# 	if queso > 100:
# 		raise DemasiadoQuesoError
# 	print("¡Pizza lista!")


#AHORA SE HACE LAS PRUEBAS DEL NUEO EXCEPT
for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
	try:
		makePizza(pz, ch)
	except DemasiadoQuesoError as tmce:
		print(tmce, ':', tmce.queso)
	except PizzaError as pe:
		print(pe, ':', pe.pizza)



#TU PROPIO GENERADOR, FOR (ITERADOR) PERO CON SERIE FIBONACHI
class Fib:
	def __init__(self, nn):
		print("__init__")
		self.__n = nn
		self.__i = 0
		self.__p1 = self.__p2 = 1

	def __iter__(self): # debe tener esto para ser considerado iterador
		print("__iter__")		
		return self

	def __next__(self):
		print("__next__")				
		self.__i += 1
		if self.__i > self.__n:
			raise StopIteration
		if self.__i in [1, 2]:
			return 1
		ret = self.__p1 + self.__p2
		self.__p1, self.__p2 = self.__p2, ret
		return ret

for i in Fib(10):
	print(i)


# CONTRUIR TU PROPIO GENERADOR, LAS PRIMERAS n POTENCIAS DE 2
def potenciasDe2(n):
    potencia = 1
    for i in range(n):
        yield potencia # yeld hace lo mismo que return pero sin terminar el bucle
        potencia *= 2

for v in potenciasDe2(8):
    print(v)


# GENERADOR FIBNACHI PERO GUARDADO EN UNA LISTA
def Fib(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(Fib(10))

print(fibs)

# OTRA FORMA DE USAR IF DENTRO DE UNA LISTA
lst = []

for x in range(10):
	# if no es una condicional, en este caso es un operador
    lst.append(1 if x % 2 == 0 else 0)

print(lst)

# LISTA Y GENERADOR
lst = [1 if x % 2 == 0 else 0 for x in range(10)] # se puede usar el for dentro de la lista
genr = (1 if x % 2 == 0 else 0 for x in range(10)) #por el parentecis se hace un generador

for v in lst:
    print(v, end=" ")
print()

for v in genr:
    print(v, end=" ")
print()

# En abos casos se recorre, solo que en la primera se crea una lista
# y en la segunda es un generador, solo hay valores subsequentes producidos por el generador, uno por uno.
for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()

for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()


#UTILIZACION DE LAMBDA, PARA VALORES MOMENTANEOS, ANONIMOS Y EVALUAR RESULTADOS 
def imprimirfuncion(args, fun):
	for x in args:
		print('f(', x,')=', fun(x), sep='')

def poli(x):
	return 2 * x**2 - 4 * x + 2

imprimirfuncion([x for x in range(-2, 3)], poli)


# AHORA USAMOS LAMBDA
def imprimirfuncion(args, fun):
	for x in args:
		print('f(', x,')=', fun(x), sep='')

imprimirfuncion([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)



#USO DEL MAP
lista1 = [x for x in range(5)]
lista2 = list(map(lambda x: 2 ** x, lista1))
print(lista2)
for x in map(lambda x: x * x, lista2):
	print(x, end=' ') # DEVUELVE UNA LISTA SIN CORCHETES
print()



#USO DEL FILTER
from random import seed, randint

seed()
data = [ randint(-10,10) for x in range(5) ] #GENERA DATOS ALEATORIOS DEL -10 AL 10
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))#FILTRA LOS QUE SON MAYOES A 0 Y PARES
print(data)
print(filtered)