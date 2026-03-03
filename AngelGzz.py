"""Escribe un programa en Python que pida al usuario su nombre y su año de nacimiento"""

año_actual = 2026

nombre = input("Introduce tu nombre: ")
año_nacimiento = int(input("Introduce tu año de nacimiento: "))

edad = año_actual - año_nacimiento

print(f"Hola, mi nombre es {nombre}. Nací en el año {año_nacimiento}.")
print(f"Actualmente tengo {edad} años y estoy aprendiendo a programar.")




"""Hallar la raíz cuadrada de número entero positivo.

"""

num = 25
resultado = num ** 0.5

print(f"El número es: {num}")
print(f"La raíz cuadrada es: {resultado}")  
"""Crear un programa para encontrar el área de un círculo, use la fórmula:

"""

PI = 3.14159
radio = 5

area = PI * (radio * radio)

print(f"El área es: {area}")
"""Hallar la potencia (número entero positivo) de un número entero positivo "a"."""

a = 2
n = 3

resultado = a ** n

print(f"La base es: {a}")
print(f"El exponente es: {n}")
print(f"El resultado es: {resultado}")
