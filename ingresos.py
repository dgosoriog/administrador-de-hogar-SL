from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql


def categoria():
    if(combo.get() == 'Sueldo'):
        return 1
    elif(combo.get() == 'Ventas'):
        return 2
    elif (combo.get() == 'Honoriarios'):
        return 3

    elif (combo.get() == 'Inversion'):
        return 4

    elif (combo.get() == 'Otros'):
        return 5

        print("----Error ----")

def limpiar():
    descripcion.set(" ")
    fecha.set(" ")
    monto.set(" ")
    combo.set(" ")


def msgExito():
    messagebox.showinfo("Correcto","Datos ingresados")
def msgError():
    messagebox.showinfo("Incorrecto", "Datos no ingresados ")


def ingresar():
    db = pymysql.connect("localhost","bdd_daniela", "TTVQ8Xh6Bpwh5t5t", "proyecto")
    cursor = db.cursor()
    # insertar

    sql = "insert into ingresos (id_categoria,descripcion,fecha,monto) values ('" + str(categoria()) + "','" + str(descripcion.get()) + "','" + str(fecha.get()) + "','" + str(monto.get()) + "');"

    msgExito()

    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()

    except:
        # Rollback in case there is any error

        db.rollback()


    # disconnect from server

    db.close()






ventana = Tk()
ventana.title("Ingresos Mensuales")
descripcion = StringVar()
fecha = StringVar()
monto = StringVar()
nombre = ['Sueldo','Ventas','Honorarios','Inversion','Otros']
colorFondo = "#100a4c"
colorLetra = "#fefafe"
ventana.geometry("500x300")
ventana.configure(background = colorFondo)
combo = ttk.Combobox(ventana)
imagen=PhotoImage(file="ingresos.png")
fondo = Label(ventana,image=imagen).place(x=20,y=20)
etiquetaDescripcion = Label(ventana,text="INGRESOS", bg=colorFondo,fg=colorLetra).place(x=170,y=10)

etiquetaCategoria = Label(ventana,text="Tipo de ingreso",bg=colorFondo,fg=colorLetra).place(x=50,y=50)
combo.place(x=150,y=50)
combo['values'] = (nombre)


etiquetaTi = Label(ventana,text="Descripcion",bg=colorFondo,fg=colorLetra).place(x=50,y=80)
cajaTi = Entry(ventana,textvariable=descripcion).place(x=150,y=80)

etiquetaSummary = Label(ventana,text="Fecha",bg=colorFondo,fg=colorLetra).place(x=50,y=110)
cajaSummary = Entry(ventana,textvariable=fecha).place(x=150,y=110)

etiquetaYear = Label(ventana,text="Monto",bg=colorFondo,fg=colorLetra).place(x=50,y=140)
cajaYear = Entry(ventana,textvariable=monto).place(x=150,y=140)


botonI = Button(ventana,text="INSERTAR",command = ingresar,bg="#fefafe",fg="black").place(x=180,y=200)
botonL = Button(ventana,text="BORRAR",command = limpiar,bg="#fefafe",fg="black").place(x=280,y=200)
mainloop()
