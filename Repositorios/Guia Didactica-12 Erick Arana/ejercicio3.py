#Crea un programa que permita al usuario crear una lista de compras
with open ("compras.txt", "w", encoding="utf-8") as C:
  while True:
    Producto=input("Ingrese un producto a la lista (Ingrese Fin para terminar): ")
    if Producto == "Fin":
        break
    else:
        C.write(f"{Producto}\n")
        
print("La lista ha sido guardada exitosamente")