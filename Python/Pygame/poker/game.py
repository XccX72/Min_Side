import pygame
import pygame_gui as pg
import random as rnd

#-------------------------------------------------------------------------------------------
#Kortstokk del
#-------------------------------------------------------------------------------------------

kortstokk = {}

def hel_kortstokk():
    global kortstokk
    farger = ["Hjerter", "Ruter", "Spar", "Kløver"]
    verdier = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, 
        "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10, "A": 11
    }

    for fage in farger:
        for navn, verdi in verdier.items():
            kortstokk[f"{fage} {navn}"] = verdi
    return kortstokk

hel_kortstokk()

def restart_kortstokk():
    kortstokk.clear()
    hel_kortstokk()

def kort_del():
    global kortstokk, trukket_kort_1, trukket_kort_2, verdi_1, verdi_2, farge1, farge2
    trukket_kort_1 = rnd.choice(list(kortstokk.keys()))
    verdi_1 = kortstokk[trukket_kort_1]
    del kortstokk[trukket_kort_1]

    trukket_kort_2 = rnd.choice(list(kortstokk.keys()))
    verdi_2 = kortstokk[trukket_kort_2]
    del kortstokk[trukket_kort_2]

    if trukket_kort_1.startswith("Hjerter") or trukket_kort_1.startswith("Ruter"):
        farge1 = "#kort_rød"
    else:
        farge1 = "#kort_svart"

    if trukket_kort_2.startswith("Hjerter") or trukket_kort_2.startswith("Ruter"):
        farge2 = "#kort_rød"
    else:
        farge2 = "#kort_svart"

    return trukket_kort_1, trukket_kort_2, verdi_1, verdi_2, farge1, farge2


#-------------------------------------------------------------------------------------------
#Chips del (Cash)
#-------------------------------------------------------------------------------------------

def kjor_bet(valgt_innsats, total_cash):
    ny_total = total_cash - valgt_innsats
    return ny_total

def restart_func():
    cash = 100000
    return cash

#--------------------------------------------------------------------------------------------
#pygame del
#--------------------------------------------------------------------------------------------
meny_liste = []

def draw_objects_game(manager, cash_total):
    global meny_liste

    WIDTH, HEIGHT = pygame.display.get_surface().get_size()
    t1, t2, v1, v2, farge_id_1, farge_id_2 = kort_del()

    #tittel og meny_knapp
    Game_tittel = pg.elements.UILabel(
        relative_rect=pygame.Rect((WIDTH*0.5 - 150, HEIGHT*0.025), (300, 80)),
        text="BlackJack",
        manager=manager,
        # Sørg for at #tittel finnes i theme.json
        object_id= "#tittel"
    )

    return_meny_knapp = pg.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH * 0.0025, HEIGHT * 0.05), (100, 75)),
        text="Restart",
        manager=manager,
        object_id="#knapp"
    )

    #---------------------------------------------------------------------------------------
    #kort 1
    kort_1 = pg.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH * 0.78, HEIGHT * 0.60), (150, 220)),
        text=str(t1),
        manager=manager,
        object_id=farge_id_1 
    )

    #kort 2
    kort_2 = pg.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH * 0.88, HEIGHT * 0.57), (150, 220)),
        text=str(t2),
        manager=manager,
        object_id=farge_id_2
    )
    #---------------------------------------------------------------------------------------
    #Cash del
    cash_total_label = pg.elements.UILabel(
        relative_rect=pygame.Rect((WIDTH*0.002, HEIGHT*0.675), (150, 70)),
        text = str(cash_total),
        manager=manager,
        object_id= "#text"
    )


    cash_betting_label = pg.elements.UILabel(
        relative_rect=pygame.Rect((WIDTH*0.002, HEIGHT*0.75), (150, 70)),
        text = "Betting:",
        manager=manager,
        object_id= "#text"
    )

    cash_betting_scroll_label = pg.elements.UILabel(
        relative_rect=pygame.Rect((WIDTH*0.058, HEIGHT*0.75), (150, 70)),
        text = "0 $",
        manager=manager,
        object_id= "#text"
    )

    #For å velge antall money
    volum_slider = pg.elements.UIHorizontalSlider(
        relative_rect=pygame.Rect((WIDTH*0.025, HEIGHT*0.85), (250, 50)),
        start_value=0.0,
        value_range=(0.0, cash_total),
        manager=manager
    )

    #---------------------------------------------------------------------------------------
    #Knapper, Call, Fold, Bet, Etc

    #Betting knapp
    cash_betting_knapp = pg.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH *0.5-250, HEIGHT * 0.8), (150, 100)),
        text="Bet",
        manager=manager,
        object_id= "#knapp"
    )

    #Call knapp
    call_knapp = pg.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH*0.5-75, HEIGHT * 0.8), (150, 100)),
        text="Call",
        manager=manager,
        object_id="#knapp"
    )

    #Fold Knapp
    fold_knapp = pg.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH*0.5 + 95, HEIGHT * 0.8), (150, 100)),
        text="Fold",
        manager=manager,
        object_id="#knapp"
    )

    meny_liste.append(Game_tittel)
    meny_liste.append(kort_1)
    meny_liste.append(kort_2)
    meny_liste.append(cash_total_label)
    meny_liste.append(volum_slider)
    meny_liste.append(cash_betting_label)
    meny_liste.append(cash_betting_knapp)
    meny_liste.append(cash_betting_scroll_label)
    meny_liste.append(call_knapp)
    meny_liste.append(fold_knapp)
    meny_liste.append(return_meny_knapp)


    return volum_slider, cash_total_label, cash_betting_scroll_label, cash_betting_knapp, return_meny_knapp

def fjern_game_ui():
    global meny_liste

    for element in meny_liste:
        element.kill()
    
    meny_liste = []

def draw_background_game(window):
    window.fill("#0A3D2E")