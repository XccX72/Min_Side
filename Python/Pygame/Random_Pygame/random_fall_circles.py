import sys
import pygame
import random as rnd
import time
# pygame setup
pygame.init()

#Hvor stor skjermen skal være målt i pixler
window = pygame.display.set_mode((600, 500))

#Tittel
pygame.display.set_caption("Rnd Kule Falling")

game_active = False

#Variabel for å kontrollere hvor raskt programmet kjører i en loop
clock = pygame.time.Clock()

liste_prikker = []
liste_prikker_slem = []
for i in range(10):
    x = rnd.randint(4, 596)
    y = rnd.randint(-500, 0)
    liste_prikker.append(pygame.Vector2(x, y))

for i in range(5):
    x_slem = rnd.randint(4, 596)
    y_slem = rnd.randint(-500, 0)
    liste_prikker_slem.append(pygame.Vector2(x_slem, y_slem))




player_width = 75
player_height = 10
player_pos = pygame.Rect(
    window.get_width() / 2 - player_width, 
    window.get_height() - (player_height + 10), 
    player_width, 
    player_height
)

score = 0

running = True
#Delta_Time og er basically tiden fra forrige bilde til nestealtså FPS(Frames Per Second) 
dt = 0
#-----------------------------------------------------------------------
#For å lage tektst og knapp
#-----------------------------------------------------------------------
#Tekst
pygame.font.init()
min_font = pygame.font.SysFont("Arial", 32)

#Knapp
knapp_rect = pygame.Rect(window.get_width() - 110, window.get_height() - 490, 100, 50)
knapp_farge = "white"

def spill():
    global game_active, score, running, player_width, dt
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True

        window.fill("black")


        if game_active:
            #--------------------------------------------------------------
            #tekst del score
            #---------------------------------------------------------------

            tekst_bilde = min_font.render(f"Score = {score}", True, "white")
            window.blit(tekst_bilde, (20, 20))

            #---------------------------------------------------------------
            #Knapp del
            #---------------------------------------------------------------
            mus_pos = pygame.mouse.get_pos()
            mus_klikk = pygame.mouse.get_pressed()

            if knapp_rect.collidepoint(mus_pos):
                knapp_farge = "lightgray" #Highligter knappen TRENGER IKKE DET EGENTLIG
                if mus_klikk[0] and knapp_rect.collidepoint(mus_pos): #[0] er venstre museklikk
                    score = 0
                    player_pos.width = 75
            else:
                knapp_farge = "white"

            pygame.draw.rect(window, knapp_farge, knapp_rect)
            knapp_tekst = min_font.render("Reset", True, "black")
            window.blit(knapp_tekst, (knapp_rect.x + 10, knapp_rect.y + 10))


            #-------------------------------------------------------------------------------------
            #For å tegne alle prikkene
            #-------------------------------------------------------------------------------------
            for kule in liste_prikker:
                kule.y += 300 * dt

                if player_pos.collidepoint(kule):
                    score += 1

                    kule.y = rnd.randint(-50, -10)
                    kule.x = rnd.randint(0, 600)

                    #For å øke størrelsen til player
                    player_pos.width += 5
                    player_width = player_pos.width

                if kule.y > 500:
                    kule.y = rnd.randint(-50, -10)
                    kule.x = rnd.randint(0, 600)

            for kule in liste_prikker:
                pygame.draw.circle(window, (100, 100, 225), kule, 4)

            #---------------------------------------------------------------
            #Tegne slemme kuler
            #---------------------------------------------------------------
            for kule in liste_prikker_slem:
                kule.y += 300* dt

                if player_pos.collidepoint(kule):
                    score -= 1

                    kule.y = rnd.randint(-50, -10)
                    kule.x = rnd.randint(0, 600)

                    #For å øke størrelsen til player
                    player_pos.width -= 5
                    player_width = player_pos.width

                if kule.y > 500:
                    kule.y = rnd.randint(-50, -10)
                    kule.x = rnd.randint(0, 600)

            for kule in liste_prikker_slem:
                pygame.draw.circle(window, "yellow", kule, 4)

            #---------------------------------------------------------------------

            player = pygame.draw.rect(window, "red", player_pos, 0, 10)

            if player_pos.width >= window.get_width():
                tekst_vunnet = min_font.render(f"Du Vant!", True, "white")
                window.blit(tekst_vunnet, (window.get_width() / 2, window.get_height() / 2))
                time.sleep(5)
                game_active = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
            if keys[pygame.K_a]:
                player_pos.x -= 300 * dt
            if keys[pygame.K_d]:
                player_pos.x += 300 * dt
            if keys[pygame.K_r]:
                score = 0

            if player_pos.x < 0:
                player_pos.x = 0
            elif player_pos.x > window.get_width() - player_width:
                player_pos.x = window.get_width() - player_width

        else:
            font = pygame.font.SysFont("Arial", 40)
            start_tekst = font.render("Trykk SPACE for å starte", True, "white")

            window.blit(start_tekst, (150, 200))
        
        pygame.display.flip()
        #Gjør at den kan maks oppdater bilde 60 ganger i sek (60 FPS)
        # / 1000 er 1 sek og lagrer det til dt for loopen
        dt = clock.tick(60) / 1000 


spill()
#Avslutter pygame
pygame.quit()
#Avslutter fullstendig python
sys.exit()