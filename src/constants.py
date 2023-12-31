FPS = 30

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_COLOUR = (251, 248, 241)

MENU_COLOUR = (201,198,193)
MENU_CENTER_X = SCREEN_WIDTH / 2
MENU_CENTER_Y = SCREEN_HEIGHT / 2
MENU_WIDTH = 300
MENU_HEIGHT = 300

PADDING = 10
SQUARE_SIZE = 120

BOARD_COLOUR = (187, 173, 160)
BOARD_X = SCREEN_WIDTH / 2 - (2 * SQUARE_SIZE + 2.5 * PADDING)
BOARD_Y = SCREEN_HEIGHT / 2 - (2 * SQUARE_SIZE + 2.5 * PADDING)
BOARD_SIZE = 4 * SQUARE_SIZE + 5 * PADDING

SCORE_CENTER_X = SCREEN_WIDTH / 4
HIGH_SCORE_CENTER_X = 3 * SCREEN_WIDTH / 4
SCORE_CENTER_Y = 75
SCORE_TEXT_CENTER_Y = 25

TEXT_COLOUR = (100,100,100)
TEXT_SIZE_1 = 48
TEXT_SIZE_2 = 32

TILE_COUNT = 4

TILE_DEFAULT_VALUE = 0

TILE_COLOUR_DICT = {
    "0": (204, 191, 183),
    "2": (238, 228, 218),
    "4": (236, 224, 202),
    "8": (242, 177, 121),
    "16": (245, 149, 101),
    "32": (245, 124, 95),
    "64": (246, 93, 59),
    "128": (237, 206, 113),
    "256": (237, 204, 99),
    "512": (236, 199, 80),
    "1024": (236, 196, 64),
    "2048": (234, 194, 44),
    "4096": (239, 102, 109),
    "8192": (237, 77, 89),
    "16384": (225, 67, 56),
    "32768": (113, 180, 214),
    "65536": (92, 160, 223),
    "131072": (1, 124, 191),
}

BUTTON_HEIGHT = 50
BUTTON_PADDING = 50

MENU_BUTTON_CENTER_X = SCREEN_WIDTH / 2
MENU_BUTTON_CENTER_Y = 50
MENU_BUTTON_WIDTH = 150
MENU_BUTTON_HEIGHT = BUTTON_HEIGHT


GAME_OVER_TEXT_Y = 750
GAME_OVER_TEXT_WIDTH = 250