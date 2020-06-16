from sys import path #se usa para verificar la raiz de las carpetas
path.append('../modulos')
import modulo as mm
import iota
import omega,psi

er= [0 for i in range(5)]
mur= [1 for i in range(5)]
print(mm.suml(er))
print(mm.prodl(mur))

