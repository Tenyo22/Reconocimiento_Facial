# Obtener el precio final que se tiene que pagar si se aplica el 36% de descuento del total de la compra

precio = float(input('Ingrese el total de la compra: '))
descuento = 0.36

precio -= precio * descuento

print(f'El precio final es: {precio:.2f}')