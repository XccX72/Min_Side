# testdata_enkel.py
# Enkel testfil: oppretter objekter og kjører alle metodene
# Forutsetter at klassene finnes og heter:
# Film, Person, Regissor, Skuespiller

from filmkatalog import Film, Person, Regissor, Skuespiller
# 👉 Endre importen hvis du har annen filstruktur


# -------------------------
# Opprette personer
# -------------------------

regissor = Regissor("Christopher Nolan", 1970, "Britisk/amerikansk")
skuespiller1 = Skuespiller("Leonardo DiCaprio", 1974, "Amerikansk")
skuespiller2 = Skuespiller("Joseph Gordon-Levitt", 1981, "Amerikansk")

person1 = Person("Emil", 1990, "Norsk")
person2 = Person("Sara", 1995, "Norsk")


# -------------------------
# Teste Regissor
# -------------------------

regissor.legg_til_film("Inception")
regissor.legg_til_film("Interstellar")
print(regissor.hent_info())


# -------------------------
# Teste Skuespiller
# -------------------------

skuespiller1.legg_til_rolle("Cobb")
skuespiller2.legg_til_rolle("Arthur")

print(skuespiller1.hent_info())
print(skuespiller2.hent_info())


# -------------------------
# Opprette Film
# -------------------------

film = Film(
    tittel="Inception",
    aar=2010,
    varighet=148,
    regissor=regissor
)


# -------------------------
# Teste Film-metoder
# -------------------------

film.legg_til_skuespiller(skuespiller1)
film.legg_til_skuespiller(skuespiller2)

print(film.hent_info())
print("Er filmen lang?", film.er_lang())


# -------------------------
# Teste vurderinger
# -------------------------

person1.gi_vurdering(film, 9)
person2.gi_vurdering(film, 8)
regissor.gi_vurdering(film, 10)  # arv: Regissor er Person

print("Gjennomsnittlig vurdering:", film.gjennomsnitt_vurdering())


# -------------------------
# Ekstra test: kort film
# -------------------------

kortfilm = Film("Toy Story", 1995, 81, regissor)
print("Er Toy Story lang?", kortfilm.er_lang())
