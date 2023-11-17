# Los sets se pueden trabajar similar a las listas
# Los sets no se encuentran ordenados y no podemos acceder a un elemento de estos sets
primer_set = {1,1,2,2,3,4}
primer_set.add(4)
print(primer_set)

segundo_set = [3,4,5]
segundo_set = set(segundo_set)
print(segundo_set)
# union - primer set con segundo set
print("Union ",primer_set | segundo_set)

# intercepcion
print("intercepcion ",primer_set & segundo_set)

# diferencia
print("diferencia ",primer_set - segundo_set)

# Diferencia simetrica
print("Diferencia simetrica", primer_set ^ segundo_set)