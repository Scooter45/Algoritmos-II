días = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
r = 0
while r < 1:
  busqueda =  input('que día quiere buscar en la lista?:')
  if busqueda in días:
    r = 1
    print('el día si se encuentra en la lista')
    print('-')
    print('fin')
  else:
    print('el día no se encuentra en la lista o no fue escrito de manera correcta')
  print('-')
