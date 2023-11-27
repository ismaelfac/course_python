try:
    n1 = int(input("ingresa un numero: "))
except Exception as e:
    print("ocurrio un error: ", type(e))
    
try:
    n1 = int(input("ingresa otro numero: "))
except ValueError as e:
    print("Ingrese un valor numerico: ")
except NameError as e:
    print("ocurrio un error")
    
try:
    n1 = int(input("ingresa otro tercer numero: "))
except ValueError as e:
    print("ocurrio un error")
else:
    print("Bien hecho: ")

try:
    n1 = int(input("ingresa otro cuarto numero: "))
except ValueError as e:
    print("ocurrio un error")
finally:
    print("Se ejecuta siempre: ")