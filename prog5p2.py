
from tkinter import *
from tkinter import messagebox

class Principal():
    def __init__(self):
        self.ven = Tk() # Crear la ventana principal como atributo (Create main window as attribute)
        # Asignar titulo a la ventana (Set window title)
        self.ven.title('Programa 5 con vantana')
        # Definir tamaño inicial (Define initial size)
        self.ven.geometry('600x250')
        self.lista = []
        self.inicio()

    def sumar(self):
        s = 0
        for i in self.lista:
            s += i
        return s

    def promediar(self):
        try:
            a = float(self.n1.get())
            b = float(self.n2.get())
            c = float(self.n3.get())
            d = float(self.n4.get())
            pro = (a+b+c+d)/4
            self.l6.config(text=str(pro))
            self.lista.append(pro)
            self.l7.config(text=str(self.lista))
            self.n1.delete(0,END)
            self.n2.delete(0,END)
            self.n3.delete(0,END)
            self.n4.delete(0,END)
            
            suma = self.sumar()
            print(suma)
            p = suma / len(self.lista)
            self.l8.config(text=f'Promedio general: {str(p)}')

        except ValueError:
            messagebox.showerror('Validacion','Algun dato no es numero')
            self.n1.delete(0,END)
            self.n2.delete(0,END)
            self.n3.delete(0,END)
            self.n4.delete(0,END)

    def salir(self):
        self.ven.destroy()

    def inicio(self):
        l1 = Label(self.ven, text="Escribe un numero").place(y=10,x=20)# y=filas, x=columnas
        l2 = Label(self.ven, text="Escribe un numero").place(y=50,x=20)
        self.n1 = Entry(self.ven)
        self.n1.place(y=10, x=130)
        self.n2 = Entry(self.ven)
        self.n2.place(y=50, x=130)
        l3 = Label(self.ven, text="Escribe un numero").place(y=90,x=20)# y=filas, x=columnas
        l4 = Label(self.ven, text="Escribe unn numero").place(y=130,x=20)
        self.n3 = Entry(self.ven)
        self.n3.place(y=90, x=130)
        self.n4 = Entry(self.ven)
        self.n4.place(y=130, x=130)
        l5 = Label(self.ven, text="Promedio: ").place(y=150,x=130)# y=filas, x=columnas
        self.l6 = Label(self.ven, text="0,0")
        self.l6.place(y=150,x=200)
        b1 = Button(self.ven, text="Promedio", command=self.promediar).place(y=50, x=300)
        b2 = Button(self.ven, text="Salir", command=self.salir).place(y=90, x=300)
        self.l7 = Label(self.ven, text="[]")
        self.l7.place(y=170,x=200)
        self.l8 = Label(self.ven, text="Promedio general: 0,0")
        self.l8.place(y=190,x=200)
        self.ven.mainloop()

if __name__=='__main__':
    APP = Principal()