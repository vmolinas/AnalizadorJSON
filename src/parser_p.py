import ply.yacc as yacc
from lexico import *
import warnings
warnings.filterwarnings("ignore")

def p_sigma(p):
    '''sigma : empresas_init'''
    print("El documento JSON es correcto")

def p_empresas(p):
    '''empresas_init : LLAVEA n_empresas n_version f_digital LLAVEC
        | LLAVEA n_empresas f_digital n_version LLAVEC
        | LLAVEA n_version n_empresas f_digital LLAVEC
        | LLAVEA n_version f_digital n_empresas LLAVEC
        | LLAVEA f_digital n_empresas n_version LLAVEC
        | LLAVEA f_digital n_version n_empresas LLAVEC
        | LLAVEA n_empresas n_version LLAVEC
        | LLAVEA n_empresas f_digital LLAVEC
        | LLAVEA n_version n_empresas LLAVEC
        | LLAVEA f_digital n_empresas LLAVEC
        | LLAVEA n_empresas LLAVEC
    '''

def p_version(p):
    '''n_version : VERSION DPUNTOS STRING
        | VERSION DPUNTOS STRING COMA'''

def p_f_digital(p):
    '''f_digital : FIRMA_DIGITAL DPUNTOS STRING
        | FIRMA_DIGITAL DPUNTOS STRING COMA'''

def p_empresasi(p):
    '''n_empresas : EMPRESAS DPUNTOS CORCHETEA EMPRESA CORCHETEC'''

def p_empresa(p):
    '''EMPRESA : LLAVEA n_empresa n_fundacion dir ingresos_a n_pyme n_link deptos LLAVEC
        | LLAVEA n_empresa n_fundacion ingresos_a n_pyme n_link deptos LLAVEC
        | LLAVEA n_empresa n_fundacion dir ingresos_a n_pyme deptos LLAVEC
        | LLAVEA n_empresa n_fundacion ingresos_a n_pyme deptos LLAVEC
        | LLAVEA n_empresa n_fundacion dir ingresos_a n_pyme n_link deptos LLAVEC COMA EMPRESA
        | LLAVEA n_empresa n_fundacion ingresos_a n_pyme n_link deptos LLAVEC COMA EMPRESA
        | LLAVEA n_empresa n_fundacion dir ingresos_a n_pyme deptos LLAVEC COMA EMPRESA
        | LLAVEA n_empresa n_fundacion ingresos_a n_pyme deptos LLAVEC COMA EMPRESA
    '''

def p_nombre_empresa(p):
    '''n_empresa : NOMBRE_EMPRESA DPUNTOS STRING COMA'''

def p_fundacion(p):
    '''n_fundacion : FUNDACION DPUNTOS INTEGER COMA'''

def p_ingresos_anuales(p):
    '''ingresos_a : INGRESOS_ANUALES DPUNTOS FLOAT COMA'''

def p_pyme(p):
    '''n_pyme : PYME DPUNTOS BOOLEAN COMA'''

def p_link(P):
    '''n_link : LINK DPUNTOS URI COMA
        | LINK DPUNTOS NULL COMA'''

def p_direccion(p):
    '''dir : DIRECCION DPUNTOS LLAVEA n_calle n_ciudad n_pais LLAVEC COMA
        | DIRECCION DPUNTOS LLAVEA n_calle n_pais n_ciudad LLAVEC COMA
        | DIRECCION DPUNTOS LLAVEA n_ciudad n_calle n_pais LLAVEC COMA
        | DIRECCION DPUNTOS LLAVEA n_ciudad n_pais n_calle LLAVEC COMA
        | DIRECCION DPUNTOS LLAVEA n_pais n_calle n_ciudad LLAVEC COMA
        | DIRECCION DPUNTOS LLAVEA n_pais n_ciudad n_calle LLAVEC COMA
        | DIRECCION DPUNTOS LLAVEA LLAVEC COMA
        | DIRECCION DPUNTOS NULL COMA
    '''

def p_calle(P):
    '''n_calle : CALLE DPUNTOS STRING COMA
        | CALLE DPUNTOS STRING'''

