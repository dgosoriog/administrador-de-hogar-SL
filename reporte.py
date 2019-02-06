import itertools
from random import randint
from statistics import mean
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import pymysql

def grouper(iterable, n):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)

def export_to_pdf(data):
    i=randint(0, 100)
    nombre="ingresos por categoria"+str(i)+".pdf"
    c = canvas.Canvas(nombre, pagesize=A4)
    w, h = A4
    max_rows_per_page = 45
    text = c.beginText(200, h - 50)
    text.textLine("Mis Ingresos")
    text.textLine("")
    c.drawText(text)

    c.drawImage("gastos.png", 50, h - 50, width=50, height=50)
    # Margin.
    x_offset = 50
    y_offset = 50
    # Space between rows.
    padding = 15

    xlist = [x + x_offset for x in [0, 200, 250]]
    ylist = [h - y_offset - i * padding for i in range(max_rows_per_page + 1)]

    for rows in grouper(data, max_rows_per_page):
        rows = tuple(filter(bool, rows))
        c.grid(xlist, ylist[:len(rows) + 1])
        for y, row in zip(ylist[:-1], rows):
            for x, cell in zip(xlist, row):
                c.drawString(x + 2, y - padding + 3, str(cell))
        c.showPage()

    c.save()


def reporte_ing():
    data = [("Categoria", "Total")]
    dbc = ("127.0.0.1", "root", "", "proyecto")
    db = pymysql.connect(dbc[0], dbc[1], dbc[2], dbc[3])  # abrir una coneccion con mysql
    cursor = db.cursor()  # obtener el cursor
    sql2 = "SELECT nombre_categoria,sum(monto) from categoria,ingresos WHERE categoria.id_categoria=ingresos.id_categoria"

    try:
        cursor.execute(sql2)
        results = cursor.fetchall()
        for row in results:
            cat=row[0]
            total=row[1]
        data.append((cat,total))
    except:
        print("")

    export_to_pdf(data)


def export_to_pdf2(data):
        i = randint(0, 100)
        nombre = "gastos por categoria" + str(i) + ".pdf"
        c = canvas.Canvas(nombre, pagesize=A4)
        w, h = A4
        max_rows_per_page = 45
        text = c.beginText(200, h - 50)
        text.textLine("Mis Gastos")
        text.textLine("")
        c.drawText(text)

        c.drawImage("gastos.png", 50, h - 50, width=50, height=50)
        # Margin.
        x_offset = 50
        y_offset = 50
        # Space between rows.
        padding = 15

        xlist = [x + x_offset for x in [0, 200, 250]]
        ylist = [h - y_offset - i * padding for i in range(max_rows_per_page + 1)]

        for rows in grouper(data, max_rows_per_page):
            rows = tuple(filter(bool, rows))
            c.grid(xlist, ylist[:len(rows) + 1])
            for y, row in zip(ylist[:-1], rows):
                for x, cell in zip(xlist, row):
                    c.drawString(x + 2, y - padding + 3, str(cell))
            c.showPage()

        c.save()

def reporte_g():
        data = [("Categoria", "Total")]
        dbc = ("127.0.0.1", "root", "", "proyecto")
        db = pymysql.connect(dbc[0], dbc[1], dbc[2], dbc[3])  # abrir una coneccion con mysql
        cursor = db.cursor()  # obtener el cursor
        sql2 = "SELECT nombre_categoria_g,sum(monto_g) from categoria_gastos,gastos WHERE categoria_gastos.id_categoria_g=gastos_id_categoria_g"

        try:
            cursor.execute(sql2)
            results = cursor.fetchall()
            for row in results:
                cat = row[0]
                total = row[1]
            data.append((cat, total))
        except:
            print("")

        export_to_pdf2(data)

