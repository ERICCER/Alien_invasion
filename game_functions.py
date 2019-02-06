import sys

import pygame

from bullet import Bullet

def check_events(ship):

    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:

            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                ship.moving_right = True

            if event.key == pygame.K_a:
                ship.moving_left = True

            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(ai_setting,screen,ship)
                bullets.add(new_bullet)


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                ship.moving_right = False

            if event.key == pygame.K_a:
                ship.moving_left = False


def update_screen(ai_settings,screen,ship,bullets):

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pygame.display.flip()