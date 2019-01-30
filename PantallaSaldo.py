from tkinter import *
from tkinter import ttk
colorFondo  = "Black"
colorLetra = "White"

saldo = Tk()
saldo.geometry("450x500")

saldo.config(bd=30)
saldo.config(relief="sunken")
saldo.resizable(False,False)
guardar=PhotoImage(file="guardar.png")
atras=PhotoImage(file="atras.png")

monto=StringVar()

#DimGray
saldo.configure(background=colorFondo)
saldo.title("SALDO")
labelIngreso=Label(saldo,text="TOTAL DE INGRESOS:",bg=colorFondo,fg = colorLetra,font=("Comic Sans MS",8)).grid(row=0,column=0,padx=10,pady=10)
txtIngreso=Entry(saldo,bd=5,relief="sunken",width=25,bg="#FFFF00",fg="Red").grid(row=0,column=1,padx=10,pady=10)
labelgasto = Label(saldo,text="TOTAL DE GASTOS: ",bg=colorFondo,fg = colorLetra,font=("Comic Sans MS",8)).grid(row=1,column=0,padx=10,pady=10)
txtGasto=Entry(saldo,bd=5,relief="sunken",width=25,bg="#FFFF00",fg="Red").grid(row=1,column=1,padx=10,pady=10)
labelSaldo = Label(saldo,text="SALDO: ",bg=colorFondo,fg = colorLetra,font=("Comic Sans MS",8)).grid(row=2,column=0,padx=10,pady=10)
txtSaldo=Entry(saldo,bd=5,relief="sunken",width=25,bg="#FFFF00",fg="Red").grid(row=2,column=1,padx=10,pady=10)
btnAtras = Button(saldo,image=atras,bd=10,relief="groove").grid(row=4,column=0,padx=10,pady=10)
btnGuardar = Button(saldo,image=guardar,bd=10,relief="groove").grid(row=4,column=1,padx=10,pady=10)
saldo.mainloop()

