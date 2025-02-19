"""""Escribe un programa
que solicite al usuario dos números
y determine cuál es mayor, menor o
si son iguales."""

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Comparar los números y mostrar el resultado
if num1 > num2:
    print(f"El primer número ({num1}) es mayor que el segundo ({num2}).")
elif num1 < num2:
    print(f"El primer número ({num1}) es menor que el segundo ({num2}).")
else:
    print(f"Ambos números son iguales: {num1} = {num2}.")