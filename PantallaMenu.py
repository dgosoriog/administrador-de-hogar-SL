import tkinter as tk
from tkinter import *
class PantallaMenu(tk.Frame):

#gastos = PhotoImage(file="gastos.png")
#saldo = PhotoImage(file="saldo.png")
#salir = PhotoImage(file="salir.png")


    def __init__(self, parent, controller):

     tk.Frame.__init__(self, parent)
     self.controller = controller
     colorFondo  = "White"
     colorBoton = "Black"
     colorLetra = "White"
     self.config(bd=30)
     self.config(relief="ridge")
     self.config(background=colorFondo)
     ingresos = tk.PhotoImage(file="ingresos.png")
     ingresos.imge=ingresos
     gastos = tk.PhotoImage(file="gastos.png")
     gastos.imge=gastos
     saldo = tk.PhotoImage(file="saldo.png")
     saldo.imge=saldo
     reporte = tk.PhotoImage(file="reporte.png")
     reporte.imge=reporte
     labelActividad=Label(self,text="SELECCIONA TU ACTIVIDAD:",bg="White",fg = "Orange",font=("Helvetica",12)).grid(row=0,column=0,padx=10,pady=10)
     btnIng =    Button(self,text="INGRESOS",image=ingresos,compound="top",bd=10,relief="groove",command=lambda: controller.show_frame("PantallaIngresos")).grid(row=1,column=0,padx=10,pady=10)
     btnGastos = Button(self,text="GASTOS", image=gastos,compound="top",bd=10,relief="groove",command=lambda: controller.show_frame("PantallaGastos")).grid(row=1,column=1,padx=10,pady=10)
     btnSaldo = Button(self,text="SALDO",image=saldo,compound="top",bd=10,relief="groove",command=lambda: controller.show_frame("PantallaSaldo")).grid(row=2,column=0,padx=10,pady=10)
     btnReporte = Button(self,text="REPORTES",image=reporte,compound="top",bd=10,relief="groove").grid(row=2,column=1,padx=10,pady=10)
