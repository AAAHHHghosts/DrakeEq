# import dependencies
import math
from random import randrange
from constants import *
import pygame


# create civilization object
class Civ:

    # create and initialize member variables
    def __init__(self):
        # generate random coords until coords are
        # within galaxy circle and outside galactic
        # center
        inGalaxy = False
        while (not inGalaxy):
            self.x, self.y = randrange(DIAM), randrange(DIAM)
            hyp = math.sqrt((self.x - RAD) ** 2 + (self.y - RAD) ** 2)
            inGalaxy = hyp < RAD and hyp > CENTER_RAD

        self.rad = 5
        self.color = (255, 0, 0)  # (111,209,164)
        self.lifespan = randrange(2, 6)
        self.age = 0


    # check if civilizations is still living
    def isAlive(self):
        return self.age < self.lifespan

    # update the civilization's age
    def advanceAge(self):
        self.age = self.age + 1

    def isContacted(self):
        return True

    # draw the civilization
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.rad)
