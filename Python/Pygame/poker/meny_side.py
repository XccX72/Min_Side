import pygame
import pygame_gui as pg

meny_liste = []

def draw_objects_meny(manager):
    global meny_liste
    WIDTH, HEIGHT = pygame.display.get_surface().get_size()

    #tittel
    meny_tittel = pg.elements.UILabel(
        relative_rect=pygame.Rect((WIDTH*(1/2) - 150, HEIGHT*(1/3)), (300, 80)), # Gjorde boksen bredere (300)
        text="BlackJack",
        manager=manager,
        object_id= "#overskrift"
    )

    #Snart knapp endrer modus til game
    start_knapp = pg.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH*(1/2) - 75, HEIGHT*(2/3)), (150, 50)),
        text='Start Spill',
        manager=manager,
        object_id= "button"
    )

    help_knapp = pg.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH * 0.0025, HEIGHT * 0.05), (100, 75)),
        text='Help',
        manager=manager,
        object_id= "button"
    )

    meny_liste.append(meny_tittel)
    meny_liste.append(start_knapp)
    meny_liste.append(help_knapp)

    return start_knapp, help_knapp


def fjern_meny_ui():
    global meny_liste

    for element in meny_liste:
        element.kill()
    
    meny_liste = []

def draw_background_meny(window):
    window.fill("#0A3D2E")

 