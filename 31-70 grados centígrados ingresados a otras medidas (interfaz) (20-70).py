# Para comenzar, importar los módulos correspondientes:
import tkinter as tk
from tkinter import Entry, ttk

def convertir_temp(): #creo la función para convertir los grados centigrados a grados kelvin y fahrenheit
    temp_centigrados = float(caja_temp_centigrados.get()) #creo la variable con los grados centigrados y le asigno el valor ingresado en la caja
    temp_kelvin = temp_centigrados + 273.15
    temp_fahrenheit = ( temp_centigrados * (9/5)) + 32
    etiqueta_temp_kelvin.config(text=f"Temperatura en K: {temp_kelvin}") #declaro que el texto de la etiqueta felvin cambie para mostrar el resultado
    etiqueta_temp_fahrenheit.config(text=f"Temperatura en °F: {temp_fahrenheit}") #declaro que el texto de la etiqueta fahrenheit cambie para mostrar el resultado

ventana = tk.Tk() #crear la ventana
ventana.title('conversor de temperatura') #título de la ventana
ventana.config(width= 300, height= 200) #configurar el tamaño de la ventana (width: ancho, height: alto)

etiqueta_grados_centigrados = ttk.Label(text="Temperatura en grados °C:") #creo el texto de los grados centígrados
etiqueta_grados_centigrados.place(x=20, y=20) #establezco la posición del texto respecto a la esquia superior izquierda

caja_temp_centigrados = ttk.Entry() #creo la caja en la cual almaceno el número ingresado
caja_temp_centigrados.place(x=170, y=20, width=60) #establezco la posición de la caja

boton_convertir = ttk.Button(text="convertir", command= convertir_temp) #creo el botón para iniciar la conversión y llamo a la función
boton_convertir.place(x=20, y=60) #establezco la posición del botón

etiqueta_temp_kelvin = ttk.Label(text= "Temperatura en K: n/a") #creo el texto con los grados kelvin
etiqueta_temp_kelvin.place(x=20, y=120) #establezco su posición

etiqueta_temp_fahrenheit = ttk.Label(text= "Temperatura en °F: n/a") #cre el texto con los grados fahrenheit
etiqueta_temp_fahrenheit.place(x=20, y=160) #establezco su posición
 
ventana.mainloop()#finalizo el ciclo de la ventana
