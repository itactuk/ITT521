lista = [1,243,43]  # un listado dinamico que puede cambiar
tuplas = (1,24,54325) # un listado estatico que no puede. no se agrega
# listas y tuplas son ordenas

dicionario = {"a": "A", "b": "B"}  # no ordenado

# tambien por defecto si se ponen comas sin [ ó ( se asume que es una tupla

x = 2, 3  # es una tupla


def ec_cuadra(a, b, c):
    d = (b**2-4*a*c)**0.5
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)
    return x1, x2

v1, v2 = ec_cuadra(2, 3, 4)
print(v1)
print(v2)
