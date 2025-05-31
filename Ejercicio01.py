#Elaborar un programa que muestre el total de un solo producto calcualando el impuesto sobre venta y dar un descuento 
#solo cuando el importe de la compra sea mayor a 10000 el importe sera de un 25%
import os
os.system("cls")

Isv=0.15

cantidad= int(input("Por favor ingrese la cantidad: "))
if cantidad >= 10000:
    Descuento=0.25
else:
    Descuento=0
TotalCompra= cantidad - (cantidad * Descuento)
TotalCompra= TotalCompra + (TotalCompra * Isv)
print(f"El total de la compra es : {TotalCompra}")