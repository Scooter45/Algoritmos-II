print('ingrese los valores enteros a ordenar separados por una coma y un espacio (ej: 3, 9, 1, 4)')
datos = list(map(int, input().split(',')))
datos.sort()
print(datos)