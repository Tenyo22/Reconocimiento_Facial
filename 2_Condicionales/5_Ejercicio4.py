# Crear un programa que simule un cajero automatico con un saldo inicial de $2000 con el sig. menu
# 1.- Ingreso de dinero
# 2.- Retirar dinero
# 3.- Mostrar dinero
# 4.- Salir

saldo = 2000

while True:
    print('')
    print('1.- Ingreso de dinero')
    print('2.- Retiro de dinero')
    print('3.- Mostrar de dinero')
    print('4.- Salir')
    
    seleccion = int(input('Elija una opcion: '))
    print('')

    if seleccion == 1:
        ingreso = float(input('Dinero a ingresar: '))
        saldo += ingreso
        print(f'El nuevo saldo es de: {saldo}')
    elif seleccion == 2:
        retiro = float(input('Dinero a retirar: '))
        if retiro > saldo:
            print('Saldo insuficiente')
        else:
            saldo -= retiro
            print(f'El nuevo saldo es de: {saldo}')
    elif seleccion == 3:
        print(f'El saldo disponible es de: {saldo}')
    elif seleccion == 4:
        print('Fin')
        break
    else:
        print('Error de entrada de datos')
        
