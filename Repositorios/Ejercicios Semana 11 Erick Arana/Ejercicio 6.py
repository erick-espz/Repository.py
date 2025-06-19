import math

def CalcAreaC(radio):
    return math.pi * radio ** 2

# Capturar el radio del círculo por teclado
try:
    radio = float(input("Ingrese el radio del círculo: "))
    if radio < 0:
        print("Error, el radio no puede ser negativo.")
    else:
        print(f"El área del círculo es: {CalcAreaC(radio):.2f}")
except ValueError:
    print("ingrese un número válido.")