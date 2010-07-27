#-*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
from sys import exit
import os
from random import randint
from time import sleep
size = (1024, 600)
white=(255,255,255)
title="Hello,Pygame!"
message =unicode("看到沒","utf-8")

def run():
    pygame.init()
    screen = pygame.display.set_mode(size, 0, 32)
    pygame.display.set_caption(title)
    font =pygame.font.Font(os.environ['SYSTEMROOT']+
                                                     "\\Fonts\\mingliu.ttc", 80)
    text =font.render(message,True,white)
    dx=1
    i=0
    x=(size[0]-text.get_width())/2
    y=(size[1]-text.get_height())/2
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        screen.fill(color)
        x +=dx
        if (x+text.get_width())>size[0] or x<0 :
            dx *= -1
        screen.blit(text,(x,y)) 
        pygame.display.set_caption("Color: " + str(color))
        '''sleep(1)'''
        pygame.display.update()
if __name__ == "__main__":
    run()    
