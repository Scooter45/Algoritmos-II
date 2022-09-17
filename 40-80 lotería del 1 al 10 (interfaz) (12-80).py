import random
import tkinter as tk
from tkinter import Entry, ttk

nada = 'n/a'

def aleatorio():
 lotería = random.randint(0, 10)
 número = int(caja_número.get())
 if 1 <= número <= 10:
    if lotería == número:
        etiqueta_resultado.config(text=f'''el número resultante de la lotería fue {lotería}, y el número jugado fue {número}
    el Usuario ganó el premio''')
    else:
        etiqueta_resultado.config(text=f'''el número resultante de la lotería fue {lotería}, y el número jugado fue {número}
    el usuario no ganó el premio''')
 else:
    etiqueta_resultado.config(text= f'''el número ingresado no está en el rango pedido
reinicie el programa e ingrese un número entre el rango necesitado''')


ventana = tk.Tk()
ventana.title('Número aleatorio en un intervalo') 
ventana.config(width=500, height= 200)

etiqueta_número = ttk.Label(text="Ingrese un número del 1 al 10: ") 
etiqueta_número.place(x=20, y=20) 

caja_número = ttk.Entry() 
caja_número.place(x=200, y=20, width=60)

boton_convertir = ttk.Button(text="Jugar", command= aleatorio) 
boton_convertir.place(x=20, y=60)

etiqueta_resultado = ttk.Label(text= f'el número resultante de la lotería fue {nada}, y el número jugado fue {nada}')
etiqueta_resultado.place(x=20, y=100)

ventana.mainloop()