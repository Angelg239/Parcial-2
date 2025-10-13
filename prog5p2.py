from tkinter import *
from tkinter import messagebox

class Principal():
    # Constructor de la clase (Class constructor)
    def __init__(self):
        self.ven = Tk() # Crear la ventana principal como atributo (Create main window as attribute)
        # Asignar titulo a la ventana (Set window title)
        self.ven.title('Programa 5 con ventana')
        # Definir tamaño inicial (Define initial size)
        self.ven.geometry('600x250')
        self.lista = [] # Lista para almacenar los promedios calculados (List to store the calculated averages)
        self.inicio() # Llamar al método para configurar la interfaz (Call the method to set up the interface)

    # Método para sumar todos los elementos de la lista (Method to sum all elements in the list)
    def sumar(self):
        s = 0
        for i in self.lista:
            s += i
        return s

    # Método para calcular el promedio de 4 números y el promedio general (Method to calculate the average of 4 numbers and the general average)
    def promediar(self):
        try:
            # Obtener y convertir los valores de las cajas de texto a flotantes (Get and convert the values from the text boxes to floats)
            a = float(self.n1.get())
            b = float(self.n2.get())
            c = float(self.n3.get())
            d = float(self.n4.get())
            
            # Calcular el promedio de los 4 números (Calculate the average of the 4 numbers)
            pro = (a + b + c + d) / 4
            
            # Actualizar la etiqueta l6 con el promedio calculado (Update label l6 with the calculated average)
            self.l6.config(text=str(pro))
            
            # Añadir el promedio a la lista (Add the average to the list)
            self.lista.append(pro)
            
            # Actualizar la etiqueta l7 con el contenido actual de la lista (Update label l7 with the current content of the list)
            self.l7.config(text=str(self.lista))
            
            # Limpiar las cajas de texto (Clear the text boxes)
            self.n1.delete(0, END)
            self.n2.delete(0, END)
            self.n3.delete(0, END)
            self.n4.delete(0, END)
            
            # Calcular la suma de todos los promedios en la lista (Calculate the sum of all averages in the list)
            suma = self.sumar()
            print(suma) # Imprimir la suma en la consola (Print the sum to the console)
            
            # Calcular el promedio general (Average of the averages) (Calculate the general average)
            p = suma / len(self.lista)
            
            # Actualizar la etiqueta l8 con el promedio general (Update label l8 with the general average)
            self.l8.config(text=f'Promedio general: {str(p)}')

        except ValueError:
            # Capturar error si algún dato no es numérico (Catch error if any data is not numeric)
            messagebox.showerror('Validacion', 'Algún dato no es número')
            # Limpiar las cajas de texto en caso de error (Clear the text boxes in case of error)
            self.n1.delete(0, END)
            self.n2.delete(0, END)
            self.n3.delete(0, END)
            self.n4.delete(0, END)

    # Método para cerrar la ventana (Method to close the window)
    def salir(self):
        self.ven.destroy()

    # Método para configurar la interfaz de usuario (Method to set up the user interface)
    def inicio(self):
        # Etiquetas para pedir números (Labels to ask for numbers)
        l1 = Label(self.ven, text="Escribe un número").place(y=10, x=20) # y=filas, x=columnas
        l2 = Label(self.ven, text="Escribe un número").place(y=50, x=20)
        
        # Cajas de texto (Entry widgets) para la entrada de números (for number input)
        self.n1 = Entry(self.ven)
        self.n1.place(y=10, x=130)
        self.n2 = Entry(self.ven)
        self.n2.place(y=50, x=130)
        
        # Más etiquetas y cajas de texto (More labels and Entry widgets)
        l3 = Label(self.ven, text="Escribe un número").place(y=90, x=20)
        l4 = Label(self.ven, text="Escribe un número").place(y=130, x=20)
        self.n3 = Entry(self.ven)
        self.n3.place(y=90, x=130)
        self.n4 = Entry(self.ven)
        self.n4.place(y=130, x=130)
        
        # Etiqueta fija para mostrar el promedio (Fixed label to show the average)
        l5 = Label(self.ven, text="Promedio: ").place(y=150, x=130)
        
        # Etiqueta que mostrará el resultado del promedio individual (Label that will show the result of the individual average)
        self.l6 = Label(self.ven, text="0.0")
        self.l6.place(y=150, x=200)
        
        # Botones de la interfaz (Interface buttons)
        b1 = Button(self.ven, text="Promedio", command=self.promediar).place(y=50, x=300) # Botón para calcular el promedio (Button to calculate the average)
        b2 = Button(self.ven, text="Salir", command=self.salir).place(y=90, x=300) # Botón para salir (Button to exit)
        
        # Etiqueta que mostrará la lista de promedios (Label that will show the list of averages)
        self.l7 = Label(self.ven, text="[]")
        self.l7.place(y=170, x=200)
        
        # Etiqueta que mostrará el promedio general (Label that will show the general average)
        self.l8 = Label(self.ven, text="Promedio general: 0.0")
        self.l8.place(y=190, x=200)
        
        # Iniciar el bucle principal de la aplicación (Start the application's main loop)
        self.ven.mainloop()

# Bloque principal para ejecutar la aplicación (Main block to run the application)
if __name__ == '__main__':
    APP = Principal()