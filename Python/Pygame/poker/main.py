import pygame
import pygame_gui as pg
import sys
from meny_side import draw_objects_meny, fjern_meny_ui, draw_background_meny
from game import draw_objects_game, fjern_game_ui, draw_background_game, kjor_bet, restart_kortstokk
from help_poker import draw_objects_help, draw_background_help, fjern_help_ui
import os

def quit_game():
    pygame.quit()
    sys.exit()

def main():
    #--------------------------------------------------------------------------
    #Basic info
    #--------------------------------------------------------------------------
    pygame.init()
    info_skjerm = pygame.display.Info()
    WIDTH, HEIGHT = info_skjerm.current_w, info_skjerm.current_h - 60
    window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("BlackJack")

    mappe = os.path.dirname(__file__)
    filsti = os.path.join(mappe, "theme.json")
    manager = pg.UIManager((WIDTH, HEIGHT), filsti)
    #modus: 0 = meny, 1 = game
    modus = 1
    cash = 100000 #100 000 $

    clock = pygame.time.Clock()
    dt = 0

    #--------------------------------------------------------------------------
    #Game side sine ting
    #--------------------------------------------------------------------------

    start_knapp, help_knapp = draw_objects_meny(manager)
    
    valgt_innsats = 0

    #--------------------------------------------------------------------------
    #While loop for spill
    #--------------------------------------------------------------------------
    running = True
    while running: 
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            manager.process_events(event)

            #Hvis noen vil fra meny -> game
            if event.type == pg.UI_BUTTON_PRESSED:
                if event.ui_element == start_knapp:
                        fjern_meny_ui()
                        modus = 1
                        cash = 100000
                        restart_kortstokk()

                        volum_slider, cash_total_label, cash_betting_visning, bet_knapp , return_meny_knapp= draw_objects_game(manager, cash)

            # Oppdater teksten når slideren flyttes
            if event.type == pg.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == volum_slider:
                    valgt_innsats = int(event.value)
                    cash_betting_visning.set_text(f"{valgt_innsats} $")

            # Trekk penger når man trykker på BET-knappen
            if event.type == pg.UI_BUTTON_PRESSED:
                if event.ui_element == bet_knapp:
                    cash = kjor_bet(valgt_innsats, cash)
                    cash_total_label.set_text(str(cash))
                    # Valgfritt: Oppdater sliderens maksverdi etter bet
                    # volum_slider.value_range = (0.0, cash)

                #Fra Game/Help -> Meny
                if event.ui_element == return_meny_knapp:
                    fjern_game_ui(), fjern_help_ui()
                    modus = 0
                    start_knapp = draw_objects_meny(manager)

                #Fra Game/Meny til Help
                if event.ui_element == help_knapp:
                    fjern_game_ui(), fjern_meny_ui()
                    modus = 2
                    help_knapp = draw_background_help(manager)


        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            quit_game()

        if modus == 0:
            draw_background_meny(window)

        if modus == 1:
            draw_background_game(window)

        if modus == 2:
            draw_background_help(window)
            

        #Oppdater manageren
        manager.update(dt)
        manager.draw_ui(window)
        pygame.display.update()

    quit_game()


if __name__ == "__main__":
    main()