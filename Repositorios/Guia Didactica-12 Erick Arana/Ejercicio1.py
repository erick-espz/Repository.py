#Programa "Diario" (Debe guardar una entrada de texto con fecha y hora actual)
#diario.txt Cada nueva entrada debe añadirse al final del archivo sin borrar las anteriores.

from datetime import datetime
texto=input("Ingrese el texto: \n")
HoraFecha=datetime.now()
with open("diario.txt", "a", encoding="utf-8") as D:
    D.write(f"{HoraFecha} - {texto}\n")
print("Tu texto fue guardado exitosamente")