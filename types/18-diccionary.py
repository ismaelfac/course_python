punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])
 
punto["z"] = 45
# Sale error
# print(punto, punto["lalala"])

if "lalala" in punto:
    print("Encontre a lalala ", punto["lalala"])
    
print(punto.get("x"))
print(punto.get("lalala", 97))
del punto["x"]
print(punto)

punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])