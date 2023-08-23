import pygame , sys
from pygame.locals import *

#메인 게임함수
def main():
    # 게임 초기화 정보
    pygame.init()
    screen_width = 800
    screen_hight = 600
    screen = pygame.display.set_mode((screen_width, screen_hight))
    pygame.display.set_caption('Nemo game')

    # 캐릭터 객체 생성
    player = pygame.Rect((screen_width - 30 )/2, screen_hight-30, 30, 30)
    player_img = pygame.image.load('image/player.png')
    player_img = pygame.transform.scale(player_img, (30, 30))

    #게임 속도 조절
    clock = pygame.time.Clock()
    game_speed = 0.5

    #중력
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

        # 중력 엔진
        player.top += y_vel 
        y_vel += 0.8
        
        if player.bottom >= 600:
            y_vel = 0
            if KeyInput[K_SPACE] or KeyInput[K_UP]:
                y_vel = -18


        screen.fill((0, 0, 0),)
        screen.blit(player_img, player)
        pygame.display.update()

main()