import pygame, sys, os
from stage import *

def main():
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Nemo game')

    # 배경 이미지 로드 및 크기 조정
    bgImage = pygame.image.load('image/rock.png')
    bgImage = pygame.transform.scale(bgImage, (screen_width, screen_height))

    # 캐릭터 및 이미지 로드
    player = pygame.Rect(((screen_width - 30) / 2), screen_height - 30, 30, 30)
    player_img = pygame.image.load('image/player.png')
    player_img = pygame.transform.scale(player_img, (30, 30))

    block1 = pygame.Rect(((screen_width - 50) / 2)-50, screen_height - 50, 50, 50)
    blokc1_img = pygame.image.load('image/rock.png')
    blokc1_img = pygame.transform.scale(blokc1_img, (50, 50))

    clock = pygame.time.Clock()
    game_speed = 0.5
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
        if player.left == block1.right:
            print("오예")
        player.top += y_vel
        y_vel += 1

        if player.bottom >= 600:
            y_vel = 0
            if KeyInput[K_SPACE] or KeyInput[K_UP]:
                y_vel = -18
        stage1()
        # 배경 이미지 그리기
        screen.fill((0, 0, 0))
        
# 캐릭터 이미지 그리기
        screen.blit(player_img, player)

        screen.blit(blokc1_img, block1)

        pygame.display.update()

main()