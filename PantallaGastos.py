import tkinter as tk
from tkinter import *
from tkinter import ttk
class PantallaGastos(tk.Frame):


    def __init__(gastos, parent, controller):
     tk.Frame.__init__(gastos, parent)
     gastos.controller = controller


     nombre = ['Estacionamiento','Servicio Internet','Bares y Antros','Cine','Alimentos para mascotas','Despensa del mes','Electricidad','Renta casa',
          'Servicios Médicos','Transporte públic','Pago Universidad']
     colorFondo  = "White"
     colorLetra = "Black"
     gastos.config(bd=30)
     gastos.config(relief="ridge")
     gastos.config(background=colorFondo)
     monto=StringVar()
     labelMonto=Label(gastos,text="INGRESA EL MONTO DEL GASTO:",bg=colorFondo,fg = colorLetra,font=("Comic Sans MS",8)).grid(row=0,column=0,padx=10,pady=10)
     txtMonto=Entry(gastos,textvariable=monto,bd=5,relief="sunken",width=22,font=("Comic Sans MS",8)).grid(row=0,column=1,padx=10,pady=10)
     labelIngreso = Label(gastos,text="CATEGORÍA DEL GASTO: ",bg=colorFondo,fg = colorLetra,font=("Comic Sans MS",8)).grid(row=1,column=0,padx=10,pady=10)
     combo = ttk.Combobox(gastos)
     combo.grid(row=1,column=1,padx=10,pady=10)
     combo['values'] = (nombre)
     combo.config(font=("Comic Sans MS",8))
     labelDescripcion=Label(gastos,text="DESCRIPCIÓN:",bg=colorFondo,fg = colorLetra,font=("Comic Sans MS",8)).grid(row=2,column=0,padx=10,pady=10)
     txtDescripcion=Text(gastos,width=19,height=5,bd=5,relief="sunken").grid(row=2,column=1,padx=10,pady=10)

     labelSaldo=Label(gastos,text="TOTAL DE GASTOS:",bg=colorFondo,fg = colorLetra,font=("Comic Sans MS",8)).grid(row=3,column=0,padx=10,pady=10)
     txtSaldo=Entry(gastos,bd=5,relief="sunken",width=25,bg="#FFFF00",fg="Red").grid(row=3,column=1,padx=10,pady=10)

     btnAtras = Button(gastos,text="ATRAS",bd=10,relief="groove",command=lambda: controller.show_frame("PantallaMenu")).grid(row=4,column=0,padx=10,pady=10)
     btnGuardar = Button(gastos,text="GUARDAR",bd=10,relief="groove").grid(row=4,column=1,padx=10,pady=10)


