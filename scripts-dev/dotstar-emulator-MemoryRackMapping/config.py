from itertools import repeat

###############################################################################
#
# pygame Configurations
#

# pygame main window size
#
# Ratio should be approximately in the ratio: (3, 0.84)
# This corresponds to an approximation of the actual Memory Rack dimensions
# _WINDOW_WIDTH = 2500
_WINDOW_WIDTH = 1920
WINDOW_SIZE = (_WINDOW_WIDTH, int(_WINDOW_WIDTH / 3 * 0.84))

###############################################################################
#
# Grid size of pixel placement drawing board
#

# Number of Rows and Columns of LEDS
#
# (3m of 60/m strip wide) x (6 shelves high)
GRID_SIZE = (3 * 60, 6)

# Take up whole screen space by having LED's stretch to fill the space.
SQUARE_LED = False


###############################################################################
#
# Custom Grid Pixel Mapping
#

def blank(num_slots):
    return list(repeat(None, num_slots))


# Corresponds to the physical layout of the strips within the Memory Rack
PIXEL_MAPPING = [
    blank(60)      + blank(60)                   + range(330, 390),
    blank(60)      + blank(60)                   + range(390, 450),
    blank(60)      + blank(30) + range(300, 330) + range(450, 510),
    blank(60)      + range(240, 300)             + range(510, 570),
    range(0, 60)   + range(180, 240)             + range(570, 630),
    range(60, 120) + range(120, 180)             + range(630, 690)
]
