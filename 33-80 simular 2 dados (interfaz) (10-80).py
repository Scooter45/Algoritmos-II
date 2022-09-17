import random
import tkinter as tk
from tkinter import Entry, ttk

def Tiro():
 Dado1 = random.randint(1, 6)
 Dado2 = random.randint(1, 6)
 etiqueta_dado1.config(text=f"Resultado del 1er dado: {Dado1}")
 etiqueta_dado2.config(text=f"Resultado del 2do dado: {Dado2}")

ventana = tk.Tk()
ventana.title('Simulación de 2 dados') 
ventana.config(width= 250, height= 150)

etiqueta_dado1 = ttk.Label(text= "Resultado del 1er dado: n/a") 
etiqueta_dado1. place(x=20, y=20)

etiqueta_dado2 = ttk.Label(text= "Resultado del 2do dado: n/a") 
etiqueta_dado2. place(x=20, y=60) 

boton_tirar = ttk.Button(text="Tirar dados", command= Tiro) 
boton_tirar.place(x=20, y=100) 

ventana.mainloop()