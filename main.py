print("Welkom bij wordle!")

input("druk op start")

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