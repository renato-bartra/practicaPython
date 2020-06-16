#!/user/bin/env python3

__contador=0

def suml(list):
	global __contador
	__contador += 1
	sum=0
	for el in list:
		sum += el
	return sum

def prodl(list):
	global __contador
	__contador+= 1
	prod=1
	for el in list:
		prod *= el
	return prod

#se veridifa si es ejecutado de forma independiente 
#osea desde el main(mostraria el nombre del modulo) 
#o desde el modulo que mostraria __main__
if __name__ == "__main__":
	print("prefiero ser un modulo pero puedo hacer unos test para ti")
	l = [i+1 for i in range(5)]
	print(suml(l) == 15)
	print(prodl(l) == 120)