# Crear un algoritmo para intercambiar variables
# a = 20 -> a = 30
# b = 30 -> b = 20

a = int(input('Ingrese el valor de a: '))
b = int(input('Ingrese el valor de b: '))

b, a = a, b

print(f'Los nuevos valores son: a = {a}, b = {b}')