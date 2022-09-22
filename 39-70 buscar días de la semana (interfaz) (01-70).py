import tkinter as tk
from tkinter import Entry, ttk

días = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

r = 0
def busqueda():
 busqueda =  str(caja_dia.get())
 if busqueda in días:
  etiqueta_resultado.config(text= "el día si se encuentra en la lista")
 else:
  etiqueta_resultado.config(text= "el día no se encuentra en la lista o no fue escrito de manera correcta")

ventana = tk.Tk()
ventana.title('PBuscar un día de la semana') 
ventana.config(width= 400, height= 160)

etiqueta_dia = ttk.Label(text="Día de la semana: ") 
etiqueta_dia.place(x=20, y=20) 

caja_dia = ttk.Entry() 
caja_dia.place(x=120, y=20, width=60)

boton_convertir = ttk.Button(text="Buscar", command= busqueda) 
boton_convertir.place(x=20, y=60)

etiqueta_resultado = ttk.Label(text= f"")
etiqueta_resultado.place(x=20, y=100)

ventana.mainloop()
