from vaisseau1 import Vaisseau
from asteroid1 import Asteroid
from tir1 import Tir
from alien1 import Alien
import core
import pygame




def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [1200, 1200]

    core.memory("asteroid", [])
    core.memory("vaisseau", Vaisseau())
    core.memory("tir",Tir())
    core.memory("alien", Alien())

    for c in range(20):
        core.memory("asteroid").append(Asteroid())


    print("Setup END-----------")


def run():
    core.cleanScreen()

    for c in core.memory("asteroid"):
        Asteroid.affichage(core.screen)

    core.memory("vaisseau").affichage()


    for c in core.memory("asteroid"):
        Asteroid.disparaitre(core.memory("vaisseau"))

core.main(setup, run)
