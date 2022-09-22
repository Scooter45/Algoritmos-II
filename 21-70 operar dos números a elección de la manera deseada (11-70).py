#listas con las palabras clave
adicion = ["suma"]
sustraccion = ["resta"]
multiplicar = ["multiplicacion"]
dividir = ["division"]
terminar = ["fin"]

while 2 == 2:
  #valores que se van a operar
  a = int(input('Ingrese el primer valor a operar: '))
  b = int(input('Ingrese el segundo valor a operar: '))
  #se toma la accíon a realizar
  print('Que acción quiere realizar (suma, resta, multiplicacion o division)?')
  accion = str(input())
  
  if accion in terminar:#condicional para romper el bucle
    break
  else:
    valorinutil = 0
  #funciones
  def suma(a,b):
    S = a + b
    print(S)
  def resta(a,b):
    R = a - b
    print(R)
  def multiplicacion(a,b):
    M = a * b
    print(M)
  def division(a,b):
    D = a / b
    print(D)
  #condicionales para saber que acción tomar  
  if accion in adicion:
    suma(a,b)
    print('-')
  elif accion in sustraccion:
    resta(a,b)
    print('-')
  elif accion in multiplicar:
    multiplicacion(a,b)
    print('-')
  elif accion in dividir:
    division(a,b)
    print('-')
  else:# mensaje en caso de no encontrar la acción a tomar
    print('escriba la accíon a tomar de manera correcta')
    print('-')
  print('cuando haya terminado, escriba "fin" en la accion a realizar')
  print('-')
