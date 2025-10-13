class Validar:
    """Clase para validar si una cadena de texto representa un número.
    Class for validating whether a string represents a number."""
    
    def __init__(self):
        # El constructor no hace nada, se podría omitir o usar para inicialización futura.
        # The constructor does nothing; it could be omitted or used for future initialization.
        pass

    def ValidarAscii(self, valor):
        """Método que valida si una cadena contiene solo dígitos ASCII (48 a 57).
        Method that validates if a string contains only ASCII digits (48 to 57)."""
        con = 0
        # Itera sobre cada carácter de la cadena de entrada.
        # Iterates over each character in the input string.
        for i in valor:
            # Comprueba si el código ASCII del carácter está en el rango de los dígitos (0-9).
            # Checks if the ASCII code of the character is within the digit range (0-9).
            if ord(i) >= 48 and ord(i) <= 57:
                con += 1
        
        # Si la cuenta de dígitos es igual a la longitud total de la cadena, es un número.
        # If the count of digits equals the total length of the string, it's a number.
        if con == len(valor):
            return "numero"
        else:
            # Si no, contiene caracteres que no son dígitos (letras, símbolos, espacios).
            # Otherwise, it contains non-digit characters (letters, symbols, spaces).
            return "contiene letras o símbolos"

    def ValidarConError(self, valor):
        """Método que utiliza el manejo de excepciones (try-except) para validar si el valor es convertible a entero.
        Method that uses exception handling (try-except) to validate if the value is convertible to an integer."""
        a = 0
        try:
            # Intenta convertir la cadena a un entero. Si falla, lanza un ValueError.
            # Attempts to convert the string to an integer. If it fails, it throws a ValueError.
            a = int(valor)
            # Si la conversión es exitosa, es un número.
            # If the conversion is successful, it's a number.
            return "numero"
        except ValueError:
            # Captura el error si la cadena no puede ser convertida (e.g., "123a").
            # Catches the error if the string cannot be converted (e.g., "123a").
            return "letra o numero"
            # NOTA: Este método también permitiría números negativos o decimales (si se usara float),
            #       pero el uso de int() lo restringe a enteros, aunque la salida de error es genérica.
            # NOTE: This method would also allow negative numbers or decimals (if float was used),
            #       but the use of int() restricts it to integers, though the error output is generic.

    def ValidarConString(self, valor):
        """Método que utiliza el método isdigit() de la clase string de Python.
        Method that uses Python's string class method isdigit()."""
        # isdigit() retorna True si todos los caracteres de la cadena son dígitos (0-9).
        # isdigit() returns True if all characters in the string are digits (0-9).
        # NOTA: isdigit() puede retornar True para algunos caracteres Unicode que parecen dígitos.
        # NOTE: isdigit() can return True for some Unicode characters that look like digits.
        return valor.isdigit()