def p_ciudad(P):
    '''n_ciudad : CIUDAD DPUNTOS STRING COMA
        | CIUDAD DPUNTOS STRING'''

def p_pais(P):
    '''n_pais : PAIS DPUNTOS STRING COMA
        | PAIS DPUNTOS STRING'''

def p_departamentos(P):
    '''deptos : DEPARTAMENTOS DPUNTOS CORCHETEA depto CORCHETEC
    '''

def p_departamento(p):
    '''depto : LLAVEA n_nombre n_jefe sub_deptos LLAVEC
        | LLAVEA n_nombre sub_deptos n_jefe LLAVEC
        | LLAVEA n_jefe n_nombre sub_deptos LLAVEC
        | LLAVEA n_jefe sub_deptos n_nombre LLAVEC
        | LLAVEA sub_deptos n_nombre n_jefe LLAVEC
        | LLAVEA sub_deptos n_jefe n_nombre LLAVEC
        | LLAVEA n_nombre sub_deptos LLAVEC
        | LLAVEA sub_deptos n_nombre LLAVEC
        | LLAVEA n_nombre n_jefe sub_deptos LLAVEC COMA deptos
        | LLAVEA n_nombre sub_deptos n_jefe LLAVEC COMA deptos
        | LLAVEA n_jefe n_nombre sub_deptos LLAVEC COMA deptos
        | LLAVEA n_jefe sub_deptos n_nombre LLAVEC COMA deptos
        | LLAVEA sub_deptos n_nombre n_jefe LLAVEC COMA deptos
        | LLAVEA sub_deptos n_jefe n_nombre LLAVEC COMA deptos
        | LLAVEA n_nombre sub_deptos LLAVEC COMA deptos
        | LLAVEA sub_deptos n_nombre LLAVEC COMA deptos
    '''

def p_nombre(p):
    '''n_nombre : NOMBRE DPUNTOS STRING COMA
        | NOMBRE DPUNTOS STRING'''


def p_jefe(p):
    '''n_jefe : JEFE DPUNTOS STRING COMA
        | JEFE DPUNTOS NULL COMA
        | JEFE DPUNTOS STRING
        | JEFE DPUNTOS NULL'''

def p_subdepartamentos(p):
    '''sub_deptos : SUBDEPARTAMENTOS DPUNTOS CORCHETEA sub_depto CORCHETEC
        | SUBDEPARTAMENTOS DPUNTOS CORCHETEA sub_depto CORCHETEC COMA
    '''

def p_subdepartamento(p):
    '''sub_depto : LLAVEA n_nombre n_jefe n_empleados LLAVEC
        | LLAVEA n_nombre n_empleados n_jefe LLAVEC
        | LLAVEA n_jefe n_empleados n_nombre LLAVEC
        | LLAVEA n_jefe n_nombre n_empleados LLAVEC
        | LLAVEA n_empleados n_nombre n_jefe LLAVEC
        | LLAVEA n_empleados n_jefe n_nombre LLAVEC
        | LLAVEA n_nombre n_empleados LLAVEC
        | LLAVEA n_nombre n_jefe LLAVEC
        | LLAVEA n_nombre LLAVEC
        | LLAVEA n_empleados n_nombre LLAVEC
        | LLAVEA n_jefe n_nombre LLAVEC
        | LLAVEA n_nombre n_jefe n_empleados LLAVEC COMA sub_deptos
        | LLAVEA n_nombre n_empleados n_jefe LLAVEC COMA sub_deptos
        | LLAVEA n_jefe n_empleados n_nombre LLAVEC COMA sub_deptos
        | LLAVEA n_jefe n_nombre n_empleados LLAVEC COMA sub_deptos
        | LLAVEA n_empleados n_nombre n_jefe LLAVEC COMA sub_deptos
        | LLAVEA n_empleados n_jefe n_nombre LLAVEC COMA sub_deptos
        | LLAVEA n_nombre n_empleados LLAVEC sub_deptos
        | LLAVEA n_nombre n_jefe LLAVEC sub_deptos
        | LLAVEA n_nombre LLAVEC sub_deptos
        | LLAVEA n_empleados n_nombre LLAVEC COMA sub_deptos
        | LLAVEA n_jefe n_nombre LLAVEC COMA sub_deptos
    '''

