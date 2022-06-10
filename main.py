import random
from colorama import Fore

    # if pogingen <= 0:
    #   print("Je hebt verloren")
    #   print('Het woord was: ' + woord)

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

with open("wordle-answers.txt") as f:
  answers = f.read()
  answers_l = answers.split("\n")

def main():
  #random woord van words.txt
  answer = random.choice(answers_l)
  #Letters of alphabet, used for char testing
  letters = "abcdefghijklmnopqrstuvwxyz"
  error = False
  rondes = 0
  #keyboard dat aantoont welke letters wel en niet zijn gebruikt
  keyboard = ["q  ", "w  ", "e  ", "r  ", "t  ", "y  ", "u  ", "i  ", "o  ", "p  ", "a  ", "s  ", "d  ","f  ", "g  ", "h  ", "j  ", "k  ", "l  ", "z  ", "x  ", "c  ","v  ", "b  ", "n  ", "m  "]

#Keyboard printer, prints the keyboard
  def keyboardPrint(keyboard, rounds):
    #Saving or updating mode
    row1 = " " + "".join(keyboard).split("a")[0]
    row2 = "  a" + "".join(keyboard).split("a")[1].split("z")[0]
    row3 = "     z" + "".join(keyboard).split("z")[1]
  


  
#pogingen = 6
# dit doen we bij elke beurt
#def beurt(correct):
  #global pogingen
  #print(f"{Fore.WHITE} Je hebt nog {pogingen} pogingen")
  #raad = input(Fore.WHITE + "kies een woord: \n")
 # raad = raad.upper()
  #if len(raad) != 5:
   # print("Zorg ervoor dat het woord 5 letters is.")    
    #beurt(correct)

  
  #if raad == correct:
     # print("Yay gewonnen!")
    
  
  #for idx in range(len(raad)):
     # if raad[idx] == correct[idx]:
      #    print(Fore.GREEN, raad[idx])
     # elif raad[idx] in correct:
       #   print(Fore.YELLOW, raad[idx]) 
     # else:
        #  print(Fore.WHITE, raad[idx])
  
  #pogingen -= 1
  #if pogingen == 0:
    #print("Je bent af!")
   # #print(f"het woord was ")
   # a = input("Wil je nog een keer spelen?")
   # a = a.lower()

   # if a == "ja":
    #  pogingen = 6
   #   woordenlijst = ["KAMER","LEEUW","PASEN","POLEN"]
     # woord = random.choice(woordenlijst)
     # beurt(woord)
    #else:
     # print("Prima! Bedankt voor het spelen. :)")
      #exit()
  #beurt(correct)
    
     

print_menu()


#woordenlijst = ["KAMER","LEEUW","PASEN","POLEN"]
#woord = random.choice(woordenlijst)
#print(f"het woord is {woord}")
#beurt(woord)
