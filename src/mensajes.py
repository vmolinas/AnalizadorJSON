# Mensaje predeterminado para los elementos reconocidos

def imprimirMensajeKey(t):
    print(t.lineno, " KEY: " + t.value, end="")

def imprimirMensajeKeyNV(t):
    print(t.lineno, " KEY: " + t.value)

def imprimirMensajeValor(t):
    print(t.lineno, " VALOR: " + t.value)
    # print(" VALOR: " + t.value)

def imprimirError(t):
    print("Token no reconocido: ", t.value + " [Linea:" , t.lineno,"]")

def imprimirApertura(t):
    print(t.lineno, " APERTURA: " + t.value)
    
def imprimirCierre(t):
    print(t.lineno, " CIERRE: " + t.value)