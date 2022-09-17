B= int(input('Ingrese la cantidad de Bytes: '))
KB = B / 1024
MB = KB / 1024
GB = MB / 1024
TB = GB / 1024
PB = TB / 1024

print('La cantidad ingresada tiene las siguientes equivalencias:')
print(f'{KB} kilobytes')
print(f'{MB} megabytes')
print(f'{GB} gigabytes')
print(f'{TB} terabytes')
print(f'{PB} petabytes')