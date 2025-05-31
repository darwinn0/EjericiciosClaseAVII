#Opereaciones arimetricas con funciones.

import os
os.system('cls' if os.name== 'nt' else 'clear')

# Definimos la funcion
def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b

def potencia(a,b):
    return a**b

print(f"La suma es: {suma(3,4)}")
print(f"La resta es {resta(5,4)}")
print(f"La multiplicacion es {multiplicacion(2,2)}")
print(f"La division es {division(10,2)}")
print(F"La potencia es {potencia(2,3)}")
