def tallspill(tall):
    while True:
        siffre = list(map(int, str(tall)))
        stigendetall = sorted(siffre)
        avstigendetall = sorted(siffre, reverse=True)

        stigende_tall = int("".join(map(str, stigendetall)))
        avstigende_tall = int("".join(map(str, avstigendetall)))

        Nyttall = avstigende_tall - stigende_tall

        print(f"{tall} -> {avstigende_tall}, {stigende_tall} = {Nyttall}")
        if tall == Nyttall:
            break
        tall = Nyttall

print(tallspill(4435))