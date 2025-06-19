def MenorTres(a, b, c):
    return min(a, b, c)

# Capturar tres números reales por teclado
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    
    print(f"El menor de los tres números es: {MenorTres(num1, num2, num3)}")
except ValueError:
    print("ingrese números válidos.")