import sys
import pygame
import random as rnd
import time
#--------------------------------------------------------------
#Funksjon Avslutt spill
#--------------------------------------------------------------
def quit_game():
    pygame.quit()
    sys.exit()

#----------------------------------------------------------------
#Funksjon Tegn objekter
#----------------------------------------------------------------
def draw_objects(window, player_rect, snille, slemme, font_text, pos_meny, mus_pos, mus_klikk, vunnet):
    window.fill("black")

    #Player 0 og 100 er for å få de runde kantene
    pygame.draw.rect(window, "khaki", player_rect, 0, 100)

    #Snille kuler
    for kule in snille:
        pygame.draw.circle(window, "forestgreen", (int(kule.x), int(kule.y)), 4)

    #slemme kuler
    for kule in slemme:
        pygame.draw.circle(window, "maroon", (int(kule.x), (int(kule.y))), 4)

    #Restart spill
    pygame.draw.rect(window, "white", pos_meny, 0 ,50)
    knapp_tekst = font_text.render("Meny", True, "black")
    window.blit(knapp_tekst, (pos_meny.x + 10, pos_meny.y + 10))


    if pos_meny.collidepoint(mus_pos):
        if mus_klikk[0]: #[0] er venstre museklikk
            return 1
    
    # Oppdater Fanen får å putte på det som er i denne funksjonen
    pygame.display.update()

    return vunnet

#--------------------------------------------------------------------------------------
#If vunnet del og tapt
#---------------------------------------------------------------------------------------
def draw_objects_vinn(window, font_text, pos_meny, mus_pos, mus_klikk, vunnet):
    window.fill("black")

    tekst_vunnet = font_text.render(f"Du Vant!", True, "white")
    tekst_rect = tekst_vunnet.get_rect(center=(window.get_width()/2, window.get_height()/2))
    window.blit(tekst_vunnet, tekst_rect)

    #Restart spill
    pygame.draw.rect(window, "white", pos_meny, 0, 50)
    knapp_tekst = font_text.render("Meny", True, "black")
    window.blit(knapp_tekst, (pos_meny.x + 10, pos_meny.y + 10))


    if pos_meny.collidepoint(mus_pos):
        if mus_klikk[0]: #[0] er venstre museklikk
            return 1
    pygame.display.update()
    return vunnet

def draw_objects_tapt(window, font_text, pos_meny, mus_pos, mus_klikk, vunnet):
    window.fill("black")

    tekst_vunnet = font_text.render(f"Du Tapte!", True, "white")
    tekst_rect = tekst_vunnet.get_rect(center=(window.get_width()/2, window.get_height()/2))
    window.blit(tekst_vunnet, tekst_rect)

    #Restart spill
    pygame.draw.rect(window, "white", pos_meny, 0, 50)
    knapp_tekst = font_text.render("Meny", True, "black")
    window.blit(knapp_tekst, (pos_meny.x + 10, pos_meny.y + 10))


    if pos_meny.collidepoint(mus_pos):
        if mus_klikk[0]: #[0] er venstre museklikk
            return 1
    pygame.display.update()
    return vunnet

#------------------------------------------------------------------------------------------
#Meny funksjon del
#------------------------------------------------------------------------------------------
def meny(window, font_text, pos_restart, mus_pos, mus_klikk, vunnet):
    window.fill("black")

    #Tittel
    tekst_vunnet = font_text.render(f"Meny", True, "white")
    tekst_rect = tekst_vunnet.get_rect(center=(window.get_width()/2, 30))
    window.blit(tekst_vunnet, tekst_rect)
    pygame.display.update()

    #Restart spill
    pygame.draw.rect(window, "white", pos_restart, 0, 50)
    knapp_tekst = font_text.render(" Reset", True, "black")
    window.blit(knapp_tekst, (pos_restart.x + 10, pos_restart.y + 10))
 

    if pos_restart.collidepoint(mus_pos):
        if mus_klikk[0]: #[0] er venstre museklikk
            return 0
    pygame.display.update()
    return vunnet

