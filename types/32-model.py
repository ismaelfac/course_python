class Model():
    table = False

    def __init__(self) -> None:
        if not self.table:
            print("Error tienes que definir una tabla")

    def save(self):
        print(f"Guardando {self.table}")

    def find_by_id(self, id):
        print(f"Buscando por id {_id}")
    

class User(Model):
    table = "User"

user = User()

user.save()