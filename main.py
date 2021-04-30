# authot: sccub and ssamypoull
# Simulation of a galaxy to generate a value for the contact rate between civilizations

# import dependencies
import sys, pygame, time
import numpy as np
from constants import *
from civ import Civ
from signal import Signal

# initialize simulation window
pygame.init()
pygame.display.set_caption("Galaxy Sim")
size = width, height = BUFFER + DIAM, DIAM
center = width/2, height/2
actual_screen = pygame.display.set_mode(size, pygame.RESIZABLE)
screen = actual_screen.copy()

# initialize information text box
line_height = 20
textbox = pygame.font.SysFont("Consolas", line_height)

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

# ticker of how many communications have occurred
num_cons = 0

# ticker of how many civilizations have had at
# least one contact
num_con_civs = 0

# log to record all contacts that have occurred.
con_log = []
# only keep in record this many contacts at a time
entries_to_keep = 10

# ticker of number of civs living or dead
num_civs = init_civ_count

# begin game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            actual_screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)

    # refresh background
    screen.fill(black)
    # refresh galaxy
    pygame.draw.circle(screen, white, center, RAD)
    pygame.draw.circle(screen, grey, center, RAD, 5)
    # refresh galactic center
    pygame.draw.circle(screen, black, center, CENTER_RAD)
    pygame.draw.circle(screen, grey, center, CENTER_RAD + 3, 3)

    # get the number of births this century
    num_births = np.random.poisson(avg_num_births)
    for i in range(num_births):
        num_civs += 1
        newCiv = Civ(num_civs)
        civilizations.append(newCiv)

        if newCiv.isAlive():
            newSig = Signal(newCiv)
            signals.append(newSig)

    # for all sigs, redraw if sig has not fully
    # left the galaxy
    for sig in signals:
        sig.advanceAge()

        if sig.inGalaxy():
            sig.draw(screen)
        else:
            signals.remove(sig)

    # for all civs, redraw if civ still alive.
    # Remove civ if deceased
    for civ in civilizations.copy():
        civ.advanceAge()

        if civ.isAlive():
            civ.draw(screen)
        else:
            civilizations.remove(civ)

        # check if civ is within any signals
        for sig in signals:
            if civ.isContacted(sig, con_log):

                # increment number of cons
                num_cons += 1

                # if this is a civ's first con,
                # increment the number of civs
                # that have had cons
                if civ.firstCon():
                    num_con_civs += 1

                # if con_log is larger than desired,
                # remove oldest entry
                if len(con_log) > entries_to_keep:
                    con_log.pop(0)

    # calculate percentage of civs
    # that have been contacted
    if num_con_civs > 0:
        percent_cons = 100 * num_con_civs/num_civs
    else:
        percent_cons = 0

    # assemble each line of model data
    data = ["===[ Model Data ]===",
            "Case: " + str(SIM_CASE),
            "Avg civ count (DrakeEq): " + str(avg_civ_count),
            "Avg civ birthrate: " + str(avg_num_births),
            "Avg lifespan: " + str(avg_lifespan),
            "Century #" + str(clock),
            "There are " + str(len(civilizations)) + " civs",
            "Signals in gal: " + str(len(signals)),
            "Total contacts: " + str(num_cons),
            "Total civs living or dead: " + str(num_civs),
            "Contacted civs: " + str(num_con_civs),
            "Contact rate: %" + str(percent_cons),
            "",
            "===[ Latest Cons: ]===",
            ]

    # add most recent cons to model data
    if num_cons < entries_to_keep:
        logs_to_print = num_cons
    else:
        logs_to_print = entries_to_keep
    for i in range(logs_to_print):
        data.append(con_log[-(i + 1)])

    # print each line of model data to the screen
    textbox_height = 100
    for line in data:
        screen.blit(textbox.render(line, False, white, black), (10, textbox_height))
        textbox_height += line_height

    # wait a century and advance clock by 1
    time.sleep(century_length - ((time.time() - starttime) % century_length))
    clock += 1

    # update screen
    # transform the drawing surface to the window size
    transformed_screen = pygame.transform.scale(screen, actual_screen.get_rect().size)
    # blit the drawing surface to the application window
    actual_screen.blit(transformed_screen, (0, 0))
    pygame.display.update()

# if the main game loop has ended,
# close the model
sys.exit()
