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

# kwargs 

def get_products(**data):
    #print(data)
    return data["id"], data["title"]

print(get_products(id="23", title="Iphone 8", description="Iphone 15 plus", value="2390"))
print(get_products(id="24", title="Iphone 15", description="Iphone 8 plus", value="1390"))