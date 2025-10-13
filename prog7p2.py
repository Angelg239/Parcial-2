
from tkinter import *
from tkinter import messagebox

class principal():
    def __init__(self):
        self.ven = Tk()
        self.ven.title('Programa 6 con ventana GRID')
        self.ven.geometry('450x250')
        self.a =0
        self.b = 0
        self.lista=[]
        self.aux1 = 0
        self.aux2 = self.lista[0]


    def inicio(self):
        l1 = Label(self.ven, text="programa 9")
        l1.place(X=10, Y=2)
        l2 = Label(self.ven, text="Escribe un numero")
        l2.place(x=3, Y=1, padx=15, pady=10)
        Label(self.ven, text="").place(x=2, y=2)
        self.n1 = Entry(self.ven)
        self.n1.place(x=3, y=2)
        l3 = Label(self.ven, text="Escribe otro numero")
        l3.place(x=5, y=1, padx=5, pady=5)
        Label(self.ven, text="").place(x=4, y=2)
        self.n2 = Entry(self.ven)
        self.n2.place(x=5, y=2)
        b1 = Button(self.ven, text="agregar", command=self.agregar)
        b1.place(x=6, y=1, pady=10)
        b2 = Button(self.ven, text="mayor", command=self.mayor)
        b2.place(x=6, y=2)
        b3 = Button(self.ven, text="menor", command=self.menor)
        b3.place(x=6, y=3, padx=10)
        b4 = Button(self.ven, text="salir", command=self.salir)
        b4.place(x=6, y=4, padx=25)
        self.listaElementos = Label(self.ven, text="")
        self.listaElementos.place(x=8, y=2, pady=15)
        self.listview = Listbox(self.ven, height=10, width=15, bg= 'grey', activestyle="dotbox", fg= "red")
        self.listview.place(x=2, y=4)

        self.ven.mainloop()

    def mayor(self):
        if len(self.lista) > 0:
        #for i in self.lista:
            if self.aux1 < self.lista[self.cont]:
                self.aux1 = self.lista[self.cont]
            self.cont += 1
            if len(self.lista)-1 < self.cont:
                print(f'el mayor es {self.aux1}')
            else:
                return self.mayor()
        else:
            print("Lista vacia")
            messagebox.showerror("Error", "La lista esta vacia")

    def menor(self):
        if len(self.lista) > 0:
            for i in self.lista:
                if self.aux2 < i:
                    self.aux2 = i
                    print(f'el menor es {self.aux2}')
                    messagebox.showinfo('El menor', self.aux2)
                else:
                    messagebox.showerror("Error","La lista esta vacia")

    def agregar(self):
        try:
            self.a =int(self.n1.get())
            self.lista.append(self.a)
            self.n1.delete(0,END)
            self.b= int(self.n2.get())
            self.listview.insert(self.listview.size.self.a)
            self.lista.append(self.b)
            self.n2.delete(0,END)
            print(self.lista)
            self.listaElementos.config(text=f"{self.lista}")
        except ValueError:
            messagebox.showerror("error","algun dato no es numero")
           

    def salir(self):
        self.ven.destroy()

if __name__ == '__main__':
    app = principal()
    app.inicio()