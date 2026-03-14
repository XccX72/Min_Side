import pandas as pd
import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
import os


class Person:
        def __init__(self, navn:str, aar:int, nasjonalitet:str):
            self.navn = navn
            self.aar = aar
            self.nasjonalitet = nasjonalitet

        def hent_info(self):
            return (f"Navn {self.navn}, år {self.aar}, nasjonalitet {self.nasjonalitet}")
        
        def gi_vurdering(self, FILM: , Vurdering):
            a = FILM.vurdering.append(Vurdering)
            return a

class Regissor(Person):
        def __init__(self, navn, aar, nasjonalitet, kjent_for:list = []):
            super().__init__(navn, aar, nasjonalitet)
            self.kjent_for = kjent_for

        def legg_til_film(self, tittel):
            a = self.kjent_for.append(tittel)
            return a

class Skuespiller(Person):
        def __init__(self, navn, aar, nasjonalitet, roller:list = []):
            super().__init__(navn, aar, nasjonalitet)
            self.roller = roller

        def legg_til_rolle(self, rolle):
            a = self.roller.append(rolle)
            return a

        def hent_info(self):
            return (f"Navn {self.navn}, år {self.aar}, nasjonalitet {self.nasjonalitet}")
        
class Film:
    def __init__(self, tittel:str, aar:int, varighet:int, regissor:Regissor, vurdering:list = [], skuespiller:list =[]):
        self.tittel = tittel
        self.aar = aar
        self.varighet = varighet
        self.regissor = regissor
        self.vurdering = vurdering
        self.skuespiller = skuespiller

    def hent_info(self):
        return (f"Tittel {self.tittel}, år {self.aar}, varighet {self.varighet}, regi {self.regissor}")
    
    def legg_til_skuespiller(self, SKUESPILLEr):
        if self.varighet > 120:
            return True
        else:
            return False
    
    def er_lang(self):
        return (f"Filmen er {self.varighet} lang")
    
    def gjsnitt_vurdering(self):
        a = sum(self.vurdering)
        b = len(self.vurdering)
        c = a / b
        return c