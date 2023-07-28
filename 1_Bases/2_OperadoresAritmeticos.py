# Operadores Aritmeticos
n1 = 3
n2 = 5
suma = n1 + n2
resta = n2 - n1
negacion = -n2
multiplicacion = n1 * n2
potencia = n1 ** n1
division = n2 / n1
divisionEntera = n2 // n1
modulo = n2 % n1

print('Suma:', suma)
print('Resta:', resta)
print(n2, ' -> Negacion:', negacion)
print('Multiplicacion:', multiplicacion)
print(n1, 'Exponente:', n1, '-> Potencia:', potencia)
print('Division de {} / {} -> {}'.format(n2, n1, division))
print(f'Division entera de {n2} / {n1} -> {divisionEntera}')
print('Modulo de {} / {} -> {}'.format(n2, n1, modulo))

r = (5 + 9 / 3)**2
print(r)