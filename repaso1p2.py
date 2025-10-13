from tkinter import *
from tkinter import messagebox
from validarRepaso import Validar # Importa la clase Validar (asumiendo que existe). / Imports the Validar class (assuming it exists).

class Principal():
    
    # ¡CRÍTICO! El constructor debe ser __init__ (doble guion bajo).
    # CRITICAL! The constructor must be __init__ (double underscore).
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("400x200")
        self.lista=[] # Lista para almacenar los datos ingresados. / List to store input data.
        self.valid = Validar() # Instancia de la clase de validación externa. / Instance of the external validation class.

    def inicio(self):
        """Configura y lanza la interfaz gráfica de Tkinter.
        Sets up and launches the Tkinter graphical interface."""
        
        # Título de la aplicación. Se usa .place() para posicionamiento absoluto.
        # Application title. Uses .place() for absolute positioning.
        Label(self.ventana, text="Programa de Python con TKInter").place(x=90,y=20)
        
        # Etiqueta para el campo de entrada. / Label for the input field.
        Label(self.ventana,text="Escribe un dato").place(x=50,y=50)
        
        # Campo de entrada (Entry). / Entry field.
        self.dato = Entry(self.ventana)
        self.dato.place(x=150,y=50,width=150)
        
        # Botón para ejecutar la validación. / Button to execute validation.
        Button(self.ventana,text="Validar",command=self.validarDatos).place(x=200,y=100,width=150)
        
        # Etiqueta para mostrar la lista de datos ingresados.
        # Label to display the list of entered data.
        self.mostrar = Label(self.ventana,text="")
        self.mostrar.place(x=200,y=150)

        self.ventana.mainloop() # Bucle principal de la interfaz gráfica. / Main loop for the GUI.

    def validarDatos(self):
        """Función que recupera, valida, agrega a la lista y llama a la clase externa.
        Function that retrieves, validates, adds to the list, and calls the external class."""
        val = self.dato.get() # Obtiene el contenido del campo de entrada. / Gets the content of the Entry field.
        
        if val !="":
            self.lista.append(val) # Agrega el dato a la lista interna. / Adds the data to the internal list.
            self.Revisar(val) # Llama a Revisar (imprime el valor). / Calls Revisar (prints the value).
            self.dato.delete(0,END) # Limpia el campo de entrada. / Clears the input field.
            self.mostrar.config(text=str(self.lista)) # Actualiza la etiqueta con la lista. / Updates the label with the list.
            
            # Llama al método de validación de la clase externa.
            # Calls the validation method from the external class.
            respuesta = self.valid.ValidarAscii(val)
            
            # Muestra el resultado de la validación. / Shows the validation result.
            messagebox.showinfo("Validar Datos", f'El dato es {respuesta}')
        else:
            # Muestra un error si la caja de texto está vacía.
            # Shows an error if the text box is empty.
            messagebox.showerror("Error","Caja de texto esta vacia")

    def Revisar(self,v):
        """Función simple para depuración: imprime el valor.
        Simple function for debugging: prints the value."""
        print(v)

if __name__=="__main__":
    app = Principal()
    app.inicio()