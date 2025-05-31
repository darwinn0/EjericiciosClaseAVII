# Programa que va hacer las tablas de multiplicar con el ciclo while.

import os
os.system('cls' if os.name== 'nt' else 'clear')

tabla=5
i=1
while i <= 10:
    print(f"{tabla} X {i} = {tabla*i}")
    i += 1
    