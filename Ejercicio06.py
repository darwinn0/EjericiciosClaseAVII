# Programa que va a calcular el descuento con funciones.

import os
os.system('cls' if os.name== 'nt' else 'clear')

def descuento(cantidad):
    if cantidad >= 10000:
        Descuento=0.25
    else:
        Descuento=0
    return Descuento
    

Isv=0.15

cantidad= int(input("Por favor ingrese la cantidad: "))
if cantidad >= 10000:
    descuento=0.25
else:
    descuento=0
TotalCompra= cantidad - (cantidad * descuento)
TotalCompra= TotalCompra + (TotalCompra * Isv)
print(f"El total de la compra es : {TotalCompra}")