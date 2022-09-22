import random
print('ingrese una pregunta:')
P = str(input())

R = random.randint(1, 5)
if R == 1:
    print('claramente si')
elif R == 2:
    print('probablemente')
elif R == 3:
    print('no lo sé')
elif R == 4:
    print('probablemente no')
else:
    print('definitivamente no')
