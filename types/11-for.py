FIND_NUMBER = 10
for number in range(11):
    print(number)
    if number == FIND_NUMBER:
        print("Encontrado ", FIND_NUMBER)
        break
    else:
        print("Numero no encontrado ")