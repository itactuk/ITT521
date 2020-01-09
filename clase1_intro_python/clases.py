
class Persona:
    pass


class Estudiante(Persona):
    def __init__(self, nombre, apellido): # constructor
        self.nombre = nombre
        self.apellido = apellido

    def obten_nombre_completo(self):
        return self.nombre + " " + self.apellido

listado_est = [Estudiante("Jesus", "Rosario"), Estudiante("Oscar", "Siri")]

for est in listado_est:
    print(est.apellido)
    print(est.nombre)
    print(est.obten_nombre_completo())
