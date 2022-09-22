import tkinter as tk
from tkinter import Entry, ttk

def calcular_iva():
 precio = int(caja_precio.get())
 iva = ( precio / 100 ) * 19
 total = iva + precio
 etiqueta_iva.config(text=f"Iva del producto: {iva}")
 etiqueta_total.config(text=f"Total a pagar: {total}") 

ventana = tk.Tk()
ventana.title('Calcular IVA') 
ventana.config(width= 300, height= 200)

etiqueta_precio = ttk.Label(text="Precio del producto: ") 
etiqueta_precio.place(x=20, y=20) 

caja_precio = ttk.Entry() 
caja_precio.place(x=130, y=20, width=60)

boton_calcular = ttk.Button(text="Operar", command= calcular_iva) 
boton_calcular.place(x=20, y=60)

etiqueta_iva = ttk.Label(text= "Iva del producto: ")
etiqueta_iva.place(x=20, y=100)

etiqueta_total = ttk.Label(text= "Total a pagar: ")
etiqueta_total.place(x=20, y=140)

ventana.mainloop()
