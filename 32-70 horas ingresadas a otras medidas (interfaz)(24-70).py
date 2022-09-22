import tkinter as tk
from tkinter import Entry, ttk

def convertir():
 horas = int(caja_horas.get())
 minutos = horas * 60
 segundos = minutos * 60
 dias = horas / 24
 etiqueta_temp_segundos.config(text=f"Tiempo en segundos: {segundos}") 
 etiqueta_temp_minutos.config(text=f"Tiempo en minutos: {minutos}")
 etiqueta_temp_dias.config(text=f"Tiempo en días: {dias}")

ventana = tk.Tk()
ventana.title('Conversor de medida de tiempo') 
ventana.config(width= 300, height= 300)

etiqueta_horas = ttk.Label(text="Cantidad de horas:") 
etiqueta_horas.place(x=20, y=20) 

caja_horas = ttk.Entry() 
caja_horas.place(x=130, y=20, width=60) 

boton_convertir = ttk.Button(text="convertir", command= convertir) 
boton_convertir.place(x=20, y=60) 

etiqueta_temp_segundos = ttk.Label(text= "Tiempo en segundos: n/a") 
etiqueta_temp_segundos.place(x=20, y=120) 

etiqueta_temp_minutos = ttk.Label(text= "Tiempo en minutos: n/a") 
etiqueta_temp_minutos.place(x=20, y=160) 

etiqueta_temp_dias = ttk.Label(text= "Tiempo en dias: n/a") 
etiqueta_temp_dias.place(x=20, y=200) 

ventana.mainloop()
