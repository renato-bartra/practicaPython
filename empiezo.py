print("holaaa") 
#la coma introduce un estacio entre cada argumento
print('hoa', "holaaaaaa")

#escapes dentro de una cadena se  hace com \ y algo mas
print("estamos\naqui")
print("\\")

#armuneto de palabras clave

#end 
print("estamos", end=" ")
print("argumento de palabra clave")

suma = "3+5"
print("matematica", end=suma)
print()

#sep separador
print("estamos","animados",sep="-")

#combinado
print("mi","nombre",sep="..",end="* ")
print("terminator","conor", sep=",,,", end="/.\n")

#practica
print("jjjj",end="*")
print("mmmmm "*2)
print('hhhhh')
print("qqqqq")

#sistema de numeracion
#octal
print(0o123)
#hexadecimal
print(0x123)

#valores boleanos
print(True > False)
print(True < False)

#practica
print('"Estoy"\n', '""aprendiendo""\n', '"""Python"""')

#operaores logicos

#** exponecial
#/ divicion siempre sera valor flotante
print(8 / 4)
#// diviion entera
print(6 // 4) # aca saldra 1 por que es el valor redondeado de la divicion pero se redondea hacia el valor menor
print(6. //4) # en este caso saldra 1.0 ya que el .6 obliga a ser flotante
print(-6 // 4)# aca saldra 2 por que es el valor redondeado de la divicion pero se redondea hacia el valor menor
print(6. // -4)

#variables

a=3
b=4
c=(a**2 + b**2)**0.5
print("c=",c)

# codifica aquí tus datos de prueba.
x = float(1)
y = 3*x**3 - 2*x**2 + 3*x -1
print("y =", y)

#funciones

kilometros = 12.25
millas = 7.38
millas_a_kilometros = millas * 1.61
kilometros_a_millas = kilometros / 1.61
#round se usa para limitar el numero de decimales de un flotante, este caso a 2 decimales
print(millas, " millas son ", round(millas_a_kilometros, 2), " kilómetros ")
print(kilometros, " kilómetros son ", round(kilometros_a_millas, 2), " millas ")

#funcion input para insertar datos
print("Dime algo...")
algo = input()
print("Mmm...", algo, "...¿en serio?")
#al usar input lo como string y se usa int o float para pasarlo a numero
algo = float(input("Inserta un número: "))
resultado = algo ** 2.0
print(algo, "al cuadrado es", resultado)

#practica
y=1/(x+(1/(x+(1/(x+(1/x))))))

#Practica calcular la hora
hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

tota_min = hora*60+min+dura
Hora = tota_min//60
Min = tota_min%60

print("termina a las: ", str(Hora)+":"+str(Min))