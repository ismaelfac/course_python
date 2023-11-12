WELCOME = """Bienvenidos a la calculadora
Escribe Salir para Salir de la calculadora
Las operaciones son suma, resta, multi y div
"""
print(WELCOME)
NUM1 = input("Ingrese un numero: ")
OP = input("Ingrese la operacion: ")
NUM2 = input("Ingrese otro numero: ")
N1 = int(NUM1)
N2 = int(NUM2)

while OP.lower() != "salir":
    if OP == "suma":
        print(N1 + N2)   
    if OP == "resta":
        print(N1 - N2)  
    if OP == "multi": 
        print(N1 * N2)  
    if OP == "div":
        print(N1 / N2)  
    OP = input("Ingrese la operacion: ")