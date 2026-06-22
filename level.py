import pygame
from settings import *

class Level:
    def __init__(self):
        self.platform = pygame.Rect(0, 350, 800, 50)

        self.coin_image = pygame.image.load(ASSET_PATH + "coin.png")
        self.coin_image = pygame.transform.scale(self.coin_image, (20, 20))
        self.coin_rect = self.coin_image.get_rect(topleft=(400, 300))

        self.goal = pygame.Rect(750, 300, 30, 50)

        self.background = pygame.image.load(ASSET_PATH + "background.png")
        self.background = pygame.transform.scale(self.background, (800, 400))

        self.score = 0

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

        pygame.draw.rect(screen, (0, 255, 0), self.platform)
        screen.blit(self.coin_image, self.coin_rect)
        pygame.draw.rect(screen, (0, 0, 255), self.goal)

    def check_coin(self, player):
        if player.rect.colliderect(self.coin_rect):
            self.score += 1
            self.coin_rect.x = 600

    def check_goal(self, player):
        return player.rect.colliderect(self.goal)
