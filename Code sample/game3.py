#-*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
from sys import exit
import os
from random import randint
from time import sleep
size = (800, 600)
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
    x=(size[0]-text.get_width())/2
    y=(size[1]-text.get_height())/2
    while True:
        test=pygame.event.wait()
        print test
if __name__ == "__main__":
    run()    
