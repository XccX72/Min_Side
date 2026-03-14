"""
testdata.py
Kjør denne filen for å teste om klassene dine fungerer.

Forventede klasser (fra oppgaven):
- Film
- Person
- Regissor(Person)
- Skuespiller(Person)

Metoder som testes:
Film: hent_info(), legg_til_skuespiller(), er_lang(), gjennomsnitt_vurdering()
Person: hent_info(), gi_vurdering(film, vurdering)
Regissor: legg_til_film()
Skuespiller: legg_til_rolle(), hent_info() (overskrevet)
"""
# --- START: import --
def _try_imports():
    global Film, Person, Regissor, Skuespiller

    try:
        from filmkatalog import Film, Person, Regissor, Skuespiller
        return True, "Importerte fra filmkatalog.py"
    except Exception:
        pass

    return False, (
        "Klarte ikke å importere klassene.\n"
        "Sjekk at du har en fil som heter filmkatalog.py med alle klassene\n"
        "og at klassene heter: Film, Person, Regissor, Skuespiller."
    )

ok, msg = _try_imports()
print("== IMPORTTEST ==")
print(msg)
print()

if not ok:
    raise SystemExit("Stopper: Fiks importene først.")

# --- SLUTT: import ---


def divider(title: str):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def try_call(desc: str, func, *args, **kwargs):
    """Kaller en funksjon/metode og skriver pent resultat + fanger feil."""
    print(f"\n-> Tester: {desc}")
    try:
        result = func(*args, **kwargs)
        if result is not None:
            print("   Returnerte:")
            print("   ", result)
        else:
            print("   OK (ingen returverdi)")
        return result
    except Exception as e:
        print("   FEIL:", type(e).__name__, "-", e)
        return None


def main():
    divider("1) Lager objekter")

    # Regissør
    reg = Regissor("Christopher Nolan", 1970, "Britisk/amerikansk")
    try_call("Regissor.hent_info()", reg.hent_info)

    # Skuespillere
    s1 = Skuespiller("Leonardo DiCaprio", 1974, "Amerikansk")
    s2 = Skuespiller("Joseph Gordon-Levitt", 1981, "Amerikansk")

    # Roller (Skuespiller.legg_til_rolle)
    try_call("Skuespiller.legg_til_rolle('Cobb')", s1.legg_til_rolle, "Cobb")
    try_call("Skuespiller.legg_til_rolle('Arthur')", s2.legg_til_rolle, "Arthur")

    # Skuespiller.hent_info (overskrevet)
    try_call("Skuespiller.hent_info() (skal vise roller)", s1.hent_info)
    try_call("Skuespiller.hent_info() (skal vise roller)", s2.hent_info)

    # Regissor.legg_til_film
    try_call("Regissor.legg_til_film('Inception')", reg.legg_til_film, "Inception")
    try_call("Regissor.legg_til_film('Interstellar')", reg.legg_til_film, "Interstellar")

    divider("2) Lager Film-objekt og kobler sammen")

    film = Film(
        tittel="Inception",
        aar=2010,
        varighet=148,
        regissor=reg
    )

    # Film.legg_til_skuespiller
    try_call("Film.legg_til_skuespiller(s1)", film.legg_til_skuespiller, s1)
    try_call("Film.legg_til_skuespiller(s2)", film.legg_til_skuespiller, s2)

    # Film.hent_info
    try_call("Film.hent_info()", film.hent_info)

    # Film.er_lang
    try_call("Film.er_lang() (True hvis >120)", film.er_lang)

    divider("3) Tester vurderinger (Person.gi_vurdering -> Film.vurdering)")

    # Person-objekter som kan gi vurdering
    p1 = Person("Emil", 1990, "Norsk")
    p2 = Person("Sara", 1995, "Norsk")

    try_call("Person.hent_info()", p1.hent_info)
    try_call("Person.hent_info()", p2.hent_info)

    # Person.gi_vurdering(film, vurdering)
    # Forventning: filmen får lagt inn tall i film.vurdering-lista
    try_call("Person.gi_vurdering(film, 9)", p1.gi_vurdering, film, 9)
    try_call("Person.gi_vurdering(film, 8)", p2.gi_vurdering, film, 8)
    try_call("Person.gi_vurdering(film, 10)", reg.gi_vurdering, film, 10)  # regissør arver fra Person

    # Film.gjennomsnitt_vurdering
    try_call("Film.gjennomsnitt_vurdering()", film.gjennomsnitt_vurdering)

    divider("4) Ekstra test: kort film (er_lang bør bli False)")

    kortfilm = Film("Toy Story", 1995, 81, reg)
    try_call("Kortfilm.er_lang()", kortfilm.er_lang)

    divider("5) Oppsummering (valgfritt, men nyttig)")

    print("Antall skuespillere i film:", len(getattr(film, "skuespillere", [])))
    print("Vurderinger i film:", getattr(film, "vurdering", []))

    print("\n✅ Ferdig! Hvis alt over kjører uten FEIL, fungerer det meste.")


if __name__ == "__main__":
    main()
