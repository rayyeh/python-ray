import pygame
from pygame.locals import *
from sys import exit
from random import randint

size = (600, 600)
title = "Pong Game Test"
black = (0, 0, 0)
gray = (128, 128, 128)
white = (255, 255, 255)
yellow = (255, 255, 0)
aqua = (0, 255, 255)
prompt = {1:"1. Play", 2:"2. Simulation", 3:"3. Exit"}

def ballcontrol(point, radius, dx, dy, seconds, bat_score, player_score):
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
        bat_score += 1
        
    if y < size[1] - radius:
        y += dy * seconds
        
    if y > size[1] - radius:
        dy *= -1
        y = size[1] - radius
        player_score += 1
        
    return x, y, dx, dy, bat_score, player_score

def rebound(point, dx, dy, seconds):
    x, y = point
    if randint(0, 1):
        dx *= -1.0
    else:
        dx *= 1.0
        dy *= -1
        x += dx * (seconds + 0.1)
        y += dy * (seconds + 0.1)
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

def batcontrol(key, point, speed, side, seconds):
    x, y = point
    if key[K_LEFT]:
        x -= speed * seconds
    if x < 0:
        x = 0
    elif key[K_RIGHT]:
        x += speed * seconds
    if x + side[0] > size[0]:
        x = size[0] - side[0]
    return x, y

def player1control(player_point, ball_point, speed, side, seconds):
    player_x, player_y = player_point
    ball_x, ball_y = ball_point
    if ball_y < 400:
        if player_x < ball_x + side[0]:
            player_x += speed * seconds
            
            if player_x < 0:
                player_x = 0
            elif player_x + side[0] > size[0]:
                player_x = size[0] - side[0]
                
        if player_x > ball_x:
            player_x -= speed * seconds
            
            if player_x < 0:
                player_x = 0
            elif player_x + side[0] > size[0]:
                player_x = size[0] - side[0]
    return player_x, player_y

def player2control(player_point, ball_point, speed, side, seconds):
    player_x, player_y = player_point
    ball_x, ball_y = ball_point
    if ball_y > 400:
        if player_x < ball_x + side[0]:
            player_x += speed * seconds
            if player_x < 0:
                player_x = 0
            elif player_x + side[0] > size[0]:
                player_x = size[0] - side[0]
                
        if player_x > ball_x:
            player_x -= speed * seconds
            if player_x < 0:
                player_x = 0
            elif player_x + side[0] > size[0]:
                player_x = size[0] - side[0]
                
    return player_x, player_y

def userplay(screen):
    ball_point = (300, 400)
    ball_x, ball_y = ball_point
    radius = 10.
    side = (80, 12)
    bat_point = (260, 740)
    player_point = (260, 60)
    bat_speed = 150
    sign_x, sign_y = initial()
    ball_dx = sign_x * speed()
    ball_dy = sign_y * speed()
    score_point = (700, 500)
    bat_score = 0
    player_score = 0
    font = pygame.font.SysFont("arial", 32)
    
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            screen.fill(black)
            seconds = clock.tick(30) / 1000.0
            ball = pygame.draw.circle(screen, yellow, ball_point, radius)
            bat = pygame.draw.rect(screen, white, Rect(bat_point, side))
            player = pygame.draw.rect(screen, gray, Rect(player_point, side))
            
            player_x, player_y = player_point
            
            bat_text = font.render(str(bat_score), True, white)
            player_text = font.render(str(player_score), True, gray)
            screen.blit(bat_text, (size[0]-bat_text.get_width()-20, \
                                   size[1]/2+80))
            screen.blit(player_text, (size[0]-player_text.get_width()-20,\
                                      size[1]/2-80))
            # ball control
            if bat.colliderect(ball):
                ball_x, ball_y, ball_dx, ball_dy = \
                      rebound(ball_point, ball_dx, ball_dy, seconds)
            elif player.colliderect(ball):
                ball_x, ball_y, ball_dx, ball_dy = \
                      rebound(ball_point, ball_dx, ball_dy, seconds)
            else:
                ball_x, ball_y, ball_dx, ball_dy, bat_score, player_score = \
                      ballcontrol(ball_point, radius, ball_dx, ball_dy,\
                                  seconds, bat_score, player_score)
            ball_point = (ball_x, ball_y)
            
            # user's bat
            pressed_key = pygame.key.get_pressed()
            bat_point = batcontrol(pressed_key, bat_point, bat_speed, \
                                 side, seconds)
            
            # artificial intelligence
            player_point = player1control(player_point, ball_point, \
                                        bat_speed, side, seconds)
          
            if pygame.key.get_pressed()[K_ESCAPE]:
                menu(screen, prompt)
                
            pygame.display.update()
          
