class Animal:
    
    def comer(self):
        print("comiendo")
        

class Perro(Animal):
    def pasear(self):
        print("paseando")
        
class Chanchito(Perro): #Herencia multi-Nivel
    def programar(self):
        print("programando")
        
perro = Perro()
chanchito = Chanchito()
perro.comer()
chanchito.comer()