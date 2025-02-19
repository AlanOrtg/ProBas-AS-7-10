"""Ejercicio 7: Calculadora de IMC
Descripción: Escribe un programa
que calcule el Índice de Masa
Corporal (IMC) de una persona,
dado su peso y altura. El IMC se
calcula con la fórmula:
IMC =peso (kg) /
altura (m)2
"""

# Solicitar el peso y la altura al usuario
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

# Calcular el IMC utilizando la fórmula: IMC = peso / altura^2
imc = peso / (altura ** 2)

# Mostrar el resultado del IMC
print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

# Clasificación según el IMC
if imc < 18.5:
    print("Estás por debajo del peso ideal.")
elif 18.5 <= imc < 24.9:
    print("Tienes un peso saludable.")
elif 25 <= imc < 29.9:
    print("Tienes sobrepeso.")
else:
    print("Tienes obesidad.")