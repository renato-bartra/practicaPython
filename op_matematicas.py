#PARA SABER SI CON TRES LADOS SE PUEDE HACERUN TRIANGULO
def esUnTriangulo (a, b, c):
    return a + b > c and b + c > a and c + a > b # devuelve True caso contrario False

print(esUnTriangulo (1, 1, 1)) #si se puede 
print(esUnTriangulo (1, 1, 3)) #no se puede

#PARA SABER SI ES UN TRIANGULO RECTANGULO
def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b

def esUnTrianguloRectangulo(a, b, c):
    if not esUnTriangulo  (a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2

print(esUnTrianguloRectangulo(5, 3, 4)) # True
print(esUnTrianguloRectangulo(1, 3, 4)) # False

#PARA SABER EL FACTORIAL DE UN NUMERO
def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    producto = 1
    for i in range(2, n + 1):
        producto *= i
    return producto

for n in range(1, 6):
    print(n, factorialFun(n))

#SERIE FIBONACHI
def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

for n in range(1, 10): # probando
    print(n, "->", fib(n))

#FACTORIAL CON RECURSIVIDAD
def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1 #hasta aca le dices que ya no siga recorriendo el for porque lo frenas con los return
    return n * factorialFun(n - 1) 

for n in range(1, 6):
    print(n, factorialFun(n))

lst = [[x for x in range(3)]for y in range(3)]

for r in range(3):
	for c in range(3):
		if lst[r][c]%2 != 0:
			print ("#")