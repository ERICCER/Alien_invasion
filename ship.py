import pygame

class Ship():
    def __init__(self,screen,ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
            #self.rect.centerx += 1
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
            #self.rect.centerx -= 1

        self.rect.centerx = self.center

        if self.moving_right and self.rect.right < self.screen_rect.right:


    def blitme(self):
        self.screen.blit(self.image,self.rect)