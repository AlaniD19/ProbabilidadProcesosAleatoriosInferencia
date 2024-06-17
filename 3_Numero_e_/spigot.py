# CIC IPN / MCIC
# Programa: spigot.py
# Descripción:
# Autor: Alan Delgado
# Fecha de creación: Junio 2024
# Versión: 1.0
def generate_and_save_e_digits(n, filename, block_size=1000):
    """ Genera un diccionario con la ocurrencia de cada palabra reservada en C de un archivo fuente
        ARGS: file_path (str): directorio del archivo del programa a evaluar
        RETURN: keyword_count (dict): ocurrencia de palabras reservadas
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
                file.write(str(a[0]))                       # Escribe la cifra calculada al archivo
            file.flush()                                    # Fuerza la escritura de los datos en el disco


if __name__ == "__main__":
    num_gb = 5                                              # Calcula el número de cifras a generar para 5 GB de datos
    num_digits = num_gb * 1024 * 1024 * 1024                # Asumimos que cada cifra ocupa un byte
    filename = "e_digits_5gb.txt"                           # Nombre del archivo donde se guardarán las cifras
    generate_and_save_e_digits(num_digits, filename)        # Genera y guarda las cifras en el archivo
    print(f"First {num_digits} digits of e saved to {filename}")
