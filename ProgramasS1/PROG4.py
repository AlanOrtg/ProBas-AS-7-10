"""Ejercicio 4: Clasificación de Edad
Descripción: Escribe un programa
que solicite al usuario su edad y
determine si es un niño (menor de 12
años), adolescente (menos de 18),
adulto (menos de 60) o adulto mayor
(60 o más).
"""

# Solicitar la edad al usuario
edad = int(input("Ingresa tu edad: "))

# Determinar la categoría de edad
if edad < 12:
    print("Eres un niño.")
elif edad < 18:
    print("Eres un adolescente.")
elif edad < 60:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")