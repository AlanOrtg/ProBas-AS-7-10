"""Ejercicio 5: Calculadora de
Descuento
Descripción: Escribe un programa
que solicite al usuario el precio de un
producto y el porcentaje de
descuento, y calcule el precio final
después del descuento"""

# Solicitar el precio del producto y el porcentaje de descuento al usuario
precio = float(input("Ingresa el precio del producto: "))
descuento = float(input("Ingresa el porcentaje de descuento: "))

# Calcular el precio final después del descuento
descuento_aplicado = (descuento / 100) * precio
precio_final = precio - descuento_aplicado

# Mostrar el precio final
print(f"El precio original es: {precio}")
print(f"El descuento aplicado es: {descuento_aplicado}")
print(f"El precio final después del descuento es: {precio_final}")