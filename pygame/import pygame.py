import pygame
import os

# 현재 위치 정의
current_path = os.path.dirname(__file__)

# 이미지 폴더 위치 정의
image_path = os.path.join(current_path, "image")


pygame.init()

screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Nemo game") #게임 이름

#스프라이트 불러오기
character = pygame.image.load(os.path.join(image_path, "red_player.png"))
character_size = character.get_rect().size #이미지 크기 구해옴
character_width = character_size[0]
character_height = character_size[1]

character_x_pos = (screen_width // 2) - (character_width // 2) #화면 중앙 좌표
character_y_pos = screen_height - character_height


#이동할 좌표

to_x = 0
to_y = 0

#이벤트 루프
running = True
while running: #게임 진행 루프 
    for  event in pygame.event.get(): #어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: #게임 X 버튼 눌렀을때
            running = False

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= 0.1
                pass
            elif event.key == pygame.K_RIGHT:
                to_x += 0.1
                pass
            elif event.key == pygame.K_UP:
                to_y -= 0.1
                pass
            elif event.key == pygame.K_DOWN:
                to_y += 0.1
                pass

        if event.type == pygame.KEYUP: #방향키를 뗴면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y
    
    #가로 경계값 처리
    if character_x_pos <0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width


    screen.fill((0, 0, 0)) #리셋
    
    screen.blit(character, (character_x_pos, character_y_pos) ) #캐릭터를 띄움
    
    pygame.display.update()

pygame.quit() #게임을 끈다