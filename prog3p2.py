
from tkinter import * # Importa todos los modulos de Tkinter (Import all Tkinter modules)
from tkinter import messagebox # Importa el módulo para cuadros de mensaje (Import message box module)

def Ventana(): # Define la función principal de la ventana (Define the main window function)
    def revisar(): # Define la funcion para revisar credenciales (Define function to check credentials)
        try:
            # Obtener el texto del campo 'Usuario' (Get text from 'User' entry field)
            u = str(us.get())
            # Obtener el texto del campo 'Password' (Get text from 'Password' entry field)
            p = str(pas.get())

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

    # Crear la ventana principal (Create the main window)
    ven = Tk()
    # Asignar titulo a la ventana (Set window title)
    ven.title('Programa 1 con vantana')
    # Definir tamaño y posicion inicial (Define initial size and position)
    ven.geometry('400x200')

    # Etiqueta 'Usuario' (Label 'Usuario')
    label = Label(ven, text = 'Usuario').pack(pady=10)
    # Campo de entrada para el usuario (Entry field for username)
    us = Entry(ven)
    us.pack(pady=3)

    # Etiqueta 'Password' (Label 'Password')
    label = Label(ven, text = 'Password').pack(pady=10)
    # Campo de entrada para la contraseña (Entry field for password)
    pas = Entry(ven)
    pas.pack(pady=3)

    # Boton 'Aceptar' que llama a 'revisar' (Button 'Accept' that calls 'revisar')
    boton = Button(ven, text='Aceptar', command=revisar).pack(pady=3)
    # Inicia el ciclo de eventos de la ventana (Starts the window's event loop)
    ven.mainloop()

# Ejecutar si el script es principal (Run if script is main)
if __name__ == '__main__':
    Ventana() # Llamar a la función de la ventana (Call the window function)