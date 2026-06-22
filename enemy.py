import pygame
from settings import *

class Enemy:
    def __init__(self):
        self.image = pygame.image.load(ASSET_PATH + "enemy.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(topleft=(600, 310))
        self.direction = 2

    def move(self):
        self.rect.x += self.direction

        if self.rect.left < 500 or self.rect.right > 750:
            self.direction *= -1

    def draw(self, screen):
        screen.blit(self.image, self.rect)
