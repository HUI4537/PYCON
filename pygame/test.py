import pygame, sys, os
from pygame.locals import *

def main():
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Nemo game')

    bgImage = pygame.image.load('image/rock.png')
    bgImage = pygame.transform.scale(bgImage, (screen_width, screen_height))

    player = pygame.Rect(((screen_width - 30) / 2), screen_height - 30, 30, 30)
    player_img = pygame.image.load('image/player.png')
    player_img = pygame.transform.scale(player_img, (30, 30))

    block1 = pygame.Rect(((screen_width - 50) / 2)-50, screen_height - 50, 50, 50)
    block1_img = pygame.image.load('image/rock.png')
    block1_img = pygame.transform.scale(block1_img, (50, 50))

    clock = pygame.time.Clock()
    game_speed = 0.5
    slow_game_speed = 0.1  # 느린 속도
    y_vel = 0

    while True:
        dt = clock.tick(80)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        KeyInput = pygame.key.get_pressed()
        if KeyInput[K_LEFT] and player.left >= 0:
            player.left -= game_speed * dt
        if KeyInput[K_RIGHT] and player.right <= screen_width:
            player.right += game_speed * dt

        # 왼쪽으로 밀기
        if (player.left <= block1.right and
            player.right >= block1.right and
            player.bottom > block1.top and
            player.top < block1.bottom):
            block1.x -= slow_game_speed * dt  # 느린 속도로 밀기
            player.x -= slow_game_speed * dt  # 느린 속도로 움직임

        # 오른쪽으로 밀기
        if (player.right >= block1.left and
            player.left <= block1.left and
            player.bottom > block1.top and
            player.top < block1.bottom):
            block1.x += slow_game_speed * dt  # 느린 속도로 밀기
            player.x += slow_game_speed * dt  # 느린 속도로 움직임

        player.top += y_vel
        y_vel += 1

        if player.bottom >= 600:
            y_vel = 0
            if KeyInput[K_SPACE] or KeyInput[K_UP]:
                y_vel = -18

        screen.fill((0, 0, 0))
        screen.blit(player_img, player)
        screen.blit(block1_img, block1)

        pygame.display.update()

main()
