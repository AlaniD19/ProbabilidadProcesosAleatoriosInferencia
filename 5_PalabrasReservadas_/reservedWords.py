# CIC IPN / MCIC
# Programa: reservedWords.py
# Descripción:
# Autor: Alan Delgado
# Fecha de creación: Junio 2024
# Versión: 1.0
# Dependencias: linux.c - código del programa a analizar

# Lista de palabras reservadas en C basada en:
# https://www.ibm.com/docs/es/debug-for-zos/16.0?topic=programs-c-reserved-keywords
c_keywords = [
    "auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern", "float",
    "for", "goto", "if", "int", "long", "register", "return", "short", "signed", "sizeof", "static", "struct", "switch",
    "typedef", "union", "unsigned", "void", "volatile", "while"
]


def count_c_keywords(file_path):
    """ Genera un diccionario con la ocurrencia de cada palabra reservada en C de un archivo fuente
        ARGS: file_path (str): directorio del archivo del programa a evaluar
        RETURN: keyword_count (dict): ocurrencia de palabras reservadas
    """
    keyword_count = {keyword: 0 for keyword in c_keywords}      # diccionario para contar las palabras reservadas
    try:                                                        # intentar abrir el archivo
        with open(file_path, 'r') as file:                      # Abrir el archivo en modo de lectura
            content = file.read()                               # Leer el contenido del archivo
        words = content.split()                                 # Separar el contenido en palabras
        for word in words:                                      # Contar las ocurrencias de cada palabra reservada
            if word in keyword_count:
                keyword_count[word] += 1
    except FileNotFoundError:                                   # si existe algún error al abrirlo
        print(f"El archivo {file_path} no fue encontrado.")     # mostramos un error
    return keyword_count                                        # al final regresamos el diccionario con las ocurrencias


if __name__ == "__main__":
    file_path = "ruta/al/archivo.c"                             # Ruta del archivo a analizar
    keyword_occurrences = count_c_keywords(file_path)           # Obtener el diccionario con las ocurrencias
    for keyword, count in keyword_occurrences.items():          # Mostrar el resultado
        print(f"{keyword}: {count}")
