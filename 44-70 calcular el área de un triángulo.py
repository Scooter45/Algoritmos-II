import tkinter as tk
from tkinter import Entry, ttk

nada = "n/a"

def convertir():
 Base = int(caja_base.get())
 Altura = int(caja_altura.get())
 Area = (Base * Altura) / 2
 etiqueta_area.config(text= f"El área de el triangulo es: {Area}") 

ventana = tk.Tk()
ventana.title('Área de un triángulo') 
ventana.config(width= 300, height= 200)

etiqueta_base = ttk.Label(text="Base del triangulo: ") 
etiqueta_base.place(x=20, y=20) 

caja_base = ttk.Entry() 
caja_base.place(x=130, y=20, width=60)

etiqueta_altura = ttk.Label(text="Altura del triangulo:") 
etiqueta_altura.place(x=20, y=60) 

caja_altura = ttk.Entry() 
caja_altura.place(x=140, y=60, width=60)

boton_convertir = ttk.Button(text="Iniciar", command= convertir) 
boton_convertir.place(x=20, y=140)

etiqueta_area = ttk.Label(text= f"El área de el triangulo es: {nada}")
etiqueta_area.place(x=20, y=100)

ventana.mainloop()
