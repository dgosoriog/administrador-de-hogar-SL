from tkinter import *
from tkinter import ttk
nombre = ['Sueldo','Ventas','Honorarios','Inversion','Otros']
colorFondo  = "Black"
colorLetra = "White"

ingresos = Tk()
ingresos.geometry("450x500")

ingresos.config(bd=30)
ingresos.config(relief="sunken")
ingresos.resizable(False,False)
guardar=PhotoImage(file="guardar.png")
atras=PhotoImage(file="atras.png")

monto=StringVar()

#DimGray
ingresos.configure(background=colorFondo)
ingresos.title("AÑADIR INGRESOS")
labelMonto=Label(ingresos,text="INGRESA EL MONTO DEL INGRESO:",bg=colorFondo,fg = colorLetra,font=("Comic Sans MS",8)).grid(row=0,column=0,padx=10,pady=10)
txtMonto=Entry(ingresos,textvariable=monto,bd=5,relief="sunken",width=22,font=("Comic Sans MS",8)).grid(row=0,column=1,padx=10,pady=10)
labelIngreso = Label(ingresos,text="TIPO DE INGRESO: ",bg=colorFondo,fg = colorLetra,font=("Comic Sans MS",8)).grid(row=1,column=0,padx=10,pady=10)
combo = ttk.Combobox(ingresos)
combo.grid(row=1,column=1,padx=10,pady=10)
combo['values'] = (nombre)
combo.config(font=("Comic Sans MS",8))
labelDescripcion=Label(ingresos,text="DESCRIPCIÓN:",bg=colorFondo,fg = colorLetra,font=("Comic Sans MS",8)).grid(row=2,column=0,padx=10,pady=10)
txtDescripcion=Text(ingresos,width=19,height=5,bd=5,relief="sunken").grid(row=2,column=1,padx=10,pady=10)

labelSaldo=Label(ingresos,text="TOTAL DE INGRESOS:",bg=colorFondo,fg = colorLetra,font=("Comic Sans MS",8)).grid(row=3,column=0,padx=10,pady=10)
txtSaldo=Entry(ingresos,bd=5,relief="sunken",width=25,bg="#FFFF00",fg="Red").grid(row=3,column=1,padx=10,pady=10)


btnGuardar = Button(ingresos,image=guardar,bd=10,relief="groove").grid(row=4,column=0,padx=10,pady=10)
btnAtras = Button(ingresos,image=atras,bd=10,relief="groove").grid(row=4,column=1,padx=10,pady=10)
ingresos.mainloop()

