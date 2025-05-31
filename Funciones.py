# funciones 

import os
os.system('cls' if os.name== 'nt' else 'clear')

#Definimos la funicon
def saludo (nombre):
    print(f"Hola {nombre}!")

def _PI():
    return 3.1416

def suma(a,b):
    return a+b


#Invocamos la funcion.
saludo ("Darwin Guzman.")

#Calcular el diametro del circulo.
r=1
diametro=2*_PI()*r
print(f"Diametro: {diametro}")

#Funcions suma
print(f"Funcion suma: {suma(1,1)}")
