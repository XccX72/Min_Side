import pygame
import pygame_gui as pg

#Hjelpe skjerm og settings
meny_liste = []

def draw_objects_help(manager):
    pass

def fjern_help_ui():
    global meny_liste

    for element in meny_liste:
        element.kill()
    
    meny_liste = []

def draw_background_help(window):
    window.fill("#0A3D2E")