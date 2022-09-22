import tkinter as tk
from tkinter import Entry, ttk

nada = "n/a"

def convertir():
 Largo = int(caja_largo.get())
 Ancho = int(caja_ancho.get())
 Area = (Largo * Ancho) / 2
 etiqueta_area.config(text= f"El área de el rectangulo es: {Area}") 

ventana = tk.Tk()
ventana.title('Área de un rectangulo') 
ventana.config(width= 300, height= 200)

etiqueta_largo = ttk.Label(text="Largo del rectangulo: ") 
etiqueta_largo.place(x=20, y=20) 

caja_largo = ttk.Entry() 
caja_largo.place(x=130, y=20, width=60)

etiqueta_ancho = ttk.Label(text="Ancho del rectangulo:") 
etiqueta_ancho.place(x=20, y=60) 

caja_ancho = ttk.Entry() 
caja_ancho.place(x=140, y=60, width=60)

boton_convertir = ttk.Button(text="Iniciar", command= convertir) 
boton_convertir.place(x=20, y=140)

etiqueta_area = ttk.Label(text= f"El área de el triangulo es: {nada}")
etiqueta_area.place(x=20, y=100)

ventana.mainloop()
