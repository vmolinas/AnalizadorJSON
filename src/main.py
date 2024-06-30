import os
import sys
import inquirer
import ply.lex as lex
from parser_p import parser
from lexico import *

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

def search_files(folder, extension):
    """
    Busca archivos con una extensión específica en un directorio y sus subdirectorios.
    Args:
        folder (str): Directorio raíz donde comenzar la búsqueda.
        extension (str): Extensión de archivo a buscar (por ejemplo, '.json').
    Returns:
        list: Lista de rutas completas de archivos encontrados.
    """
    files = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(extension):
                files.append(os.path.join(dirpath, filename))
    return files

# Obtener el directorio del script actual
directorio_actual = os.path.dirname(os.path.abspath(__file__))
    
# Obtener el directorio de pruebas que está un nivel arriba del actual
directorio_pruebas = os.path.abspath(os.path.join(directorio_actual, "..", "prueba"))

# Inicializar la variable ruta_archivo_json
ruta_archivo_json = None

# Si se proporciona un argumento de línea de comandos, léelo como archivo de entrada
if len(sys.argv) > 1:
    ruta_archivo_json = sys.argv[1]
    entradaJson = obtener_entrada_desde_archivo(ruta_archivo_json)
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
        ruta_archivo_json = os.path.join(directorio_pruebas, archivo_seleccionado)
        entradaJson = obtener_entrada_desde_archivo(ruta_archivo_json)

# Procesar la entrada con el lexer
lexer.input(entradaJson)

# Parser
result = parser.parse(entradaJson)

# Generar archivo HTML de salida con el mismo nombre que el archivo JSON
if ruta_archivo_json:
    nombre_archivo = os.path.splitext(os.path.basename(ruta_archivo_json))[0]
    directorio_salida = os.path.dirname(ruta_archivo_json)
    salida_html = os.path.join(directorio_salida, nombre_archivo + '.html')

    file = open(salida_html, 'w')
    file.write(str(result))
    file.close()

    print(f"Archivo HTML generado: {salida_html}")
else:
    print("No se ha especificado un archivo JSON de entrada.")