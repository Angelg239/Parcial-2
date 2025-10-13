from tkinter import *
from tkinter import messagebox
import random

class principal():
    # Constructor de la clase
    # Class constructor
    def __init__(self):
        # Crear la ventana principal de Tkinter
        # Create the main Tkinter window
        self.ven = Tk()
        # Establecer el título de la ventana
        # Set the window title
        self.ven.title('Programa 6 con ventana GRID')
        # Establecer el tamaño de la ventana
        # Set the window size
        self.ven.geometry('450x300') # Aumentado el alto un poco para mejor visibilidad / Increased height slightly for better visibility
        
        # Variables de instancia para almacenar los números de entrada
        # Instance variables to store the input numbers
        self.a = 0
        self.b = 0
        
        # Lista para almacenar los números agregados
        # List to store the added numbers
        self.lista = []
        
        # Variables auxiliares para encontrar el mayor y el menor (se usan min/max)
        # Auxiliary variables for finding the maximum and minimum (min/max are used)
        self.aux_mayor = 0 # Usar un nombre más descriptivo / Use a more descriptive name
        self.aux_menor = 0 # Inicializado a 0, se actualizará en agregar() / Initialized to 0, will be updated in agregar()
        
        # Inicializar contador para la función mayor (si se usa recursión)
        # Initialize counter for the mayor function (if recursion is used)
        self.cont = 0

    # Función para configurar los elementos de la interfaz gráfica
    # Function to set up the graphical interface elements
    def inicio(self):
        # Etiqueta de título
        # Title label
        l1 = Label(self.ven, text="Programa 9")
        l1.grid(row=1, column=2, columnspan=2) # Uso del gestor grid (Use of grid manager)
        
        # Etiqueta e campo de entrada para el primer número
        # Label and entry field for the first number
        l2 = Label(self.ven, text="Escribe un número (A):")
        l2.grid(row=3, column=1, padx=15, pady=10, sticky=W)
        Label(self.ven, text="").grid(row=2, column=2) # Espaciador / Spacer
        self.n1 = Entry(self.ven)
        self.n1.grid(row=3, column=2, columnspan=2)
        
        # Etiqueta e campo de entrada para el segundo número
        # Label and entry field for the second number
        l3 = Label(self.ven, text="Escribe otro número (B):")
        l3.grid(row=5, column=1, padx=15, pady=5, sticky=W)
        Label(self.ven, text="").grid(row=4, column=2) # Espaciador / Spacer
        self.n2 = Entry(self.ven)
        self.n2.grid(row=5, column=2, columnspan=2)
        
        # Botones de acción
        # Action buttons
        b1 = Button(self.ven, text="Agregar", command=self.agregar, width=8)
        b1.grid(row=6, column=1, pady=10)
        b2 = Button(self.ven, text="Mayor", command=self.mayor, width=8)
        b2.grid(row=6, column=2)
        b3 = Button(self.ven, text="Menor", command=self.menor, width=8)
        b3.grid(row=6, column=3, padx=10)
        b4 = Button(self.ven, text="Salir", command=self.salir, width=8)
        b4.grid(row=6, column=4, padx=15)
        
        # Etiqueta para mostrar los elementos de la lista (texto)
        # Label to display the list elements (text)
        Label(self.ven, text="Elementos en Lista:").grid(row=7, column=1, pady=15, sticky=W)
        self.listaElementos = Label(self.ven, text="")
        self.listaElementos.grid(row=7, column=2, columnspan=2, pady=15, sticky=W)
        
        # Listbox para mostrar los elementos de la lista de forma gráfica
        # Listbox to display the list elements graphically
        Label(self.ven, text="Números Agregados:").grid(row=2, column=4, sticky=S)
        self.listview = Listbox(self.ven, height=10, width=15, bg='grey', activestyle="dotbox", fg="red")
        self.listview.grid(row=3, column=4, rowspan=4, padx=15)
        
        # Iniciar el bucle principal de la ventana
        # Start the main window loop
        self.ven.mainloop()

    # Función para encontrar y mostrar el número mayor en la lista
    # Function to find and display the largest number in the list
    def mayor(self):
        if not self.lista: # Verificar si la lista está vacía / Check if the list is empty
            print("Lista vacía")
            messagebox.showerror("Error", "La lista está vacía. ¡Agrega números primero!")
            return # Salir de la función si la lista está vacía / Exit the function if the list is empty

        # Usar la función max() de Python para encontrar el mayor de forma eficiente
        # Use Python's max() function to find the largest efficiently
        el_mayor = max(self.lista)
        
        # Mostrar el resultado
        # Display the result
        print(f'El mayor es {el_mayor}')
        messagebox.showinfo('El Mayor', f"El número mayor es: {el_mayor}")

    # Función para encontrar y mostrar el número menor en la lista
    # Function to find and display the smallest number in the list
    def menor(self):
        if not self.lista: # Verificar si la lista está vacía / Check if the list is empty
            print("Lista vacía")
            messagebox.showerror("Error", "La lista está vacía. ¡Agrega números primero!")
            return # Salir de la función si la lista está vacía / Exit the function if the list is empty

        # Usar la función min() de Python para encontrar el menor de forma eficiente
        # Use Python's min() function to find the smallest efficiently
        el_menor = min(self.lista)
        
        # Mostrar el resultado
        # Display the result
        print(f'El menor es {el_menor}')
        messagebox.showinfo('El Menor', f"El número menor es: {el_menor}")

    # Función para agregar los números de las entradas a la lista
    # Function to add the numbers from the entries to the list
    def agregar(self):
        try:
            # Intentar obtener los valores de las entradas como enteros
            # Try to get the values from the entries as integers
            a_val = self.n1.get()
            b_val = self.n2.get()
            
            # Verificar si las entradas no están vacías
            # Check if the entries are not empty
            if not a_val and not b_val:
                messagebox.showwarning("Advertencia", "Ambos campos están vacíos. Escribe al menos un número.")
                return

            if a_val:
                self.a = int(a_val)
                self.lista.append(self.a)
                self.listview.insert(END, self.a) # Insertar en el Listbox / Insert into the Listbox
                self.n1.delete(0, END) # Limpiar la entrada / Clear the entry
            
            if b_val:
                self.b = int(b_val)
                self.lista.append(self.b)
                self.listview.insert(END, self.b) # Insertar en el Listbox / Insert into the Listbox
                self.n2.delete(0, END) # Limpiar la entrada / Clear the entry

            # Actualizar la etiqueta que muestra los elementos de la lista
            # Update the label that shows the list elements
            self.listaElementos.config(text=f"{self.lista}")
            print(f"Lista actual: {self.lista}")
            
            # Inicializar o actualizar aux_menor con el primer elemento si es necesario
            # Initialize or update aux_menor with the first element if necessary
            if len(self.lista) == 1:
                 self.aux_menor = self.lista[0] 
                 self.aux_mayor = self.lista[0] 

        except ValueError:
            # Manejar el error si la entrada no es un número
            # Handle the error if the input is not a number
            messagebox.showerror("Error", "Al menos un dato no es un número válido. Por favor, ingresa solo números enteros.")

    # Función para salir de la aplicación
    # Function to exit the application
    def salir(self):
        self.ven.destroy()

# Ejecutar la aplicación
# Run the application
if __name__ == '__main__':
    app = principal()
    app.inicio()