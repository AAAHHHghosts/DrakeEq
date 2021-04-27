# import dependencies

from constants import DIAM
import pygame

# create signal object
class Signal:

    # create and initialize member variables
    def __init__(self, civ):
        self.x, self.y = civ.x, civ.y
        self.rad = 0
        self.width = 0
        self.color = (209, 111, 156)
        self.lifespan = civ.lifespan
        self.age = 0
        self.ID = civ.ID

    # check if civilizations is still living
    def isEmitting(self):
        return self.age < self.lifespan

    # check if the signal is still within the galaxy
    def inGalaxy(self):
        return self.rad < DIAM

    # update the civilization's age
    def advanceAge(self):
        self.age += 1
        self.rad += 1

        if (self.isEmitting()):
            self.width = self.width + 1

    # draw the civilization
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.rad, self.width)


