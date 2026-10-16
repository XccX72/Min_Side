import pygame
import sys

pygame.init()
window = pygame.display.set_mode((600, 500), pygame.RESIZABLE)
pygame.display.set_caption("1. Game")

clock = pygame.time.Clock()
running = True

dt = 0

player_width = 75
player_height = 40
player_pos = pygame.Rect(window.get_width() / 2 - (player_width / 2) , window.get_height() - 100, player_width, player_height)


score = 0


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill("black")

    #Player------------------------------------------------------------------------------

    player = pygame.draw.rect(window, "blue", player_pos)

    #Keys for player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt 
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    
    #For å holde player innenfor skjermen
    if player_pos.y < 0:
        player_pos.y = 0
    elif player_pos.y > window.get_height() - player_height:
        player_pos.y =  window.get_height() - player_height
    elif player_pos.x < 0:
        player_pos.x = 0
    elif player_pos.x > window.get_width() - player_width:
        player_pos.x = window.get_width() - player_width








    pygame.display.flip()
    dt = clock.tick(60) / 1000 
pygame.quit()
sys.exit()