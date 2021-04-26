# authot: sccub and ssamypoull
# Simulation of a galaxy to generate a value for the contact rate between civilizations

# import dependencies
import sys
import pygame
import time
import numpy as np
from constants import *
from civ import Civ
from signal import Signal

# initialize simulation window
pygame.init()
pygame.display.set_caption("Galaxy Sim")
size = width, height = DIAM, DIAM
center = RAD, RAD
screen = pygame.display.set_mode(size)
black = 0, 0, 0

# declare a set for all civilizations
# and a set for all of their signals
init_civ_count = np.random.poisson(avg_civ_count)
civilizations = [Civ(i) for i in range(init_civ_count)]
signals = [Signal(civ) for civ in civilizations]

# set up game clock and simulation speed
starttime = time.time()
century_length = 1.0 / SIM_SPEED
# variable to hold the century count
clock = 0

print ("avg birthrate " + str(avg_num_births))
# ticker of how many communications have occurred
num_coms = 0
# ticker of number of civs that have been born
num_civs = init_civ_count

# begin game loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    print("century #" + str(clock) + ". Number of civs: " + str(len(civilizations)))
    print("total coms: " + str(num_coms))

    # get the number of births this century
    num_births = np.random.poisson(avg_num_births)
    for i in range(num_births):
        num_civs += 1
        newCiv = Civ(num_civs)
        civilizations.append(newCiv)

        if newCiv.isAlive():
            newSig = Signal(newCiv)
            signals.append(newSig)

    # refresh screen background
    screen.fill(black)
    pygame.draw.circle(screen, (255, 255, 255), center, RAD)
    pygame.draw.circle(screen, (155, 155, 155), center, RAD, 5)
    # galactic center
    pygame.draw.circle(screen, (0, 0, 0), center, CENTER_RAD)

    # For all civs, redraw civ is still alive.
    # Remove civ if deceased
    for civ in civilizations.copy():
        civ.advanceAge()

        if civ.isAlive():
            civ.draw(screen)
        else:
            civilizations.remove(civ)

        for sig in signals:
            if civ.isContacted(sig):
                num_coms += 1

    # redraw all signals
    for sig in signals:
        sig.advanceAge()
        sig.draw(screen)

    # update newly refreshed screen
    pygame.display.flip()

    # wait a century and advance clock by 1
    time.sleep(century_length - ((time.time() - starttime) % century_length))
    clock += 1