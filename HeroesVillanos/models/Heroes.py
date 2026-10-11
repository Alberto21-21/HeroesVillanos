import random

from models.PersonaComunes import PersonaComunes

class Heroe(PersonaComunes):
    def __init__(self,nombre,apellidos,fechaNacimiento,id):
        self.codigoLimpio = random.randint(0,100)
        self.bienDocumentado = random.randint(0,100)
        self.gitGod = random.randint(0,100)
        self.ausencias = random.randint(0,100)
        self.hablador = random.randint(0,100)
        self.calcular_puntuacion()
        super().__init__(nombre, apellidos, fechaNacimiento, id, self.puntuacionTotal)

    def calcular_puntuacion(self):
        self.puntuacionTotal = (self.codigoLimpio + self.bienDocumentado + self.ausencias + self.hablador) / 4


    def __str__(self):
        return f'{self.nombre} {self.apellidos} {self.fechaNacimiento} {self.id} {self.puntuacionTotal}'


