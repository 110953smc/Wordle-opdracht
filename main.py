from colorama import Fore
def print_menu():
  print("Welkom bij wordle!")
  print("De computer zal willekeurig een nederlands woord kiezen van vijf letters. Hoe het werkt: \n\n-Typ een woord van vijf letters\n-Als een letter in het woord staat maar niet op de juiste plaats, wordt het " + Fore.YELLOW + "GEEL" + Fore.WHITE + "\n-Als een letter in het woord voorkomt en op de juiste plaats staat, wordt deze " + Fore.GREEN + "GROEN" + Fore.WHITE + "\n-Als een letter helemaal niet in het woord voorkomt, blijft hij wit.\n-Je hebt zes kansen. ")
print_menu()


