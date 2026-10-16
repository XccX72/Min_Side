num = -2

while num <= 2:
    if num < 0: #alle tall som er neg
        if num % 2 == 0:
            print(f"neg og partall {num}")
        else:
            print(f"neg og oddetall {num}")
    elif num == 0:
        print(f"null {num}")
    else:   #Alle tall større enn null altså pos
        if num % 2 == 0:
            print(f"pos og partall {num}")
        else:
            print(f"pos og oddetall {num}")