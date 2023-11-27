from abc import ABC, abstractmethod
class Model(ABC):
    @abstractmethod
    def save(self):
        pass
    
class User(Model):
    def save(self):
        print("Guardando en la bd")
        
class Sesion(Model):
    def save(self):
        print("Guardando en Archivo")
        

def save(entidades):
    for entidad in entidades:
        entidad.save()
    
    
user = User()
sesion = Sesion()

save([sesion, user])
