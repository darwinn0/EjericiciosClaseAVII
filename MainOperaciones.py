# Invocamos la clase de Operaciones.

import os
os.system('cls' if os.name== 'nt' else 'clear')

from Clase02 import OperacionesAritmeticas


a=int(input("Por favor ingrese el primer numero: "))
b=int(input("Por favor ingrese el segundo numero: "))

calculo = OperacionesAritmeticas(a,b)
calculo.suma()
calculo.resta()
calculo.multiplicacion()
calculo.division()
