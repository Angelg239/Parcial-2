
from validar import validacion # Importar la clase de validación (Import validation class)
val = validacion() # Crear instancia de la clase (Create class instance)

class Principal(): # Define la clase principal (Define the main class)
    def __init__(self): # Constructor de la clase (Class constructor)
        self.lista = []# Lista para guardar notas (List to store grades)
        self.num = 0 # Contador de notas (Grade counter)
        self.a = "" # Variable para la entrada (Input variable)

    def inicio(self):
        # Solicita la calificacion (Request the grade)
        self.a = input('Escribe una calificacion \n')

        # Incrementa el contador (Increment counter)
        if val.ValidarNumeros(self.a):
            # Incrementa el contador (Increment counter)
            self.num += 1
            # Añade la nota a la lista (Add grade to list
            self.lista.append(int(self.a))

            # Condicion de fin (End condition: 5 grades)
            if self.num >= 5:
                print(self.lista) # Imprime la lista (Print the list)
                # Calcula y muestra el promedio (Calculate and show average)
                print(f'El promedio es:  {val.Promedio(self.lista)}')
            else:
                # Llamada recursiva (Recursive call)
                self.inicio()
        else:
            # Mensaje de error (Error message)
            print('No es un numero')
             # Llama de nuevo para reintentar (Call again to retry)
            self.inicio()

# Ejecutar si el script es principal (Run if script is main)
if __name__ == '__main__':
    app = Principal() # Crear instancia de Principal (Create Principal instance)
    app.inicio() # Iniciar el proceso (Start the process)