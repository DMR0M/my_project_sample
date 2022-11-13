"""Pygame demo create a window"""

# 1 : Import libraries
import pygame
from pygame.locals import *
import sys

# 2: Define constants
BLACK = (0, 0, 0)
WINDOW_HEIGHT = 640
WINDOW_WIDTH = 480
FRAMES_PER_SECOND = 30

# 3: Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4: Load assets: image(s) and sound(s), etc.
ball_image = pygame.image.load('Pygame_Images/pngtree-basket-ball-png-transparent-3d-png-image_1078997.jpg')

# 5: Initialize variables


# 6: Loop forever
while True:
    # 7: Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# 8: Do any "per frame" actions

# 9: Clear the window
window.fill(BLACK)

# 10: Draw all window elements
window.blit(ball_image, (100, 200))

# 11: Update the window
pygame.display.update()

# 12: Slow things down a bit
clock.tick(FRAMES_PER_SECOND)



