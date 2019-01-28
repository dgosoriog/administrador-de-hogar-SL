#Archivo en el que se imprimira el reporte de gastos mensuales de la familia
# david
#reporte pdf
from reportlab.pdfgen import canvas
 
c = canvas.Canvas("hola_mundo.pdf")
c.drawString(100,750,"Hola mundo pdf!")
c.save()
