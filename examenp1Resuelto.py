from tkinter import *
from tkinter import messagebox

def calificacion():
    """Función principal que crea la ventana de la aplicación para ingresar calificaciones.
    Main function that creates the application window to enter grades."""
    
    def revisar():
        """Función interna que recopila y valida los datos de entrada, y muestra los resultados.
        Inner function that collects and validates input data, and displays the results."""
        try:
            # Obtiene el nombre del alumno (cadena de texto).
            # Gets the student's name (string).
            nombre = us.get()
            
            # Intenta obtener y convertir las tres calificaciones a enteros.
            # Attempts to get and convert the three grades to integers.
            cal1 = int(pas1.get())
            cal2 = int(pas2.get())
            cal3 = int(pas3.get())
            
            # Muestra un cuadro de información (showinfo) con los datos recopilados.
            # Displays an information box (showinfo) with the collected data.
            messagebox.showinfo("Resultado / Result",f"Alumno: {nombre}\nStudent: {nombre}\nCalificación 1: {cal1}\nGrade 1: {cal1}\nCalificación 2: {cal2}\nGrade 2: {cal2}\nCalificación 3: {cal3}\nGrade 3: {cal3}")
            
        except ValueError:
            # Captura el error si alguna calificación no es un número entero válido (ValueError).
            # Catches the error if any grade is not a valid integer (ValueError).
            messagebox.showerror("Error", "Debes ingresar números en las calificaciones. / You must enter numbers for the grades.")

    # Crea la ventana principal de Tkinter. / Creates the main Tkinter window.
    ven = Tk()
    ven.title('Calificaciones / Grades')
    ven.geometry('800x500') # Establece el tamaño de la ventana. / Sets the window size.

    # === Widgets usando .pack() para el diseño lineal ===
    # === Widgets using .pack() for linear layout ===
    
    # Etiqueta y campo de entrada para el Nombre.
    # Label and entry field for the Name.
    Label(ven, text='Nombre / Name').pack(pady=10)
    us = Entry(ven)
    us.pack(pady=3)

    # Etiqueta y campo de entrada para la Calificación 1.
    # Label and entry field for Grade 1.
    Label(ven, text='Calificación 1 / Grade 1').pack(pady=5)
    pas1 = Entry(ven)
    pas1.pack(pady=3)

    # Etiqueta y campo de entrada para la Calificación 2.
    # Label and entry field for Grade 2.
    Label(ven, text='Calificación 2 / Grade 2').pack(pady=5)
    pas2 = Entry(ven)
    pas2.pack(pady=3)

    # Etiqueta y campo de entrada para la Calificación 3.
    # Label and entry field for Grade 3.
    Label(ven, text='Calificación 3 / Grade 3').pack(pady=5)
    pas3 = Entry(ven)
    pas3.pack(pady=3)

    # Botón que llama a la función revisar al ser presionado.
    # Button that calls the 'revisar' function when pressed.
    Button(ven, text='Agregar / Add', command=revisar).pack(pady=10)

    # Inicia el bucle principal de la aplicación.
    # Starts the application's main loop.
    ven.mainloop()

if __name__ == "__main__":
    # Asegura que la función 'calificacion' se ejecute solo si el script se corre directamente.
    # Ensures the 'calificacion' function runs only if the script is executed directly.
    calificacion()