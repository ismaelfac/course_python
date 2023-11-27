
from abc import ABC, abstractmethod

class Model(ABC):

    @property
    @abstractmethod
    def table(self):
        pass
    
    @abstractmethod
    def save(self):
        pass

    @classmethod
    def find_by_id(self, _id):
        print(f"Buscando por id {_id} en la tabla {self.table}")
    

class User(Model):
    table = "User"
    
    def save(self):
        print("Guardando usuario")


user = User()
user.save()
user.find_by_id(123)