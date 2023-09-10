import pygame

def stage1(screen, screen_width, screen_height):
    player = pygame.Rect(20, screen_height - 30, 30, 30)
    player_img = pygame.image.load('image/player.png')
    player_img = pygame.transform.scale(player_img, (30, 30))
    print("z")
    return player, player_img