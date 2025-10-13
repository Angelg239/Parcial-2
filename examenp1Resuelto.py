
from tkinter import *
from tkinter import messagebox

def calificacion():
    def revisar():
        try:
            nombre = us.get()
            cal1 = int(pas1.get())
            cal2 = int(pas2.get())
            cal3 = int(pas3.get())
            
        
            messagebox.showinfo("Resultado",f"Alumno: {nombre}\nCalificación 1: {cal1}\nCalificación 2: {cal2}\nCalificación 3: {cal3}")
        except ValueError:
            messagebox.showerror("Error", "Debes ingresar números en las calificaciones.")

    ven = Tk()
    ven.title('Calificaciones')
    ven.geometry('800x500')

    Label(ven, text='Nombre').pack(pady=10)
    us = Entry(ven)
    us.pack(pady=3)

    Label(ven, text='Calificación 1').pack(pady=5)
    pas1 = Entry(ven)
    pas1.pack(pady=3)

    Label(ven, text='Calificación 2').pack(pady=5)
    pas2 = Entry(ven)
    pas2.pack(pady=3)

    Label(ven, text='Calificación 3').pack(pady=5)
    pas3 = Entry(ven)
    pas3.pack(pady=3)

    Button(ven, text='Agregar', command=revisar).pack(pady=10)

    ven.mainloop()

if __name__ == "__main__":
    calificacion()