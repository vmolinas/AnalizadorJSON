import os
import sys
import ply.yacc as yacc
from lexico import *
# from lexico import entradaJson
# from main import entradaJson
import warnings
warnings.filterwarnings("ignore")

def p_sigma(p):
    '''sigma : EMPRESAS_INIT'''
    print("El documento JSON es correcto")

def p_empresas(p):
    '''EMPRESAS_INIT : LLAVEA N_EMPRESAS COMA N_VERSION COMA F_DIGITAL LLAVEC
        | LLAVEA N_EMPRESAS COMA F_DIGITAL COMA N_VERSION LLAVEC
        | LLAVEA N_VERSION COMA N_EMPRESAS COMA F_DIGITAL LLAVEC
        | LLAVEA N_VERSION COMA F_DIGITAL COMA N_EMPRESAS LLAVEC
        | LLAVEA F_DIGITAL COMA N_EMPRESAS COMA N_VERSION LLAVEC
        | LLAVEA F_DIGITAL COMA N_VERSION COMA N_EMPRESAS LLAVEC
        | LLAVEA N_EMPRESAS COMA N_VERSION LLAVEC
        | LLAVEA N_EMPRESAS COMA F_DIGITAL LLAVEC
        | LLAVEA N_VERSION COMA N_EMPRESAS LLAVEC
        | LLAVEA F_DIGITAL COMA N_EMPRESAS LLAVEC
        | LLAVEA N_EMPRESAS LLAVEC
    '''
def p_version(p):
    '''N_VERSION : VERSION DPUNTOS STRING'''


def p_f_digital(p):
    '''F_DIGITAL : FIRMA_DIGITAL DPUNTOS STRING '''

def p_empresasi(p):
    '''N_EMPRESAS : EMPRESAS DPUNTOS CORCHETEA EMPRESA CORCHETEC'''

def p_empresa(p):
    '''EMPRESA : LLAVEA N_EMPRESA N_FUNDACION DIR INGRESOS_A N_PYME N_LINK DEPTOS LLAVEC COMA
        | LLAVEA N_EMPRESA N_FUNDACION INGRESOS_A N_PYME N_LINK DEPTOS LLAVEC COMA
        | LLAVEA N_EMPRESA N_FUNDACION DIR INGRESOS_A N_PYME DEPTOS LLAVEC COMA
        | LLAVEA N_EMPRESA N_FUNDACION INGRESOS_A N_PYME DEPTOS LLAVEC COMA
        | LLAVEA N_EMPRESA N_FUNDACION DIR INGRESOS_A N_PYME N_LINK DEPTOS LLAVEC COMA EMPRESA
        | LLAVEA N_EMPRESA N_FUNDACION INGRESOS_A N_PYME N_LINK DEPTOS LLAVEC COMA EMPRESA
        | LLAVEA N_EMPRESA N_FUNDACION DIR INGRESOS_A N_PYME DEPTOS LLAVEC COMA EMPRESA
        | LLAVEA N_EMPRESA N_FUNDACION INGRESOS_A N_PYME DEPTOS LLAVEC COMA EMPRESA
    '''

def p_nombre_empresa(p):
    '''N_EMPRESA : NOMBRE_EMPRESA DPUNTOS STRING COMA'''

def p_fundacion(p):
    '''N_FUNDACION : FUNDACION DPUNTOS INTEGER COMA'''

def p_ingresos_anuales(p):
    '''INGRESOS_A : INGRESOS_ANUALES DPUNTOS FLOAT COMA'''

def p_pyme(p):
    '''N_PYME : PYME DPUNTOS BOOLEAN COMA'''

def p_link(P):
    '''N_LINK : LINK DPUNTOS URI COMA
        | LINK DPUNTOS NULL COMA'''