def simulateplay(screen):
    ball_point = (300, 400)
    ball_x, ball_y = ball_point
    radius = 10.
    side = (80, 12)
    bat_point = (260, 740)
    player_point = (260, 60)
    bat_speed = 150
    sign_x, sign_y = initial()
    ball_dx = sign_x * speed()
    ball_dy = sign_y * speed()
    score_point = (700, 500)
    bat_score = 0
    player_score = 0
    font = pygame.font.SysFont("arial", 32)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        screen.fill(black)
        seconds = clock.tick(30) / 1000.0
        ball = pygame.draw.circle(screen, yellow, ball_point, radius)
        bat = pygame.draw.rect(screen, white, Rect(bat_point, side))
        player = pygame.draw.rect(screen, gray, Rect(player_point, side))
        player_x, player_y = player_point
        bat_text = font.render(str(bat_score), True, white)
        player_text = font.render(str(player_score), True, gray)
        screen.blit(bat_text, (size[0]-bat_text.get_width()-20, \
                               size[1]/2+80))
        screen.blit(player_text, (size[0]-player_text.get_width()-20,\
                                  size[1]/2-80))
        # ball control
        if bat.colliderect(ball):
            ball_x, ball_y, ball_dx, ball_dy = \
                  rebound(ball_point, ball_dx, ball_dy, seconds)
        elif player.colliderect(ball):
            ball_x, ball_y, ball_dx, ball_dy = \
                  rebound(ball_point, ball_dx, ball_dy, seconds)
        else:
            ball_x, ball_y, ball_dx, ball_dy, bat_score, player_score = \
                  ballcontrol(ball_point, radius, ball_dx, ball_dy,\
                              seconds, bat_score, player_score)
            ball_point = (ball_x, ball_y)
        # artificial intelligence
        player_point = player1control(player_point, ball_point, \
                                      bat_speed, side, seconds)
        bat_point = player2control(bat_point, ball_point, bat_speed, \
                                   side, seconds)
        
        if pygame.key.get_pressed()[K_ESCAPE]:
            menu(screen, prompt)
            pygame.display.update()
            
def menu(screen, prompt):
    font = pygame.font.SysFont("arial", 40)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        text1 = font.render(prompt[1], True, white)
        text1_1 = font.render(prompt[1], True, aqua)
        text2 = font.render(prompt[2], True, white)
        text2_1 = font.render(prompt[2], True, aqua)
        text3 = font.render(prompt[3], True, white)
        text3_1 = font.render(prompt[3], True, aqua)
        x, y = pygame.mouse.get_pos()
        
        screen.fill(black)
        if 200 <= x <= 200 + text1.get_width() and \
           200 <= y <= 200 + text1.get_height():
            screen.blit(text1_1, (200, 200))
            screen.blit(text2, (200, 240))
            screen.blit(text3, (200, 280))
            
        if pygame.mouse.get_pressed()[0]:
            userplay(screen)
        elif 200 <= x <= 200 + text2.get_width() and \
             240 <= y <= 240 + text1.get_height():
            screen.blit(text1, (200, 200))
            screen.blit(text2_1, (200, 240))
            screen.blit(text3, (200, 280))
            
        if pygame.mouse.get_pressed()[0]:
            simulateplay(screen)
        elif 200 <= x <= 200 + text3.get_width() and \
             280 <= y <= 280 + text1.get_height():
            screen.blit(text1, (200, 200))
            screen.blit(text2, (200, 240))
            screen.blit(text3_1, (200, 280))
            
        if pygame.mouse.get_pressed()[0]:
            exit()
        else:
            screen.blit(text1, (200, 200))
            screen.blit(text2, (200, 240))
            screen.blit(text3, (200, 280))
            pygame.display.update()
            
def run():
    pygame.init()
    screen = pygame.display.set_mode(size, 0, 32)
    pygame.display.set_caption(title)
    menu(screen, prompt)
    
if __name__ == "__main__":
    '''import psyco'''
    '''psyco.profile() '''
    run()
