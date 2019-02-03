import tkinter as tk
from tkinter import *
class PantallaSaldo(tk.Frame):
    def __init__(saldo, parent, controller):
     tk.Frame.__init__(saldo, parent)
     saldo.controller = controller
     label = tk.Label(saldo, text="This is page 1", font=controller.title_font)
     colorFondo  = "White"
     colorLetra = "Black"
     saldo.config(bd=30)
     saldo.config(relief="ridge")
     saldo.config(background=colorFondo)
     monto=StringVar()
     saldo.configure(background=colorFondo)
     labelIngreso=Label(saldo,text="TOTAL DE INGRESOS:",bg=colorFondo,fg = colorLetra,font=("Comic Sans MS",8)).grid(row=0,column=0,padx=10,pady=10)
     txtIngreso=Entry(saldo,bd=5,relief="sunken",width=25,bg="#FFFF00",fg="Red").grid(row=0,column=1,padx=10,pady=10)
     labelgasto = Label(saldo,text="TOTAL DE GASTOS: ",bg=colorFondo,fg = colorLetra,font=("Comic Sans MS",8)).grid(row=1,column=0,padx=10,pady=10)
     txtGasto=Entry(saldo,bd=5,relief="sunken",width=25,bg="#FFFF00",fg="Red").grid(row=1,column=1,padx=10,pady=10)
     labelSaldo = Label(saldo,text="SALDO: ",bg=colorFondo,fg = colorLetra,font=("Comic Sans MS",8)).grid(row=2,column=0,padx=10,pady=10)
     txtSaldo=Entry(saldo,bd=5,relief="sunken",width=25,bg="#FFFF00",fg="Red").grid(row=2,column=1,padx=10,pady=10)
     btnAtras = Button(saldo,text="ATRAS",bd=10,relief="groove",command=lambda: controller.show_frame("PantallaMenu")).grid(row=4,column=0,padx=10,pady=10)
     btnGuardar = Button(saldo,text="GUARDAR",bd=10,relief="groove").grid(row=4,column=1,padx=10,pady=10)
