"""Ejercicio 10: Calculadora de Área
de un Triángulo
Descripción: Escribe un programa
que calcule el área de un triángulo,
dados su base y altura. """

# Solicitar la base y la altura del triángulo al usuario
base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))

# Calcular el área del triángulo utilizando la fórmula: Área = (base * altura) / 2
area = (base * altura) / 2

# Mostrar el resultado
print(f"El área del triángulo es: {area:.2f}")

