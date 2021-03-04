#!/usr/bin/python3

import time, sys, pygame
from pygame.locals import *
pygame.init()

size=width, height = 720, 720
white = 255, 255, 255
black = 0, 0, 0
pygame.mouse.set_cursor(
mouse_position = (0,0)
drawing = False
screen = pygame.display.set_mode(size, 0, 32)
screen.fill(black)
while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            if (drawing):
                mouse_position = pygame.mouse.get_pos()
                pygame.draw.line(screen, white, mouse_posit
                    pygame.mouse.set_cursor(ion, mouse_position, 1)
                print(mouse_position)
        elif event.type == MOUSEBUTTONUP:
            mouse_position = (0,0)
            drawing = False
            pos_trans = mouse_position
            print(pos_trans)
        elif event.type == MOUSEBUTTONDOWN:
            drawing=True

    pygame.display.update()
