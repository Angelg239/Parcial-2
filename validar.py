
class validacion(): # Define la clase de validacion y calculo (Define validation and calculation class)
    def __init__(self): # Constructor de la clase (Class constructor)
        self.suma = 0 # Inicializa la suma de valores (Initialize sum of values)
        self.promedio = 0.0 # Inicializa el valor del promedio (Initialize average value)

    def ValidarNumeros(self, valor): # Metodo para validar si la entrada es un numero (Method to validate if input is a number)
        if valor.isdigit(): # Verifica si todos los caracteres son digitos (Checks if all characters are digits)
            return True # Retorna verdadero (Returns True)
        else:
            return False # Retorna falso (Returns False)
        
    def Promedio(self, lista): # Metodo para calcular el promedio (Method to calculate the average)
        # Recorre la lista para sumar los elementos (Iterate list to sum elements)
        for i in lista:
            self.suma += i # Acumula la suma total (Accumulate the total sum)
        # Calcula el promedio (Calculate the average)
        self.Promedio = self.suma / len(lista)
        # Retorna el promedio calculado (Return the calculated average)
        return self.promedio
            