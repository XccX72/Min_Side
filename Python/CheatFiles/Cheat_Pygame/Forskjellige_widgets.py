import sys
import pygame

# pygame setup
pygame.init()

#Hvor stor skjermen skal være målt i pixler
window = pygame.display.set_mode((600, 500))

#Tittel
pygame.display.set_caption("Rød Kule Spill")

#Variabel for å kontrollere hvor raskt programmet kjører i en loop
clock = pygame.time.Clock()
running = True

#Delta_Time og er basically tiden fra forrige bilde til nestealtså FPS(Frames Per Second) 
dt = 0

#Posisjon til rød sirkel ved å ta hele lengden og dele på 2 og det samme med høyde
#Da vil du få koordinasjone til midten av fanen
#.Vector2 er for å lagre 2 verdier i en parantes
kule_pos = pygame.Vector2(window.get_width() / 2, window.get_height() / 2)
arc_pos = (100, 100, 200, 50)

while running:
    # poll for events
    # Sjekker hvis noen har trykket på x knappen oppe i høuyre hjlrner
    # if True så sletter stopper den while loopen som kjører hele programmet
    # for loopen og if setningen sjekker om x knapp trykket
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    window.fill("black")


    #Tegner en sicrle ved hjelp av:
    #(hvilket vindu, farge, posisjon start, størrelse (pixler i radius) )
    sirkel = pygame.draw.circle(window, "red", kule_pos, 40)


    abc = pygame.draw.rect(window, "blue", arc_pos)

    if kule_pos.y < 40:
        kule_pos.y = 40
    elif kule_pos.y > 500 - 40:
        kule_pos.y =  500 - 40
    elif kule_pos.x < 40:
        kule_pos.x = 40
    elif kule_pos.x > 600 - 40:
        kule_pos.x = 600 - 40

    #----------------------------------------------------------------------------
    # Keys delen 
    #----------------------------------------------------------------------------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        kule_pos.y -= 300 * dt 
    if keys[pygame.K_s]:
        kule_pos.y += 300 * dt
    if keys[pygame.K_a]:
        kule_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        kule_pos.x += 300 * dt
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    # flip() the display to put your work on screen
    #Vise hele koden samtidig på skjermen
    #Uten den ville for eks rød sirkel ikke bli vist
    pygame.display.flip()

    #Gjør at den kan maks oppdater bilde 60 ganger i sek (60 FPS)
    # / 1000 er 1 sek og lagrer det til dt for loopen
    dt = clock.tick(60) / 1000 


#Avslutter pygame
pygame.quit()
#Avslutter fullstendig python
sys.exit()