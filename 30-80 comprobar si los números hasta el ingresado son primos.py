def calculo(numero):
 numero = inicio
 contador=0
 for i in range(2,numero):
   if numero % i == 0:
     contador+=1
 if contador>0:
   print(f'el numero {numero} no es primo')
 else:
  print(f'el número {numero} es primo')

inicio = 0
final = int(input('ingrese un valor límite para evaluar'))

while inicio <= final:
    calculo(inicio)
    inicio = inicio+1