# Crear un programa que pida 2 numeros y obtenga como resultado cual de ellos es par o si ambos lo son

numero1 = int(input('Ingrese el numero 1: '))
numero2 = int(input('Ingrese el numero 2: '))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print('Ambos numeros son pares')
elif numero1 % 2 == 0:
    print(f'El numero {numero1} es par')
elif numero2 % 2 == 0:
    print(f'El numero {numero2} es par')
else:
    print('Ningun numero es par')