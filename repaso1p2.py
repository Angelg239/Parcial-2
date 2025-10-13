from tkinter import *
from tkinter import messagebox
from validarRepaso import Validar

class Principal():
    def _init_(self):
        self.ventana = Tk()
        self.ventana.geometry("400x200")
        self.lista=[]
        self.valid = Validar()

    def inicio(self):
        Label(self.ventana, text="Programa de Python con TKInter").place(x=90,y=20)
        #X es columna y Y es Fila
        Label(self.ventana,text="Escribe un dato").place(x=50,y=50)
        self.dato = Entry(self.ventana)
        self.dato.place(x=150,y=50,width=150)
        Button(self.ventana,text="Validar",command=self.validarDatos).place(x=200,y=100,width=150)
        self.mostrar = Label(self.ventana,text="")
        self.mostrar.place(x=200,y=150)

        self.ventana.mainloop()

    def validarDatos(self):
        val= self.dato.get()
        if val !="":
            self.lista.append(val)
            self.Revisar(val)
            self.dato.delete(0,END)
            self.mostrar.config(text=str(self.lista))
            respuesta = self.valid.ValidarAscii(val)
            messagebox.showinfo("Validar Dstos", f'El dato es {respuesta}')
        else:
            messagebox.showerror("Error","Caja de texto esta vacia")

    def Revisar(self,v):
        print(v)

if __name__=="__main__":
    app = Principal()
    app.inicio()