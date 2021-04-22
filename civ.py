# import dependencies
import math
from random import randrange
from constants import *
import pygame


# create civilization object
class Civ:

    # create and initialize member variables
    def __init__(self, id):
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
        self.ID = int(id)
        self.coms = []


    # check if civilizations is still living
    def isAlive(self):
        return self.age < self.lifespan

    # update the civilization's age
    def advanceAge(self):
        self.age = self.age + 1

    def isContacted(self, sig):

        # distance from civ to center of signal
        hyp = math.sqrt((self.x - sig.x) ** 2 + (self.y - sig.y) ** 2)

        # signal radii
        sig_inner_rad = sig.rad - sig.width
        sig_outer_rad = sig.rad

        # signal check
        if hyp < sig_outer_rad and hyp > sig_inner_rad and sig.ID not in self.coms:
            self.coms.append(sig.ID)
            print("civ " + str(self.ID) + " has received signal " + str(sig.ID))
            return True
        else:
            return False


        return True

    # draw the civilization
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.rad)
