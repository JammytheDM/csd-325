"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
Tags: short, bext, simulation

Module 6 changes:
- Added WATER as a separate forest-cell type.
- Added a centered, oval-like lake with a slightly irregular outline.
- Preserved water cells in every simulation cycle.
- Displayed water in blue.
- Fire only spreads to TREE cells, so it cannot cross the lake.
"""

import random
import sys
import time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = '~'  # Module 6: permanent lake symbol, distinct from trees and fire.

# Module 6: Each number gives the lake's half-width for a row relative
# to the center. Varying the widths creates an oval-like lake outline.
LAKE_ROW_WIDTHS = {
    -5: 2,
    -4: 5,
    -3: 7,
    -2: 9,
    -1: 10,
     0: 10,
     1: 9,
     2: 8,
     3: 7,
     4: 5,
     5: 3,
}

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5


def isLakeCell(x, y):
    """Return True when a coordinate belongs to the fixed lake."""
    center_x = WIDTH // 2
    center_y = HEIGHT // 2
    row_offset = y - center_y

    # Rows outside the lake's defined shape are land, not water.
    if row_offset not in LAKE_ROW_WIDTHS:
        return False

    return abs(x - center_x) <= LAKE_ROW_WIDTHS[row_offset]


def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {
            'width': forest['width'],
            'height': forest['height']
        }

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # A burning neighbor may already have updated this cell.
                    continue

                # Module 6: water is copied unchanged into the next forest.
                if forest[(x, y)] == WATER:
                    nextForest[(x, y)] = WATER

                elif (forest[(x, y)] == EMPTY
                      and random.random() <= GROW_CHANCE):
                    # Grow a tree in this empty space.
                    nextForest[(x, y)] = TREE

                elif (forest[(x, y)] == TREE
                      and random.random() <= FIRE_CHANCE):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE

                elif forest[(x, y)] == FIRE:
                    # This tree is currently burning.
                    # Fire can ignite neighboring trees, but not water.
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE

                    # The tree has burned down now, so erase it.
                    nextForest[(x, y)] = EMPTY

                else:
                    # Just copy the existing object.
                    nextForest[(x, y)] = forest[(x, y)]

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Return a new forest containing a permanent central lake."""
    forest = {'width': WIDTH, 'height': HEIGHT}

    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Module 6: place water before randomly creating trees.
            if isLakeCell(x, y):
                forest[(x, y)] = WATER
            elif random.random() <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY

    return forest


def displayForest(forest):
    """Display the forest and its blue lake."""
    bext.goto(0, 0)

    for y in range(forest['height']):
        for x in range(forest['width']):
            cell = forest[(x, y)]

            if cell == TREE:
                bext.fg('green')
                print(TREE, end='')

            elif cell == FIRE:
                bext.fg('red')
                print(FIRE, end='')

            elif cell == WATER:
                # Module 6: distinguish the permanent lake in blue.
                bext.fg('blue')
                print(WATER, end='')

            elif cell == EMPTY:
                bext.fg('reset')
                print(EMPTY, end='')

        print()

    bext.fg('reset')
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
