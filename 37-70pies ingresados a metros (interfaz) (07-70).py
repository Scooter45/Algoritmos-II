import tkinter as tk
from tkinter import Entry, ttk

nada = "n/a"

def conversion():
 Pies = float(caja_pies.get())
 Metros = Pies / 3.281
 etiqueta_metros.config(text=f"La cantidad ingresada equivale a {Metros} pies aproximadamente") 

ventana = tk.Tk()
ventana.title('Pies a Metros') 
ventana.config(width= 500, height= 200)

etiqueta_pies = ttk.Label(text="Cantidad de pies: ") 
etiqueta_pies.place(x=20, y=20) 

caja_pies = ttk.Entry() 
caja_pies.place(x=130, y=20, width=60)

boton_convertir = ttk.Button(text="Operar", command= conversion) 
boton_convertir.place(x=20, y=60)

etiqueta_metros = ttk.Label(text= f"La cantidad ingresada equivale a {nada} metros ")
etiqueta_metros.place(x=20, y=100)

ventana.mainloop()
