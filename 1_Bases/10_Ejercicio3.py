# Obtener el radio y longitud de un circulo
# area = pi * r**2
# longitud = 2 * pi * r
import math

radio = float(input('Ingrese el radio del circulo: '))

area = math.pi * radio**2
long = 2 * math.pi * radio

print(f'La longitud del circulo es: {long:.2f} y el area es: {area:.2f}')