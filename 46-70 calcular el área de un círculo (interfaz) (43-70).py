import tkinter as tk
from tkinter import Entry, ttk

nada = "n/a"

def convertir():
 Radio = int(caja_radio.get())
 Area = 3.14159265359 * (Radio * Radio)
 etiqueta_area.config(text= f"El área de el círculo es: {Area}") 

ventana = tk.Tk()
ventana.title('Área de un circulo') 
ventana.config(width= 300, height= 200)

etiqueta_radio = ttk.Label(text="Radio del círculo: ") 
etiqueta_radio.place(x=20, y=20) 

caja_radio = ttk.Entry() 
caja_radio.place(x=120, y=20, width=60)

etiqueta_area = ttk.Label(text= f"El área de el círculo es: {nada}")
etiqueta_area.place(x=20, y=60)

boton_convertir = ttk.Button(text="Iniciar", command= convertir) 
boton_convertir.place(x=20, y=100)

ventana.mainloop()
