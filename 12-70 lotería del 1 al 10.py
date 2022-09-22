import random

lotería = random.randint(0, 10)
número = int(input('ingrese un valor del 1 al 10'))
if 1 <= número <= 10:
    print('el número resultante de la lotería fue'f'{lotería}, y el número jugado fue {número}')
    if lotería == número:
        print('el Usuario ganó el premio')
    else:
        print('el usuario no ganó el premio')
else:
    print('el número ingresado en el rango pedido, reinicie el programa e ingrese un número entre el rango necesitado')
