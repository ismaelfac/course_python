class Perro:
    patas = 4
    
     # constructor
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        

    def habla(self):
        print(f"{self.__nombre} y dice: Guau!")

    # Factory Method
    @classmethod
    def factory(cls):
        return cls("Lucas feliz", 12)

perro1 = Perro.factory()
perro1.habla()
print(perro1.get_nombre())
print(perro1.__dict__)
print(perro1._Perro__nombre)