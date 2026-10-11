import random

from models.PersonaComunes import PersonaComunes



class Villano(PersonaComunes):
    def __init__(self, nombre, apellidos, fechaNacimiento, id):
        self.chatgepeteador = random.randint(1,100)
        self.entregadorTardio = random.randint(1,100)
        self.ausencias = random.randint(1,100)
        self.hablador = random.randint(1,100)
        self.calcular_puntuacion()
        super().__init__(nombre, apellidos, fechaNacimiento, id, self.puntuacionTotal)

    def calcular_puntuacion(self):
        self.puntuacionTotal = (self.chatgepeteador + self.entregadorTardio + self.ausencias + self.hablador) / 4


    def __str__(self):
        return f'{self.nombre} {self.apellidos} {self.fechaNacimiento} {self.id} {self.puntuacionTotal}'

