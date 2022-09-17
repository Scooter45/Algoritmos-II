import random
import tkinter as tk
from tkinter import Entry, ttk

nada = "n/a"

def aleatorio():
 Min = int(caja_min.get())
 Max = int(caja_max.get())
 Re = random.randint(Min, Max)
 etiqueta_aleatorio.config(text= f"El número aleatorio resultante fué {Re}") 
 print(Re)

ventana = tk.Tk()
ventana.title('Número aleatorio en un intervalo') 
ventana.config(width= 300, height= 200)

etiqueta_min = ttk.Label(text="Numero mínimo en el intervalo: ") 
etiqueta_min.place(x=20, y=20) 

caja_min = ttk.Entry() 
caja_min.place(x=200, y=20, width=60)

etiqueta_max = ttk.Label(text="Numero máximo en el intervalo: ") 
etiqueta_max.place(x=20, y=60) 

caja_max = ttk.Entry() 
caja_max.place(x=200, y=60, width=60)

boton_convertir = ttk.Button(text="Iniciar", command= aleatorio) 
boton_convertir.place(x=20, y=140)

etiqueta_aleatorio = ttk.Label(text= f"El número aleatorio resultante fué {nada} ")
etiqueta_aleatorio.place(x=20, y=100)

ventana.mainloop()