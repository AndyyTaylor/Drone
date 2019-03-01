
# This will allow basic simulation of a few different slam algorithms
# The landmarks here will eventually be replaced by 'features' from the video feed

# I'm writing this in Python initially because it's much quicker for testing
# proper implementation will still be C++

# Things to be done
# [ ] Graphical model of robot & landmarks
# [ ] Ability to control robot with keys
# [ ] Sensing of landmarks dependent on robots position
# [ ] Create an Environment class that can be saved and loaded
# [ ] Addition of noise to the sensor readings
# [ ] Handling for 3D landmarks & movement
# [ ] Create a way to interface the python sim with c++ implementation of controller
# [ ] Ability to load landmarks from an actual flight into the sim
# [ ] ? Also load the actual flight path if we have it

import random
import pygame

from config import COLORS, NOISE, SCREEN_WIDTH, SCREEN_HEIGHT
from robot import Robot
from landmark import Landmark


def update():
    """ Handles the sim logic """
    robot.update(moving_up, moving_down, moving_right, moving_left)

    total_movement = abs(int(moving_up) + int(moving_left) - int(moving_down) - int(moving_right))
    total_movement /= 2

    for landmark in landmarks:
        if random.random() < total_movement * NOISE.LANDMARK.MOVE_TOGGLE + NOISE.LANDMARK.STATIC:
            landmark.toggle_hidden()

def render():
    """ Render all sim objects """
    robot.render(screen)

    for landmark in landmarks:
        landmark.render(screen)

# Wrap in this block since I don't want to use __name__ == '__main__'
# pylint: disable=invalid-name
pygame.init()  # pylint: disable=no-member
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

robot = Robot(50, 50)

landmarks = []
for i in range(100):
    landmarks.append(Landmark(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)))

moving_right = False
moving_left = False
moving_up = False
moving_down = False

running = True
#pylint: enable=invalid-name

while running:
    clock.tick(60)
    screen.fill(COLORS.WHITE)

    update()
    render()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                moving_up = True
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                moving_down = True
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                moving_right = True
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                moving_up = False
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                moving_down = False
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                moving_right = False
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                moving_left = False

    pygame.display.update()
