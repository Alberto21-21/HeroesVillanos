import logging
from datetime import datetime
from abc import ABC, abstractmethod

class PersonaComunes(ABC):
    def __init__(self, nombre, apellidos,fechaNacimiento,id,puntuacionTotal):
        self.nombre = nombre
        self.apellidos = apellidos
        self.fechaNacimiento = fechaNacimiento
        self.id = id
        self.puntuacionTotal = 0


    @abstractmethod
    def calcular_puntuacion(self):
        pass

    @property
    def edad(self):
        try:
            fNac = datetime.strptime(self.fechaNacimiento, "%Y-%m-%d")
            hoy = datetime.now()
            edad = hoy.year - fNac.year
            if ((hoy.month - fNac.month) < 0) or ( (hoy.day - fNac.day) < 0):
                edad -= 1
            return edad
        except Exception as e:
            logging.error(f"Error al calcular la edad: {e}")
            return None