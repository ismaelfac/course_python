class Perro:
    
     # constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f"CLase Perro: {self.nombre}"
    
    
    def habla(self):
        print(f"{self.nombre} dice: Guau!")
    
    
perro = Perro("Lucas", 7)
print(perro)