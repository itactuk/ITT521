# No existe el switch
# Sin embargo se hace con un diccionario, algo similar

meses = {
    1: 'Enero',
    2: 'Febrero',
    3: 'Marzo'
}

mes = int(input("Digite numero de mes: "))

if mes in meses:
    nombre_mes  = meses[mes]
    print(nombre_mes)
else:
    print("No existe el mes")
