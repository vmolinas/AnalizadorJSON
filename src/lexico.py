import warnings

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
    return (t)

def t_CORCHETEA(t):
    r'\['
    return (t)

def t_CORCHETEC(t):
    r'\]'
    return (t)

def t_LLAVEA(t):
    r'\{'
    return (t)

def t_LLAVEC(t):
    r'\}'
    return (t)

def t_DPUNTOS(t):
    r'\:'
    return (t)

def t_NULL(t):
    r'null'
    return (t)

def t_FALSE(t):
    r'false'
    return (t)

def t_TRUE(t):
    r'true'
    return (t)

def t_URI(t):
    r'"(http|https|ftp)://[^\s<>&]+(\.[^\s<>&]+)*(:\d+)?(/[^\s<>&]*)*(\?[^\s<>&]*)?(\#[^\s<>&]*)?"'
    return (t)

def t_EMPRESAS(t):
    r'"empresas"'
    return (t)

def t_VERSION(t):
    r'"version"'
    return (t)

def t_FIRMA_DIGITAL(t):
    r'"firma_digital"'
    return (t)

def t_NOMBRE_EMPRESA(t):
    r'"nombre_empresa"'
    return (t)

def t_FUNDACION(t):
    r'"fundación"'
    return (t)

def t_DIRECCION(t):
    r'"dirección"'
    return (t)

def t_INGRESOS_ANUALES(t):
    r'"ingresos_anuales"'
    return (t)

def t_PYME(t):
    r'"pyme"'
    return (t)

def t_LINK(t):
    r'"link"'
    return (t)

def t_DEPARTAMENTOS(t):
    r'"departamentos"'
    return (t)

def t_CALLE(t):
    r'"calle"'
    return (t)

def t_CIUDAD(t):
    r'"ciudad"'
    return (t)

def t_PAIS(t):
    r'"país"'
    return (t)

def t_NOMBRE(t):
    r'"nombre"'
    return (t)

def t_JEFE(t):
    r'"jefe"'
    return (t)

def t_SUBDEPARTAMENTOS(t):
    r'"subdepartamentos"'
    return (t)

def t_EMPLEADOS(t):
    r'"empleados"'
    return (t)

def t_EDAD(t):
    r'"edad"'
    return (t)

def t_CARGO(t):
    r'"cargo"'
    return (t)

def t_SALARIO(t):
    r'"salario"'
    return (t)

def t_ACTIVO(t):
    r'"activo"'
    return (t)

def t_FECHA_CONTRATACION(t):
    r'"fecha_contratación"'
    return (t)

def t_PROYECTOS(t):
    r'"proyectos"'
    return (t)

def t_ESTADO(t):
    r'"estado"'
    return (t)

def t_FECHA_INICIO(t):
    r'"fecha_inicio"'
    return (t)

def t_FECHA_FIN(t):
    r'"fecha_fin"'
    return (t)

def t_FLOAT(t):
    r'[0-9]+\.[0-9]+'
    return (t)

def t_INTEGER(t):
    r'[0-9]+'
    return (t)

def t_FECHA(t):
    r'"((19[0-9]{2}|20[0-9]{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01]))"'
    return (t)

def t_STRING(t):
    r'"[a-zA-Z0-9 | _ | \- | , | . | : | \{ | \} | \[ | \] | \t]+"'
    return (t)

def t_error(t):
    print("TOKEN NO RECONOCIDO: ", t.value + " [Linea:", t.lineno, "]")
    t.lexer.skip(1)