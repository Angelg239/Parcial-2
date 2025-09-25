from tkinter import * # Importa todos los modulos de Tkinter (Import all Tkinter modules)
from tkinter import messagebox # Importa el módulo para cuadros de mensaje (Import message box module)

class Ventana(): # Define la clase de la ventana (Define the window class)
    def __init__(self): # Constructor de la clase (Class constructor)
        self.ven = Tk() # Crear la ventana principal como atributo (Create main window as attribute)
        # Asignar titulo a la ventana (Set window title)
        self.ven.title('Programa 1 con vantana')
        # Definir tamaño inicial (Define initial size)
        self.ven.geometry('400x200')
        
    def inicio(self):
        # Etiqueta 'Usuario' (Label 'Usuario')
        label = Label(self.ven, text = 'Usuario').pack(pady=10)
        # Campo de entrada (Entry field)
        self.us = Entry(self.ven)
        self.us.pack(pady=3)
        
        # Etiqueta 'Password' (Label 'Password')
        label = Label(self.ven, text = 'Password').pack(pady=10)
        # Campo de entrada (Entry field)
        self.pas = Entry(self.ven)
        self.pas.pack(pady=3)
        
        # Boton 'Aceptar' que llama a 'self.revisar' (Button 'Accept' calls 'self.revisar')
        # El comando llama al metodo de la clase (Command calls class method)
        boton = Button(self.ven, text='Aceptar', command=self.revisar).pack(pady=3)
        
        # Inicia el ciclo de eventos (Starts the event loop)
        self.ven.mainloop()
    
    def revisar(self): # Metodo para revisar credenciales (Method to check credentials)
        try:
            # Obtener usuario del atributo self.us (Get user from self.us attribute)
            u = str(self.us.get())
            # Obtener password del atributo self.pas (Get password from self.pas attribute)
            p = str(self.pas.get())
            
            # Comprobar credenciales (Check credentials)
            if u == 'admin' and p == '12345':
                # Mensaje de exito (Success message)
                messagebox.showinfo('Validacion','Usuario y contraseña correcto')
            else:
                # Mensaje de error (Error message)
                messagebox.showerror('Error','Usuario y/o contraseña incorrecto')
        except ValueError:
            # Manejar error si no hay datos (Handle error if no data is entered)
            messagebox.showerror('Error','Introduce datos')

# Ejecutar si el script es principal (Run if script is main)
if __name__ == '__main__':
    # Crear una instancia de la clase (Create an instance of the class)
    app = Ventana()
    # Iniciar la interfaz (Start the interface)
    app.inicio()