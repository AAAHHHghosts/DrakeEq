# import dependencies
import pygame
import numpy as np
import math
from random import randrange
from constants import *


# create civilization object
class Civ:

    # create and initialize member variables
    def __init__(self, id):

        # generate random coords until coords are
        # within galaxy circle and outside galactic
        # center
        in_galaxy = False
        while not in_galaxy:
            self.x, self.y = randrange(DIAM), randrange(DIAM)
            hyp = math.sqrt((self.x - RAD) ** 2 + (self.y - RAD) ** 2)
            in_galaxy = RAD > hyp > CENTER_RAD

        # offset civ x coord by display buffer
        self.x += BUFFER/2

        # define remaining civ attributes
        self.rad = 2
        self.color = (255, 0, 0)  # (111,209,164)
        self.lifespan = np.random.normal(avg_lifespan)
        self.age = 0
        self.ID = int(id)
        self.cons = []

    # check if civilizations is still living
    def isAlive(self):
        return self.age < self.lifespan

    # update the civilization's age
    def advanceAge(self):
        self.age += 1

    # function to tell if a given signal has
    # made contact with the this civ
    def isContacted(self, sig, con_log):

        # distance from civ to center of signal
        hyp = math.sqrt((self.x - sig.x) ** 2 + (self.y - sig.y) ** 2)

        # signal radii
        sig_inner_rad = sig.rad - sig.width
        sig_outer_rad = sig.rad

        # signal check
        if sig_inner_rad < hyp < sig_outer_rad and sig.ID not in self.cons:
            self.cons.append(sig.ID)
            con_log.append("civ " + str(self.ID) + " heard civ " + str(sig.ID))
            return True
        else:
            return False

    # return true if civ has had one and
    # only one contact
    def firstCon(self):
        return len(self.cons) == 1

    # draw the civilization
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.rad)
