import random

print('ingrese una lista de nombres separados por una coma y un espacio para barajarlos y obtener un orden aleatorio (ej: pedro, josé, hernesto, juan)')
nombres = list(map(str, input().split(',')))
random.shuffle(nombres)
print(nombres)