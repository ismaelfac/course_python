def hello(last_name, first_name):
    print("Welcome")
    print(f"{last_name} {first_name} al sistema")


hello("Lastre Alvarez", "Ismael Enrique")
hello(last_name="Vasquez Cuesta", first_name="Valeria")

# xargs

def suma(*NUMBERS):
    RESULT = 0
    for NUMBER in NUMBERS:
        RESULT += NUMBER
    print(RESULT) 

suma(2,3,7,8,9)
suma(3,7)
suma(23,456,34,123,22)