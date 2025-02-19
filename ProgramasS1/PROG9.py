"""Ejercicio 9: Calculadora de
Promedio
Descripción: Escribe un programa
que solicite al usuario tres
calificaciones y calcule el promedio."""

# Solicitar las tres calificaciones al usuario
calificacion1 = float(input("Ingresa la primera calificación: "))
calificacion2 = float(input("Ingresa la segunda calificación: "))
calificacion3 = float(input("Ingresa la tercera calificación: "))

# Calcular el promedio
promedio = (calificacion1 + calificacion2 + calificacion3) / 3

# Mostrar el promedio
print(f"El promedio de las calificaciones es: {promedio:.2f}")