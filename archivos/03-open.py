from io import open

# escritura
texto = "Hola Mundo"

# archivo = open("archivos/hola-mundo.txt", "w", encoding="utf-8")
# archivo.write(texto)
# archivo.close()

# archivo = open("archivos/hola-mundo.txt", "r", encoding="utf-8")
# texto = archivo.read()
# archivo.close()
# print(texto)

# archivo = open("archivos/hola-mundo.txt", "r", encoding="utf-8")
# texto = archivo.readlines()
# archivo.close()
# print(texto)

# ESta forma no requiere cerrar el archivo. se cierra el archivo
# automaticamente al terminar la funcion o si genera un error
# with
# with open("archivos/hola-mundo.txt", "r", encoding="utf-8") as archivo:
#     print(archivo.readlines())
    
# agregar
# archivo = open("archivos/hola-mundo.txt", "a+", encoding="utf-8")
# archivo.write("Chao Mundo :)")
# archivo.close()

# lectura y escritura
with open("archivos/hola-mundo.txt", "r+", encoding="utf-8") as archivo:
    texto =archivo.readlines()
    archivo.seek(0) # movemos el puntero al inicio
    texto[0] = "Esto es un texto de prueba"
    archivo.writelines(texto)