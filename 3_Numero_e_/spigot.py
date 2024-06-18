# CIC IPN / MCIC
# Programa: spigot.py
# Descripción:
# Autor: Alan Delgado
# Fecha de creación: Junio 2024
# Versión: 1.0
'''def generate_and_save_e_digits(n, filename, block_size=1000):
    """ Calcula cifras significativas del número e en bloques para grandes volumenes
        ARGS: n (int): GB a generar. filename (str): archivo a escribir cifras. block_size (int): tamaño de bloque a escribir
        RETURN: NA
    """
    a = [1] * (n + 1)                                       # Inicializa una lista 'a' con n+1 elementos, todos a 1.
    for block_start in range(0, n, block_size):             # Recorre los bloques de cifras, en pasos de block_size
        with open(filename, 'a') as file:                   # Abre el archivo en modo anexar ('a'), para agregar datos al final del archivo existente
            for i in range(block_start, min(block_start + block_size, n)):  # Para cada posición en el bloque actual
                q = 0                                       # Inicializa la variable q para el acarreo y la cifra actual
                for j in range(n, 0, -1):                   # Procesa la lista 'a' desde el final hacia el principio
                    a[j] = 10 * a[j] + q                    # Actualiza el valor en la posición j de 'a' multiplicándolo por 10 y sumándole el acarreo 'q'
                    q = a[j] // j                           # Calcula el nuevo valor de 'q' como la parte entera de a[j] dividido por j
                    a[j] %= j                               # Actualiza a[j] con el resto de la división
                a[0] = q                                    # La primera cifra del bloque se almacena en a[0]
                print(a[0], end='')
                file.write(str(a[0]))                       # Escribe la cifra calculada al archivo
            file.flush()                                    # Fuerza la escritura de los datos en el disco


if __name__ == "__main__":
    num_gb = 5                                              # Calcula el número de cifras a generar para 5 GB de datos
    num_digits = num_gb * 1024 * 1024 * 1024                # Asumimos que cada cifra ocupa un byte
    filename = "e_digits_5gb.txt"                           # Nombre del archivo donde se guardarán las cifras
    generate_and_save_e_digits(num_digits, filename)        # Genera y guarda las cifras en el archivo
    print(f"First {num_digits} digits of e saved to {filename}")
'''

from collections import deque


def generate_and_save_e_digits(n, filename, block_size=1000000):
    # Utiliza deque para una mejor gestión de memoria
    a = deque([1])  # Inicializa con una sola posición en 1

    for block_start in range(0, n, block_size):
        with open(filename, 'a') as file:
            for i in range(block_start, min(block_start + block_size, n)):
                q = 0
                a.appendleft(0)  # Agrega una nueva posición al frente

                for j in range(len(a) - 1, 0, -1):
                    a[j] = 10 * a[j] + q
                    q = a[j] // j
                    a[j] %= j

                a[0] = q
                file.write(str(a[0]))

            file.flush()

        # Limita el tamaño del deque para ahorrar memoria
        while len(a) > 1 and a[-1] == 0:
            a.pop()


if __name__ == "__main__":
    # Calcula el número de cifras a generar para obtener aproximadamente 5 GB de datos
    # Asumimos que cada cifra ocupa un byte
    num_gb = 5
    num_digits = num_gb * 1024 * 1024 * 1024

    # Nombre del archivo donde se guardarán las cifras
    filename = "e_digits_5gb.txt"

    # Genera y guarda las cifras en el archivo
    generate_and_save_e_digits(num_digits, filename)
    print(f"First {num_digits} digits of e saved to {filename}")