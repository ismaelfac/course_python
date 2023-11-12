EDAD = 25
if EDAD > 54:
    print("Puedes ver la pelicula con descuento")
elif EDAD > 18:
    print("Puedes ver la pelicula")
else:
    print("Lo siento, no puedes ver la pelicula")
    
## If ternario

MENSAJE = "Es mayor" if EDAD > 17 else "Es menor"

print(MENSAJE)

## Operadores logicos

GAS = True
ENCENDIDO = True
LAVADO = False
if GAS and ENCENDIDO:
    print("Puedes Avazar")
else:
    print("Quieto")

if GAS and (ENCENDIDO or LAVADO):
    print("Puedes Avazar")

# Cadena comparadores
if 15 <= EDAD <= 65:
    print("Puedes entrar a la piscina")