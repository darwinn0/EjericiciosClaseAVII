#Creamos la clase Opreaciones arimetricas

import os
os.system('cls' if os.name== 'nt' else 'clear')

class OperacionesAritmeticas:
    def __init__ (self, a,b):
        self.a = a
        self.b = b

    #Suma 
    def suma(self):
        return self.a + self.b
    
    #Resta
    def resta(self):
        return self.a - self.b
    
    #Multiplicacion
    def multiplicacion(self):
        return self.a * self.b
    
    #Division
    def division(self):
        return self.a / self.b
    
a=int(input("Por favor ingrese el primer numero: "))
b=int(input("Por favor ingrese el segundo numero: "))

print(f"La suma {a,b} es: ",OperacionesAritmeticas(a,b).suma())
print(f"La resta {a,b} es: ",OperacionesAritmeticas(a,b).resta())
print(f"La miltiplicacion {a,b} es: ",OperacionesAritmeticas(a,b).multiplicacion())
print(f"La divicion {a,b} es: ",OperacionesAritmeticas(a,b).division())