numero = int(input('ingrese un numero'))
contador=0
for i in range(2,numero):
  if numero % i == 0:
    contador+=1
if contador>0:
  print('el numero no es primo')
else:
  print('el número es primo')
