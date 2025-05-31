#Crearemos la clase animal 

import os
os.system('cls' if os.name== 'nt' else 'clear')


class Animal:
    def __init__(self, nombre):
        self.nombre  = nombre

    def comer(self):
         print(f"{self.nombre} Esta comiendo ")
         
    def correr(self):
        print(f"Corraaaaaaaaaaaaaaaa que lo persigue el chupa cabras {self.nombre}")
    

class Perro(Animal):
    def ladrar (self):
        print("Grrrrrr Grrr Grrrrr")

class Gato(Animal):
    def maulla (self):
        print(f" {self.nombre} Miaaaaau Miauuuuuu ")

    
#definir objeto para usar la clase Perro

# miperro=Perro("Maria Juana")

# miperro.ladrar()
# miperro.correr()
# miperro.comer()

#Definir objeto para usar la clase Gato
migato = Gato("Candinga")

migato.maulla()
migato.comer()
migato.correr




# perro=Animal("Firulais")

# perro.correr()
# perro.ladrar()
# perro.comer()

