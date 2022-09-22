import tkinter as tk
from tkinter import Entry, ttk

nada = "n/a"

def conversion():
 Metros = float(caja_metros.get())
 Pies = Metros * 3.281
 etiqueta_pies.config(text=f"La cantidad ingresada equivale a {Pies} pies aproximadamente") 

ventana = tk.Tk()
ventana.title('Metros a Pies') 
ventana.config(width= 300, height= 200)

etiqueta_metros = ttk.Label(text="Cantidad de metros: ") 
etiqueta_metros.place(x=20, y=20) 

caja_metros = ttk.Entry() 
caja_metros.place(x=135, y=20, width=60)

boton_convertir = ttk.Button(text="Operar", command= conversion) 
boton_convertir.place(x=20, y=60)

etiqueta_pies = ttk.Label(text= f"La cantidad ingresada equivale a {nada} pies ")
etiqueta_pies.place(x=20, y=100)

ventana.mainloop()
