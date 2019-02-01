from tkinter import *
ventana = Tk()
ventana.geometry("450x500")
ventana.config(bd=30)
colorFondo  = "White"
#DimGray
ventana.configure(background=colorFondo)
ventana.config(relief="groove")
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
bntIng = Button(ventana, image=ingresos,bd=10,relief="groove").grid(row=0,column=0,padx=10,pady=10)
#place(x=130,y=15)
btnGastos = Button(ventana, image=gastos,bd=10,relief="groove").grid(row=0,column=1,padx=10,pady=10)
#place(x=130,y=160)
btnSaldo = Button(ventana,image=saldo,bd=10,relief="groove").grid(row=1,column=0,padx=10,pady=10)
btnSaldo = Button(ventana,image=reporte,bd=10,relief="groove").grid(row=1,column=1,padx=10,pady=10)
ventana.mainloop()
