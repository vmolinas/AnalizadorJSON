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

def t_CORCHETEA(t):
    r'\['
    print(t.lineno, " APERTURA CORCHETE: " + t.value)

def t_CORCHETEC(t):
    r'\]'
    print(t.lineno, " CIERRE CORCHETE: " + t.value)

def t_LLAVEA(t):
    r'\{'
    print(t.lineno, " APERTURA LLAVE: " + t.value)

def t_LLAVEC(t):
    r'\}'
    print(t.lineno, " CIERRE LLAVE: " + t.value)

def t_DPUNTOS(t):
    r'\:'

def t_NULL(t):
    r'null'
    print(t.lineno, " VALOR: " + t.value)

def t_FALSE(t):
    r'false'
    print(t.lineno, " BOOLEANO: " + t.value)

def t_TRUE(t):
    r'true'
    print(t.lineno, " BOOLEANO: " + t.value)

def t_URI(t):
    r'"(http|https|ftp)://[^\s<>&]+(\.[^\s<>&]+)*(:\d+)?(/[^\s<>&]*)*(\?[^\s<>&]*)?(\#[^\s<>&]*)?"'
    print(t.lineno, " URL: " + t.value)

def t_EMPRESAS(t):
    r'"empresas"'
    print(t.lineno, " KEY EMPRESAS: " + t.value)

def t_VERSION(t):
    r'"version"'
    print(t.lineno, " KEY VERSION: " + t.value)

def t_FIRMA_DIGITAL(t):
    r'"firma_digital"'
    print(t.lineno, " KEY FIRMA DIGITAL: " + t.value)

def t_NOMBRE_EMPRESA(t):
    r'"nombre_empresa"'
    print(t.lineno, " KEY NOMBRE EMPRESA: " + t.value)

def t_FUNDACION(t):
    r'"fundación"'
    print(t.lineno, " KEY FUNDACION: " + t.value)

def t_DIRECCION(t):
    r'"dirección"'
    print(t.lineno, " KEY DIRECCION: " + t.value)

def t_INGRESOS_ANUALES(t):
    r'"ingresos_anuales"'
    print(t.lineno, " KEY INGRESOS ANUALES: " + t.value)

def t_PYME(t):
    r'"pyme"'
    print(t.lineno, " KEY PYME: " + t.value)

def t_LINK(t):
    r'"link"'
    print(t.lineno, " KEY LINK: " + t.value)

def t_DEPARTAMENTOS(t):
    r'"departamentos"'
    print(t.lineno, " KEY DEPARTAMENTOS: " + t.value)

def t_CALLE(t):
    r'"calle"'
    print(t.lineno, " KEY CALLE: " + t.value)

def t_CIUDAD(t):
    r'"ciudad"'
    print(t.lineno, " KEY CIUDAD: " + t.value)

def t_PAIS(t):
    r'"país"'
    print(t.lineno, " KEY PAIS: " + t.value)

def t_NOMBRE(t):
    r'"nombre"'
    print(t.lineno, " KEY NOMBRE: " + t.value)

def t_JEFE(t):
    r'"jefe"'
    print(t.lineno, " KEY JEFE: " + t.value)

def t_SUBDEPARTAMENTOS(t):
    r'"subdepartamentos"'
    print(t.lineno, " KEY SUBDEPARTAMENTOS: " + t.value)

def t_EMPLEADOS(t):
    r'"empleados"'
    print(t.lineno, " KEY EMPLEADOS: " + t.value)

def t_EDAD(t):
    r'"edad"'
    print(t.lineno, " KEY EDAD: " + t.value)

def t_CARGO(t):
    r'"cargo"'
    print(t.lineno, " KEY CARGO: " + t.value)

def t_SALARIO(t):
    r'"salario"'
    print(t.lineno, " KEY SALARIO: " + t.value)

def t_ACTIVO(t):
    r'"activo"'
    print(t.lineno, " KEY ACTIVO: " + t.value)

def t_FECHA_CONTRATACION(t):
    r'"fecha_contratación"'
    print(t.lineno, " KEY FECHA CONTRATACION: " + t.value)

def t_PROYECTOS(t):
    r'"proyectos"'
    print(t.lineno, " KEY PROYECTOS: " + t.value)

def t_ESTADO(t):
    r'"estado"'
    print(t.lineno, " KEY ESTADO: " + t.value)

def t_FECHA_INICIO(t):
    r'"fecha_inicio"'
    print(t.lineno, " KEY FECHA INICIO: " + t.value)

def t_FECHA_FIN(t):
    r'"fecha_fin"'
    print(t.lineno, " KEY FECHA FIN: " + t.value)

def t_FLOAT(t):
    r'[0-9]+\.[0-9]+'
    print(t.lineno, " FLOAT: " + t.value)

def t_INTEGER(t):
    r'[0-9]+'
    print(t.lineno, " INTEGER: " + t.value)

def t_FECHA(t):
    r'"((19[0-9]{2}|20[0-9]{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01]))"'
    print(t.lineno, " FECHA: " + t.value)

def t_STRING(t):
    r'"[a-zA-Z0-9 | _ | \- | , | . | : | \{ | \} | \[ | \] | \t]+"'
    print(t.lineno, " STRING: " + t.value)

def t_error(t):
    print("TOKEN NO RECONOCIDO: ", t.value + " [Linea:", t.lineno, "]")
    t.lexer.skip(1)