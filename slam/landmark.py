
import pygame
import numpy as np
from config import COLORS


class Landmark:
    """ Simple class to represent a landmark """

    def __init__(self, x: int, y: int):
        self.pos = np.array([x, y])
        self.hidden = False

        self.radius = 5

    def render(self, surface: pygame.Surface):
        """ Render the landmark to the surface provided """
        if self.hidden:
            color = COLORS.GRAY
        else:
            color = COLORS.BLACK

        pygame.draw.circle(surface, color, self.get_pos(), self.radius)
    
    def toggle_hidden(self):
        """ Toggle whether this landmark is hidden """
        self.hidden = not self.hidden

    def hide(self):
        """ Hide this landmark from the robot """
        self.hidden = True

    def show(self):
        """ Make this landmark visible to the robot """
        self.hidden = False

    def get_pos(self):
        """ Returns (x, y) """

        return (self.pos[0], self.pos[1])
