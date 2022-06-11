import random
from colorama import Fore

# if pogingen <= 0:
#   print("Je hebt verloren")
#   print('Het woord was: ' + woord)
pogingen = 6


#instructies
def print_menu():
    print("Welkom bij wordle!")
    print(
        "De computer zal willekeurig een nederlands woord kiezen van vijf letters. Hoe het werkt: \n\n-Typ een woord van vijf letters\n-Als een letter in het woord staat maar niet op de juiste plaats, wordt het "
        + Fore.YELLOW + "GEEL" + Fore.WHITE +
        "\n-Als een letter in het woord voorkomt en op de juiste plaats staat, wordt deze "
        + Fore.GREEN + "GROEN" + Fore.WHITE +
        "\n-Als een letter helemaal niet in het woord voorkomt, blijft hij wit.\n-Je hebt zes kansen. "
    )


#dit doen we bij elke beurt
def beurt(correct):
    global pogingen
    global woord
    print(f"{Fore.WHITE} Je hebt nog {pogingen} pogingen")
    raad = input(Fore.WHITE + "kies een woord: \n")
    raad = raad.upper()
    if len(raad) != 5:
        print("Zorg ervoor dat het woord 5 letters is.")
        beurt(correct)

    if raad == correct:
        print("Yay gewonnen! Het woord was inderdaad " + woord)
        a = input("Wil je nog een keer spelen?")
        a = a.lower()
        if a == "ja":
            pogingen = 6
            woordenlijst = ["KAMER", "LEEUW", "PASEN", "POLEN", "LEPEL", "BAKJE", "DEKEN", "PIANO", "PLANT", "REGEN", "SPORT", "BLAUW", "VOGEL", "APPEL", "LAKEN", "BOVEN", "KWAST", "NAAST", "KRAMP", "BINGO", "ONDER", "TAFEL", "ZAGEN", "SLANG", "KOGEL"]
            woord = random.choice(woordenlijst)
            beurt(woord)
        else:
            print("Prima! Bedankt voor het spelen. :)")
            exit()

    for idx in range(len(raad)):
        if raad[idx] == correct[idx]:
            print(Fore.GREEN, raad[idx])
        elif raad[idx] in correct:
            print(Fore.YELLOW, raad[idx])
        else:
            print(Fore.WHITE, raad[idx])

    pogingen -= 1
    if pogingen == 0:
        print("Je bent af!")
        print("het woord was " + woord)
        a = input("Wil je nog een keer spelen?")
        a = a.lower()

        if a == "ja":
            pogingen = 6
            woordenlijst = ["KAMER", "LEEUW", "PASEN", "POLEN", "LEPEL", "BAKJE", "DEKEN", "PIANO", "PLANT", "REGEN", "SPORT", "BLAUW", "VOGEL", "APPEL", "LAKEN", "BOVEN", "KWAST", "NAAST", "KRAMP", "BINGO", "ONDER", "TAFEL", "ZAGEN", "SLANG", "KOGEL"]
            woord = random.choice(woordenlijst)
            beurt(woord)
        else:
            print("Prima! Bedankt voor het spelen. :)")
            exit()
    beurt(correct)


print_menu()

woordenlijst = ["KAMER", "LEEUW", "PASEN", "POLEN", "LEPEL", "BAKJE", "DEKEN",   "PIANO", "PLANT", "REGEN", "SPORT", "BLAUW", "VOGEL", "APPEL", "LAKEN", "BOVEN", "KWAST", "NAAST", "KRAMP", "BINGO", "ONDER", "TAFEL", "ZAGEN", "SLANG", "KOGEL"]
woord = random.choice(woordenlijst)

beurt(woord)
