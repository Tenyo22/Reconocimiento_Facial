# Pasar la ecuacion a una expresion algoritmica
# Ecuacion: ( (c + 5) (b**2 - 3ac)a**2 ) / 4a

a = float(input('Ingrese el valor de a: '))
b = float(input('Ingrese el valor de b: '))
c = float(input('Ingrese el valor de c: '))

result = ((c + 5) * (b**2 - 3*a*c)*a**2) / (4*a)
print(f'El resultado es: {result}')