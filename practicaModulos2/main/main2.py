from sys import path #se usa para verificar la raiz de las carpetas
path.append('../modulos/paquetes/extra')
import iota
import ugly.omega , ugly.psi #se encuentra una carpeta dentro de la raiz que es lo que esta en path.append
#como esta dos carpetas dentro se importa de esta manera o como la de la siguiente linea
from good.best import sigma 
import good.best.tau as tau
# se encuentra una carpeta dentro
import good.alpha as alpha , good.beta as beta


print(iota.FunI())
print(ugly.omega.FunO())
print(ugly.psi.FunP())
print(sigma.FunS())
print(tau.FunT())
print(alpha.FunA())
print(beta.FunB())