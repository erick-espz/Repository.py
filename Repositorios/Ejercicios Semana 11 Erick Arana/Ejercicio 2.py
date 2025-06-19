def calcular_comision(ventas, porcentaje_comision):
    #Calcula la comisión total por las ventas.
    return ventas * porcentaje_comision

def calcularSueldoTotal(sueldo_base, comision_total):
    return sueldo_base + comision_total

try:
    numeroVendedores = int(input("Ingrese el número de vendedores: "))
    sueldoBase = float(input("Ingrese el sueldo base de cada vendedor: "))
    montoVenta = float(input("Ingrese el monto de cada venta: "))
    
    porcentaje_comision = 0.10  
    VentasPorVendedor = 3     
    
    for i in range(numeroVendedores):
        comision = calcular_comision(montoVenta * VentasPorVendedor, porcentaje_comision)
        sueldo_total = calcularSueldoTotal(sueldoBase, comision)
        
        print(f"\nVendedor {i+1}:")
        print(f"Comisión por las tres ventas: ${comision:.2f}")
        print(f"Sueldo total con comisiones: ${sueldo_total:.2f}")

except ValueError:
    print(" ingrese valores numéricos válidos")