#----------------------------------------------------------------
#Funksjon Main
#----------------------------------------------------------------
def main():
    #-----------------------------------------------------------------
    #Basically __init__ for funksjonen
    global player_height, player_width, liste_prikker, liste_prikker_slem
    pygame.init()
    window = pygame.display.set_mode((600, 500))
    pygame.display.set_caption("Spill!")
    #Delta_Time og er basically tiden fra forrige bilde til nestealtså FPS(Frames Per Second) 
    dt = 0
    clock = pygame.time.Clock()
    score = 0
    # 0 er spillet, 1 er meny, 2 er du har vunnet del, 3 er du har tapt del
    vunnet = 1

    #-----------------------------------------------------------------
    #Posisjons del Player
    player_width = 100
    player_height = 15

    player_pos = pygame.Rect(
    window.get_width() / 2 - player_width, 
    window.get_height() - (player_height + 10), 
    player_width, 
    player_height
    )

    #-----------------------------------------------------------------
    #Posisjon del Kule
    #Kuler
    liste_prikker = [pygame.Vector2(rnd.randint(0, 600), rnd.randint(-500, 0)) for i in range(10)]
    liste_prikker_slem = [pygame.Vector2(rnd.randint(0, 600), rnd.randint(-500, 0)) for i in range(10)]

    #------------------------------------------------------------------
    #Posisjons text for alle de forskjellige tingene
    pygame.font.init()
    hoved_font = pygame.font.SysFont("Arial", 32)

    #--------------------------------------------------------------------
    #Posisjon mus
    knapp_restart_pos = pygame.Rect(window.get_width() - 110, 10, 100, 50)
    mus_pos = (0,0)
    mus_klikk = (False, False, False)


    #------------------------------------------------------------------
    #While loop for spill
    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = clock.tick(60) / 1000
        #Spill skjerm
        if vunnet == 0:

            if player_pos.width >= window.get_height():
                vunnet = 2

            if player_pos.width <= 0:
                vunnet = 3

            #----------------------------------------------------------------
            #Del for tastatur knapp
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
            if keys[pygame.K_a]:
                player_pos.x -= 300 * dt
            if keys[pygame.K_d]:
                player_pos.x += 300 * dt



            #---------------------------------------------------------------
            #Beveging av Player
            if player_pos.x < 0:
                    player_pos.x = 0
            elif player_pos.right > window.get_width():
                player_pos.right = window.get_width()

            #----------------------------------------------------------------
            #Kule bevegelser
            
            #Kule snill
            for kule in liste_prikker:
                #Fart for kuler
                kule.y += 300 * dt

                #Sjekker hvis kulene har truffet player
                if player_pos.collidepoint(kule.x, kule.y):
                    score += 1
                    player_pos.width += 5
                    kule.y = rnd.randint(-100, -10)
                    kule.x = rnd.randint(0, 600)

                #Sjekk hvis kule har gått forbi skjermen og under player
                if kule.y > 500:
                    kule.y = rnd.randint(-100, -10)
                    kule.x = rnd.randint(0, 600)

            #Slemme kuler
            for kule in liste_prikker_slem:
                #Fart for kuler
                kule.y += 300 * dt

                #Sjekker hvis kulene har truffet player
                if player_pos.collidepoint(kule.x, kule.y):
                    score -= 1
                    player_pos.width -= 5
                    kule.y = rnd.randint(-100, -10)
                    kule.x = rnd.randint(0, 600)

                #Sjekk hvis kule har gått forbi skjermen og under player
                if kule.y > 500:
                    kule.y = rnd.randint(-100, -10)
                    kule.x = rnd.randint(0, 600)

            #knapp meny
            #Posisjon til knapp for restarting
            knapp_restart_pos = pygame.Rect(window.get_width() - 110, window.get_height() - 490, 100, 50)

            #posisjon til musen
            mus_pos = pygame.mouse.get_pos()
            mus_klikk = pygame.mouse.get_pressed()

            vunnet = draw_objects(window, player_pos, liste_prikker, liste_prikker_slem, hoved_font, knapp_restart_pos, mus_pos, mus_klikk, vunnet)

        #Meny skjerm
        elif vunnet == 1:
            #Posisjon til knapp for restarting
            knapp_restart_pos = pygame.Rect(window.get_width() - 110, window.get_height() - 490, 100, 50)

            #posisjon til musen
            mus_pos = pygame.mouse.get_pos()
            mus_klikk = pygame.mouse.get_pressed()

            vunnet = meny(window, hoved_font, knapp_restart_pos, mus_pos, mus_klikk, vunnet)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()

        #Vunnet skjerm
        elif vunnet == 2:

            #Posisjon til knapp for meny
            knapp_meny_pos = pygame.Rect(window.get_width() - 110, window.get_height() - 490, 100, 50)

            #posisjon til musen
            mus_pos = pygame.mouse.get_pos()
            mus_klikk = pygame.mouse.get_pressed()

            vunnet = draw_objects_vinn(window, hoved_font, knapp_meny_pos, mus_pos, mus_klikk, vunnet)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()

        elif vunnet == 3:
            #Posisjon til knapp for meny
            knapp_meny_pos = pygame.Rect(window.get_width() - 110, window.get_height() - 490, 100, 50)

            #posisjon til musen
            mus_pos = pygame.mouse.get_pos()
            mus_klikk = pygame.mouse.get_pressed()

            vunnet = draw_objects_tapt(window, hoved_font, knapp_meny_pos, mus_pos, mus_klikk, vunnet)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()


    quit_game()

#-----------------------------------------------------------------
#Main
#-----------------------------------------------------------------
if __name__ == "__main__":
    main()
