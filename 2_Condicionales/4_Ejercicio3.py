# Crea un programa que compare dos nombres y verifique si hay coincidencias o no:
# si es que ambos nombres comienzan con la misma letra o si terminan con la misma letra

name1 = input('Ingrese el primer nombre: ')
name2 = input('Ingrese el segundo nombre: ')

if name1[0] == name2[0] or name1[-1] == name2[-1]:
    print('Si hay coincidencias')
else:
    print('No hay coincidencias')