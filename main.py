print("Welkom bij wordle!")

# invoer = input("druk op start")

# if invoer == "start":
#   print("yay")
# else:
#   print("meh")

woorden = ["aap","noot","mies"]

#hoe doe ik random in python

gekozenwoord = woorden[1]

woord = input("schrijf een woord: \n")

if gekozenwoord == woord:
  print("goed geraden")
else:
  print("fout!")

  
print(gekozenwoord)
print(woord)