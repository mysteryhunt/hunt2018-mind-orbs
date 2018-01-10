###############################################################################
#
# pygame Configurations
#

# pygame main window size
# WINDOW_SIZE = (640, 480)


###############################################################################
#
# Grid size of pixel placement drawing board
#

# Number of Rows and Columns of LEDS
GRID_SIZE = (9, 9)


###############################################################################
#
# Custom Grid Pixel Mapping
#

# Crud approximation of the Hero Orb LED positions.
# Outer ring -> equatorial ring of 24 LEDs facing outwards
# Middle ring -> 4x up-and-out facing wedges of 4 LEDs each
# Center dot -> single LED pointing up
NA = None
PIXEL_MAPPING = [
    [NA, NA, 10, 11, 12, 13, 14, NA, NA],
    [NA,  9, NA, NA, NA, NA, NA, 15, NA],
    [ 8, NA, 32, 33, 34, 35, 36, NA, 16],
    [ 7, NA, 31, NA, NA, NA, 37, NA, 17],
    [ 6, NA, 30, NA, 40, NA, 38, NA, 18],
    [ 5, NA, 29, NA, NA, NA, 39, NA, 19],
    [ 4, NA, 28, 27, 26, 25, 24, NA, 20],
    [NA,  3, NA, NA, NA, NA, NA, 21, NA],
    [NA, NA,  2,  1,  0, 23, 22, NA, NA]
]
