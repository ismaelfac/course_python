class Model():
    table = False

    def __init__(self) -> None:
        if not self.table:
            print("Error tienes que definir una tabla")

    def save(self):
        print(f"Guardando {self.table}")

    @classmethod
    def find_by_id(self, _id):
        print(f"Buscando por id {_id} en la tabla {self.table}")
    

class User(Model):
    table = "User"

user = User()

user.save()
user.find_by_id(123)