import warnings
from mensajes import *

warnings.filterwarnings("ignore")

tokens = ("NEWLINE", "BLANK", "COMA", "CORCHETEA", "CORCHETEC", "LLAVEA", "LLAVEC", "DPUNTOS",
          "NULL", "FALSE", "TRUE", "URI", "EMPRESAS", "VERSION", "FIRMA_DIGITAL",
          "NOMBRE_EMPRESA", "FUNDACION", "DIRECCION", "INGRESOS_ANUALES", "PYME",
          "LINK", "DEPARTAMENTOS", "CALLE", "CIUDAD", "PAIS", "NOMBRE", "JEFE",
          "SUBDEPARTAMENTOS", "EMPLEADOS", "EDAD", "CARGO", "SALARIO", "ACTIVO",
          "FECHA_CONTRATACION", "PROYECTOS", "ESTADO", "FECHA_INICIO", "FECHA_FIN",
          "FLOAT", "INTEGER", "FECCHA", "STRING")

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_BLANK(t):
    r'(\s)+'

def t_COMA(t):
    r'\,'

def t_CORCHETEA(t):
    r'\['
    imprimirApertura(t)

def t_CORCHETEC(t):
    r'\]'
    imprimirCierre(t)

def t_LLAVEA(t):
    r'\{'
    imprimirApertura(t)

def t_LLAVEC(t):
    r'\}'
    imprimirCierre(t)

def t_DPUNTOS(t):
    r'\:'

def t_NULL(t):
    r'null'
    imprimirMensajeValor(t)

def t_FALSE(t):
    r'false'
    imprimirMensajeValor(t)

def t_TRUE(t):
    r'true'
    imprimirMensajeValor(t)

def t_URI(t):
    r'"(http|https|ftp)://[^\s<>&]+(\.[^\s<>&]+)*(:\d+)?(/[^\s<>&]*)*(\?[^\s<>&]*)?(\#[^\s<>&]*)?"'
    imprimirMensajeValor(t)

def t_EMPRESAS(t):
    r'"empresas"'
    imprimirMensajeKeyNV(t)

def t_VERSION(t):
    r'"version"'
    imprimirMensajeKeyNV(t)

def t_FIRMA_DIGITAL(t):
    r'"firma_digital"'
    imprimirMensajeKeyNV(t)

def t_NOMBRE_EMPRESA(t):
    r'"nombre_empresa"'
    imprimirMensajeKeyNV(t)

def t_FUNDACION(t):
    r'"fundación"'
    imprimirMensajeKeyNV(t)

def t_DIRECCION(t):
    r'"dirección"'
    imprimirMensajeKeyNV(t)

def t_INGRESOS_ANUALES(t):
    r'"ingresos_anuales"'
    imprimirMensajeKeyNV(t)

def t_PYME(t):
    r'"pyme"'
    imprimirMensajeKeyNV(t)

def t_LINK(t):
    r'"link"'
    imprimirMensajeKeyNV(t)

def t_DEPARTAMENTOS(t):
    r'"departamentos"'
    imprimirMensajeKeyNV(t)

def t_CALLE(t):
    r'"calle"'
    imprimirMensajeKeyNV(t)

def t_CIUDAD(t):
    r'"ciudad"'
    imprimirMensajeKeyNV(t)

def t_PAIS(t):
    r'"país"'
    imprimirMensajeKeyNV(t)

def t_NOMBRE(t):
    r'"nombre"'
    imprimirMensajeKeyNV(t)

def t_JEFE(t):
    r'"jefe"'
    imprimirMensajeKeyNV(t)

def t_SUBDEPARTAMENTOS(t):
    r'"subdepartamentos"'
    imprimirMensajeKeyNV(t)

def t_EMPLEADOS(t):
    r'"empleados"'
    imprimirMensajeKeyNV(t)

def t_EDAD(t):
    r'"edad"'
    imprimirMensajeKeyNV(t)

def t_CARGO(t):
    r'"cargo"'
    imprimirMensajeKeyNV(t)

def t_SALARIO(t):
    r'"salario"'
    imprimirMensajeKeyNV(t)

def t_ACTIVO(t):
    r'"activo"'
    imprimirMensajeKeyNV(t)

def t_FECHA_CONTRATACION(t):
    r'"fecha_contratación"'
    imprimirMensajeKeyNV(t)

def t_PROYECTOS(t):
    r'"proyectos"'
    imprimirMensajeKeyNV(t)

def t_ESTADO(t):
    r'"estado"'
    imprimirMensajeKeyNV(t)

def t_FECHA_INICIO(t):
    r'"fecha_inicio"'
    imprimirMensajeKeyNV(t)

def t_FECHA_FIN(t):
    r'"fecha_fin"'
    imprimirMensajeKeyNV(t)

def t_FLOAT(t):
    r'[0-9]+\.[0-9]+'
    imprimirMensajeValor(t)

def t_INTEGER(t):
    r'[0-9]+'
    imprimirMensajeValor(t)

def t_FECHA(t):
    r'"\d{4}-\d{2}-\d{2}"'
    imprimirMensajeValor(t)

def t_STRING(t):
    r'"[a-zA-Z0-9 | _ | \- | , | . | : | \{ | \} | \[ | \] | \t]+"'
    imprimirMensajeValor(t)

def t_error(t):
    imprimirError(t)
    t.lexer.skip(1)