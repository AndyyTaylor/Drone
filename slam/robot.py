
import pygame
from config import COLORS, ROBOT_DEFAULTS


class Robot:
    """
    A simple class to hold the robot for the simulation

    x: int
    y: int
    ? w: int
    ? h: int
    ? heading: float
    """

    def __init__(self, x: int, y: int, **kwargs):
        self.x = x
        self.y = y

        # For linting and type completion
        self.w = 0
        self.h = 0
        self.speed = 0
        self.heading = 0

        for key in ROBOT_DEFAULTS:
            setattr(self, key, kwargs.get(key) or ROBOT_DEFAULTS[key])
    
    def update(self, moving_up, moving_down, moving_right, moving_left):
        """ Updates the robot based on moving booleans """
        if moving_up:
            self.y -= self.speed
        if moving_down:
            self.y += self.speed
        if moving_left:
            self.x -= self.speed
        if moving_right:
            self.x += self.speed

    def render(self, surface: pygame.Surface):
        """ Render the robot to the given surface """

        pygame.draw.rect(surface, COLORS.BLUE, self.get_rect())
    
    def get_rect(self):
        """ Returns a (x, y, w, h) tuple of the robot's attributes """

        return (self.x, self.y, self.w, self.h)
