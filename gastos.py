from tkinter import *



#def gastos(): # creacion de la clase gastos
#
 #   gastoIng = float(input(" Ingrese cuanto Gasto"));
  #  ingreso = float(input("Cuanto ingreso "));

  #  Total= gastoIng-ingreso
   # print(Total)


#print(gastos());

from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

class Application(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("GASTOS GENERALES ")

        self.combo = ttk.Combobox(self)
        self.combo.place(x=10, y=10)

        gastoIng = float()
        txtIngresos=Entry(main_window,textvariable=gastoIng).place(x=330, y=10)
        lblGastos=Label(text="Gastos").place(x=180, y=10)
        ingreso = float()
        txtIngresos = Entry(main_window, textvariable=ingreso).place(x=330, y=40)
        lblGastos = Label(text="Ingresos").place(x=180, y=40)
        button = Button(main_window, text="Start").place(x=500, y=30)





        self.combo["values"] = ["Gasolina ", "Servicio Basicos", "Bares y Atros", "Cine", "Alimentacion Mascota", "Despensa del mes","Servicios Medicos","Transporte Publico","PagoU"]
        self.combo.bind("<<ComboboxSelected>>", self.selection_changed)

        main_window.configure(width=550, height=200)
        self.place(width=300, height=200)



    def gastos(self): # creacion de la clase gastos

      gastoIng = float(input(" Ingrese cuanto Gasto"));
      ingreso = float(input("Cuanto ingreso "));

      Total= gastoIng-ingreso
      print(Total)


    def selection_changed(self, event):
        print("Nuevo elemento seleccionado:", self.combo.get())







main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
