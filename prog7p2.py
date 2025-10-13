from tkinter import *
from tkinter import messagebox

class principal:
    """Clase principal para la aplicación Tkinter.
    Main class for the Tkinter application."""

    def __init__(self):
        self.ven = Tk()
        self.ven.title('Programa 9 con ventana GRID - Mejorado / Program 9 with GRID window - Improved')
        # La geometría se deja como referencia, pero 'grid' maneja el diseño.
        # Geometry is left as a reference, but 'grid' manages the layout.
        self.ven.geometry('550x300') 
        
        # Inicializa la lista principal para almacenar los números.
        self.lista = []
        # self.aux1 y self.aux2 se eliminan al usar min() y max().
        # self.a y self.b se mantienen solo si la función agregar va a usarlos.
        self.a = 0
        self.b = 0
        
    def inicio(self):
        """Configura la interfaz gráfica usando el gestor de geometría grid.
        Sets up the graphical interface using the grid geometry manager."""
        
        # Título de la aplicación.
        Label(self.ven, text="Programa 9 - Lista de Números", font=('Arial', 12, 'bold')).grid(row=0, column=0, columnspan=4, pady=10)

        # === Entradas (Columna 0 y 1) ===
        
        # Entrada 1
        Label(self.ven, text="Escribe un número 1:").grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.n1 = Entry(self.ven, width=15)
        self.n1.grid(row=1, column=1, padx=5, pady=5, sticky='ew')
        
        # Entrada 2
        Label(self.ven, text="Escribe un número 2:").grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.n2 = Entry(self.ven, width=15)
        self.n2.grid(row=2, column=1, padx=5, pady=5, sticky='ew')
        
        # === Botones (Columna 2) ===
        Button(self.ven, text="Agregar", command=self.agregar, width=10).grid(row=1, column=2, padx=10, pady=5)
        Button(self.ven, text="Mayor", command=self.mayor, width=10).grid(row=2, column=2, padx=10, pady=5)
        Button(self.ven, text="Menor", command=self.menor, width=10).grid(row=3, column=2, padx=10, pady=5)
        Button(self.ven, text="Salir", command=self.salir, width=10).grid(row=4, column=2, padx=10, pady=5)
        
        # === Listbox y Display de Lista (Columna 3) ===
        Label(self.ven, text="Elementos Agregados:", font=('Arial', 10)).grid(row=0, column=3, sticky='w', padx=5, pady=5)

        self.listview = Listbox(self.ven, height=10, width=20, bg='lightgrey', fg='red', activestyle="dotbox")
        # El Listbox se expande vertical y horizontalmente.
        self.listview.grid(row=1, column=3, rowspan=4, sticky='nsew', padx=10, pady=5)
        
        # Etiqueta para mostrar la lista interna de Python (debajo de las entradas).
        Label(self.ven, text="Lista Interna:", font=('Arial', 10, 'italic')).grid(row=3, column=0, sticky='w', padx=5, pady=5)
        self.listaElementos = Label(self.ven, text=f"{self.lista}", relief=SUNKEN, anchor='w')
        self.listaElementos.grid(row=4, column=0, columnspan=2, sticky='ew', padx=5)

        # Configura las expansiones de columnas y filas.
        self.ven.grid_columnconfigure(3, weight=1)
        self.ven.grid_rowconfigure(4, weight=1)

        self.ven.mainloop()

    def mayor(self):
        """Encuentra y muestra el número mayor de la lista usando max().
        Finds and displays the maximum number in the list using max()."""
        # Verifica si la lista está vacía.
        if not self.lista: 
            messagebox.showerror("Error", "La lista está vacía. Agregue números primero. / The list is empty. Add numbers first.")
            return

        # Uso eficiente de la función integrada max().
        numero_mayor = max(self.lista)
        messagebox.showinfo('El Mayor / The Maximum', f'El número mayor en la lista es: {numero_mayor}')

    def menor(self):
        """Encuentra y muestra el número menor de la lista usando min().
        Finds and displays the minimum number in the list using min()."""
        # Verifica si la lista está vacía.
        if not self.lista:
            messagebox.showerror("Error", "La lista está vacía. Agregue números primero. / The list is empty. Add numbers first.")
            return

        # Uso eficiente de la función integrada min().
        numero_menor = min(self.lista)
        messagebox.showinfo('El Menor / The Minimum', f'El número menor en la lista es: {numero_menor}')

    def agregar(self):
        """Obtiene dos números, los valida y los agrega a la lista y Listbox.
        Gets two numbers, validates them, and adds them to the list and Listbox."""
        try:
            # Obtiene y valida el primer número.
            self.a = int(self.n1.get())
            # Obtiene y valida el segundo número.
            self.b = int(self.n2.get())
            
            # Agrega ambos a la lista interna.
            self.lista.append(self.a)
            self.lista.append(self.b)
            
            # Agrega ambos al Listbox para visualización.
            self.listview.insert(END, self.a) 
            self.listview.insert(END, self.b) 
            
            # Limpia los campos de entrada.
            self.n1.delete(0, END)
            self.n2.delete(0, END)
            
            # Actualiza la etiqueta de la lista.
            self.listaElementos.config(text=f"{self.lista}")
            
        except ValueError:
            # Manejo de error si el input no es un entero o está vacío.
            messagebox.showerror("Error", "Ambos valores deben ser números enteros válidos. / Both values must be valid integers.")
            
    def salir(self):
        """Cierra la ventana de la aplicación. / Closes the application window."""
        self.ven.destroy()

if __name__ == '__main__':
    # Crea y ejecuta la aplicación.
    app = principal()
    app.inicio()