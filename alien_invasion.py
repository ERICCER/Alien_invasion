#import sys
#import os
import pygame
####use module####
from setting import Setting
from ship import Ship
import game_functions as gf
####use module####
def run_game():
    pygame.init()

    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_height,ai_setting.screen_width))
    #screen = pygame.display.set_mode((1000,600))

    pygame.display.set_caption("Alien")

    ship = Ship(ai_setting,screen)

    while True:

            gf.check_events(ship)
            ship.update()
            gf.update_screen(ai_setting,screen,ship)
"""
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                sys.exit()

        screen.fill(ai_setting.bg_color)
        ship.blitme()
        pygame.display.flip()
"""
run_game()