def p_direccion(p):
    '''DIR : DIRECCION DPUNTOS LLAVEA N_CALLE N_CIUDAD N_PAIS LLAVEC COMA
        | DIRECCION DPUNTOS LLAVEA N_CALLE COMA N_PAIS COMA N_CIUDAD LLAVEC COMA
        | DIRECCION DPUNTOS LLAVEA N_CIUDAD COMA N_CALLE COMA N_PAIS LLAVEC COMA
        | DIRECCION DPUNTOS LLAVEA N_CIUDAD COMA N_PAIS COMA N_CALLE LLAVEC COMA
        | DIRECCION DPUNTOS LLAVEA N_PAIS COMA N_CALLE COMA N_CIUDAD LLAVEC COMA
        | DIRECCION DPUNTOS LLAVEA N_PAIS COMA N_CIUDAD COMA N_CALLE LLAVEC COMA
        | DIRECCION DPUNTOS LLAVEA LLAVEC
        | DIRECCION DPUNTOS NULL COMA
    '''

def p_calle(P):
    '''N_CALLE : CALLE DPUNTOS STRING'''

def p_ciudad(P):
    '''N_CIUDAD : CIUDAD DPUNTOS STRING'''

def p_pais(P):
    '''N_PAIS : PAIS DPUNTOS STRING'''

def p_departamentos(P):
    '''DEPTOS : DEPARTAMENTOS DPUNTOS CORCHETEA DEPTO CORCHETEC
    '''

def p_departamento(p):
    '''DEPTO : LLAVEA N_NOMBRE COMA N_JEFE COMA SUB_DEPTOS LLAVEC
        | LLAVEA N_NOMBRE COMA SUB_DEPTOS COMA N_JEFE LLAVEC
        | LLAVEA N_JEFE COMA N_NOMBRE COMA SUB_DEPTOS LLAVEC
        | LLAVEA N_JEFE COMA SUB_DEPTOS COMA N_NOMBRE LLAVEC
        | LLAVEA SUB_DEPTOS COMA N_NOMBRE COMA N_JEFE LLAVEC
        | LLAVEA SUB_DEPTOS COMA N_JEFE COMA N_NOMBRE LLAVEC
        | LLAVEA N_NOMBRE COMA SUB_DEPTOS LLAVEC
        | LLAVEA SUB_DEPTOS COMA N_NOMBRE LLAVEC
        | LLAVEA N_NOMBRE COMA N_JEFE COMA SUB_DEPTOS LLAVEC COMA DEPTOS
        | LLAVEA N_NOMBRE COMA SUB_DEPTOS COMA N_JEFE LLAVEC COMA DEPTOS
        | LLAVEA N_JEFE COMA N_NOMBRE COMA SUB_DEPTOS LLAVEC COMA DEPTOS
        | LLAVEA N_JEFE COMA SUB_DEPTOS COMA N_NOMBRE LLAVEC COMA DEPTOS
        | LLAVEA SUB_DEPTOS COMA N_NOMBRE COMA N_JEFE LLAVEC COMA DEPTOS
        | LLAVEA SUB_DEPTOS COMA N_JEFE COMA N_NOMBRE LLAVEC COMA DEPTOS
        | LLAVEA N_NOMBRE COMA SUB_DEPTOS LLAVEC COMA DEPTOS
        | LLAVEA SUB_DEPTOS COMA N_NOMBRE LLAVEC COMA DEPTOS
    '''

def p_nombre(p):
    '''N_NOMBRE : NOMBRE DPUNTOS STRING'''

def p_jefe(p):
    '''N_JEFE : JEFE DPUNTOS STRING
        | JEFE DPUNTOS NULL'''

def p_subdepartamentos(p):
    '''SUB_DEPTOS : SUBDEPARTAMENTOS DPUNTOS CORCHETEA SUB_DEPTO CORCHETEC COMA
    '''
    
