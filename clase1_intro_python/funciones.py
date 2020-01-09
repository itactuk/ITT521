
def suma(valor1, valor2):
    return valor1 + valor2


def suma_anotacion_tipo(valor1: int, valor2: int) -> int:
    return valor1 + valor2


def calcular_itbis(valor_prod, porcentaje=0.18):  # valor por defecto
    return valor_prod * porcentaje


print(suma(1, 2))
print(suma(valor2=1, valor1=2))

print(calcular_itbis(100))
print(calcular_itbis(100, 0.17))
print(calcular_itbis(porcentaje=0.17, valor_prod=100))
