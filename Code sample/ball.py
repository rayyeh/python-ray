import pygame
from pygame.locals import *
from sys import exit
from random import randint


size = (600, 800)
title = "Pong Test"
black = (0, 0, 0)
yellow = (255, 255, 0)


def move(point, radius, dx, dy, seconds):
    x, y = point
    if x > 0 + radius:
        x += dx * seconds
        
    if x < 0 + radius:
        dx *= -1
        x = 0 + radius
        
    if x < size[0] - radius:
        x += dx * seconds
        
    if x > size[0] - radius:
        dx *= -1
        x = size[0] - radius
        
    if y > 0 + radius:
        y += dy * seconds
        
    if y < 0 + radius:
        dy *= -1
        y = 0 + radius
        
    if y < size[1] - radius:
        y += dy * seconds
        
    if y > size[1] - radius:
        dy *= -1
        y = size[1] - radius
    return x, y, dx, dy

def initial():
    if randint(0, 1):
        sx = 1
    else:
        sx = -1
    if randint(0, 1):
        sy = 1
    else:
        sy = -1
    return sx, sy

def speed():
    return float(randint(50, 100))

def run():
    pygame.init()
    screen = pygame.display.set_mode(size, 0, 32)
    pygame.display.set_caption(title)
    point = (300, 400)
  
    radius = 10
    sign_x, sign_y = initial()
    dx = sign_x * speed()
    dy = sign_y * speed()
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
                
        screen.fill(black)
        seconds = clock.tick(30) / 1000.0
                 
        ball = pygame.draw.circle(screen, yellow, ball_point, radius)
           
        x, y, dx, dy = move(ball_point, radius, dx, dy, seconds)
        ball_point = (x, y)
           
        pygame.display.update()
            
if __name__ == "__main__":
    run()
