#!/usr/bin/python3
#CLIENT!!
import socket, utility, easysocket, pickle, time, sys, pygame
from pygame.locals import *

pygame.init()

size=width, height = 720, 720
black = 255, 255, 255
white = 0, 0, 0
mouse_position = (0,0)
drawing = False
screen = pygame.display.set_mode(size, 0, 32)
screen.fill(black)
s = easysocket.make_client_socket('localhost', 10000)
while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            if (drawing):
                mouse_position = pygame.mouse.get_pos()
                pygame.draw.line(screen, white, mouse_position, 1)
                print(mouse_position)
                #s= easysocket.make_client_socket('localhost', 10000)
                easysocket.send(s, pickle.dumps((mouse_position)))

        elif event.type == MOUSEBUTTONUP:
            mouse_position = (0,0)
            drawing = False
            pos_trans = mouse_position
        elif event.type == MOUSEBUTTONDOWN:
            drawing=True

    pygame.display.flip()
s.close()