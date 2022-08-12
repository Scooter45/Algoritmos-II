precio = int(input('Ingrese el precio del producto al cual desea calcular el IVA: '))
iva = ( precio / 100 ) * 19
total = iva + precio
print('el IVA del producto es :'f'{iva}')
print('el valor total a pagar es :'f'{total}')