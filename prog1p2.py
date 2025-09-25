
def inicio(num):
    # Escribe una calificacion (Grade input)
    a = int(input('Escribe una calificacion '))
     # Incrementa el contador (Increment counter)
    num += 1
    # Añade la nota a la lista (Add grade to list)
    lista.append(a)
    # Condicion de fin (End condition: 5 grades)
    if (num >= 5):
        print()
    else:
        # Llamada recursiva (Recursive call)
        return inicio(num)

# Lista para guardar notas (List to store grades)
lista = []
# Declarar variable global (Declare global variable)
global num
# Inicializa el contador (Initialize counter)
num = 0
# Ejecutar si el script es principal (Run if script is main)
if __name__ == '__main__':
    # Iniciar la recoleccion de notas (Start grade collection)
    inicio(num)