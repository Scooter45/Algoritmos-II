print('ingrese los valores enteros separados por una coma y un espacio (ej: 6, 2, 5, 1)')
numeros = list(map(int, input().split(',')))
print(f'el número menor de la lista es {min(numeros)} y el número mayor de la lista es {max(numeros)}')
