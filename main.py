import random
from colorama import Fore

def print_menu():
  print("Welkom bij wordle!")
  print("De computer zal willekeurig een nederlands woord kiezen van vijf letters. Hoe het werkt: \n\n-Typ een woord van vijf letters\n-Als een letter in het woord staat maar niet op de juiste plaats, wordt het " + Fore.YELLOW + "GEEL" + Fore.WHITE + "\n-Als een letter in het woord voorkomt en op de juiste plaats staat, wordt deze " + Fore.GREEN + "GROEN" + Fore.WHITE + "\n-Als een letter helemaal niet in het woord voorkomt, blijft hij wit.\n-Je hebt zes kansen. ")

def raad_systeem(correct):
  raad = input("kies een woord: \n")

  if len(raad) != 5:
    print("mag niet")

  if raad == correct:
    print("Yay gewonnen!")
  
  for letter in range(len(raad)):
    if raad[letter] == correct[letter]:
      print(Fore.GREEN, raad[letter])
    elif raad[letter] in correct:
      print(Fore.YELLOW, raad[letter])
    else:
      print(Fore.WHITE, raad[letter])

  
  raad_systeem(correct)

  
print_menu()

woordenlijst = ["aapje","noots","miesp"] # todo lijst uit txt halen
woord = woordenlijst[0] # todo: random woord

raad_systeem(woord)