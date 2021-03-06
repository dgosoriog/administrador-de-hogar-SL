import tkinter as tk
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
from tkinter import Label,Tk
import PantallaSaldo
class PantallaIngresos(tk.Frame):
    def validacion(self):
        monto=txtMonto.get()
        ingreso=self.cat.get()
        fecha = txtFecha.get()
        descripcion = txtDescripcion.get()
        vacio=""

        if(monto!=vacio  and fecha!=vacio and descripcion!=vacio and  ingreso!=vacio):

                self.conexion()

        else:
            messagebox.showerror("ERROR","POR FAVOR  LLENE TODOS LOS CAMPOS")

    def conexion(self):
        dbc = ("127.0.0.1", "root", "", "proyecto")
        db = pymysql.connect(dbc[0], dbc[1], dbc[2], dbc[3])  # abrir una coneccion con mysql
        cursor = db.cursor()  # obtener el cursor
        cursor.execute("SELECT VERSION()")  # consultar la version de mysql
        dato = cursor.fetchone()  # OBTENER UNA SOLA FILA
        cat = self.cat.get()
        sql2 = "SELECT id_categoria FROM categoria where nombre_categoria='" + cat + "'"
        print(sql2)
        try:
            cursor.execute(sql2)
            results = cursor.fetchall()

            for row in results:
                t = int(row[0])
                print(t)
        except:
            print("Error")
        descripcion = self.descripcionIngreso.get()
        monto = int(self.montoIngreso.get())
        fecha = self.fechaIngreso.get()
        sql1 = "INSERT INTO ingresos( id_categoria, descripcion,fecha, monto) VALUES ( '%d', '%s', '%s','%d')" % (t, descripcion,fecha,monto)
        print(sql1)
        try:
            cursor.execute(sql1)
            db.commit()
            messagebox.showinfo("Guardado", "Los datos ha sido guardados  ")
            self.montoIngreso.set("")
            self.cat.set("")
            self.fechaIngreso.set("")
            self.descripcionIngreso.set("")
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

        self.totalI.set(t)
        return self.totalI
    def __init__(self, parent, controller):
     tk.Frame.__init__(self, parent)
     self.controller = controller
     nombre = ['Sueldo','Ventas','Honorarios','Inversion','Otros']
     colorFondo  = "White"
     colorLetra = "Blue"
     self.config(bd=30)
     self.config(relief="ridge")
     self.config(background=colorFondo)
     self.montoIngreso=StringVar()
     self.descripcionIngreso=StringVar()
     self.fechaIngreso=StringVar()
     self.cat=StringVar()
     self.totalI=StringVar()

     labelMonto=Label(self,text="INGRESA EL MONTO DEL INGRESO:",bg=colorFondo,fg = colorLetra,font=controller.title_font).grid(row=0,column=0,padx=10,pady=10)
     global txtMonto
     txtMonto=Entry(self,textvariable=self.montoIngreso,bd=5,relief="sunken",width=25,font=("Helvetica",9))
     txtMonto.grid(row=0,column=1,padx=10,pady=10)

     labelIngreso = Label(self,text="TIPO DE INGRESO: ",bg=colorFondo,fg = colorLetra,font=controller.title_font).grid(row=1,column=0,padx=10,pady=10)
     combo = ttk.Combobox(self,textvariable=self.cat)
     combo.grid(row=1,column=1,padx=10,pady=10)
     combo['values'] = (nombre)
     combo.config(font=("Helvetica",10))

     labelFecha = Label(self, text="FECHA:", bg=colorFondo, fg=colorLetra,font=controller.title_font).grid(row=3,column=0, padx=10, pady=10)
     global txtFecha
     txtFecha = Entry(self,text="año/mes/dia", bd=5, relief="sunken",textvariable=self.fechaIngreso,width=25,font=("Helvetica",9))
     txtFecha.grid(row=3, column=1, padx=10, pady=10)

     labelDescripcion=Label(self,text="DESCRIPCIÓN:",bg=colorFondo,fg = colorLetra,font=controller.title_font).grid(row=4,column=0,padx=10,pady=10)
     global txtDescripcion
     txtDescripcion=Entry(self,bd=5,relief="sunken",width=25,textvariable=self.descripcionIngreso,font=("Helvetica",9))
     txtDescripcion.grid(row=4,column=1,padx=10,pady=10)

     labelSaldo=Label(self,text="TOTAL DE INGRESOS:",bg=colorFondo,fg = colorLetra,font=controller.title_font).grid(row=5,column=0,padx=10,pady=10)
     txtSaldo=Entry(self,state="readonly",text=self.totalI,bd=5,relief="sunken",width=25,bg="#FFFF00",fg="Red",font=("Helvetica",9)).grid(row=5,column=1,padx=10,pady=10)
     btnGuardar = Button(self,text="GUARDAR",font=controller.title_font,bd=14,relief="groove",cursor="hand2",command = self.validacion).grid(row=6,column=1,padx=10,pady=10)
     btnAtras = Button(self,text="ATRAS",font=controller.title_font,bd=14,relief="groove",cursor="hand2",command=lambda:controller.show_frame("PantallaMenu")).grid(row=6,column=0,padx=10,pady=10)
