from models.Gestion import Gestion
from models.Heroes import Heroe
from models.Villanos import Villano
import logging

logging.basicConfig(
    filename='HeroesVillanos.log',
    level=logging.INFO,
    encoding='UTF-8')

if __name__ == '__main__':
    gestion = Gestion()
    h1 = Heroe("Superman", "Clark Kent", "1978-06-18", 1)
    h2 = Heroe("Batman", "Bruce Wayne", "1989-06-23", 2)
    h3 = Heroe("Wonder Woman", "Diana Prince", "2001-06-14", 3)
    v1 = Villano("Joker", "Jack Napier", "1989-09-22", 4)
    v2 = Villano("Lex Luthor", "Lex Luthor", "1978-06-18", 5)
    v3 = Villano("Cheetah", "Barbara Ann Minerva", "2001-06-14", 6)

    gestion.agregar_personaje(h1)
    gestion.agregar_personaje(h2)
    gestion.agregar_personaje(h3)
    gestion.agregar_personaje(v1)
    gestion.agregar_personaje(v2)
    gestion.agregar_personaje(v3)

    print("Listado de personajes:")
    for p in gestion.personajes:
        print(p)

    print("\nBuscar por nombre 'Batman':")
    resultados = gestion.buscarNombre("Batman")
    for r in resultados:
        print(r)

    print("\nBuscar por gitgod 50:")
    resultados = gestion.buscarGitgodMayor(50)
    for r in resultados:
        print(r)

    print("\nEmparejamiento aleatorio:")
    gestion.emparejarAleatorio()
    gestion.emparejarAleatorio()
    gestion.emparejarAleatorio()
