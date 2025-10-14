
'''Hacer un programa que meediante un vantana de tkiter realize lo siguiente:
1. la vantana deve contener 3 cajas de texto y 2 botones.
2. el programa validara que en la primer caja de texto solo permita minuscula en la segunda solo mayuasculas y la tersera solo numero,
    si en la caja no tiene datos que de un error.
3. unicamente cuando las 3 caja de texto estan validadas se contet3estara se visualusara en un acaja visbox y en una etiqueta se
    mostrara el numero de elementos de la lista'''

from tkinter import *
from tkinter import messagebox

class Principal():
    def __init__(self):
        self.ven = Tk()
        self.ven.title("Lista de mayusculas y minisculas con numero")
        self.ven.geometry('450x300')
        self.lista = []
        self.inicio()

    def inicio(self):
        b1 = Button(self.ven, text="Agregar", command=self.agregar, width=8)
        b1.grid(row=6, column=1, pady=10)
        b2 = Button(self.ven, text="validar", command=self.validar, width=8)
        b2.grid(row=6, column=2)

if __name__=="__main__":
    app = Principal()
    app.inicio()