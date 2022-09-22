import tkinter as tk
from tkinter import Entry, ttk

nada = "n/a"

def operar():
 Num1 = int(caja_primer_numero.get())
 Num2 = int(caja_segundo_numero.get())
 Suma = Num1 + Num2
 Resta = Num1 - Num2
 Multiplicacion = Num1 * Num2
 Division = Num1 / Num2
 etiqueta_suma.config(text= f"{Num1} + {Num2} = {Suma}")
 etiqueta_resta.config(text= f"{Num1} - {Num2} = {Resta}")
 etiqueta_multiplicación.config(text= f"{Num1} × {Num2} = {Multiplicacion}")
 etiqueta_division.config(text= f"{Num1} ÷ {Num2} = {Division}")

ventana = tk.Tk()
ventana.title('Operar números') 
ventana.config(width= 300, height= 300)

etiqueta_primer_numero = ttk.Label(text="Ingrese el primer número a operar:") 
etiqueta_primer_numero.place(x=20, y=20) 

caja_primer_numero = ttk.Entry()
caja_primer_numero.place(x=210, y=20, width=60)

etiqueta_segundo_numero = ttk.Label(text="Ingrese el segundo número a operar:") 
etiqueta_segundo_numero.place(x=20, y=60) 

caja_segundo_numero = ttk.Entry()
caja_segundo_numero.place(x=220, y=60, width=60)

boton_operar = ttk.Button(text="Operar", command= operar) 
boton_operar.place(x=20, y=100) 

etiqueta_suma = ttk.Label(text= f"{nada} + {nada} = {nada}") 
etiqueta_suma.place(x=20, y=140) 

etiqueta_resta = ttk.Label(text= f"{nada} - {nada} = {nada}") 
etiqueta_resta.place(x=20, y=180) 

etiqueta_multiplicación = ttk.Label(text= f"{nada} × {nada} = {nada}") 
etiqueta_multiplicación.place(x=20, y=220)

etiqueta_division = ttk.Label(text= f"{nada} ÷ {nada} = {nada}") 
etiqueta_division.place(x=20, y=260) 

ventana.mainloop()
