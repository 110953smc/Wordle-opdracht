import random
from colorama import Fore


    # if pogingen <= 0:
    #   print("Je hebt verloren")
    #   print('Het woord was: ' + woord)


def print_menu():
    print("Welkom bij wordle!")
    print(
        "De computer zal willekeurig een nederlands woord kiezen van vijf letters. Hoe het werkt: \n\n-Typ een woord van vijf letters\n-Als een letter in het woord staat maar niet op de juiste plaats, wordt het "
        + Fore.YELLOW + "GEEL" + Fore.WHITE +
        "\n-Als een letter in het woord voorkomt en op de juiste plaats staat, wordt deze "
        + Fore.GREEN + "GROEN" + Fore.WHITE +
        "\n-Als een letter helemaal niet in het woord voorkomt, blijft hij wit.\n-Je hebt zes kansen. "
    )

pogingen = 6
# dit doen we bij elke beurt
def beurt(correct):
  global pogingen
  print(f"je hebt {pogingen} pogingen over")
  raad = input(Fore.WHITE + "kies een woord: \n")
  if len(raad) != 5:
    print("Zorg ervoor dat het woord 5 letters is.")    
    beurt(correct)

  
  if raad == correct:
      print("Yay gewonnen!")

  for letter in range(len(raad)):
      if raad[letter] == correct[letter]:
          print(Fore.GREEN, raad[letter])
      elif raad[letter] in correct:
          print(Fore.YELLOW, raad[letter])
      else:
          print(Fore.WHITE, raad[letter])
  
  pogingen -= 1
  beurt(correct)
    
     

print_menu()


woordenlijst = ("words.txt")
woord = woordenlijst
beurt(woord)
