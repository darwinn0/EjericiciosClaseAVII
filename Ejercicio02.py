import os
os.system('cls' if os.name== 'nt' else 'clear')

#Calcular la edad de una persona
fNacimiento=int(input("Por favor ingrese la fecha de nacimiento: "))
anioActual = 2025

edad = anioActual - fNacimiento
print (f"La edad que usted tiene es {edad}")

if edad >=21:
    print(f"ya tiene {edad} años, ya eres mayor de edad.")
else:
    if edad >= 18:
        print("ya eres cuidadano")
    print(f"ya tienes {edad} anios, eres menor de edad.")