def p_empleados(p):
    '''n_empleados : EMPLEADOS DPUNTOS CORCHETEA n_empleado CORCHETEC
        | EMPLEADOS DPUNTOS CORCHETEA CORCHETEC
        | EMPLEADOS DPUNTOS NULL
    '''

def p_empleado(p):
    '''n_empleado : LLAVEA n_nombre n_edad n_cargo n_salario n_activo f_contratacion n_proyectos LLAVEC
        | LLAVEA n_nombre n_cargo n_salario n_activo f_contratacion n_proyectos LLAVEC
        | LLAVEA n_nombre n_edad n_cargo n_salario n_activo f_contratacion LLAVEC
        | LLAVEA n_nombre n_cargo n_salario n_activo f_contratacion LLAVEC
        | LLAVEA n_nombre n_edad n_cargo n_salario n_activo f_contratacion n_proyectos LLAVEC COMA n_empleados
        | LLAVEA n_nombre n_cargo n_salario n_activo f_contratacion n_proyectos LLAVEC COMA n_empleados
        | LLAVEA n_nombre n_edad n_cargo n_salario n_activo f_contratacion LLAVEC COMA n_empleados
        | LLAVEA n_nombre n_cargo n_salario n_activo f_contratacion LLAVEC COMA n_empleados
    '''

def p_edad(p):
    '''n_edad : EDAD DPUNTOS INTEGER COMA
        | EDAD DPUNTOS NULL COMA
    '''

def p_cargo(p):
    '''n_cargo : CARGO DPUNTOS CARGOS COMA
    '''

def p_salario(p):
    '''n_salario : SALARIO DPUNTOS FLOAT COMA
        | SALARIO DPUNTOS INTEGER COMA
    '''

def p_activo(p):
    '''n_activo : ACTIVO DPUNTOS BOOLEAN COMA
    '''

def p_fecha_contratacion(p):
    '''f_contratacion : FECHA_CONTRATACION DPUNTOS FECHA COMA'''


def p_proyectos(p):
    '''n_proyectos : PROYECTOS DPUNTOS CORCHETEA n_proyecto CORCHETEC
        | PROYECTOS DPUNTOS CORCHETEA CORCHETEC
        | PROYECTOS DPUNTOS NULL
    '''

def p_estados(p):
    '''n_estado : ESTADO DPUNTOS ESTADOS COMA
        | ESTADO DPUNTOS NULL COMA
    '''

def p_proyecto(p):
    '''n_proyecto : LLAVEA n_nombre n_estado f_inicio f_fin LLAVEC
        | LLAVEA n_nombre f_inicio f_fin LLAVEC
        | LLAVEA n_nombre n_estado f_inicio LLAVEC
        | LLAVEA n_nombre f_inicio LLAVEC
        | LLAVEA n_nombre n_estado f_inicio f_fin LLAVEC COMA n_proyecto
        | LLAVEA n_nombre f_inicio f_fin LLAVEC COMA n_proyecto
        | LLAVEA n_nombre n_estado f_inicio LLAVEC COMA n_proyecto
        | LLAVEA n_nombre f_inicio LLAVEC COMA n_proyecto
    '''

def p_fecha_inicio(p):
    '''f_inicio : FECHA_INICIO DPUNTOS FECHA COMA
        | FECHA_INICIO DPUNTOS FECHA
    '''

def p_fecha_fin(p):
    '''f_fin : FECHA_FIN DPUNTOS FECHA
        | FECHA_FIN DPUNTOS NULL
    '''

def p_error(p):
    if p:
        print("Error sintáctico en '%s' [Línea: %d]" % (p.value, p.lineno))
        # Avanzar el parser un token
        parser.errok()
    else:
        print("Error sintáctico al final del archivo")

parser = yacc.yacc(debug=0, start='sigma')