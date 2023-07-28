import math

# numero = 0
# while numero < 20:
#     print(numero)
#     numero += 1

numero = int(input('Escriba un numero: '))

while numero < 0:
    print('Ingrese un numero positivo')
    numero = int(input('Escriba un numero positivo: '))

print(f'El resultado de la raiz cuadrada de {numero} es {math.sqrt(numero):.2f}')