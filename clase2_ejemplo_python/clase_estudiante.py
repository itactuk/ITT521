from typing import List


class Materia:
    PUNTOS_LETRAS = {
        'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0
    }

    def __init__(self, nombre: str, letra: str, creditos: int):
        self.nombre = nombre
        self.letra = letra.upper()
        self.creditos = creditos

    def puntos_letra(self):
        if self.letra not in self.PUNTOS_LETRAS:
            raise Exception("Letra no válida")
        return  self.PUNTOS_LETRAS[self.letra]

    def calcula_puntos(self):
        return self.puntos_letra() * self.creditos


class Estudiante:
    def __init__(self, nombre: str, materias: List[Materia]):
        self.nombre = nombre
        self.materias = materias

    def calcula_indice(self):
        acc_creditos = 0
        acc_puntos = 0
        for m in self.materias:
            acc_creditos += m.creditos
            acc_puntos += m.calcula_puntos()
        return acc_puntos/acc_creditos


def main():
    print("Mi nombre")


if __name__ == '__main__':
    main()
