def TablaMult(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Solicitar el número al usuario
try:
    numero = int(input("Ingrese un número entero: "))
    TablaMult(numero)
except ValueError:
    print("Por favor, ingrese un número válido.")