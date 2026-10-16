import pygame

# 1. Innstillinger
SKJERM_BREDDE = 600
SKJERM_HOYDE = 600
CELLE_STORRELSE = 40  # Hvor stor hver rute skal være

# Farger (RGB)
HVIT = (255, 255, 255)
GRA = (200, 200, 200)
SVART = (0, 0, 0)

def tegn_grid(skjerm):
    # Tegn vertikale linjer (kolonner)
    for x in range(0, SKJERM_BREDDE, CELLE_STORRELSE):
        pygame.draw.line(skjerm, GRA, (x, 0), (x, SKJERM_HOYDE))
    
    # Tegn horisontale linjer (rader)
    for y in range(0, SKJERM_HOYDE, CELLE_STORRELSE):
        pygame.draw.line(skjerm, GRA, (0, y), (SKJERM_BREDDE, y))

def main():
    pygame.init()
    skjerm = pygame.display.set_mode((SKJERM_BREDDE, SKJERM_HOYDE))
    pygame.display.set_caption("Mitt Pygame Grid")
    klokke = pygame.time.Clock()

    kjorer = True
    while kjorer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kjorer = False

        # Fyll skjermen med hvit bakgrunn
        skjerm.fill(HVIT)

        # Kall funksjonen som tegner rutenettet
        tegn_grid(skjerm)

        # Oppdater skjermen
        pygame.display.flip()
        klokke.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()