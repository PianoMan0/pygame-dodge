# Copyright 2023-2025 PianoMan0
import pygame
import sys
import random

# Game constants
WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 5
BULLET_SPEED = 5
ENEMY_SPEED = 5
MAX_ENEMIES = 1000000
SPAWN_RATE = 5  # Enemies spawn every 5 frames

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)
bullets = []
enemies = []

frame_count = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player.y += PLAYER_SPEED
    if keys[pygame.K_LEFT]:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += PLAYER_SPEED

    player.clamp_ip(screen.get_rect())

    if keys[pygame.K_SPACE] and frame_count % 10 == 0:
        bullet = pygame.Rect(player.centerx, player.centery, 10, 10)
        bullets.append(bullet)

    for bullet in bullets:
        bullet.y -= BULLET_SPEED
        if not screen.get_rect().colliderect(bullet):
            bullets.remove(bullet)

    if frame_count % SPAWN_RATE == 0 and len(enemies) < MAX_ENEMIES:
        enemy = pygame.Rect(random.randrange(WIDTH), 0, 30, 30)
        enemies.append(enemy)

    for enemy in enemies:
        enemy.y += ENEMY_SPEED
        if player.colliderect(enemy):
            pygame.quit()
            sys.exit()
        for bullet in bullets:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                bullets.remove(bullet)
                break

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player)
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 0), bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)


    pygame.display.flip()

    clock.tick(30)

    frame_count += 1
