lista1 = [1,2,3,4,5]

lista2 = [5,6]

combinada = ["Hola", *lista1, "Mundo", *lista2, "Todos"]
print(combinada)

punto1 = {"x": 19}
punto2 = {"y": 20}
puntoCombinado = {**punto1, **punto2}
print(puntoCombinado)

punto3 = {"x": 19, "y": "hola"}
punto4 = {"y": 20}
puntoCombinado2 = {**punto3, "title": "Hola Mundo", **punto4}
print(puntoCombinado2)
