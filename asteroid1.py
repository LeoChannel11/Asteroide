import pygame
from pygame.math import Vector2
import random
import core
from core import getMouseLeftClick


class Asteroid:
    def __init__(self):
        self.taille = 10
        self.couleur = (100, 0, 0)
        self.masse = 5
        self.position = Vector2(random.randint(0, 1200), random.randint(0, 1200))
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

            F = self.k * u * abs(l - self.l0) / self.taille
            print(F)

            # limiter la force max
            if F.length() > self.accMax:
                F.scale_to_length(self.accMax)

            # ajouter la force a la vitesse
            self.vitesse = self.vitesse + F

            # limiter la vitesse
            if self.vitesse.length() > self.vitesseMax - self.taille * 0.05:
                self.vitesse.scale_to_length(self.vitesseMax - self.taille * 0.05)

        # ajouter la vitesse a la position

        self.position = self.position + self.vitesse

    def affichage(self, screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.taille)

    def disparaitre(self, vaisseau):
        if vaisseau.position.distance_to(self.position) < self.taille + vaisseau.taille:
            vaisseau.position = Vector2(2000, 2000)

        if Alien.position.distance_to(self.position) < self.taille + vaisseau.taille:
            Alien.position = Vector2(2000, 2000)