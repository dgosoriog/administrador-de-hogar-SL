import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql
class PantallaSaldo(tk.Frame):

    def ver_ingresos(saldo):
     dbc = ("127.0.0.1", "root", "", "proyecto")
     db = pymysql.connect(dbc[0], dbc[1], dbc[2], dbc[3])  # abrir una coneccion con mysql
     cursor = db.cursor()  # obtener el cursor
     sql2 = "SELECT sum(monto) FROM ingresos"
     try:
       cursor.execute(sql2)
       results = cursor.fetchall()
       for row in results:
          t = int(row[0])
     except:
       print("Error")

     saldo.totalI.set(t)
     return saldo.totalI


    def ver_gastos(saldo):
        dbc = ("127.0.0.1", "root", "", "proyecto")
        db = pymysql.connect(dbc[0], dbc[1], dbc[2], dbc[3])  # abrir una coneccion con mysql
        cursor = db.cursor()  # obtener el cursor
        sql2 = "SELECT sum(monto_g) FROM gastos"
        try:
            cursor.execute(sql2)
            results = cursor.fetchall()
            for row in results:
                t = int(row[0])
        except:
            print("Error")
        saldo.totalG.set(t)
        return saldo.totalG

    def calcular(saldo):
        totalSaldo=saldo.ver_ingresos()-saldo.ver_gastos()
        return totalSaldo

    def __init__(saldo, parent, controller):
        tk.Frame.__init__(saldo, parent)
        saldo.controller = controller
        label = tk.Label(saldo, text="This is page 1", font=controller.title_font)
        colorFondo  = "White"
        colorLetra = "Blue"
        saldo.config(bd=30)
        saldo.config(relief="ridge")
        saldo.config(background=colorFondo)
        saldo.totalI=StringVar()
        saldo.totalG=StringVar()
        saldo.totalSaldo=StringVar()
        saldo.configure(background=colorFondo)
        labelIngreso=Label(saldo,text="TOTAL DE INGRESOS:",bg=colorFondo,fg = colorLetra,font=controller.title_font).grid(row=0,column=0,padx=10,pady=10)
        global txtIngreso
        global txtGasto
        txtIngreso=Entry(saldo,text=saldo.totalI,bd=5,relief="sunken",width=25,bg="#FFFF00",fg="Red",font=("Helvetica",11)).grid(row=0,column=1,padx=10,pady=10)
        labelgasto = Label(saldo,text="TOTAL DE GASTOS: ",bg=colorFondo,fg = colorLetra,font=controller.title_font).grid(row=1,column=0,padx=10,pady=10)
        txtGasto=Entry(saldo,text=saldo.totalG,bd=5,relief="sunken",width=25,bg="#FFFF00",fg="Red",font=("Helvetica",11)).grid(row=1,column=1,padx=10,pady=10)
        labelSaldo = Label(saldo,text="SALDO: ",bg=colorFondo,fg = "Red",font=controller.title_font).grid(row=2,column=0,padx=10,pady=10)
        txtSaldo=Entry(saldo,text=saldo.calcular,bd=5,relief="sunken",width=25,bg="#FFFF00",fg="Red",font=("Helvetica",11)).grid(row=2,column=1,padx=10,pady=10)
        btnAtras = Button(saldo,text="ATRAS",font=controller.title_font,bd=10,relief="groove",command=lambda: controller.show_frame("PantallaMenu")).grid(row=4,column=0,padx=10,pady=10)
        btnGuardar = Button(saldo,text="GUARDAR",font=controller.title_font,bd=10,relief="groove").grid(row=4,column=1,padx=10,pady=10)

