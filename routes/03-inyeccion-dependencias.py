# Case 1:
# class Perro:
#     def __init__(self, Correa) -> None:
#         self.correa = Correa()

# Case 2:
# import usuario

# def guardar():
#     usuario.guardar()
    
# def guardar(entidad):
#     entidad.guardar()

from pathlib import Path

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]
dependencias = {
    "db": "Data BASE",
    "api": "esta es la api",
    "graphql": "esto es graphql"
}

def load(p):
    #print(str(p))
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except:
        print("El paquete no tiene funcion init")
    
list(map(load, paths))
