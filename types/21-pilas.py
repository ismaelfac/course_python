pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)
ultimoenlapila = pila.pop()
print(ultimoenlapila)

print(pila)
print(pila[-1])

if not pila:
    print("pila vacia")