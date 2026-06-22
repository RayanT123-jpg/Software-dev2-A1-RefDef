import pygame
import sys

from settings import *
from player import Player
from enemy import Enemy
from level import Level

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Style Platformer")

clock = pygame.time.Clock()

player = Player()
enemy = Enemy()
level = Level()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player.move(keys)

    if keys[pygame.K_SPACE]:
        player.jump(level.platform)

    player.update(level.platform)

    enemy.move()

    # Collisions
    if player.rect.colliderect(enemy.rect):
        print("Game Over")
        running = False

    level.check_coin(player)

    if level.check_goal(player):
        print("You Win!")
        running = False

    # Draw everything
    level.draw(screen)
    player.draw(screen)
    enemy.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
