import pygame, sys, os
from pygame.locals import *
from stage import stage1
def up(player, rect, y_vel, GR, KeyInput):
    if (player.bottom >= rect.top and
            player.bottom <= rect.top + y_vel and
            player.right >= rect.left and
            player.left <= rect.right):
        y_vel = 0
        if KeyInput[K_SPACE] or KeyInput[K_UP] and GR == 1:
            y_vel = -14 * GR
        player.bottom = rect.top
    
    # player.top이 rect.bottom에 닿았을 때
    elif (player.top <= rect.bottom and
            player.top >= rect.bottom + y_vel and
            player.right >= rect.left and
            player.left <= rect.right):
        if GR == -1:
            y_vel = 0
        else:
            y_vel = 2
        if KeyInput[K_SPACE] or KeyInput[K_UP]:
            if GR == -1:
                y_vel = 14  # 중력 반전 상태에서는 양수 방향으로 뛰어올립니다.
        player.top = rect.bottom

    # 바닥의 측면 감지
    if (player.right >= rect.left and
            player.left <= rect.left and
            player.bottom > rect.top and
            player.top < rect.bottom):
        player.right = rect.left
        
    
    # 바닥의 왼쪽 감지
    if (player.bottom >= rect.top and
            player.top <= rect.bottom and
            player.right >= rect.left and
            player.right <= rect.left + y_vel):
        player.right = rect.left

    # 바닥의 오른쪽 감지
    if (player.left <= rect.right and
            player.right >= rect.right and
            player.bottom > rect.top and
            player.top < rect.bottom):
        player.left = rect.right
    
    return y_vel

def main():
    pygame.init()
    screen_width = 1100
    screen_height = 650
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Nemo game')
    
    stage1_result = stage1(screen, screen_width, screen_height)
    player, player_img = stage1_result

    #스프라이트 시트
    dying_img = pygame.image.load('image/dying_motion.png').convert_alpha()
    #가시
    trap = pygame.Rect(500, screen_height -90, 50, 50)
    trap_img = pygame.image.load('image/trap.png')
    trap_img = pygame.transform.scale(trap_img, (50, 50))

    #가시2
    trap2 = pygame.Rect(500, screen_height-411, 50, 50)
    trap2_img = pygame.transform.flip(pygame.image.load('image/trap.png'), False, True)
    trap2_img = pygame.transform.scale(trap2_img, (50, 50))

    #가시 3
    trap3 = pygame.Rect(200, 154, 50, 50)
    trap3_img = pygame.image.load('image/trap.png')
    trap3_img = pygame.transform.scale(trap3_img, (50, 50))

    block1 = pygame.Rect(((screen_width - 50) / 2)-50, screen_height - 50, 50, 50)
    block1_img = pygame.image.load('image/rock.png')
    block1_img = pygame.transform.scale(block1_img, (50, 50))

    # 바닥 1의 Rect 객체 생성
    floor1_rect = pygame.Rect(250, screen_height - 40, screen_width - 250, 40)
    #바닥 2
    floor2 = pygame.Rect(555, screen_height-243, 445, 35)
    # 3
    floor3 = pygame.Rect(710, screen_height-80, screen_width-710, 40)
    #4
    floor4 = pygame.Rect( 0, screen_height-233, 495, 35)
    #바닥 5
    floor5 = pygame.Rect(200, 202, 900, 35)
        
    #천장 
    celing = pygame.Rect( 0, 0, 410, 34)
    #천장 2
    celing2 = pygame.Rect(470, 0, screen_width -470, 44)

    #벽
    wall = pygame.Rect(688, screen_height -380, 30, 150)

    wall2 = pygame.Rect(850, screen_height-415, 30, 138)
    
    
    clock = pygame.time.Clock()

    #변수설정
    GR = 1 #중력반전
    game_speed = 0.5
    y_vel = 0
    colltime = 50
        
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
        
        #중력 반전

        colltime +=1
        print(colltime)
        if colltime >= 50:
            colltime = 50
        
        if KeyInput[K_LSHIFT] and colltime == 50:
            y_vel = 0
            GR = GR * -1
            
            colltime = 0
        
        if GR == -1:
            player_img = pygame.image.load('image/player2.png')
            player_img = pygame.transform.scale(player_img, (30, 30))
        else:
            player_img = pygame.image.load('image/player.png')
            player_img = pygame.transform.scale(player_img, (30, 30))
       
        # 캐릭터가 바닥 1과 충돌한 경우
        y_vel = up(player, floor1_rect, y_vel, GR, KeyInput)

        #2
        y_vel = up(player, floor2, y_vel, GR, KeyInput)

        y_vel = up(player, floor3, y_vel, GR, KeyInput)
        y_vel = up(player, floor4, y_vel, GR, KeyInput)
        y_vel = up(player, floor5, y_vel, GR, KeyInput)
        #천장
        y_vel = up(player, celing, y_vel, GR, KeyInput)
        y_vel = up(player, celing2, y_vel, GR, KeyInput)
        #벽
        y_vel = up(player, wall, y_vel, GR, KeyInput)
        y_vel = up(player, wall2, y_vel, GR, KeyInput)
            

        #중력처리
        player.top += y_vel
        # 중력 처리 부분
        if GR == 1:
            # 기본 중력 (아래로 떨어짐)
            y_vel += 1
        else:
            # 중력 반전 (위로 떨어짐)
            y_vel -= 1
        
   
        
        #바닥처리
        if player.bottom >= screen_height and GR == 1:
            y_vel = 0
            if KeyInput[K_SPACE] or KeyInput[K_UP] :
                y_vel = -14 * GR
        elif player.bottom >= screen_height and GR == -1:
            y_vel = -2

        #천장처리
        if player.top <= 0:
            player.top = 0
            
        screen.fill((0, 0, 0))
        screen.blit(player_img, player)
        # screen.blit(block1_img, block1)
        #가시 1
        screen.blit(trap_img, trap)
        #가시2
        screen.blit(trap2_img, trap2)

        screen.blit(trap3_img, trap3)

        #바닥 1
        pygame.draw.rect(screen, (255, 255, 255), floor1_rect)
        #바닥 2
        white = (255, 255, 255)
        pygame.draw.rect(screen,white,floor2)
        #바닥 3
        pygame.draw.rect(screen,white,floor3)
        #4
        pygame.draw.rect(screen,white,floor4)
        #바닥 5
        pygame.draw.rect(screen,white, floor5)
        
        #천장 
        pygame.draw.rect(screen,white, celing)
        #천장 2
        pygame.draw.rect(screen,white, celing2)

        pygame.draw.rect(screen,white, wall)
        pygame.draw.rect(screen,white, wall2)


        pygame.display.update()

main()