import logging

from models.Heroes import Heroe
from models.Villanos import Villano
import random

class Gestion:
    def __init__(self):
        self.personajes = []
        logging.info("Gestion creada correctamente")


    def __str__(self):
        return f"Gestion(id_gestion={self.id_gestion}, nombre={self.nombre}, descripcion={self.descripcion})"

    def agregar_personaje(self, personaje):
        try:
            self.personajes.append(personaje)
            logging.info(f"Personaje agregado correctamente {personaje.id} {personaje.nombre}")
        except Exception as e:
            print (f"Error al agregar personaje: {e}")

    def buscarNombre(self,nombre):
        resultados = []
        for personaje in self.personajes:
            if personaje.nombre.lower() == nombre.lower():
                resultados.append(personaje)
        logging.info(f"Busqueda por nombre {nombre} realizada correctamente. Se han encontrado {len(resultados)} resultados.")
        return resultados

    def buscarGitgodMayor(self,valor):
        resultados =  []
        for personaje in self.personajes:
            if isinstance(personaje,Heroe):
                if personaje.gitGod > valor:
                    resultados.append(personaje)
        logging.info(f"Busqueda por gitgod mayor a {valor} realizada correctamente. Se han encontrado {len(resultados)} resultados.")
        return resultados

    def emparejarAleatorio(self):
        heroes = []
        villanos = []

        for personaje in self.personajes:
            if isinstance(personaje,Heroe):
                heroes.append(personaje)
            elif isinstance(personaje,Villano):
                villanos.append(personaje)
        if not heroes or not villanos:
            print("No hay suficientes heroes o villanos para emparejar.")
            logging.warning("No hay suficientes heroes o villanos para emparejar.")
            return

        indiceHeroe =  random.randint(0,len(heroes)-1)
        indiceVillano = random.randint(0,len(villanos)-1)
        heroe = heroes[indiceHeroe]
        villano = villanos[indiceVillano]
        print (f"HEROE:{heroe.nombre} {heroe.puntuacionTotal}")
        print (f"VILLANO:{villano.nombre} {villano.puntuacionTotal}")

        diferenciaPuntuacion = heroe.puntuacionTotal - villano.puntuacionTotal
        if diferenciaPuntuacion < 0:
            diferenciaPuntuacion *= -1

        if diferenciaPuntuacion <= 20:
            print("Estan equilibrados")
        else:
            print("Tiene una alta desviacion")
        logging.info(f"Emparejamiento aleatorio realizado correctamente entre {heroe.nombre} y {villano.nombre}. Diferencia de puntuacion: {diferenciaPuntuacion}")
