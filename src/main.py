import sys
import os
import inquirer
from lexico import *
import ply.lex as lex

lexer = lex.lex(debug=0)  # debug=1 si queremos ver que hace internamente

def listar_archivos(directorio):
    try:
        archivos = os.listdir(directorio)
        archivos = [f for f in archivos if os.path.isfile(os.path.join(directorio, f))]
        return archivos
    except FileNotFoundError:
        print(f"El directorio {directorio} no se encontró.")
        sys.exit(1)

def seleccionar_archivo(archivos):
    preguntas = [
        inquirer.List('archivo',
                      message="Seleccione un archivo",
                      choices=archivos,
                      carousel=True)
    ]
    respuestas = inquirer.prompt(preguntas)
    return respuestas['archivo']

if __name__ == '__main__':
    entradaJson = ""

    # Obtener el directorio del script actual
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    
    # Obtener el directorio de pruebas que está un nivel arriba del actual
    directorio_pruebas = os.path.abspath(os.path.join(directorio_actual, "..", "prueba"))

    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], 'r') as f:
                entradaJson = f.read()
        except FileNotFoundError:
            print(f"El archivo {sys.argv[1]} no se encontró.")
            sys.exit(1)
    else:
        print("--OPCIONES--")
        print("1. Escribir por consola")
        print("2. Seleccionar archivo desde la carpeta de pruebas")
        try:
            opcion = int(input())
        except ValueError:
            print("Ingrese una opción válida")
            sys.exit(1)

        if opcion == 1:
            print("Ingrese por consola, una vez terminado apriete CTRL+D (Linux) o CTRL+Z (Windows)")
            while True:
                try:
                    entra = input()
                    entradaJson += entra + "\n"
                except EOFError:
                    break
        elif opcion == 2:
            archivos = listar_archivos(directorio_pruebas)
            if not archivos:
                print(f"No hay archivos en el directorio {directorio_pruebas}.")
                sys.exit(1)
            archivo_seleccionado = seleccionar_archivo(archivos)
            ruta_archivo = os.path.join(directorio_pruebas, archivo_seleccionado)
            try:
                with open(ruta_archivo, 'r') as f:
                    entradaJson = f.read()
            except FileNotFoundError:
                print(f"El archivo {ruta_archivo} no se encontró.")
                sys.exit(1)
        else:
            print("Ingrese una opción válida")
            sys.exit(1)

    lexer.input(entradaJson)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)