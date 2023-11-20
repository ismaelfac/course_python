class Perro:
    patas = 4
    
     # constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    #Trasforma este metodo en un metodo propio de la clase perro
    @classmethod
    def habla(cls):
        print(" y dice: Guau!")

    # Factory Method
    @classmethod
    def factory(cls):
        return cls("Lucas feliz", 12)

Perro.habla()
perro1 = Perro("Lucas", 4)
perro2 = Perro("Laika", 4)

# With methos Factory
perro3 = Perro.factory()
print(perro3.nombre, perro3.edad)