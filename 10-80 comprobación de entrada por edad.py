Nom = str(input('nombre del usuario :'))
Doc = int(input('número de documento del usuario :'))
Ed = int(input('edad del usuario :'))
Tarifa = 450
if Ed < 18:
  print('el usuario 'f'{Nom} con número de documento 'f'{Doc} no tiene permitido el acceso al ser menor de edad')
else:
  print('el usuario 'f'{Nom} con número de documento 'f'{Doc} puede ingresar despues de pagar una tarifa de 'f'{Tarifa}')