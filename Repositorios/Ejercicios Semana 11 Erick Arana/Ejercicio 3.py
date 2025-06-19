def calcular_descuento_renta(salario):
    return salario * 0.10

# Solicitar cantidad de empleados
try:
    numEmpleados = int(input("Ingrese la cantidad de empleados: "))

    for i in range(numEmpleados):
        salario = float(input(f"Ingrese el salario del empleado {i+1}: "))
        descuento = calcular_descuento_renta(salario)
        salarioT = salario - descuento

        print(f"\nEmpleado {i+1}:")
        print(f"Salario bruto: C${salario:.2f}")
        print(f"Descuento de renta: C${descuento:.2f}")
        print(f"Salario neto a pagar: C${salarioT:.2f}")

except ValueError:
    print("ingrese valores numéricos válidos.")