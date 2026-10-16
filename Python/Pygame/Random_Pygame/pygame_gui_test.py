import pygame
import pygame_gui

# 1. Initialisering
pygame.init()

BREDDE, HOYDE = 800, 600
skjerm = pygame.display.set_mode((BREDDE, HOYDE))
pygame.display.set_caption("Moderne knapper i Pygame")

# 2. Opprett manageren (denne styrer alle UI-elementene)
manager = pygame_gui.UIManager((BREDDE, HOYDE))

# 3. Lag en knapp
# relative_rect bestemmer (x, y, bredde, høyde)
trykk_meg_knapp = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((300, 250), (200, 50)),
    text='Trykk her!',
    manager=manager
)

klokke = pygame.time.Clock()
kjorer = True

while kjorer:
    # regn ut tid siden forrige bilde (viktig for animasjoner i GUI)
    tid_delta = klokke.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kjorer = False
        
        # 4. Gi eventene videre til manageren!
        manager.process_events(event)

        # 5. Sjekk om knappen ble trykket
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == trykk_meg_knapp:
                print("Knappen ble trykket! Her kan du starte spillet.")

    # 6. Oppdater manageren
    manager.update(tid_delta)

    # 7. Tegn alt
    skjerm.fill((40, 40, 40)) # Mørkegrå bakgrunn
    manager.draw_ui(skjerm)

    pygame.display.update()

pygame.quit()