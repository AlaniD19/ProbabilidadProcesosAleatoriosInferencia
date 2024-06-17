# CIC IPN / MCIC
# Programa: reservedWords.py
# Descripción:
# Autor: Alan Delgado
# Fecha de creación: Junio 2024
# Versión: 1.0
# Dependencias: linux.c - código del programa a analizar
def generate_and_save_e_digits(n, filename):
    """ Genera un diccionario con la ocurrencia de cada palabra reservada en C de un archivo fuente
        ARGS: file_path (str): directorio del archivo del programa a evaluar
        RETURN: keyword_count (dict): ocurrencia de palabras reservadas
    """
    # Abre el archivo en modo escritura
    with open(filename, 'w') as file:
        # Inicializa las variables
        a = [1] * (n + 1)

        # Calcula las cifras de e utilizando el algoritmo Spigot
        for i in range(n):
            q = 0
            for j in range(n, 0, -1):
                a[j] = 10 * a[j] + q
                q = a[j] // j
                a[j] %= j
            a[0] = q
            # Escribe la cifra calculada al archivo
            file.write(str(a[0]))


if __name__ == "__main__":
    import math

    # Calcula el número de cifras a generar para obtener aproximadamente 5 GB de datos
    # Asumimos que cada cifra ocupa un byte
    num_gb = 1
    num_digits = num_gb * 1024 * 1024 * 1024

    # Nombre del archivo donde se guardarán las cifras
    filename = "e_digits_5gb.txt"

    # Genera y guarda las cifras en el archivo
    generate_and_save_e_digits(num_digits, filename)
    print(f"First {num_digits} digits of e saved to {filename}")
