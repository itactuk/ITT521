from clase2_ejemplo_python.clase_estudiante import Estudiante, Materia


def main():
    cant_est = int(input("Digite cantidad estudiantes: "))
    listado_est = []
    for i in range(cant_est):
        nombre_est = input(f"Nombre estudiante {i + 1}: ")
        cant_mat = int(input(f"Digite cantidad materias: "))
        lista_mat = []
        for j in range(0, cant_mat):
            nombre_materia = input(f"Nombre materia {j + 1}: ")
            cant_cred = int(input(f"Creditos materia {j + 1}: "))
            letra = None
            while letra not in Materia.PUNTOS_LETRAS:
                letra = input(f"Letra materia {j + 1}: ").upper()
                if letra not in Materia.PUNTOS_LETRAS:
                    print("Letra incorrecta. Por favor digítela otra vez")
            lista_mat.append(Materia(nombre_materia, letra, cant_cred))
        listado_est.append(Estudiante(nombre_est, lista_mat))

    for e in listado_est:
        print(f"El índice para el estudiante {e.nombre} es {e.calcula_indice()}")



if __name__ == '__main__':
    main()
