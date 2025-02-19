"""Escribe un programa
que solicite al usuario un número y
determine si es par o impar."""

# Solicitar un número al usuario
numero = int(input("Ingresa un número entero: "))

# Determinar si el número es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")