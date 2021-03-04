#!/usr/bin/python3
#SERVER!!!

import socket, easysocket, pickle, utility, time, sys, pygame
from pygame.locals import *
pygame.init()
size=width, height = 720,720
white = 255, 255, 255
black = 0, 0, 0
mouse_position = (0,0)
drawing = True
screen = pygame.display.set_mode(size, 0, 32)
screen.fill(white)
s = easysocket.make_server_socket(10000)
print("waiting...")
socket_to_client, client_address = s.accept()
print("Un client est arrive")
screen = pygame.display.set_mode()
while(True):
    message = easysocket.receive((socket_to_client))
    x, y = pickle.loads(message)
    print("x: ", x, "y: ", y)
    pygame.draw.line(screen, black, x, y, 1)
    pygame.display.flip()
socket_to_client.close()
s.close()
