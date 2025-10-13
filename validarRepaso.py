
class Validar:
    def __init__(self):
        pass

    def ValidarAscii(self, valor):
        con = 0
        for i in valor:
            if ord(i) >= 48 and ord(i) <= 57:
                con += 1
        
        if con == len(valor):
            return "numero"
        else:
            return "contiene letras o símbolos"

    def ValidarConError(self, valor):
        a = 0
        try:
            a = int(valor)
            return "numero"
        except ValueError:
            return "letra o numero"

    def ValidarConString(self, valor):
        return valor.isdigit()