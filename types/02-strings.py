COURSE_NAME = "Lorem itsu"
print(len(COURSE_NAME))
print(COURSE_NAME[5:9])
print(COURSE_NAME[5:])

LAST_NAME = "Lastre Alvarez"
FIRST_NAME = "Ismael Enrique"
full_name = f"  {LAST_NAME} {FIRST_NAME} with {30 + 9} years old"
print(full_name.upper())
print(full_name.lower())
print(full_name.strip().capitalize())
print(full_name.title())
print(full_name.strip())
print(full_name.rstrip())
print(full_name.find("ca"))
print(full_name.replace("La","LLa"))
print("Is" in full_name)
print("La" not in full_name)