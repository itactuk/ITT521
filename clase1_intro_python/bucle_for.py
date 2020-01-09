

# iterar sobre un rango
for i in range(0, 100):
    print(i)

for i in range(0, 100, 1):
    print(i)

for i in range(100):
    print(i)

# iterar sobre listas (arreglos)
listado = [1, 2, "Hola", 43, "434", 2.3]
listado.append("2")
for vi in listado:
    print(vi, end=',+')

print()
# iterar sobre un diccionario
meses = {1: 'Enero', 2: 'Febrero', 3: 'Marzo'}
for llave, valor in meses.items():
    print(f"Mi llave es: {llave} y mi valor es {valor}")