def p_subdepartamento(p):
    '''SUB_DEPTO : LLAVEA N_NOMBRE COMA N_JEFE COMA N_EMPLEADOS LLAVEC
        | LLAVEA N_NOMBRE COMA N_EMPLEADOS COMA N_JEFE LLAVEA
        | LLAVEA N_JEFE COMA N_EMPLEADOS COMA N_NOMBRE LLAVEA
        | LLAVEA N_JEFE COMA N_NOMBRE COMA N_EMPLEADOS LLAVEA
        | LLAVEA N_EMPLEADOS COMA N_NOMBRE COMA N_JEFE LLAVEA
        | LLAVEA N_EMPLEADOS COMA N_JEFE COMA N_NOMBRE LLAVEA
        | LLAVEA N_NOMBRE COMA N_EMPLEADOS LLAVEA
        | LLAVEA N_NOMBRE COMA N_JEFE LLAVEA
        | LLAVEA N_NOMBRE LLAVEA
        | LLAVEA N_EMPLEADOS COMA N_NOMBRE LLAVEA
        | LLAVEA N_JEFE COMA N_NOMBRE CORCHETEC
        | LLAVEA N_NOMBRE COMA N_JEFE COMA N_EMPLEADOS LLAVEA COMA SUB_DEPTOS
        | LLAVEA N_NOMBRE COMA N_EMPLEADOS COMA N_JEFE LLAVEA COMA SUB_DEPTOS
        | LLAVEA N_JEFE COMA N_EMPLEADOS COMA N_NOMBRE LLAVEA COMA SUB_DEPTOS
        | LLAVEA N_JEFE COMA N_NOMBRE COMA N_EMPLEADOS LLAVEA COMA SUB_DEPTOS
        | LLAVEA N_EMPLEADOS COMA N_NOMBRE COMA N_JEFE LLAVEA COMA SUB_DEPTOS
        | LLAVEA N_EMPLEADOS COMA N_JEFE COMA N_NOMBRE LLAVEA COMA SUB_DEPTOS
        | LLAVEA N_NOMBRE COMA N_EMPLEADOS LLAVEA COMA SUB_DEPTOS
        | LLAVEA N_NOMBRE COMA N_JEFE LLAVEA COMA SUB_DEPTOS
        | LLAVEA N_NOMBRE CORCHETEC COMA SUB_DEPTOS
        | LLAVEA N_EMPLEADOS COMA N_NOMBRE CORCHETEC COMA SUB_DEPTOS
        | LLAVEA N_JEFE COMA N_NOMBRE CORCHETEC COMA SUB_DEPTOS
    '''

def p_empleados(p):
    '''N_EMPLEADOS : EMPLEADOS DPUNTOS CORCHETEA N_EMPLEADO CORCHETEC
        | EMPLEADOS DPUNTOS CORCHETEA CORCHETEC
        | EMPLEADOS DPUNTOS NULL
    '''

def p_empleado(p):
    '''N_EMPLEADO : LLAVEA N_NOMBRE COMA N_EDAD COMA N_CARGO COMA N_SALARIO COMA N_ACTIVO COMA F_CONTRATACION COMA N_PROYECTOS LLAVEC
        | LLAVEA N_NOMBRE COMA N_CARGO COMA N_SALARIO COMA N_ACTIVO COMA F_CONTRATACION COMA N_PROYECTOS LLAVEC
        | LLAVEA N_NOMBRE COMA N_EDAD COMA N_CARGO COMA N_SALARIO COMA N_ACTIVO COMA F_CONTRATACION LLAVEC
        | LLAVEA N_NOMBRE COMA N_CARGO COMA N_SALARIO COMA N_ACTIVO COMA F_CONTRATACION LLAVEC
        | LLAVEA N_NOMBRE COMA N_EDAD COMA N_CARGO COMA N_SALARIO COMA N_ACTIVO COMA F_CONTRATACION COMA N_PROYECTOS LLAVEC COMA N_EMPLEADOS
        | LLAVEA N_NOMBRE COMA N_CARGO COMA N_SALARIO COMA N_ACTIVO COMA F_CONTRATACION COMA N_PROYECTOS LLAVEC COMA N_EMPLEADOS
        | LLAVEA N_NOMBRE COMA N_EDAD COMA N_CARGO COMA N_SALARIO COMA N_ACTIVO COMA F_CONTRATACION LLAVEC COMA N_EMPLEADOS
        | LLAVEA N_NOMBRE COMA N_CARGO COMA N_SALARIO COMA N_ACTIVO COMA F_CONTRATACION LLAVEC COMA N_EMPLEADOS
    '''

def p_edad(p):
    '''N_EDAD : EDAD DPUNTOS INTEGER
        | EDAD DPUNTOS NULL
    '''

def p_cargo(p):
    '''N_CARGO : CARGO DPUNTOS CARGOS
    '''

def p_salario(p):
    '''N_SALARIO : SALARIO DPUNTOS FLOAT
    '''

