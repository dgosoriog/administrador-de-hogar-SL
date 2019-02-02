from tkinter import *
import PantallaIngresos
ventana = Tk()
ventana.geometry("500x550")
ventana.config(bd=30)
colorFondo  = "White"
#DimGray
ventana.configure(background=colorFondo)
ventana.config(relief="ridge")
ventana.config(cursor="hand2")
ventana.title("INGRESOS GASTOS MOVIMIENTOS")
ventana.resizable(False,False)
colorBoton = "Black"
colorLetra = "White"
ingresos = PhotoImage(file="ingresos.png")
gastos = PhotoImage(file="gastos.png")
saldo = PhotoImage(file="saldo.png")
salir = PhotoImage(file="salir.png")
reporte = PhotoImage(file="reporte.png")
labelActividad=Label(ventana,text="SELECCIONA TU ACTIVIDAD:",bg="White",fg = "Orange",font=("Helvetica",12)).grid(row=0,column=0,padx=10,pady=10)
bntIng = Button(ventana, image=ingresos,bd=10,relief="groove",command=PantallaIngresos.runIngresos).grid(row=1,column=0,padx=10,pady=10)
#place(x=130,y=15)
btnGastos = Button(ventana, image=gastos,bd=10,relief="groove").grid(row=1,column=1,padx=10,pady=10)
#place(x=130,y=160)
btnSaldo = Button(ventana,image=saldo,bd=10,relief="groove").grid(row=2,column=0,padx=10,pady=10)
btnSaldo = Button(ventana,image=reporte,bd=10,relief="groove").grid(row=2,column=1,padx=10,pady=10)
ventana.mainloop()
