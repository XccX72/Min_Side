"""
Alt er målt i pixler

sirkel = pygame.draw.circle(vindu den er i, farge, posisjon(x, y), radius(størrelse), width(optional))
width er tykkelse på omkretsen
OBS! Bruke Vector2 for posisjon del

Rektangel = pygame.draw.rect(vindu, farge, [x, y, bredde, høyde], width, border_radius(hvor sjukk))

linje = .line(vindu, farge, start_pos(x, y), slutt_pos(x, y), width)
width er tykkelse på linjen

Oval = .ellipse(vindu, farge, Hvilken rektangel den skal fylle, width)

bue = .arc(vindu, farge, rektangel som skal brukes, start vinkel, slutt vinkel, width)
vinlene måles i radianer, bruk import math -> math.pi

polygon = .polygon(vindu, farge, points, widht)
points = [(x, y), [x, y], [x, y]]
Vil da lage trekant, for firkant så er det 4 () innenfor listen


Utenfor while loop
pygame.font.init()
min_font = pygame.font.Sysfont("Arial", Størrelse:int)

I while loop

tekst_bilde = min_font.render(Tekst:str, True, Farge:str)
window.blit(tekst_bilde, (Posisjon x, y))


"""