def p_activo(p):
    '''N_ACTIVO : ACTIVO DPUNTOS BOOLEAN
    '''

def p_fecha_contratacion(p):
    '''F_CONTRATACION : FECHA_CONTRATACION DPUNTOS FECHA'''

def p_proyectos(p):
    '''N_PROYECTOS : PROYECTOS DPUNTOS CORCHETEA N_PROYECTO CORCHETEC
        | PROYECTOS DPUNTOS CORCHETEA CORCHETEC
        | PROYECTOS DPUNTOS NULL
    '''

def p_proyecto(p):
    '''N_PROYECTO : LLAVEA N_NOMBRE COMA N_ESTADO COMA F_INICIO COMA F_FIN LLAVEC
        | LLAVEA N_NOMBRE COMA F_INICIO COMA F_FIN LLAVEC
        | LLAVEA N_NOMBRE COMA N_ESTADO COMA F_INICIO LLAVEC
        | LLAVEA N_NOMBRE COMA F_INICIO LLAVEC
        | LLAVEA N_NOMBRE COMA N_ESTADO COMA F_INICIO COMA F_FIN LLAVEC COMA N_PROYECTOS
        | LLAVEA N_NOMBRE COMA F_INICIO COMA F_FIN LLAVEC COMA N_PROYECTOS
        | LLAVEA N_NOMBRE COMA N_ESTADO COMA F_INICIO LLAVEC COMA N_PROYECTOS
        | LLAVEA N_NOMBRE COMA F_INICIO LLAVEC COMA N_PROYECTOS
    '''

def p_estados(p):
    '''N_ESTADO : ESTADO DPUNTOS ESTADOS 
        | ESTADO DPUNTOS NULL
    '''

def p_fecha_inicio(p):
    '''F_INICIO : FECHA_INICIO DPUNTOS FECHA
    '''

def p_fecha_fin(p):
    '''F_FIN : FECHA_FIN DPUNTOS FECHA
        | FECHA_FIN DPUNTOS NULL
    '''

def p_error(p):
    # print("Error sintáctico en '%s'" % p.value + " [Línea: %d]" % p.lineno)
    # parser.errok()
    if p:
        print("Error sintáctico en '%s' [Línea: %d]" % (p.value, p.lineno))
        # Avanzar el parser un token
        parser.errok()
    else:
        print("Error sintáctico al final del archivo")


entradaJson = ""
entra = ""
salida = "out.html"

def search_files(folder, extension):
    files = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(extension):
                files.append(os.path.join(dirpath, filename))
    return files

if len(sys.argv) > 1:  # se ingresó un comando al ejecutar el programa
    entra = sys.argv[1]
    f = open(entra, 'r')
    salida = entra.split('.')[0] + '.html'
    entradaJson = f.read()
else:
    print("Ingrese 1 para ingresar un docbook por consola y 2 para ingresarlo por archivo")
    opcion = int(input())
    if opcion == 1:
        print("Ingrese el código por teclado.")
        print("Para terminar, presione Ctrl+Z en Windows o Ctrl+D en sistemas UNIX/Linux")
        while True:
            try:
                entra = input('> ')
                entradaJson += entra + '\n'
            except EOFError:
                break
    elif opcion == 2:
        while True:
            print("Ingrese el nombre/dirección de la carpeta:")
            folder = input()
            files = search_files(folder, ".json")
            if len(files) == 0:
                print("No se encontraron archivos en la carpeta especificada.")
                continue
            print("Archivos encontrados:")
            for i, f in enumerate(files):
                print(f"{i+1}. {f}")
            print("Ingrese el número del archivo que desea seleccionar:")
            file_num = int(input())
            if file_num < 1 or file_num > len(files):
                print("Número de archivo inválido.")
                continue
            entra = files[file_num - 1]
            f = open(entra, "r", encoding="utf-8")
            salida = entra.split('.')[0] + '.html'
            entradaJson = f.read()
            break
    else:
        print("Ingrese una opción válida.")
        quit()

file = open(salida, 'w')



parser = yacc.yacc(debug=0,start='sigma')
# parser = yacc.yacc(start='sigma')
result = parser.parse(entradaJson)

print (result)