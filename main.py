###LAS CLASES ABSTRACTAS OBLIGA A LAS CLASES HIJAS QUE HEREDEN DE LA
#   CLASE ABSTRACTA A IMPLEMENTAR TODOS SUS METODOS, SERIA COMO UN CONTRATO.
#   TAMBIEN FOMENTA Y OBLIGA EL USO DE POLIMORFISMO.

#Importar abc y abstractclassmethod para definir una clase abstracta.
from abc import ABC, abstractmethod

#Debemos heredar ABC para decir que es una clase abstracta.
class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print("Hola me llamo ",self.nombre, " y tengo ", self.edad ," anios.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print("Estoy estudiando: ", self.actividad)

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print("Estoy trabajando actualmente en el rubro de: ", self.actividad)


#Crear objetos y ejecutar sus metodos
estudiante = Estudiante("Nicolas","24","Masculino","Programacion")
trabajador = Trabajador("Roberto","27","Masculino","profesorado")

estudiante.hacer_actividad()
trabajador.hacer_actividad()

estudiante.presentarse()
trabajador.presentarse()