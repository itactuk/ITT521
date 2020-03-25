
from string import Template

ARCHIVO_PLANTILLA = "plantilla.txt"

def lee_plantilla(filename):
    """
    Returna un objeto Template que encapsula el contenido de filename
    """

    with open(filename, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    return Template(contenido)


message_template = lee_plantilla(ARCHIVO_PLANTILLA)
mensaje = message_template.substitute(NOMBRE_PERSONA="nombre")
print(mensaje)