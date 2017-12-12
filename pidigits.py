#Programa para calcular los digitos de Pi
#Creado por @neridev13

from math import *
import webbrowser
#from datetime import datetime

n = 2

respusta = 1

limite = int(input("Introduzca limite de suma: "))

#instanteInicial = datetime.now()

while limite >= n:
	respusta = 1/(n**2) + respusta
	n = n + 1
	print(respusta)
	print (n)


respusta = sqrt(6*(respusta))

"""Tiempo: Activalo si quieres saber cuanto tarda el programa en calcular
instanteFinal = datetime.now()
tiempo = instanteFinal - instanteInicial
segundos = tiempo.seconds
microsegundos = tiempo.microseconds
print(microsegundos,"microsegundos tardo en calcular o,", segundos,"segundos")"""

#Respuesta
print("\nEl programa calculo que pi es aproximadamente:",respusta)

espera = 0

while espera < 10000000:
	espera = espera + 1

if espera == 10000000:
	print("Si te ha servido este pequeño programa sigueme en Twitter")
	espera = 0
	while espera < 25000000:
		espera = espera + 1
	if espera == 25000000:
		webbrowser.open("https://twitter.com/neridev13")