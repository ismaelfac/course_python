class Perro:
    patas: 4
    # constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def habla(self, patas):
        print(f"{self.nombre} tiene {self.edad} años, tienen {patas} patas y dice: Guau!")

        
mi_perro = Perro("Laika", 8)
mi_perro.habla(6)
print(isinstance(mi_perro, Perro))
Perro.patas = 3
print(mi_perro.patas)
mi_perro2 = Perro("Lucas", 12)
mi_perro2.patas = 5
print(mi_perro2.nombre, mi_perro2.patas)

