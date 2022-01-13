import pygame
from pygame.math import Vector2

import core
from core import getMouseLeftClick


class Tir:
    def __init__(self):
        self.taille = 10
        self.couleur = (255, 255, 0)
        self.position = Vector2(2000, 2000)
        self.vitesse = Vector2(0, 0)
        self.vitesseMin = Vector2(0, 0)
        self.vitesseMax = 2
        self.k = 0.01
        self.l0 = 1
        self.accMax = 0.5


    def move(self, destination):
        if destination is not None:
            # bilan des forces
            # F=k * u * |l-l0|

            l = self.position.distance_to(destination)
            u = destination - self.position
            u = u.normalize()

            F = self.k * u * abs(l - self.l0)


            # limiter la force max
            if F.length() > self.accMax:
                F.scale_to_length(self.accMax)

            # ajouter la force a la vitesse
            self.vitesse = self.vitesse + F

            # limiter la vitesse

            if self.vitesse.length() > self.vitesseMax:
                self.vitesse.scale_to_length(self.vitesseMax)

        # ajouter la vitesse a la position

        self.position = self.position + self.vitesse




    def disparaitre(self):

        if asteroid.position.distance_to(self.position) < self.taille + vaisseau.taille:
            asteroid.position = Vector2(2000, 2000)





    def setVitesse(self, v):
        self.vitesse = v

    def setPosition(self, pos):
        self.position = pos

    def getVitesse(self):
        return self.vitesse

    def getPosition(self):
        return self.position

    def getTaille(self):
        return self.taille