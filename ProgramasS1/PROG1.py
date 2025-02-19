"""Escribe un programa
que solicite al usuario dos números
enteros y realice las operaciones
aritméticas básicas (suma, resta,
multiplicación, división, división de
piso y residuo) entre ellos. Muestra
los resultados en pantalla."""

num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))

# Realizar las operaciones aritméticas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "Error: División entre cero"
division_piso = num1 // num2 if num2 != 0 else "Error: División entre cero"
residuo = num1 % num2 if num2 != 0 else "Error: División entre cero"

# Mostrar los resultados
print(f"\nResultados de las operaciones con los números {num1} y {num2}:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"División de piso: {division_piso}")
print(f"Residuo: {residuo}")