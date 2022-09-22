import random

print('ingrese una lista de nombres separados por una coma y un espacio para elegir uno aleatorio (ej: pedro, josé, hernesto, juan)')
nombres = list(map(str, input().split(',')))
random.shuffle(nombres)
print(f'{nombres[0]}')
