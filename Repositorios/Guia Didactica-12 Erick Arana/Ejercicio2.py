#programa que pida al usuario el nombre de un archivo de texto.

NombreArchivo=input("Ingrese el nombre del archivo (.txt): ")
try:
   with open(NombreArchivo, "r", encoding="utf-8") as A:
    Longitud=A.readlines()
    print(f"La cantidad de lineas del archivo es de: ",len(Longitud))
except FileNotFoundError:
  print(f"El archivo -{NombreArchivo}- no fue encontrado")