# Crear un programa que pida 3 numeros y determine cual es mayor

n1 = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))
n3 = int(input('Ingrese el segundo numero: '))

if n1 >= n2 and n1 >= n3:
    print(f'El numero mayor es {n1}')
elif n2 >= n1 and n2 >= n3:
    print(f'El numero mayor es {n2}')
elif n3 >= n1 and n3 >= n2:
    print(f'El numero mayor es {n3}')