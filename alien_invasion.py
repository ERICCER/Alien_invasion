import sys
import os
import pygame
from pygame.locals import *
from setting import Setting

def run_game():
    pygame.init()

    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_height,ai_setting.screen_width))
    #screen = pygame.display.set_mode((1000,600))

    pygame.display.set_caption("Alien")

    bg_c = ('C:/Users/Eric/Desktop/alien/image/bg.png')

    bg = pygame.image.load(bg_c).convert()

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                sys.exit()

        screen.blit(bg,(0,0))

        pygame.display.flip()

run_game() 