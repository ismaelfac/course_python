mascotas = ["Gato", "Perro", "Caballo", "Gallo", "Oso"]

for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
    
# Buscar elementos
ELEMENT = "Gato"

print(mascotas)
if ELEMENT in mascotas:
    print(mascotas.index(ELEMENT)) 
    mascotas.remove(ELEMENT) 
    print(mascotas)
    mascotas.pop()
    mascotas.append(ELEMENT)
    del mascotas[1]
    print(mascotas)
    mascotas.clear
    print("Mascotas: ",mascotas)
    
    # ordenamiento Listas