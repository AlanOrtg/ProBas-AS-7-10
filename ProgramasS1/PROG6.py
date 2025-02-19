"""Ejercicio 6: Conversión de
Temperaturas
Descripción: Escribe un programa
que convierta una temperatura dada
en grados Celsius a grados
Fahrenheit y Kelvin."""

# Solicitar la temperatura en grados Celsius al usuario
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Realizar las conversiones a Fahrenheit y Kelvin
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

# Mostrar los resultados
print(f"{celsius} grados Celsius son equivalentes a:")
print(f"{fahrenheit} grados Fahrenheit.")
print(f"{kelvin} grados Kelvin.")


