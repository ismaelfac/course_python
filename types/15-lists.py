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
    
users = [
    ["Luis", 4],
    ["Maria", 2],
    ["Fernando", 5]
]
names = []
for user in users:
    names.append(user[0])

#Otra forma - comprension de listas
#map
names_compacto = [user[0] for user in users]
#filter
names_filter = [user[0] for user in users if user[1] > 2] #Lista de comprension
print(names)
print(names_compacto)
print(names_filter)

names = list(map(lambda user: user[0], users)) # map
print(names)

namesMenus = list(filter(lambda user: user[1] > 2, users))
print(namesMenus)
