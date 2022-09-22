Hor = int(input('Ingrese la cantidad de horas: '))
Min = Hor * 60
Seg = Min * 60
Dia = Hor / 24
print('La cantidad de horas ingresadas equivale a 'f'{Min} minutos')
print('La cantidad de horas ingresadas equivale a 'f'{Seg} segundos')
if Dia >= 1:
  print('La cantidad de horas ingresadas equivale a 'f'{Dia} días')
