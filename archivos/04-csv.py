import csv

# escribir
# with open("archivos/archivo.csv", "w", encoding="utf-8") as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["twit_id", "user_id", "text"])
#     writer.writerow([100, 1, "Twit number 1"])
#     writer.writerow([101, 2, "Twit number 2"])
    
# leer
with open("archivos/archivo.csv", encoding="utf-8") as archivo:
    reader = csv.reader(archivo)
    #print(list(reader))
    for linea in reader:
        print(linea)