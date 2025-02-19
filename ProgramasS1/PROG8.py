"""Ejercicio 8: Calculadora de Año
Bisiesto
Descripción: Escribe un programa
que determine si un año dado es
bisiesto o no. Un año es bisiesto si es
divisible por 4, pero no por 100, a
menos que también sea divisible por
400."""

# Solicitar el año al usuario
anio = int(input("Ingresa un año: "))

# Determinar si el año es bisiesto o no
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")