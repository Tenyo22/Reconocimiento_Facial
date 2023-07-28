# Funciones en listas
'''

array = ['Futbol', 'PC', 18.6, 18, [6, 7, 10.4], True, False]

# Agregar
array.append(66)
array.append(True)

array.insert(1, 88) # Posicion para ingresarlo en la lista y elemento a agregar
array.extend([1, 75, 100, True])

# print(len(array))
# print(array)

array2 = [200, 250, 'Hola']

array3 = array + array2
print(array3)


# Buscar
# print('PC' in array3)
# print('Indice de PC:', array3.index('PC'))

# Repeticiones
# print('Hay', array3.count('PC'), 'PC')
# print('Hay', array3.count('Hola'), 'Hola')
# print('Hay', array3.count(True), 'True')

# Cambiar posicion
# array3.reverse()
# print(array3)

# Eliminar
array3.remove(True)
print(array3)
array3.clear()
print(array3)
'''

array = [1, 2, 8, -11, 14]
# array.sort()
array.sort(reverse=True)

print(array)