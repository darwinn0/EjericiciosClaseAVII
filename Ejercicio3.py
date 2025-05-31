import os
os.system('cls' if os.name== 'nt' else 'clear')

#Ciclo for para mostrar las tablas de multiplicar que el usuario ingresa.

tabla = int(input("Por favor ingrese la tabla a multiplicar: "))

for i in range(1,11):
    print(f"{tabla} X {i} = {tabla*i}")