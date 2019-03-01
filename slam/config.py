
# Simple config file for the simulator

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

# pylint: disable=invalid-name,too-few-public-methods

class COLORS:
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)


class NOISE:
    class LANDMARK:
        MOVE_TOGGLE = 0.05
        STATIC = 0.01


ROBOT_DEFAULTS = {
    'w': 25,
    'h': 50,
    'speed': 5,
    'heading': 0
}

# pylint: enable=invalid-name
