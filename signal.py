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

    # Check if civilizations is still living
    # Notice that if age and lifespan happens to be zero,
    # (less than a century), this method still returns true,
    # If this method instead returned false, the signal's width
    # will never increment and remain zero. If this happens,
    # pygame interprets circles of width zero as solid circles.
    # A solid circle, in this model, represents a immortal
    # civilization. We
    def isEmitting(self):
        return self.age < self.lifespan

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


