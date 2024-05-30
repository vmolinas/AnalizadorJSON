import sys
import os
import inquirer
from lexico import *
import ply.lex as lex

lexer = lex.lex(debug=0)

def listar_archivos(directorio):
    """
    Lista todos los archivos en un directorio dado.
    Args: directorio (str): Ruta del directorio a listar.
    Returns: list: Lista de nombres de archivos en el directorio.
    """
    try:
        archivos = os.listdir(directorio)
        archivos = [f for f in archivos if os.path.isfile(os.path.join(directorio, f))]
        return archivos
    except FileNotFoundError:
        print(f"El directorio {directorio} no se encontró.")
        sys.exit(1)

def seleccionar_archivo(archivos):
    """
    Muestra un menú interactivo para seleccionar un archivo de una lista.
    Args: archivos (list): Lista de nombres de archivos.
    Returns: str: Nombre del archivo seleccionado.
    """
    preguntas = [
        inquirer.List('archivo',
                      message="Seleccione un archivo",
                      choices=archivos,
                      carousel=True)
    ]
    respuestas = inquirer.prompt(preguntas)
    return respuestas['archivo']

def obtener_entrada_desde_archivo(archivo_path):
    """
    Lee el contenido de un archivo y lo devuelve como una cadena.
    Args: archivo_path (str): Ruta del archivo a leer.
    Returns: str: Contenido del archivo.
    """
    try:
        with open(archivo_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"El archivo {archivo_path} no se encontró.")
        sys.exit(1)

def obtener_entrada_desde_consola():
    """
    Lee la entrada del usuario desde la consola hasta que se introduce EOF (Ctrl+D o Ctrl+Z).
    Returns: str: Entrada del usuario como una cadena.
    """
    print("Ingrese por consola, una vez terminado apriete CTRL+Z (Windows) o CTRL+D (Linux)")
    entradaJson = ""
    while True:
        try:
            entra = input()
            entradaJson += entra + "\n"
        except EOFError:
            break
    return entradaJson

if __name__ == '__main__':
    entradaJson = ""

    # Obtener el directorio del script actual
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    
    # Obtener el directorio de pruebas que está un nivel arriba del actual
    directorio_pruebas = os.path.abspath(os.path.join(directorio_actual, "..", "prueba"))

    # Si se proporciona un argumento de línea de comandos, léelo como archivo de entrada
    if len(sys.argv) > 1:
        entradaJson = obtener_entrada_desde_archivo(sys.argv[1])
    else:
        # Pregunta al usuario si quiere seleccionar un archivo o escribir por consola
        preguntas = [
            inquirer.List('opcion',
                          message="--OPCIONES--",
                          choices=['Seleccionar archivo desde la carpeta de pruebas', 'Escribir por consola'],
                          carousel=True)
        ]
        respuestas = inquirer.prompt(preguntas)
        opcion = respuestas['opcion']

        # Obtener entrada del usuario según la opción seleccionada
        if opcion == 'Escribir por consola':
            entradaJson = obtener_entrada_desde_consola()
        elif opcion == 'Seleccionar archivo desde la carpeta de pruebas':
            archivos = listar_archivos(directorio_pruebas)
            if not archivos:
                print(f"No hay archivos en el directorio {directorio_pruebas}.")
                sys.exit(1)
            archivo_seleccionado = seleccionar_archivo(archivos)
            ruta_archivo = os.path.join(directorio_pruebas, archivo_seleccionado)
            entradaJson = obtener_entrada_desde_archivo(ruta_archivo)

    # Procesar la entrada con el lexer
    lexer.input(entradaJson)

    # Se pasa la entrada obtenida al lexer para su procesamiento y se imprime cada token generado.
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)