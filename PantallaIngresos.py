import tkinter as tk
from tkinter import *
from tkinter import ttk
class PantallaIngresos(tk.Frame):



    def __init__(self, parent, controller):
     tk.Frame.__init__(self, parent)
     self.controller = controller
     nombre = ['Sueldo','Ventas','Honorarios','Inversion','Otros']
     colorFondo  = "White"
     colorLetra = "Black"
     monto=StringVar()
     self.config(bd=30)
     self.config(relief="ridge")
     self.config(background=colorFondo)
     labelMonto=Label(self,text="INGRESA EL MONTO DEL INGRESO:",bg=colorFondo,fg = colorLetra,font=("Comic Sans MS",8)).grid(row=0,column=0,padx=10,pady=10)
     txtMonto=Entry(self,textvariable=monto,bd=5,relief="sunken",width=22,font=("Comic Sans MS",8)).grid(row=0,column=1,padx=10,pady=10)
     labelIngreso = Label(self,text="TIPO DE INGRESO: ",bg=colorFondo,fg = colorLetra,font=("Comic Sans MS",8)).grid(row=1,column=0,padx=10,pady=10)
     combo = ttk.Combobox(self)
     combo.grid(row=1,column=1,padx=10,pady=10)
     combo['values'] = (nombre)
     combo.config(font=("Comic Sans MS",8))
     labelDescripcion=Label(self,text="DESCRIPCIÓN:",bg=colorFondo,fg = colorLetra,font=("Rouge",10)).grid(row=2,column=0,padx=10,pady=10)
     txtDescripcion=Text(self,width=19,height=5,bd=5,relief="ridge").grid(row=2,column=1,padx=10,pady=10)
     labelSaldo=Label(self,text="TOTAL DE INGRESOS:",bg=colorFondo,fg = colorLetra,font=("Helvetica",10)).grid(row=3,column=0,padx=10,pady=10)
     txtSaldo=Entry(self,bd=5,relief="sunken",width=25,bg="#FFFF00",fg="Red").grid(row=3,column=1,padx=10,pady=10)
     guardar=PhotoImage(file="guardar.png")
     #atras=PhotoImage(file="atras.png")
     btnGuardar = Button(self,text="Guardar",bd=14,relief="groove",cursor="hand2").grid(row=4,column=1,padx=10,pady=10)
     btnAtras = Button(self,text="Atras",bd=14,relief="groove",cursor="hand2",command=lambda:controller.show_frame("PantallaMenu")).grid(row=4,column=0,padx=10,pady=10)
