NUMBER = 1
while NUMBER < 100:
    print(NUMBER)
    NUMBER *= 2
print("termino en", NUMBER)

COMANDO = ""
while COMANDO.lower() != "salir":
    COMANDO = input("$ ")
    print(COMANDO)