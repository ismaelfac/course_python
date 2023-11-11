EDAD = 15
if EDAD > 54:
    print("Puedes ver la pelicula con descuento")
elif EDAD > 18:
    print("Puedes ver la pelicula")
else:
    print("Lo siento, no puedes ver la pelicula")
    
## If ternario

MENSAJE = "Es mayor" if EDAD > 17 else "Es menor"

print(MENSAJE)