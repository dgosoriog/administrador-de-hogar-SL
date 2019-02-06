import tkinter as tk
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
from tkinter import Label,Tk

from tkinter import filedialog

class PantallaGastos(tk.Frame):

    def validacion(gastos):
        montoG = txtMonto.get()
        ingreso = gastos.catG.get()
        fechaG= txtFecha.get()
        descripcionG= txtDescripcion.get()
        vacio = ""

        if (montoG != vacio and fechaG != vacio and descripcionG != vacio and ingreso != vacio):

            gastos.conexion()

        else:
            messagebox.showerror("ERROR", "POR FAVOR  LLENE TODOS LOS CAMPOS")

    def conexion(gastos):
        dbc = ("127.0.0.1", "root", "", "proyecto")
        db = pymysql.connect(dbc[0], dbc[1], dbc[2], dbc[3])  # abrir una coneccion con mysql
        cursor = db.cursor()  # obtener el cursor
        cursor.execute("SELECT VERSION()")  # consultar la version de mysql
        dato = cursor.fetchone()  # OBTENER UNA SOLA FILA
        catG =  gastos.catG.get()
        sql2 = "SELECT id_categoria_g FROM categoria_gasto where nombre_categoria_g='" + catG + "'"
        print(sql2)
        try:
            cursor.execute(sql2)
            results = cursor.fetchall()

            for row in results:
                a = int(row[0])
                print(a)
        except:
            print("Error")
        descripcionG = gastos.descripcionG.get()
        fechaG = gastos.fechaG.get()
        montoG = int(gastos.montoG.get())

        sql1 = "INSERT INTO gastos( id_categoria_g, descripcion_g,fecha_g, monto_g) VALUES ( '%d', '%s','%s', '%d')" % (a, descripcionG, fechaG, montoG)
        print(sql1)
        try:
            cursor.execute(sql1)
            db.commit()
            messagebox.showinfo("Guardado","Los datos han sido guardados")
        except:
            print("No se ha podido ingresar")

        cursor.execute("SELECT VERSION()")
        sql3 = "select sum(monto) from ingresos"

        try:
            cursor.execute(sql3)
            results = cursor.fetchall()
            for row in results:
                t = int(row[0])
                print(t)
        except:
            print("Error")

        gastos.totalGastos.set(t)
        return gastos.totalGastos

    def __init__(gastos, parent, controller):
     tk.Frame.__init__(gastos, parent)
     gastos.controller = controller


     nombre = ['Estacionamiento','Servicio Internet','Bares y Antros','Cine','Alimentos para mascotas']
     colorFondo  = "White"
     colorLetra = "Black"
     gastos.config(bd=30)
     gastos.config(relief="ridge")
     gastos.config(background=colorFondo)
     gastos.catG=StringVar()
     gastos.montoG=StringVar()
     gastos.descripcionG=StringVar()
     gastos.fechaG=StringVar()
     gastos.totalGastos=StringVar()


     labelMonto=Label(gastos,text="INGRESA EL MONTO DEL GASTO:",bg=colorFondo,fg = colorLetra,font=controller.title_font).grid(row=0,column=0,padx=10,pady=10)
     global txtMonto
     txtMonto=Entry(gastos,textvariable=gastos.montoG,bd=5,relief="sunken",width=25,font=("Helvetica",9))
     txtMonto.grid(row=0,column=1,padx=10,pady=10)

     labelIngreso = Label(gastos,text="CATEGORÍA DEL GASTO: ",bg=colorFondo,fg = colorLetra,font=controller.title_font).grid(row=1,column=0,padx=10,pady=10)

     combo = ttk.Combobox(gastos,textvariable=gastos.catG)
     combo.grid(row=1,column=1,padx=10,pady=10)
     combo['values'] = (nombre)
     combo.config(font=("Helvetica",9))

     labelFecha = Label(gastos, text="FECHA:", bg=colorFondo, fg=colorLetra, font=controller.title_font).grid(row=2, column=0,padx=10, pady=10)
     global txtFecha
     txtFecha = Entry(gastos, textvariable=gastos.fechaG, text="año/mes/dia", bd=5, relief="sunken",width=25,font=("Helvetica",9))
     txtFecha.grid(row=2,column=1,padx=10,pady=10)

     labelDescripcion=Label(gastos,text="DESCRIPCIÓN:",bg=colorFondo,fg = colorLetra,font=controller.title_font).grid(row=3,column=0,padx=10,pady=10)
     global txtDescripcion
     txtDescripcion=Entry(gastos,bd=5,relief="sunken",textvariable=gastos.descripcionG,width=25,font=("Helvetica",9))
     txtDescripcion.grid(row=3,column=1,padx=10,pady=10)



     global txtSaldo
     labelSaldo=Label(gastos,text="TOTAL DE GASTOS:",bg=colorFondo,fg = "Red",font=controller.title_font).grid(row=4,column=0,padx=10,pady=10)
     txtSaldo=Entry(gastos,text=gastos.totalGastos,bd=5,relief="sunken",width=25,bg="#FFFF00",fg="Red",font=("Helvetica",9)).grid(row=4,column=1,padx=10,pady=10)

     btnAtras = Button(gastos,text="ATRAS",font=controller.title_font,bd=10,relief="groove",command=lambda: controller.show_frame("PantallaMenu")).grid(row=5,column=0,padx=10,pady=10)
     btnGuardar = Button(gastos,text="GUARDAR",font=controller.title_font,bd=10,relief="groove",command = gastos.validacion).grid(row=5,column=1,padx=10,pady=10)


         
