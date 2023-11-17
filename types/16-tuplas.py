# Las tuplas a diferencia de las listas, no se pueden modificar
numers = (1,2,3) + (4,5,6)
print(numers)

punto = tuple([1,2])
print(punto)

primero, segundo, *otros = numers
print(primero, segundo, otros)